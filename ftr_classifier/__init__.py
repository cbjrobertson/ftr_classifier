#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""
#imports
import ftr_classifier.lemma_count as lemma_count
import ftr_classifier.word_lists as word_lists
import ftr_classifier.classify as classify
from ftr_classifier.lemma_count import count_lemmas,format_lemma_df
from ftr_classifier.classify import prepare,score,apply_dominance,classify_df,clean_spacy,_debug_check_words
from ftr_classifier.word_lists import FEATURES,WORD_LISTS,ALL_FEATURES,MAIN_FEATURES,DOMINANT_FEATURES
from ftr_classifier.word_lists import SUBMISSIVE_FEATURES,DOMINATED_FEATURES,SUMMARY_FEATURES,EXTRA_FEATURES,DESIRE

#add versions
from ftr_classifier.info import INFO
__version__ = INFO['version']
description = INFO['description']
long_description = INFO['long_description']
