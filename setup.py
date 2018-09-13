#!/usr/bin/env python

import sys

try:
    from setuptools import setup
except ImportError:
    print('Flask-Webpack needs setuptools in order to build. ' +
          'Install it using your package manager ' +
          '(usually python-setuptools) or via pip (pip install setuptools).')
    sys.exit(1)

long_description = None

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='Flask-Webpack-Fork',
    version=open('VERSION', 'r').read()[:-1],
    author='Nick Janetakis, 5kyc0d3r',
    author_email='nick.janetakis@gmail.com',
    url='https://github.com/5kyc0d3r/flask-webpack',
    description='Flask extension for managing assets with Webpack.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    license='GPLv3',
    install_requires=['setuptools', 'Flask'],
    tests_require=['pytest'],
    packages=['flask_webpack'],
    package_data={'Flask-Webpack-Fork': ['VERSION']},
    zip_safe=False,
    data_files=[]
)
