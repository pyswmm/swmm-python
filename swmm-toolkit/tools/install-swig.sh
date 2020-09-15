#!/bin/bash

#
# Builds swig from source and installes
#


CUR_DIR=${PWD}
cd /tmp


yum install -y pcre-devel

curl -L http://prdownloads.sourceforge.net/swig/swig-4.0.2.tar.gz > swig-4.0.2.tar.gz
tar xzf swig-4.0.2.tar.gz


cd swig-4.0.2

./configure > /dev/null
make > /dev/null

make install


cd ${CUR_DIR}
