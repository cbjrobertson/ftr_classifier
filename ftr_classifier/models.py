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
    en = spacy.load('en_core_web_sm')
except OSError:
    print('Downloading English language model for the spaCy\n'
          "(don't worry, this will only happen once)")
    spacy.cli.download('en_core_web_sm')
    en = spacy.load('en_core_web_sm')
    
#dutch
try:    
    nl = spacy.load('nl_core_news_sm')
except OSError:
    print('Downloading Dutch language model for the spaCy\n'
          "(don't worry, this will only happen once)")
    spacy.cli.download('nl')
    nl = spacy.load('nl_core_news_sm')
    
try:    
    de = spacy.load('de_core_news_sm')
except OSError:
    print('Downloading German language model for the spaCy\n'
          "(don't worry, this will only happen once)")
    spacy.cli.download('de_core_news_sm')
    de = spacy.load('de_core_news_sm')

#make MODELS dictionary
MODELS = {'english':en,
          'dutch':nl,
          'german':de}