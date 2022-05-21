#!/bin/bash

#
#  build-wheels.sh - in a manyLinux docker image using dockcross
#
#  Date created: Feb 2, 2021
#  Date modified: Jun 7, 2021
#
#  Author:       See AUTHORS
#

set -e -x


# Install a system package required by our library
sudo yum install -y swig


# Setup and build in swmm-toolkit dir
mkdir -p ./dist
cd swmm-toolkit

# Build wheels
for PYBIN in /opt/python/cp{37,38,39,310}*/bin; do
    # Setup python virtual environment for build
    ${PYBIN}/python -m venv --clear ./build-env
    source ./build-env/bin/activate

    # Install build requirements
    python -m pip install -r build-requirements.txt

    # Build wheel
    python setup.py bdist_wheel
    mv ./dist/*.whl ../dist/

    # cleanup
    python setup.py clean
    deactivate
done

# Cleanup
rm -rf ./build-env


# Repairing and testing from swmm-python directory
cd ..

# Bundle external shared libraries into the wheels
for WHL in ./dist/*-linux_x86_64.whl; do
    auditwheel repair -L '' -w ./dist $WHL
done


# Install packages and test
for PYBIN in /opt/python/cp{37,38,39,310}*/bin; do
    # Setup python virtual environment for test
    ${PYBIN}/python -m venv --clear ./test-env
    source ./test-env/bin/activate

    python -m pip install -r swmm-toolkit/test-requirements.txt

    python -m pip install --verbose --no-index --find-links=./dist swmm_toolkit
    pytest

    deactivate
done

# Cleanup
rm -rf ./test-env
