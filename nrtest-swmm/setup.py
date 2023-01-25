# -*- coding: utf-8 -*-

#
#  setup.py
#
#  Author:     Michael E. Tryby
#              US EPA - ORD/NRMRL
#
#  Modified: Jul 28, 2021
#
#  Usage:
#    \>python setup.py bdist_wheel
#
''' Setup up script for nrtest_swmm package. '''


from setuptools import setup


entry_points = {
    'nrtest.compare': [
        'swmm allclose = nrtest_swmm:swmm_allclose_compare',
        'swmm report = nrtest_swmm:swmm_report_compare',
        # Add the entry point for new comparison functions here
    ]
}

setup(
    name='nrtest-swmm',
    version='0.7.0',
    description="SWMM extension for nrtest",

    author="Michael E. Tryby",
    author_email='tryby.michael@epa.gov',
    url='https://github.com/USEPA',

    packages=['nrtest_swmm',],
    scripts=['scripts/report-diff',],
    entry_points=entry_points,

    install_requires=[
        'header_detail_footer>=2.3',
        'nrtest>=0.2.0',
        'numpy>=1.7.0',
        'swmm-toolkit',
    ],

    keywords='nrtest_swmm',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
)
