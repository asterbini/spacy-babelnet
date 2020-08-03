from spacy.tokens.doc   import Doc
from spacy.tokens.token import Token

import babelnet

class BabelnetAnnotator():
    __FIELD = 'babelnet'

    def __init__(self, lang: str = 'en'):
        Token.set_extension(BabelnetAnnotator.__FIELD, default=None, force=True)
        self.__lang = lang
        babelnet.initVM()
        self.__babelnet = babelnet.BabelNet.getInstance()

    def __call__(self, doc: Doc):
        for token in doc:
            babelnet = Babelnet(token=token, lang=self.__lang)
            token._.set(BabelnetAnnotator.__FIELD, babelnet)

        return doc

__SPACY_BN_POS_MAPPING = {
        spacy.part_of_speech.VERB : babelnet.BabelPOS.VERB,
        spacy.part_of_speech.NOUN : babelnet.BabelPOS.NOUN,
        spacy.part_of_speech.ADJ  : babelnet.BabelPOS.ADJECTIVE,
        spacy.part_of_speech.ADV  : babelnet.BabelPOS.ADVERB,
        }

def spacy2babelnet_pos(pos):
    return __SPACY_BN_POS_MAPPING[pos]

class Babelnet():

    def __init__(self, token: Token, lang: str = 'en'):
        self.__token   = token
        self.__lang    = lang
        self.__synsets = self.__find_synsets(token, self.__lang)
        self.__lemmas  = self.__find_lemmas()

    def synsets(self):
        return self.__synsets

    def lemmas(self):
        return self.__lemmas

    @staticmethod
    def __find_synsets(token: Token, lang: str):
        word_variants = [token.text]
        if token.pos in [spacy.part_of_speech.VERB, spacy.part_of_speech.NOUN, spacy.part_of_speech.ADJ]:
            # extend synset coverage using lemmas
            word_variants.append(token.lemma_)

        for word in word_variants:
            token_synsets = self.__babelnet.synsets(word, pos=spacy2babelnet_pos(token.pos), language=lang)
            if token_synsets:
                return token_synsets

        return []

    @staticmethod
    def __find_lemmas(self):
        return [lemma for synset in self.__synsets for lemma in synset.lemmas(lang=self.__lang)]
