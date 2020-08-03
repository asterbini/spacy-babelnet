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

__SPACY_BN_POS_MAPPING = {
        ADJ   : bn.BabelPOS.ADJECTIVE,
#        ADP   :
        ADV   : bn.BabelPOS.ADVERB,
#        AUX   :
#        CCONJ :
#        CONJ  :
#        DET   :
#        EOL   :
#        IDS   :
#        INTJ  :
#        NAMES :
#        NO_TAG:
        NOUN  : bn.BabelPOS.NOUN,
#        NUM   :
#        PART  :
#        PRON  :
#        PROPN :
#        PUNCT :
#        SCONJ :
#        SPACE :
#        SYM   :
        VERB  : bn.BabelPOS.VERB,
#        X     :
        }

def spacy2babelnet_pos(pos):
    return __SPACY_BN_POS_MAPPING.get(pos)

class Babelnet():
    __bn = bn.BabelNet.getInstance()

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

        for word in word_variants:
            pos = spacy2babelnet_pos(token.pos)
            if pos!=None:
                token_synsets = self.__bn.getSynsets(word, lang, pos)
            else:
                token_synsets = self.__bn.getSynsets(word, lang)
            if token_synsets:
                return token_synsets
        return []

    def __find_lemmas(self):
        return [lemma for synset in self.__synsets for lemma in synset.getLemmas(self.__bn_lang)]
