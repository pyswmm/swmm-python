#!/bin/bash
set -e -x

# Install a system package required by our library
sudo yum install -y swig

# Compile wheels
for PYBIN in /opt/python/*/bin; do
    ${PYBIN}/python -m venv ./build-env
    source ./build-env/bin/activate 
    ${PYBIN}/pip wheel --wheel-dir=./dist ./swmm-toolkit
done

# Bundle external shared libraries into the wheels
#for whl in wheelhouse/*.whl; do
#    auditwheel repair $whl -w ./wheelhouse/
#done

# Install packages and test
#for PYBIN in /opt/python/*/bin/; do
#    ${PYBIN}pip install pytest numpy
#    ${PYBIN}pip install --no-index --find-links=./dist swmm-toolkit
#    pytest
#done