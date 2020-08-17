from spacy.tokens.doc      import Doc
from spacy.tokens.token    import Token
from spacy.parts_of_speech import *

import babelnet as bn

bn.initVM()

class BabelnetAnnotator():
    __FIELD = 'babelnet'

    def __init__(self, lang: str = 'en'):
        Token.set_extension(BabelnetAnnotator.__FIELD, default=None, force=True)
        self.__lang = lang
        #bn.initVM()

    def __call__(self, doc: Doc):
        for token in doc:
            babelnet = Babelnet(token=token, lang=self.__lang)
            token._.set(BabelnetAnnotator.__FIELD, babelnet)

        return doc


class Babelnet():
    __bn = bn.BabelNet.getInstance()
    # FIXME: check if correct
    __SPACY_BN_POS_MAPPING = {
            ADJ   : bn.BabelPOS.ADJECTIVE,
    #       ADP   :
            ADV   : bn.BabelPOS.ADVERB,
            AUX   : bn.BabelPOS.VERB,
    #       CCONJ :
    #       CONJ  :
            DET   : bn.BabelPOS.NOUN,
    #       EOL   :
    #       IDS   :
    #       INTJ  :
    #       NO_TAG:
            NOUN  : bn.BabelPOS.NOUN,
            NUM   : bn.BabelPOS.NOUN,
    #       PART  :
            PRON  : bn.BabelPOS.NOUN,
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

    def __init__(self, token: Token, lang: str = 'en'):
        self.__token    = token
        self.__lang     = lang
        self.__bn_lang  = bn.Language.fromISO(lang)
        self.__synsets  = self.__find_synsets(token, self.__bn_lang)
        self.__lemmas   = self.__find_lemmas()

    def synsets(self):
        return self.__synsets

    def lemmas(self):
        return self.__lemmas

    def __find_synsets(self, token: Token, lang):
        word_variants = [token.text]
        if token.pos in [VERB, NOUN, ADJ]:
            # extend synset coverage using lemmas
            word_variants.append(token.lemma_)

        token_synsets = set()
        for word in word_variants:
            pos = self.spacy2babelnet_pos(token.pos)
            if pos!=None:
                token_synsets |= set(self.__bn.getSynsets(word, lang, pos))
        if token_synsets:
            return list(token_synsets)
        return []

    def __find_lemmas(self):
        return list({lemma for synset in self.__synsets for lemma in synset.getLemmas(self.__bn_lang)})
