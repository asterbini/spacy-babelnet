from spacy.tokens.doc      import Doc
from spacy.tokens.token    import Token
from spacy.parts_of_speech import *
from spacy.language        import Language

import babelnet as bn

bn.initVM()

DEBUG=True
DEBUG=False

@Language.factory("babelnet")
class BabelnetAnnotator():
    __FIELD = 'babelnet'

    def __init__(self, nlp, name, source=None):
        Token.set_extension(BabelnetAnnotator.__FIELD, default=None, force=True)
        self.__lang      = nlp.lang
        self.__bn_lang   = bn.Language.fromISO(nlp.lang)
        self.__source    = source
        self.__bn_source = None
        if source:
            self.__bn_source = getattr(bn.BabelSenseSource,source)

    def __call__(self, doc: Doc):
        for token in doc:
            babelnet = Babelnet(token=token, lang=self.__bn_lang, source=self.__bn_source)
            token._.set(BabelnetAnnotator.__FIELD, babelnet)
            if DEBUG:
                print(token, babelnet)
        return doc

class Babelnet():
    # keep __bn if it's needed, even if it's deprecated
    __bn  = bn.BabelNet.getInstance()
    # LKB allows to select the source and seems to be faster
    __lkb = bn.LKB.cast_(__bn)

    # FIXME: check if correct
    __SPACY_BN_POS_MAPPING = {
            ADJ   : bn.BabelPOS.ADJECTIVE,
    #       ADP   :
            ADV   : bn.BabelPOS.ADVERB,
            AUX   : bn.BabelPOS.VERB,
    #       CCONJ :
    #       CONJ  :
    #       DET   : bn.BabelPOS.NOUN,
    #       EOL   :
    #       IDS   :
    #       INTJ  :
    #       NO_TAG:
            NOUN  : bn.BabelPOS.NOUN,
            NUM   : bn.BabelPOS.NOUN,
    #       PART  :
    #       PRON  : bn.BabelPOS.NOUN,
            PROPN : bn.BabelPOS.NOUN,
    #       PUNCT :
    #       SCONJ :
    #       SPACE :
    #       SYM   :
            VERB  : bn.BabelPOS.VERB,
    #       X     :
            }

    def spacy2babelnet_pos(self, pos):
        return self.__SPACY_BN_POS_MAPPING.get(pos)

    def __init__(self, token: Token, lang: bn.Language = bn.Language.EN, source=None):
        self.__token    = token
        self.__bn_lang  = lang
        self.__bn_source= source
        self.__synsets  = self.__find_synsets(token)    # we store only the IDs
        self.__lemmas   = None                          # computed only on demand

    def synsets(self):
        # retrive the BabelnetSynset from their IDs
        return [ self.__bn.getSynset(bn.BabelSynsetID(s)) for s in self.__synsets ]

    def synset_IDs(self):
        return self.__synsets

    def lemmas(self):
        if self.__lemmas is None:
            self.__lemmas = self.__find_lemmas()
        return self.__lemmas

    def __find_synsets(self, token: Token):
        '''Retrieves the IDs of the token synsets. POS and source are used to restrict the search.'''
        word_variants = [token.text]
        if token.pos in [VERB, NOUN, ADJ]:
            # extend synset coverage using lemmas
            word_variants.append(token.lemma_)

        token_synsets = set()
        pos = self.spacy2babelnet_pos(token.pos)
        for word in word_variants:
            if pos is not None:
                # we use LKBQuery to be able to select the main SenseSource
                qb = bn.BabelNetQuery.Builder(word)
                qb.POS(pos)
                getattr(qb,'from')(self.__bn_lang)  # from is a reserved word
                if self.__bn_source:
                    qb.source(self.__bn_source)
                q = qb.build()
                q = bn.LKBQuery.cast_(q)
                token_synsets |= set(bn.BabelSynset.cast_(s).getID().toString() for s in self.__lkb.getSynsets(q))
        if token_synsets:
            return list(token_synsets)  # sorted?
        return []

    def __find_lemmas(self):
        return list({lemma for synset in self.synsets() for lemma in synset.getLemmas(self.__bn_lang)})

    def __str__(self):
        return f"Babelnet({self.__token}, {self.__token.pos_}, {self.__synsets})"
