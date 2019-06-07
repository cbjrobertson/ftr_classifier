#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 00:17:04 2019

@author: cole
"""
import pandas as pd
import ftr_classifier as ftr


# =============================================================================
# # file types 
# When working with languages which use a lot of non-ascii characters (i.e. 
# Dutch and German), it is recommended that researchers DO NOT use .csv file 
# formats. Despite claims to support utf-8, some versions of Excel mangle 
# non-ascii characters when opening and closing .csv files. These vignettes 
# therefore use python's endemic object permanence file format, pickle. 
# If a users wants to save to a format openable outside of python, it is 
# recommended they use .xlsx formats. However, doing so will mangle all spacy 
# docs stored in a dataframe. If the user wants to save and reload python data
# objects (lists, spacy docs, etc.), pickle is recommended.
# =============================================================================

# =============================================================================
# # # import example data
# =============================================================================
df = pd.read_pickle('./toy_data/example.pkl')

# =============================================================================
# classify dataframe 
# =============================================================================
df_class = ftr.classify_df(df)

# =============================================================================
# count lemma frequency
# =============================================================================
df_lemma_count = ftr.count_lemmas(df_class)

# =============================================================================
# ## Clean up dataframe
# It is recommended that after calling ftr.classify_df() and ftr.count_lemmas(),
# the user call ftr.clean_spacy(), which drops the automatically created columns
# containing spacy documents. These are memory intensive, and not necessary to keep
# once the responses have been classified and counted.
# =============================================================================
df_class = ftr.clean_spacy(df_class)

# =============================================================================
# save to desired format (pickle or .xlxs) recommended
# =============================================================================
##pickle
df_class.to_pickle('df_class.pkl')
df_lemma_count.to_pickle('df_lemma_count.pkl')

##excel
df_class.to_excel('df_class.xlsx',index=False)
df_lemma_count.to_excel('df_lemma_count.xlsx',index=False)