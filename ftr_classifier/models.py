#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:57:28 2019

@author: cole
"""
#load spacy
import spacy

#import models
#english
try:    
    en = spacy.load('en')
except OSError:
    print('Downloading English language model for the spaCy\n'
          "(don't worry, this will only happen once)")
    spacy.cli.download('en')
    en = spacy.load('en')
    
#dutch
try:    
    nl = spacy.load('nl')
except OSError:
    print('Downloading Dutch language model for the spaCy\n'
          "(don't worry, this will only happen once)")
    spacy.cli.download('nl')
    nl = spacy.load('nl')
    
try:    
    de = spacy.load('de')
except OSError:
    print('Downloading German language model for the spaCy\n'
          "(don't worry, this will only happen once)")
    spacy.cli.download('de')
    de = spacy.load('de')

#make MODELS dictionary
MODELS = {'english':en,
          'dutch':nl,
          'german':de}