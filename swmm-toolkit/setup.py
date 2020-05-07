#
# setup.py - Setup script for swmm-toolkit python package
#
# Created:    7/2/2018
# Modified:   4/17/2020
#
# Author:     Michael E. Tryby
#             US EPA - ORD/NRMRL
#
# Suggested Usage:
#   python setup.py build
#   python setup.py bdist_wheel
#   python setup.py clean
#

import platform
import subprocess

from skbuild import setup
from setuptools import Command


# Determine platform
platform_system = platform.system()


class CleanCommand(Command):
    ''' Cleans project tree '''
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        if platform_system == "Windows":
            cmd = ['del' '/Q', 'tests\\data\\temp_*.*' '&&' \
            'rd' '/s/q', '_cmake_test_compile', '_skbuild', 'dist', '.pytest_cache', \
            'src\\swmm\\toolkit\\swmm_toolkit.egg-info', 'tests\\__pycache__']
            exe = "C:\\Windows\\System32\\cmd.exe"

        elif platform_system == "Linux":
            cmd = ["rm -vrf _skbuild/ dist/ **/build .pytest_cache/ **/__pycache__  \
            **/*.egg-info **/data/temp_*.* **/data/en* **/.DS_Store MANIFEST"]
            exe = "/bin/bash"

        elif platform_system == "Darwin":
            cmd = ['setopt extended_glob nullglob; rm -vrf _skbuild dist **/build .pytest_cache \
            **/__pycache__ **/*.egg-info **/data/(^test_*).* **/data/en* **/.DS_Store MANIFEST']
            exe = '/bin/zsh'

        p = subprocess.Popen(cmd, shell=True, executable=exe)
        p.wait()


# Set Platform specific cmake args here
if platform_system == "Windows":
    cmake_args = ["-GVisual Studio 14 2015 Win64"]

elif platform_system == "Darwin":
    cmake_args = ["-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.10"]

else:
    cmake_args = ["-GUnix Makefiles"]


setup(
    name = "swmm-toolkit",
    version = "0.4.0",

    cmake_args = cmake_args,

    packages = ["swmm.toolkit"],
    package_dir = {"": "src"},
    package_data = {"extern": ["libomp.*"]},

    zip_safe = False,

    install_requires = ["aenum"],

    cmdclass = {"clean": CleanCommand}
)
