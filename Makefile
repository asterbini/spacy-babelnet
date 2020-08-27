#######################################################################
#### Fit this variable as for your setup ####

## Directory containing the JDK installation with include/jni.h and include/linux/jni_md.h
JNI_DIR:=/opt/anaconda3/envs/MLC
#JNI_DIR:=/usr/lib/jvm/java

#######################################################################

# BabelNet-API-4.0.1 file
BN_API_URL:=https://babelnet.org/data/4.0/BabelNet-API-4.0.1.zip
# BabelNet API directory once unzipped
BN_DIR=BabelNet-API-4.0.1

#######################################################################

all:
	@if [ ! -e $(JNI_DIR)/include/jni.h ] ; then echo "Missing jni.h, install openjdk, edit Makefile and set JNI_DIR variable" ; fi
	@echo "make get_api		# get and unzip the BabelNet API"
	@echo "make babelnet		# build and install the babelnet module with JCC 3.8"
	@echo "make spacy-babelnet	# build and install the spacy_babelnet module"

# download and unzip the API
get_api:
	wget $(BN_API_URL)
	unzip $(BN_DIR).zip

# copy this makefile in the BabelNet-API- and build/install the babelnet module
babelnet:
	cp Makefile $(BN_DIR)
	make -C $(BN_DIR) compile install

# build and install the spacy-babelnet module
spacy-babelnet:
	python setup.py install

#######################################################################

CPLUS_INCLUDE_PATH:=$(JNI_DIR)/include:$(JNI_DIR)/include/linux

JARS+=babelnet-api-4.0.1.jar
JARS+=lib/babelscape-data-commons-1.0.jar

INCLUDE+=commons-beanutils-1.7.0.jar
INCLUDE+=commons-beanutils-core-1.7.0.jar
INCLUDE+=commons-codec-1.8.jar
INCLUDE+=commons-collections-3.2.jar
INCLUDE+=commons-configuration-1.5.jar
INCLUDE+=commons-digester-1.8.jar
INCLUDE+=commons-lang-2.3.jar
INCLUDE+=commons-logging-1.1.jar
INCLUDE+=gson-2.8.2.jar
INCLUDE+=guava-23.0.jar
INCLUDE+=httpclient-4.3.6.jar
INCLUDE+=httpcore-4.3.3.jar
INCLUDE+=icu4j-56.1.jar
INCLUDE+=jwi-2.2.3.jar
INCLUDE+=lcl-jlt-2.4.jar
INCLUDE+=logback-classic-1.2.3.jar
INCLUDE+=logback-core-1.2.3.jar
INCLUDE+=lucene-analyzers-common-7.2.0.jar
INCLUDE+=lucene-core-7.2.0.jar
INCLUDE+=lucene-queries-7.2.0.jar
INCLUDE+=lucene-queryparser-7.2.0.jar
INCLUDE+=lucene-sandbox-7.2.0.jar
INCLUDE+=slf4j-api-1.7.25.jar

PACKAGES+=com.babelscape.util
PACKAGES+=com.babelscape.pipeline.annotation.maps
PACKAGES+=com.babelscape.babelmorph
PACKAGES+=com.babelscape.util.tags
PACKAGES+=it.uniroma1.lcl.babelnet.data
PACKAGES+=it.uniroma1.lcl.babelnet.impl
PACKAGES+=it.uniroma1.lcl.babelnet.iterators
PACKAGES+=it.uniroma1.lcl.babelnet.resources
PACKAGES+=it.uniroma1.lcl.kb
PACKAGES+=it.uniroma1.lcl.jlt.util
PACKAGES+=it.uniroma1.lcl.babelnet
PACKAGES+=java.util
PACKAGES+=java.lang

CLASSES+=it.uniroma1.lcl.kb.LKB
CLASSES+=it.uniroma1.lcl.kb.LKBQuery
CLASSES+=it.uniroma1.lcl.babelnet.BabelNetQuery
CLASSES+=it.uniroma1.lcl.babelnet.BabelNet
COLLECTIONS+=--sequence java.util.List 'size:()I' 'get:(I)Ljava/lang/Object;'
MAPPINGS=
JCC:=CPLUS_INCLUDE_PATH=$(CPLUS_INCLUDE_PATH) python -m jcc

OPTS=
OPTS+=--python babelnet
OPTS+=--version 4.0.1-2
OPTS+=--debug
OPTS+=--shared
#OPTS+=--wheel

compile:
	$(JCC) \
	$(patsubst %,--include lib/%,$(INCLUDE)) \
	$(patsubst %,--jar %,$(JARS)) \
	$(patsubst %,--package %,$(PACKAGES)) \
	$(CLASSES) \
	$(COLLECTIONS) \
	$(MAPPINGS) \
	$(OPTS) --build
install:
	$(JCC) \
	$(patsubst %,--include lib/%,$(INCLUDE)) \
	$(patsubst %,--jar %,$(JARS)) \
	$(patsubst %,--package %,$(PACKAGES)) \
	$(CLASSES) \
	$(COLLECTIONS) \
	$(MAPPINGS) \
	$(OPTS) --install

################################################################
