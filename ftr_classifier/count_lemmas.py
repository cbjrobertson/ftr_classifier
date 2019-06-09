#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""
#load libraries
import pandas as pd
from copy import deepcopy
import itertools

#local imports
from ftr_classifier.classify import prepare
from ftr_classifier.word_lists import LEMMA_MAP

def _make_counts_df(counts,lang_col='language'):
    
    #initialise serialized dataframe    
    d = {'language':[],
         'feature':[],
         'lemma':[],
         'count':[],
         'num_responses':[],
         'num_words':[]}
    
    #write into lists
    for lang,lang_dict in counts.items():
        for feature,feature_dict in lang_dict.items():
            for lemma,count in feature_dict.items():
                d['language'] += [lang]
                d['feature'] += [feature]
                d['lemma'] += [lemma]
                d['count'] += [count]
                d['num_responses'] += [word_sums[lang][0]]
                d['num_words'] += [word_sums[lang][1]]
                
    #aconvert to dataframe
    dx = pd.DataFrame(d)

    #sort
    dx = dx.sort_values(by=['language','feature','count'],ascending=False)
   
    #drop will and go future (as the lemmas are alredy counted in future)
    dx = dx[~dx['feature'].isin(['will_future','go_future'])]
    #return
    return dx

def _count_to_lemma_map(feature_lem_map,lexeme_counts):
    #initialize lemma dict
    lemma_counts = {}
    #map lexemes onto lemmas/stems
    for lexeme,lemma in feature_lem_map.items():
        if lemma in lemma_counts.keys():
            lemma_counts[lemma] += lexeme_counts[lexeme]
        else:
            lemma_counts[lemma] = lexeme_counts[lexeme]
    return lemma_counts

def _counter(df,lang_col='language',phrase_col='final_sentence',word_col='response_clean'):
    #group by language
    df_groups = df.groupby(lang_col)
    
    #counts dict initiate
    counts = deepcopy(WORD_LISTS)
    
    #add count data
    global word_sums
    word_sums = {}

    #iterate though langauges 
    for lang,dy in df_groups:
        #count uique words and length of dataframe to assign to counts df
        no_responses = len(dy)
        no_words = len(list(itertools.chain.from_iterable(dy['response_clean'].to_list())))
        word_sums[lang] = (no_responses,no_words)
        for feature in counts[lang]:
            #count phrases
            phrase_counts = {phrase : sum(dy[phrase_col].apply(lambda doc:doc.text.lower().count(phrase)))\
                                      for phrase in counts[lang][feature][0]}
            
            #count phrase lemmas
            phrase_lemma_counts = _count_to_lemma_map(LEMMA_MAP[lang][feature][0],phrase_counts)

            #count word
            word_counts = {word : sum(dy[word_col].apply(lambda response_clean: response_clean.count(word)))\
                           for word in counts[lang][feature][1]}
            
            #count word lemmas
            word_lemma_counts = _count_to_lemma_map(LEMMA_MAP[lang][feature][1],word_counts)

            #merge two together
            counts[lang][feature] = {**phrase_lemma_counts, **word_lemma_counts}
    return counts


def count_lemmas(df,lang_col='language',*args,**kwargs):
    #copy
    df = df.copy()
    
    #set WORD_LISTS as global
    global WORD_LISTS
    
    #import
    from ftr_classifier.word_lists import WORD_LISTS
    
    #get list of working languages
    working_langs = list(set(df[lang_col]))
    
    #take out out of sample lanuages 
    WORD_LISTS = {key:value for (key,value) in WORD_LISTS.items() if key in working_langs}
    
    #re make spacy docs if not present
    if 'final_sentence' not in df.columns:
        df = prepare(df)
    #do the counts
    counts = _counter(df,lang_col=lang_col,*args,**kwargs)
    counts_df = _make_counts_df(counts)
    #return
    return counts_df
