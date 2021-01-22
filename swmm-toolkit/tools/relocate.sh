#!/bin/bash

#
#  relocate.sh - Relocate lib to install/extern for Linux
#
#  Date created: Jan 21, 2021
#
#  Author:       See AUTHORS
#
#  Arguments:
#    1 - Path to library
#


# Check for required arguments
if [[ -z "$1" ]]; then
    echo "ERROR: Required argument is missing"
    exit 1
fi

echo "INFO: Relocating ... $1"

base=${1##*/}
chmod 755 extern/${base}


# Changes load path for lib in libswmm5
patchelf --set-rpath '$ORIGIN/FKY' lib/libswmm5.so/*