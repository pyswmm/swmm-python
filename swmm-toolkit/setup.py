#
# setup.py - Setup script for swmm-toolkit python package
#
# Created:    Jul 2, 2018
# Updated:    Jun 7, 2021
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
import os
from skbuild import setup
from setuptools import Command
import sys

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


# Set up location of wheel libraries depending on build platform and command
# commands that trigger cmake from skbuild.setuptools_wrap._should_run_cmake
commands_that_trigger_cmake = {
        "build",
        "build_ext",
        "develop",
        "install",
        "install_lib",
        "bdist",
        "bdist_dumb",
        "bdist_egg",
        "bdist_rpm",
        "bdist_wininst",
        "bdist_wheel",
        "test",
    }
command = sys.argv[1] if len(sys.argv) > 1 else None
if command in commands_that_trigger_cmake:
    swmm_toolkit_dir= "bin" if platform_system == "Windows" else "lib"
else:
    swmm_toolkit_dir= "swmm-solver"
package_dir = {"swmm_toolkit" : swmm_toolkit_dir, "swmm.toolkit": "src/swmm/toolkit"}


if os.environ.get('SWMM_CMAKE_ARGS') is not None:
    cmake_args = os.environ.get('SWMM_CMAKE_ARGS').split()

# Set Platform specific cmake args here
elif platform_system == "Windows":
    cmake_args = ["-GVisual Studio 17 2022","-Ax64"]

elif platform_system == "Darwin":
    cmake_args = ["-GNinja","-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9"]

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

if platform_system == "Darwin":
    license_files = ['LICENSE.md', 'extern/license-llvm-openmp.txt']
else:
    license_files = ['LICENSE.md']

setup(
    name = "swmm-toolkit",
    version = "0.15.1",

    packages = ["swmm_toolkit", "swmm.toolkit"],
    package_dir = package_dir,

    zip_safe = False,
    install_requires = ["aenum==3.1.11"],

    cmdclass = {"clean": CleanCommand},
    cmake_args = cmake_args,
    cmake_process_manifest_hook = exclude_files,

    description='OWA SWMM Python Toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/OpenWaterAnalytics/swmm-python',

    author='See AUTHORS',
    maintainer_email='bemcdonnell@gmail.com',
    license='CC0',
    license_files=license_files,
    keywords="swmm5, swmm, stormwater, hydraulics, hydrology",
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: C",
        "Development Status :: 5 - Production/Stable",
    ]
)