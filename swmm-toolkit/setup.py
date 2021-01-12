#
# setup.py - Setup script for swmm-toolkit python package
#
# Created:    Jul 2, 2018
# Updated:    May 7, 2020
#
#  Author:    See AUTHORS
#
# Suggested Usage:
#   python setup.py build
#   python setup.py bdist_wheel
#   python setup.py sdist
#   python setup.py clean
#

import platform
import subprocess
import pathlib

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
    cmake_args = ["-GVisual Studio 15 2017 Win64"]

elif platform_system == "Darwin":
    cmake_args = ["-GXcode","-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.10"]

else:
    cmake_args = ["-GUnix Makefiles"]


# Filters cmake manifest for wheel build
def exclude_files(cmake_manifest):
    print("INFO: processing cmake manifest")
    exclude_pats = ('runswmm', '.exe', '.cmake', '.h', '.lib')
    return list(filter(lambda name: not (name.endswith(exclude_pats)), cmake_manifest))



# Get the long description from the README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name = "swmm-toolkit",
    version = "0.8.1",

    packages = ["swmm.toolkit"],
    package_dir = {"": "src"},

    zip_safe = False,
    install_requires = ["aenum"],

    cmdclass = {"clean": CleanCommand},
    cmake_args = cmake_args,
    cmake_process_manifest_hook = exclude_files,


    description='OWA SWMM Python Toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/OpenWaterAnalytics/swmm-python',
    
    author='See AUTHORS',
    maintainer_email='tryby.michael@epa.gov',
    license='CC0',

    keywords="swmm5, swmm, stormwater, hydraulics, hydrology, ",
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: C",
        "Development Status :: 4 - Beta",
    ]
)
