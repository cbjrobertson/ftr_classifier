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
from ftr_classifier.word_lists import WORD_LISTS,LEMMA_MAP

def _make_counts_df(counts,df,lang_col='textLang'):
    
    #initialise serialized dataframe
    d = {'language':[lang for lang in counts for feature in counts[lang] for lemma in counts[lang][feature]],
         'feature':[feature for lang in counts for feature in counts[lang] for lemma in counts[lang][feature]],
         'lemma':[lemma for lang in counts for feature in counts[lang] for lemma in counts[lang][feature]],
         'count':[count for lang in counts for feature in counts[lang] for count in counts[lang][feature].values()],
         'num_responses':[word_sums[lang][0] for lang in counts for feature in counts[lang] for lemma in counts[lang][feature]],
         'num_words':[word_sums[lang][1] for lang in counts for feature in counts[lang] for lemma in counts[lang][feature]]}
    
    #aconvert to dataframe
    dx = pd.DataFrame(d)

    #sort
    dx = dx.sort_values(by=['language','feature','count'],ascending=False)
   
    #return
    return dx

def _counter(df,lang_col='textLang',process_col='final_sentence'):

    #group by language
    df_groups = df.groupby(lang_col)
    
    #counts dict initiate
    COUNTS = deepcopy(WORD_LISTS)

    #add count data
    global word_sums
    word_sums = {}

    #iterate though langauges 
    for lang,dy in df_groups:
        #count uique words and length of dataframe to assign to counts df
        no_responses = len(dy)
        no_words = len(list(itertools.chain.from_iterable(dy['response_clean'].to_list())))
        word_sums[lang] = (no_responses,no_words)
        for feature in COUNTS[lang]:
            #count phrases
            phrase_counts = {phrase : sum(dy[process_col].apply(lambda doc:doc.text.count(phrase)))\
                                      for phrase in COUNTS[lang][feature][0]}
            #sum phrase counts to lemma
            phrase_lemma_counts = {}
            phrase_lemma_counts = {LEMMA_MAP[lang][feature][0][phrase] : (val+LEMMA_MAP[phrase] if phrase in phrase_lemma_counts.keys() else val) for phrase,val in phrase_counts.items()}
            
            #count word
            word_counts = {word : sum(dy[process_col].apply(lambda doc:doc.text.count(word)))\
                           for word in COUNTS[lang][feature][1]}
            
            #sum word counts to lemma
            word_lemma_counts = {}
            phrase_lemma_counts = {LEMMA_MAP[lang][feature][1][word] : (val+LEMMA_MAP[word] if word in word_lemma_counts.keys() else val) for word,val in word_counts.items()}

            #merge two together
            COUNTS[lang][feature] = {**phrase_lemma_counts, **word_lemma_counts}
    return COUNTS


def count_lemmas(df,*args,**kwargs):
    #copy
    df = df.copy()
    
    if 'final_sentence' not in df.columns:
        df = prepare(df)
    #do the counts
    counts = _counter(df,*args,**kwargs)
    counts_df = _make_counts_df(counts,df)
    #return
    return counts_df
