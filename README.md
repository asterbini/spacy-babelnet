# Spacy Babelnet

A Spacy pipeline component that annotates tokens with their Babelnet Synsets (and Lemmas?).

### Build and install the babelnet module

- install the jcc module
  > anaconda install jcc
- or else
  > pip install jcc
- download and unzip the Babelnet-API archive version 4.0.1 
  > make get_api
- register to Babelnet.org and place your API key in the BabelNet-API-4.0.1/config/babelnet.vars.properties file
- build and install the babelnet python wrapper to the Babelnet API jars
  > make babelnet
- Build and install the spacy-babelnet module
  > make spacy-babelnet

## Copy the config directory containing your key
The babelnet module must find the config directory in the current directory.

## Install locally the BabelNet indices (29G compressed, 50G on disk)
Instead than using the Babelnet REST service, you could install it locally
- download the Babelnet indices from BabelNet.org
- unzip them
- edit the config/babelnet.vars.properties file to indicate the directory position

# Usage Example

The wrapper adds the 'babelnet' property to tokens, containing a Babelnet object that can be used to retrieve its synsets or lemmas
```
import spacy
from spacy_babelnet import BabelnetAnnotator

nlp = spacy.load('it')
nlp.add_pipe(BabelnetAnnotator('it'))

doc = nlp('Mi piace la pizza')
for token in doc:
    print(token, token._.babelnet.synsets(), token._.babelnet.lemmas(), sep='\n\t')
```
    Mi
            [WIKIDATA:EN:E, mu#n#1, WIKI:EN:Jón_Leifs, WIKI:EN:methylisothiazolinone, WIKI:EN:Mi_(kana), WIKI:EN:Province_of_Milan, mi#n#8, Milan#n#1, WIKIDATA:EN:Mi]
            [<BabelLemma: Fa♭>, <BabelLemma: Mi>, <BabelLemma: Fa_bemolle>, <BabelLemma: Μ>, <BabelLemma: Mi>, <BabelLemma: mu>, <BabelLemma: Mu>, <BabelLemma: μ>, <BabelLemma: Jón_Leifs>, <BabelLemma: mi>, <BabelLemma: Methylisothiazolinone>, <BabelLemma: Metilisotiazolinone>, <BabelLemma: MIT>, <BabelLemma: MI>, <BabelLemma: methylisothiazolinone>, <BabelLemma: Mi>, <BabelLemma: み>, <BabelLemma: ミ>, <BabelLemma: Provincia_di_Milano>, <BabelLemma: Città_metropolitana_di_Milano>, <BabelLemma: MI>, <BabelLemma: provincia_di_Milano>, <BabelLemma: mi>, <BabelLemma: Fa♭>, <BabelLemma: mu>, <BabelLemma: Mi>, <BabelLemma: Fa_bemolle>, <BabelLemma: Milano>, <BabelLemma: Mediolanum>, <BabelLemma: MI>, <BabelLemma: Milàn>, <BabelLemma: Occupazione_francese_di_Milano>, <BabelLemma: Milano_Jazzin'_Festival>, <BabelLemma: milano>, <BabelLemma: Mi>]
    piace
            [like#v#2]
            [<BabelLemma: piacere>, <BabelLemma: piace>]
    la
            [lanthanum#n#1, la#n#3, WIKIDATA:NL:La, WIKI:EN:English_articles, WIKIDATA:EN:alif, WIKI:EN:La_(genus), claim#v#2, WIKI:EN:La_(Tarzan), OMWIKI:EN:the]
            [<BabelLemma: lantanio>, <BabelLemma: La>, <BabelLemma: Lanthanio>, <BabelLemma: numero_atomico_57>, <BabelLemma: la>, <BabelLemma: La>, <BabelLemma: lah>, <BabelLemma: La>, <BabelLemma: il>, <BabelLemma: articoli_inglesi>, <BabelLemma: gl'>, <BabelLemma: lo>, <BabelLemma: gli>, <BabelLemma: la>, <BabelLemma: i>, <BabelLemma: le>, <BabelLemma: l'>, <BabelLemma: Alif>, <BabelLemma: لا>, <BabelLemma: ʾalif>, <BabelLemma: Alif_wasla>, <BabelLemma: Lām_ʼalif>, <BabelLemma: ا>, <BabelLemma: ʼalif_makṣūra>, <BabelLemma: ʼalif_madda>, <BabelLemma: Lām-alif>, <BabelLemma: La>, <BabelLemma: rivendicare>, <BabelLemma: reclamare>, <BabelLemma: possesso>, <BabelLemma: il>, <BabelLemma: la>, <BabelLemma: proprietà>, <BabelLemma: La>, <BabelLemma: la>, <BabelLemma: le>, <BabelLemma: l'>]
    pizza
            [reel#n#1, pizza#n#1, bore#n#1, WIKIDATA:EN:Pizza]
            [<BabelLemma: bobina>, <BabelLemma: pizza>, <BabelLemma: pizza>, <BabelLemma: pizza_surgelata>, <BabelLemma: pasta_della_pizza>, <BabelLemma: pasta_per_pizza>, <BabelLemma: forno_da_pizza>, <BabelLemma: pizza_congelata>, <BabelLemma: Pizza_alla_pala>, <BabelLemma: Pizza_a_taglio>, <BabelLemma: Pizza_tonda>, <BabelLemma: Pizza_in_teglia>, <BabelLemma: Pizza_al_taglio>, <BabelLemma: Pizza_classica>, <BabelLemma: pizza_pie>, <BabelLemma: pizze>, <BabelLemma: forno_per_la_pizza>, <BabelLemma: noioso>, <BabelLemma: pizza>, <BabelLemma: mattone>, <BabelLemma: cataplasma>, <BabelLemma: impiastro>, <BabelLemma: palla>, <BabelLemma: lagna>, <BabelLemma: noia>, <BabelLemma: pittima>, <BabelLemma: Pizza>, <BabelLemma: Dj_Pizza>, <BabelLemma: DJ_Pizza>]

## TODO
- add tests
- speed-up the synsets retrieval 
    - convert BN to a simpler database?
    - build a lemma-synset external index?
