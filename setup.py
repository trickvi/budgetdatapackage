#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

description = "Manage and load Budget Data Packages"
with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name = 'budgetdatapackage',
    version = '0.0.4',
    url = 'https://github.com/tryggvib/budgetdatapackage',
    license = 'GPLv3',
    description = description,
    long_description = long_description,
    maintainer = 'Tryggvi Björgvinsson',
    maintainer_email = 'tryggvi.bjorgvinsson@okfn.org',
    install_requires = ['datapackage>=0.5.2'],
    packages = ['budgetdatapackage'],
    package_dir={'budgetdatapackage': 'budgetdatapackage'},
    package_data={'budgetdatapackage': ['data/*.json']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
