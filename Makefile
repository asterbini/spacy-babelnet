#######################################################################
#### Fit this variable as for your setup ####

## Directory containing the JDK installation with include/jni.h and include/linux/jni_md.h
#JNI_DIR:=/opt/anaconda3/envs/MLC
JNI_DIR:=/usr/lib/jvm/java

#######################################################################

# BabelNet-API-4.0.1 file
BN_API_URL:=https://babelnet.org/data/4.0/BabelNet-API-4.0.1.zip
# BabelNet API directory once unzipped
BN_DIR=BabelNet-API-4.0.1

#######################################################################

# download and unzip the API
get_api:
	wget $(BN_API_URL)
	unzip $(BN_DIR).zip

# copy this makefile in the BabelNet-API- and build/install the babelnet module
babelnet:
	cp Makefile $(BN_DIR)
	make -C $(BN_DIR) build_install_api

# build and install the spacy-babelnet module
spacy-babelnet:
	python setup.py install

#######################################################################

CPLUS_INCLUDE_PATH:=$(JNI_DIR)/include:$(JNI_DIR)/include/linux

JARS=  --jar babelnet-api-4.0.1.jar
JARS+= --jar lib/babelscape-data-commons-1.0.jar

CP=config:lib:lib/commons-beanutils-1.7.0.jar:lib/commons-beanutils-core-1.7.0.jar:lib/commons-codec-1.8.jar:lib/commons-collections-3.2.jar:lib/commons-configuration-1.5.jar:lib/commons-digester-1.8.jar:lib/commons-lang-2.3.jar:lib/commons-logging-1.1.jar:lib/gson-2.8.2.jar:lib/guava-23.0.jar:lib/httpclient-4.3.6.jar:lib/httpcore-4.3.3.jar:lib/icu4j-56.1.jar:lib/jwi-2.2.3.jar:lib/lcl-jlt-2.4.jar:lib/logback-classic-1.2.3.jar:lib/logback-core-1.2.3.jar:lib/lucene-analyzers-common-7.2.0.jar:lib/lucene-core-7.2.0.jar:lib/lucene-queries-7.2.0.jar:lib/lucene-queryparser-7.2.0.jar:lib/lucene-sandbox-7.2.0.jar:lib/slf4j-api-1.7.25.jar

INCLUDE+=--include lib/commons-beanutils-1.7.0.jar
INCLUDE+=--include lib/commons-beanutils-core-1.7.0.jar
INCLUDE+=--include lib/commons-codec-1.8.jar
INCLUDE+=--include lib/commons-collections-3.2.jar
INCLUDE+=--include lib/commons-configuration-1.5.jar
INCLUDE+=--include lib/commons-digester-1.8.jar
INCLUDE+=--include lib/commons-lang-2.3.jar
INCLUDE+=--include lib/commons-logging-1.1.jar
INCLUDE+=--include lib/gson-2.8.2.jar
INCLUDE+=--include lib/guava-23.0.jar
INCLUDE+=--include lib/httpclient-4.3.6.jar
INCLUDE+=--include lib/httpcore-4.3.3.jar
INCLUDE+=--include lib/icu4j-56.1.jar
INCLUDE+=--include lib/jwi-2.2.3.jar
INCLUDE+=--include lib/lcl-jlt-2.4.jar
INCLUDE+=--include lib/logback-classic-1.2.3.jar
INCLUDE+=--include lib/logback-core-1.2.3.jar
INCLUDE+=--include lib/lucene-analyzers-common-7.2.0.jar
INCLUDE+=--include lib/lucene-core-7.2.0.jar
INCLUDE+=--include lib/lucene-queries-7.2.0.jar
INCLUDE+=--include lib/lucene-queryparser-7.2.0.jar
INCLUDE+=--include lib/lucene-sandbox-7.2.0.jar
INCLUDE+=--include lib/slf4j-api-1.7.25.jar

MAPPING+=--mapping it/uniroma1/lcl/babelnet/BabelNetQuery/Builder 'from:(Lit/uniroma1/lcl/babelnet/Language;)Lit/uniroma1/lcl/babelnet/BabelNetQuery/Builder;'
MAPPING+=--mapping it/uniroma1/lcl/babelnet/BabelNet 'getSynsets:(Lit/uniroma1/lcl/babelnet/BabelNetQuery;)Ljava/lang/List<it/uniroma1/lcl/babelnet/BabelSynset>;'

JCC:=python -m jcc

build_install_api:
	CPLUS_INCLUDE_PATH=$(CPLUS_INCLUDE_PATH) $(JCC) $(INCLUDE) $(JARS) $(MAPPING) --python babelnet --build --install --version 4.0.1

#######################################################################
