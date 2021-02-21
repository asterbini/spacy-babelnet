## Spacy Babelnet

A Spacy pipeline component that annotates tokens with their corresponding Babelnet Synsets (and Lemmas).
The synsets are searched only in the specified language, but other languages can be retrieved through Babelnet.
If the token has a POS annotation, the synsets are searched only with that POS.
Notice that Babelnet uses only the 4 main POS tags: `NAME,ADJ,VERB,ADV`.
Only tokens that map to these 4 types are searched in BabelNet.

### Build and install the `babelnet` module
The `babelnet` module is a python wrapper to the Babelnet API jars
- install the `jcc` and `openjdk` packages \
  `conda install jcc openjdk`
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
import spacy, babelnet
from spacy_babelnet import BabelnetAnnotator

nlp = spacy.load('it_core_news_lg')	# spacy 3

# with spacy 3
nlp.add_pipe('babelnet', config={
	#'domain': babelnet.BabelDomain.BUSINESS_INDUSTRY_AND_FINANCE.value,
	'source': babelnet.BabelSenseSource.OMWN_IT.toString()
	})

doc = nlp('Mi piace la pizza')    # I like pizza
for token in doc:
    print(token, token.pos_, token._.babelnet.synsets(), token._.babelnet.lemmas(), sep='\n\t')
```
That produces the output

	Mi
        PRON
        []
        []
	piace
        VERB
        [<BabelSynset: bn:00090362v__like#v#2>, <BabelSynset: bn:00086519v__delight#v#1>, <BabelSynset: bn:00090363v__like#v#3>, <BabelSynset: bn:00087646v__enjoy#v#3>, <BabelSynset: bn:00084526v__wish#v#2>]
        [<BabelLemma: piacere>, <BabelLemma: contentare>, <BabelLemma: provare_gioia>, <BabelLemma: piacere>, <BabelLemma: assecondare>, <BabelLemma: dilettare>, <BabelLemma: preferire>, <BabelLemma: compiacere>, <BabelLemma: piacere>, <BabelLemma: godere>, <BabelLemma: accontentare>, <BabelLemma: appagare>, <BabelLemma: piace>, <BabelLemma: deliziare>, <BabelLemma: gratificare>, <BabelLemma: piacere>, <BabelLemma: prediligere>, <BabelLemma: piacere>, <BabelLemma: amare>, <BabelLemma: soddisfare>]
	la
        DET
        []
        []
	pizza
        NOUN
        [<BabelSynset: bn:00062694n__pizza#n#1>, <BabelSynset: bn:00066766n__reel#n#1>, <BabelSynset: bn:00012225n__bore#n#1>]
        [<BabelLemma: pizza_al_taglio>, <BabelLemma: mattone>, <BabelLemma: pizzetta>, <BabelLemma: pizza_surgelata>, <BabelLemma: impiastro>, <BabelLemma: pizza_a_taglio>, <BabelLemma: pizza_congelata>, <BabelLemma: pizza_pie>, <BabelLemma: pizze>, <BabelLemma: palla>, <BabelLemma: pasta_della_pizza>, <BabelLemma: bobina>, <BabelLemma: pizza>, <BabelLemma: noioso>, <BabelLemma: pizza>, <BabelLemma: pizza>, <BabelLemma: pizza_classica>, <BabelLemma: noia>, <BabelLemma: forno_da_pizza>, <BabelLemma: lagna>, <BabelLemma: pasta_per_pizza>, <BabelLemma: cataplasma>, <BabelLemma: pizza_tonda>, <BabelLemma: pizzette>, <BabelLemma: pizza_in_teglia>, <BabelLemma: pittima>, <BabelLemma: forno_per_la_pizza>, <BabelLemma: pizza_alla_pala>]



## TODO
- add tests
- find a better location for the `babelnet` configuration (``~/babelnet_data`` ?)
- speed-up synsets retrieval
    - convert BN to a simpler/faster database?
    - build a lemma-synset external index?
## DONE
- added domain and source parameters
- added (word,pos) caching of synsets shared at class level, with json save/load
- mapped other spacy POS types to Babelnet POS types
- filter out tokens with unmapped POS
- moved to faster LKB queries
- added source selection
