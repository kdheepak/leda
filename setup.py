#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os

with open('README.rst') as readme_file:
    readme = readme_file.read()

from pip.req import parse_requirements

here = os.path.abspath(os.path.dirname(__file__))
requirements = [str(ir.req) for ir in parse_requirements(os.path.join(here, 'requirements.txt'), session=False)]

setup(
    name='leda',
    version='0.1.0',
    description="js for jupyter",
    long_description=readme,
    author="Dheepak Krishnamurthy",
    author_email='kdheepak89@gmail.com',
    url='https://github.com/kdheepak/leda',
    packages=[
        'leda',
    ],
    package_dir={'leda':
                 'leda'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='leda',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
