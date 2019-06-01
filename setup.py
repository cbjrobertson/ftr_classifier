#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name='ftr_classifier',
      py_modules=['ftr_classifier'],
      url = 'https://github.com/cbjrobertson/ftr_classifier.git',
      author = 'cole robertson',
      author_email = 'cbjrobertson@gmail.com',
      version = '1.0.2',
      license = 'MIT',
      packages=find_packages(),
      description = "classifies english, dutch and german sentence  in terms of how they refer to the future.",
      install_requires=[
            "spacy==2.4.1",
            "pandas==0.24.2",
            'pathlib==1.0.1; python_version < "3.4"',
                        ],
        python_requires='==3.6.*',
        download_url='https://github.com/cbjrobertson/future_modality/archive/1.0.2.tar.gz',
        key_words = ['natural-language-processing'],
        classifiers = []
      )
