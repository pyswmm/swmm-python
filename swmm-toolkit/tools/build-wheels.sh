#!/bin/bash
set -e -x


# Install a system package required by our library
sudo yum install -y swig


# Setup and build in swmm-toolkit dir
mkdir -p ./dist
cd swmm-toolkit

# Build wheels
for PYBIN in /opt/python/*/bin; do
    if [ ${PYBIN} != "/opt/python/cp35-cp35m/bin" ]; then
        # Setup python virtual environment for build
        ${PYBIN}/python -m venv --clear ./build-env
        source ./build-env/bin/activate

        # Install build requirements
        python -m pip install setuptools wheel scikit-build cmake

        # Build wheel
        python setup.py bdist_wheel
        mv ./dist/*.whl ../dist/

        # cleanup
        python setup.py clean
        deactivate
    fi
done

# Cleanup
rm -rf ./build-env


# Repairing and testing from swmm-python directory
cd ..

# Bundle external shared libraries into the wheels
for whl in ./dist/*-linux_x86_64.whl; do
    auditwheel repair $whl -w ./dist
done


# Install packages and test
for PYBIN in /opt/python/*/bin; do
    if [ ${PYBIN} != "/opt/python/cp35-cp35m/bin" ]; then
        # Setup python virtual environment for test
        ${PYBIN}/python -m venv --clear ./test-env
        source ./test-env/bin/activate

        python -m pip install pytest numpy aenum==2.2.4

        python -m pip install --verbose --no-index --find-links=./dist swmm_toolkit
        pytest

        deactivate
    fi
done

# Cleanup 
rm -rf ./test-env