## Spacy Babelnet

A Spacy pipeline component that annotates tokens with their corresponding Babelnet Synsets (and Lemmas).
The synsets are searched only in the specified language, but other languages can be retrieved through Babelnet.
If the token has a POS annotation, the synsets are searched only with that POS.
Notice that Babelnet uses only the 4 main POS tags: `NAME,ADJ,VERB,ADV`.
Only tokens that map to these 4 types are searched in BabelNet.

### Build and install the `babelnet` module
The `babelnet` module is a python wrapper to the Babelnet API jars
- install the `jcc` module \
  ``anaconda install jcc``
- or else \
  ``pip install jcc``
- download and unzip the Babelnet-API archive version 4.0.1 \
  ``make get_api``
- NOTICE: `jcc` 3.7 compiles its class wrappers in non-deterministic order sometimes producing a non-working `babelnet` module. To fix this:
  - change line 696 of file ``.../site-packages/jcc/cpp.py`` from \
    ``for cls in todo:``  
    to \
    ``for cls in sorted(todo, key=lambda c: c.getName()): ``
- build and install the `babelnet` module \
  ``make babelnet``

### Build and install the `spacy-babelnet` module
- ``make spacy-babelnet`` \
  or else
- ``python setup.py install``

### Copy the config directory containing your key
The `babelnet` module must find the `config` directory in the current application directory.

