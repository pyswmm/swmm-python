#!/bin/bash
set -e -u -x

function repair_wheel {
    wheel="$1"
    if ! auditwheel show "$wheel"; then
        echo "Skipping non-platform wheel $wheel"
    else
        auditwheel repair "$wheel" --plat "$PLAT" -w /io/dist/
    fi
}

# Install a system package required by our library
yum install -y swig

# Compile wheels
cd /io/swmm-toolkit/
for PYBIN in /opt/python/*/bin; do
    # export PYTHON_INCLUDE_DIR=$(${PYBIN}/python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")
    # export PYTHON_LIBRARY=$(${PYBIN}/python -c "import distutils.sysconfig as sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
    "${PYBIN}/pip" install six
    "${PYBIN}/python" setup.py bdist_wheel
done

# Bundle external shared libraries into the wheels
for whl in dist/*.whl; do
    repair_wheel "$whl"
done

# # Install packages and test
# for PYBIN in /opt/python/*/bin/; do
#     "${PYBIN}/pip" install python-manylinux-demo --no-index -f /io/wheelhouse
#     (cd "$HOME"; "${PYBIN}/nosetests" pymanylinuxdemo)
# done
