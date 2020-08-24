## Spacy Babelnet

A Spacy pipeline component that annotates tokens with their corresponding Babelnet Synsets (and Lemmas).
The synsets are searched only in the specified language, but other languages can be retrieved through Babelnet.
If the token has a POS annotation, the synsets are searched only with that POS.
Notice that Babelnet uses only the 4 main POS tags: `NAME,ADJ,VERB,ADV`.
Only tokens that map to these 4 types are searched in BabelNet.

### Build and install the `babelnet` module
The `babelnet` module is a python wrapper to the Babelnet API jars
- install the `jcc` module \
  ``anaconda install jcc
- or else \
  ``pip install jcc
- download and unzip the Babelnet-API archive version 4.0.1 \
  ``make get_api``
- build and install the `babelnet` module \
  ``make babelnet``

### Build and install the `spacy_babelnet` module
- ``make spacy-babelnet`` \
  or else
- ``python setup.py install``

### Copy the config directory containing your key
The `babelnet` module must find the `config` directory in the current directory. Copy the `config` directory and edit the `config/babelnet.var.properties` to add your BabelNet API key.

### Optional: local install of the BabelNet indices (29G compressed, 49G on disk)
- download the BabelNet indices from BabelNet.org
- unzip them
- edit the `config/babelnet.vars.properties` file to set the indices directory

