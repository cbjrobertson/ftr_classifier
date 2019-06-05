#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""
#imports
import ftr_classifier.classify
import ftr_classifier.count_lemmas
from ftr_classifier.classify import prepare,score,apply_dominance,classify_df,clean_spacy
from ftr_classifier.count_lemmas import count_lemmas
from ftr_classifier.info import INFO

__version__ = INFO['version']
description = INFO['description']
long_description = INFO['long_description']
