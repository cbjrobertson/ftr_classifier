#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""
#imports 
import spacy
import ftr_classifier.ftr_classify as ftr

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