### Local install of the BabelNet indices (29G compressed, 49G on disk)
- download the Babelnet indices from BabelNet.org
- unzip them
- edit the `config/babelnet.vars.properties` file to indicate the directory position

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

    Mi
        [<BabelSynset: mu#n#1>, <BabelSynset: WIKI:EN:Province_of_Milan>, <BabelSynset: WIKIDATA:EN:E>, <BabelSynset: WIKI:EN:Jón_Leifs>, <BabelSynset: WIKIDATA:EN:Mi>, <BabelSynset: mi#n#8>, <BabelSynset: Milan#n#1>, <BabelSynset: WIKI:EN:methylisothiazolinone>, <BabelSynset: WIKI:EN:Mi_(kana)>]
        [<BabelLemma: Mi>, <BabelLemma: milano>, <BabelLemma: Mi>, <BabelLemma: mu>, <BabelLemma: Città_metropolitana_di_Milano>, <BabelLemma: μ>, <BabelLemma: mu>, <BabelLemma: MIT>, <BabelLemma: ミ>, <BabelLemma: methylisothiazolinone>, <BabelLemma: Mi>, <BabelLemma: mi>, <BabelLemma: Mu>, <BabelLemma: MI>, <BabelLemma: み>, <BabelLemma: Fa_bemolle>, <BabelLemma: Milàn>, <BabelLemma: Occupazione_francese_di_Milano>, <BabelLemma: MI>, <BabelLemma: Fa_bemolle>, <BabelLemma: MI>, <BabelLemma: Methylisothiazolinone>, <BabelLemma: Mi>, <BabelLemma: Mi>, <BabelLemma: Milano>, <BabelLemma: Provincia_di_Milano>, <BabelLemma: mi>, <BabelLemma: Jón_Leifs>, <BabelLemma: Mediolanum>, <BabelLemma: Fa♭>, <BabelLemma: Fa♭>, <BabelLemma: Milano_Jazzin'_Festival>, <BabelLemma: provincia_di_Milano>, <BabelLemma: Metilisotiazolinone>, <BabelLemma: Μ>]
    piace
        [<BabelSynset: like#v#2>, <BabelSynset: like#v#2>, <BabelSynset: gratify#v#1>, <BabelSynset: WIKT:EN:fond>, <BabelSynset: delight#v#1>, <BabelSynset: care#v#3>, <BabelSynset: like#v#3>, <BabelSynset: enjoy#v#3>]
        [<BabelLemma: dilettare>, <BabelLemma: piacere>, <BabelLemma: piace>, <BabelLemma: piacere>, <BabelLemma: compiacere>, <BabelLemma: accontentare>, <BabelLemma: assecondare>, <BabelLemma: godere>, <BabelLemma: accontentare>, <BabelLemma: prediligere>, <BabelLemma: provare_gioia>, <BabelLemma: amare>, <BabelLemma: soddisfare>, <BabelLemma: volere_bene>, <BabelLemma: deliziare>, <BabelLemma: piacere>, <BabelLemma: contentare>, <BabelLemma: piacere>, <BabelLemma: gratificare>, <BabelLemma: piacere>, <BabelLemma: piacere>, <BabelLemma: piacere>, <BabelLemma: appagare>, <BabelLemma: soddisfare>, <BabelLemma: gratificare>, <BabelLemma: piace>, <BabelLemma: appagare>, <BabelLemma: preferire>, <BabelLemma: contentare>, <BabelLemma: piacere>]
    la
        [<BabelSynset: WIKI:EN:La_(genus)>, <BabelSynset: WIKIDATA:NL:La>, <BabelSynset: WIKIDATA:EN:alif>, <BabelSynset: WIKI:EN:English_articles>, <BabelSynset: WIKI:EN:La_(Tarzan)>, <BabelSynset: la#n#3>, <BabelSynset: lanthanum#n#1>]
        [<BabelLemma: lantanio>, <BabelLemma: numero_atomico_57>, <BabelLemma: i>, <BabelLemma: La>, <BabelLemma: lo>, <BabelLemma: ا>, <BabelLemma: ʼalif_madda>, <BabelLemma: Lanthanio>, <BabelLemma: ʼalif_makṣūra>, <BabelLemma: ʾalif>, <BabelLemma: La>, <BabelLemma: La>, <BabelLemma: la>, <BabelLemma: Lām-alif>, <BabelLemma: le>, <BabelLemma: il>, <BabelLemma: gl'>, <BabelLemma: La>, <BabelLemma: l'>, <BabelLemma: Alif>, <BabelLemma: lah>, <BabelLemma: Alif_wasla>, <BabelLemma: Lām_ʼalif>, <BabelLemma: La>, <BabelLemma: لا>, <BabelLemma: articoli_inglesi>, <BabelLemma: gli>, <BabelLemma: la>]
    pizza
        [<BabelSynset: WIKIDATA:EN:Pizza>, <BabelSynset: bore#n#1>, <BabelSynset: reel#n#1>, <BabelSynset: pizza#n#1>, <BabelSynset: reel#n#1>, <BabelSynset: WIKIDATA:EN:Pizza>, <BabelSynset: pizza#n#1>, <BabelSynset: bore#n#1>]
        [<BabelLemma: DJ_Pizza>, <BabelLemma: Pizza_tonda>, <BabelLemma: Pizza_al_taglio>, <BabelLemma: noioso>, <BabelLemma: noia>, <BabelLemma: Pizza_in_teglia>, <BabelLemma: pittima>, <BabelLemma: pizza_surgelata>, <BabelLemma: bobina>, <BabelLemma: pizza>, <BabelLemma: pizze>, <BabelLemma: Dj_Pizza>, <BabelLemma: pizza>, <BabelLemma: Pizza>, <BabelLemma: pizza>, <BabelLemma: Pizza_a_taglio>, <BabelLemma: pasta_della_pizza>, <BabelLemma: forno_per_la_pizza>, <BabelLemma: mattone>, <BabelLemma: Dj_Pizza>, <BabelLemma: mattone>, <BabelLemma: impiastro>, <BabelLemma: lagna>, <BabelLemma: DJ_Pizza>, <BabelLemma: forno_da_pizza>, <BabelLemma: Pizza_a_taglio>, <BabelLemma: pizza_congelata>, <BabelLemma: Pizza_classica>, <BabelLemma: pasta_della_pizza>, <BabelLemma: pizze>, <BabelLemma: pizza_pie>, <BabelLemma: pizza_congelata>, <BabelLemma: forno_per_la_pizza>, <BabelLemma: cataplasma>, <BabelLemma: Pizza_alla_pala>, <BabelLemma: Pizza_tonda>, <BabelLemma: noia>, <BabelLemma: bobina>, <BabelLemma: pizza>, <BabelLemma: lagna>, <BabelLemma: pasta_per_pizza>, <BabelLemma: pasta_per_pizza>, <BabelLemma: pizza>, <BabelLemma: pizza>, <BabelLemma: pittima>, <BabelLemma: pizza_surgelata>, <BabelLemma: cataplasma>, <BabelLemma: impiastro>, <BabelLemma: Pizza_alla_pala>, <BabelLemma: Pizza_in_teglia>, <BabelLemma: Pizza_classica>, <BabelLemma: noioso>, <BabelLemma: pizza_pie>, <BabelLemma: palla>, <BabelLemma: forno_da_pizza>, <BabelLemma: Pizza_al_taglio>, <BabelLemma: palla>, <BabelLemma: Pizza>]

## TODO
- add tests
- find a better location for the `babelnet` configuration (`~/babelnet_data` ?)
- speed-up synsets retrieval
    - convert BN to a simpler/faster database?
    - build a lemma-synset external index?
## DONE
- mapped other spacy POS types to Babelnet POS types
- filter out tokens with unmapped POS