## Usage Example
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
That produces the output

    mi
        [<BabelSynset: mu#n#1>, <BabelSynset: WIKI:EN:Province_of_Milan>, <BabelSynset: WIKIDATA:EN:E>, <BabelSynset: WIKI:EN:Jón_Leifs>, <BabelSynset: WIKIDATA:EN:Mi>, <BabelSynset: mi#n#8>, <BabelSynset: Milan#n#1>, <BabelSynset: WIKI:EN:methylisothiazolinone>, <BabelSynset: WIKI:EN:Mi_(kana)>]
        [<BabelLemma: Mi>, <BabelLemma: MIT>, <BabelLemma: mu>, <BabelLemma: Occupazione_francese_di_Milano>, <BabelLemma: Milano_Jazzin'_Festival>, <BabelLemma: Jón_Leifs>, <BabelLemma: Fa♭>, <BabelLemma: Provincia_di_Milano>, <BabelLemma: mi>, <BabelLemma: Mu>, <BabelLemma: μ>, <BabelLemma: MI>, <BabelLemma: Milàn>, <BabelLemma: Mi>, <BabelLemma: Μ>, <BabelLemma: Milano>, <BabelLemma: milano>, <BabelLemma: mi>, <BabelLemma: ミ>, <BabelLemma: methylisothiazolinone>, <BabelLemma: Mi>, <BabelLemma: Mi>, <BabelLemma: Fa♭>, <BabelLemma: Metilisotiazolinone>, <BabelLemma: Mi>, <BabelLemma: Fa_bemolle>, <BabelLemma: Mediolanum>, <BabelLemma: Methylisothiazolinone>, <BabelLemma: Fa_bemolle>, <BabelLemma: Città_metropolitana_di_Milano>, <BabelLemma: MI>, <BabelLemma: MI>, <BabelLemma: み>, <BabelLemma: provincia_di_Milano>, <BabelLemma: mu>]

    piace
        [<BabelSynset: like#v#2>, <BabelSynset: like#v#2>, <BabelSynset: gratify#v#1>, <BabelSynset: WIKT:EN:fond>, <BabelSynset: delight#v#1>, <BabelSynset: care#v#3>, <BabelSynset: like#v#3>, <BabelSynset: enjoy#v#3>]
        [<BabelLemma: soddisfare>, <BabelLemma: gratificare>, <BabelLemma: soddisfare>, <BabelLemma: compiacere>, <BabelLemma: appagare>, <BabelLemma: piacere>, <BabelLemma: deliziare>, <BabelLemma: assecondare>, <BabelLemma: prediligere>, <BabelLemma: provare_gioia>, <BabelLemma: appagare>, <BabelLemma: volere_bene>, <BabelLemma: piacere>, <BabelLemma: accontentare>, <BabelLemma: piacere>, <BabelLemma: contentare>, <BabelLemma: accontentare>, <BabelLemma: piace>, <BabelLemma: preferire>, <BabelLemma: contentare>, <BabelLemma: piacere>, <BabelLemma: piacere>, <BabelLemma: amare>, <BabelLemma: gratificare>, <BabelLemma: piacere>, <BabelLemma: piacere>, <BabelLemma: dilettare>, <BabelLemma: godere>, <BabelLemma: piace>, <BabelLemma: piacere>]

    la
        [<BabelSynset: WIKI:EN:La_(genus)>, <BabelSynset: WIKIDATA:NL:La>, <BabelSynset: WIKIDATA:EN:alif>, <BabelSynset: WIKI:EN:English_articles>, <BabelSynset: WIKI:EN:La_(Tarzan)>, <BabelSynset: la#n#3>, <BabelSynset: lanthanum#n#1>]
        [<BabelLemma: lo>, <BabelLemma: numero_atomico_57>, <BabelLemma: ʼalif_makṣūra>, <BabelLemma: La>, <BabelLemma: لا>, <BabelLemma: l'>, <BabelLemma: La>, <BabelLemma: La>, <BabelLemma: le>, <BabelLemma: ا>, <BabelLemma: Alif>, <BabelLemma: i>, <BabelLemma: articoli_inglesi>, <BabelLemma: Lām_ʼalif>, <BabelLemma: gli>, <BabelLemma: lantanio>, <BabelLemma: la>, <BabelLemma: ʾalif>, <BabelLemma: la>, <BabelLemma: Lām-alif>, <BabelLemma: il>, <BabelLemma: Alif_wasla>, <BabelLemma: gl'>, <BabelLemma: lah>, <BabelLemma: La>, <BabelLemma: La>, <BabelLemma: ʼalif_madda>, <BabelLemma: Lanthanio>]

    pizza
        [<BabelSynset: WIKIDATA:EN:Pizza>, <BabelSynset: bore#n#1>, <BabelSynset: reel#n#1>, <BabelSynset: pizza#n#1>, <BabelSynset: reel#n#1>, <BabelSynset: WIKIDATA:EN:Pizza>, <BabelSynset: pizza#n#1>, <BabelSynset: bore#n#1>]
        [<BabelLemma: lagna>, <BabelLemma: Pizza>, <BabelLemma: pasta_della_pizza>, <BabelLemma: Pizza_classica>, <BabelLemma: Pizza_alla_pala>, <BabelLemma: Pizza_in_teglia>, <BabelLemma: pasta_per_pizza>, <BabelLemma: pizza>, <BabelLemma: pizza_pie>, <BabelLemma: noia>, <BabelLemma: pittima>, <BabelLemma: Pizza_al_taglio>, <BabelLemma: Dj_Pizza>, <BabelLemma: Pizza_al_taglio>, <BabelLemma: mattone>, <BabelLemma: Pizza_classica>, <BabelLemma: palla>, <BabelLemma: pizza>, <BabelLemma: impiastro>, <BabelLemma: pizza_surgelata>, <BabelLemma: cataplasma>, <BabelLemma: DJ_Pizza>, <BabelLemma: pizze>, <BabelLemma: lagna>, <BabelLemma: pizza_congelata>, <BabelLemma: bobina>, <BabelLemma: cataplasma>, <BabelLemma: bobina>, <BabelLemma: pizza_surgelata>, <BabelLemma: pasta_della_pizza>, <BabelLemma: Pizza_a_taglio>, <BabelLemma: pizze>, <BabelLemma: Pizza>, <BabelLemma: forno_per_la_pizza>, <BabelLemma: Pizza_tonda>, <BabelLemma: pasta_per_pizza>, <BabelLemma: pizza>, <BabelLemma: pizza>, <BabelLemma: noioso>, <BabelLemma: noioso>, <BabelLemma: pizza>, <BabelLemma: pizza_pie>, <BabelLemma: Pizza_in_teglia>, <BabelLemma: DJ_Pizza>, <BabelLemma: pizza>, <BabelLemma: Pizza_a_taglio>, <BabelLemma: Pizza_tonda>, <BabelLemma: Pizza_alla_pala>, <BabelLemma: pizza_congelata>, <BabelLemma: Dj_Pizza>, <BabelLemma: noia>, <BabelLemma: impiastro>, <BabelLemma: pittima>, <BabelLemma: forno_per_la_pizza>, <BabelLemma: palla>, <BabelLemma: forno_da_pizza>, <BabelLemma: forno_da_pizza>, <BabelLemma: mattone>]

## TODO
- add tests
- find a better location for the `babelnet` configuration (`~/babelnet_data` ?)
- speed-up synsets retrieval
    - convert BN to a simpler/faster database?
    - build a lemma-synset external index?
## DONE
- mapped other spacy POS types to Babelnet POS types
- filter out tokens with unmapped POS
