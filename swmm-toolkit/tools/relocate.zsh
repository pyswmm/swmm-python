#!/usr/bin/env zsh

#
#  relocate.zsh - Relocate lib to install/extern for MacOS
#
#  Date created: May 7, 2020
#
#  Author:       See AUTHORS
#
#  Arguments:
#    1 - Path to library
#

if [[ -z "$1" ]]; then
    echo "ERROR: Required argument is missing"; return 1
fi

echo "INFO: Relocating ... $1"


chmod 755 lib/$1:t


# Grabs current path for lib
IFS=$' '
TOKEN=($( otool -l lib/$1:t | grep LC_ID_DYLIB -A2 | grep name ))
LIB_PATH=${TOKEN[2]}


# Changes load path for lib in _solver.so
install_name_tool -change ${LIB_PATH} @rpath/$1:t src/swmm/toolkit/_solver*.so

# Changes load path for lib in libswmm5
install_name_tool -change ${LIB_PATH} @rpath/$1:t lib/libswmm5.dylib

# Changes id on relocated lib
install_name_tool -id @rpath/$1:t lib/$1:t
