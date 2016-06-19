#!/usr/bin/env python
import os
from codecs import open
from setuptools import setup, find_packages
import imp

here = os.path.abspath(os.path.dirname(__file__))
__version__ = imp.load_source('landsat8util.version', 'landsat8util/version.py').__version__

# get the dependencies and installs
with open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' not in x]

setup(
    name='landsat8util',
    version=__version__,
    author='Matthew Hanson (matthewhanson), Alireza J (scisco)',
    description='Landsat-8 utility for search, download, and processing',
    url='https://github.com/sat-utils/landsat8-util',
    license='MIT',
    classifiers=[
        'Framework :: Pytest',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: Freeware',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    scripts=['bin/landsat8'],
    install_requires=install_requires,
    dependency_links=dependency_links,
    tests_require=['nose'],
)
