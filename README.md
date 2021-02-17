## Spacy Babelnet

A Spacy pipeline component that annotates tokens with their corresponding Babelnet Synsets (and Lemmas).
The synsets are searched only in the specified language, but other languages can be retrieved through Babelnet.
If the token has a POS annotation, the synsets are searched only with that POS.
Notice that Babelnet uses only the 4 main POS tags: `NAME,ADJ,VERB,ADV`.
Only tokens that map to these 4 types are searched in BabelNet.

### Build and install the `babelnet` module
The `babelnet` module is a python wrapper to the Babelnet API jars
- install the `jcc` and `openjdk` packages \
  `anaconda install jcc openjdk`
- or else \
  `pip install jcc` \
    and install `openjdk` for your Linux distribution
- edit `Makefile` and set `JNI_DIR` to the directory containing `include/jni.h`
- download and unzip the Babelnet-API archive version 5.0 \
  `make get_api`
- build and install the `babelnet` module \
  `make babelnet`

### Build and install the `spacy_babelnet` module
- `make spacy-babelnet` \
  or else
- `python setup.py install`

### Copy the config directory containing your key
The `babelnet` module must find the `config` directory in the current directory. 
Copy the `config` directory and edit the `config/babelnet.var.properties` to add your BabelNet API key.

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
nlp.add_pipe('babelnet')    # TODO: example with source argument (optional)

doc = nlp('Mi piace la pizza')    # I like pizza
for token in doc:
    print(token, token.pos_, token._.babelnet.synsets(), token._.babelnet.lemmas(), sep='\n\t')
```
That produces the output

    mi
        PRON
        []
        []

    piace
        VERB
        [<BabelSynset: like#v#2>, <BabelSynset: like#v#2>, <BabelSynset: gratify#v#1>, <BabelSynset: delight#v#1>, <BabelSynset: care#v#3>, <BabelSynset: enjoy#v#3>, <BabelSynset: like#v#3>]
        [<BabelLemma: piace>, <BabelLemma: piace>, <BabelLemma: piacere>, <BabelLemma: prediligere>, <BabelLemma: contentare>, <BabelLemma: piacere>, <BabelLemma: accontentare>, <BabelLemma: appagare>, <BabelLemma: piacere>, <BabelLemma: contentare>, <BabelLemma: piacere>, <BabelLemma: amare>, <BabelLemma: gratificare>, <BabelLemma: piacere>, <BabelLemma: accontentare>, <BabelLemma: provare_gioia>, <BabelLemma: appagare>, <BabelLemma: piacere>, <BabelLemma: gratificare>, <BabelLemma: soddisfare>, <BabelLemma: compiacere>, <BabelLemma: assecondare>, <BabelLemma: soddisfare>, <BabelLemma: godere>, <BabelLemma: preferire>, <BabelLemma: piacere>, <BabelLemma: dilettare>, <BabelLemma: deliziare>]

    la
        DET
        []
        []

    pizza
        NOUN
        [<BabelSynset: bore#n#1>, <BabelSynset: pizza#n#1>, <BabelSynset: reel#n#1>, <BabelSynset: reel#n#1>, <BabelSynset: pizza#n#1>, <BabelSynset: bore#n#1>]
        [<BabelLemma: forno_per_la_pizza>, <BabelLemma: cataplasma>, <BabelLemma: Pizza_tonda>, <BabelLemma: impiastro>, <BabelLemma: cataplasma>, <BabelLemma: pizza_pie>, <BabelLemma: noia>, <BabelLemma: Pizza_tonda>, <BabelLemma: pizza>, <BabelLemma: pizza_congelata>, <BabelLemma: noioso>, <BabelLemma: palla>, <BabelLemma: pizza>, <BabelLemma: bobina>, <BabelLemma: pizza>, <BabelLemma: lagna>, <BabelLemma: pizza>, <BabelLemma: noia>, <BabelLemma: pizza_congelata>, <BabelLemma: Pizza_a_taglio>, <BabelLemma: Pizza_alla_pala>, <BabelLemma: pizza>, <BabelLemma: Pizza_al_taglio>, <BabelLemma: palla>, <BabelLemma: Pizza_a_taglio>, <BabelLemma: mattone>, <BabelLemma: Pizza_classica>, <BabelLemma: Pizza_in_teglia>, <BabelLemma: pittima>, <BabelLemma: pasta_della_pizza>, <BabelLemma: forno_da_pizza>, <BabelLemma: pittima>, <BabelLemma: lagna>, <BabelLemma: pizze>, <BabelLemma: Pizza_al_taglio>, <BabelLemma: pasta_della_pizza>, <BabelLemma: pizza>, <BabelLemma: noioso>, <BabelLemma: forno_da_pizza>, <BabelLemma: Pizza_in_teglia>, <BabelLemma: pizza_surgelata>, <BabelLemma: forno_per_la_pizza>, <BabelLemma: Pizza_classica>, <BabelLemma: pasta_per_pizza>, <BabelLemma: pizze>, <BabelLemma: bobina>, <BabelLemma: pasta_per_pizza>, <BabelLemma: mattone>, <BabelLemma: Pizza_alla_pala>, <BabelLemma: pizza_pie>, <BabelLemma: impiastro>, <BabelLemma: pizza_surgelata>]


## TODO
- add tests
- find a better location for the `babelnet` configuration (``~/babelnet_data`` ?)
- speed-up synsets retrieval
    - convert BN to a simpler/faster database?
    - build a lemma-synset external index?
## DONE
- added (word,pos) caching of synsets shared at class level, with json save/load
- mapped other spacy POS types to Babelnet POS types
- filter out tokens with unmapped POS
- moved to faster LKB queries
- added source selection
