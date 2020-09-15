#!/bin/bash

#
# Builds swig from source and installes
#

yum install -y pcre-devel

curl -L http://prdownloads.sourceforge.net/swig/swig-4.0.2.tar.gz > swig-4.0.2.tar.gz

tar xvzf swig-4.0.2.tar.gz

cd swig-4.0.2

./configure && make

make install
