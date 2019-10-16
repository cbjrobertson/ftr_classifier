#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""
#imports
import ftr_classifier.lemma_count 
import ftr_classifier.word_lists
import ftr_classifier.classify
from ftr_classifier.lemma_count import count_lemmas,merge_md
from ftr_classifier.classify import prepare
from ftr_classifier.classify import score
from ftr_classifier.classify import apply_dominance
from ftr_classifier.classify import classify_df
from ftr_classifier.classify import clean_spacy
from ftr_classifier.classify import _debug_check_words
from ftr_classifier.word_lists import FEATURES
from ftr_classifier.word_lists import WORD_LISTS
from ftr_classifier.word_lists import ALL_FEATURES
from ftr_classifier.word_lists import MAIN_FEATURES
from ftr_classifier.word_lists import DOMINANT_FEATURES
from ftr_classifier.word_lists import SUBMISSIVE_FEATURES
from ftr_classifier.word_lists import DOMINATED_FEATURES
from ftr_classifier.word_lists import SUMMARY_FEATURES
from ftr_classifier.word_lists import EXTRA_FEATURES

#add versions
from ftr_classifier.info import INFO
__version__ = INFO['version']
description = INFO['description']
long_description = INFO['long_description']
