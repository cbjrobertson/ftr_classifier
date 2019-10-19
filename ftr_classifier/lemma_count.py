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
from ftr_classifier.manage_functions import _load_obj
from ftr_classifier.word_lists import META_FEATURE_MAP,FEATURE_NAME_MAP

#import lemma map
LEMMA_MAP = _load_obj('lemma_map')
META_DATA = _load_obj('meta_data')

def _make_counts_df(counts,lang_col):
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
    
    #add percentage
    dx['percent'] = dx['count']/dx['num_responses']*100
   
    #drop will and go future (as the lemmas are alredy counted in future)
    dx = dx[~dx['feature'].isin(['will_future','go_future'])]
    #return
    return dx

def _count_to_lemma_map(feature_lem_map,lexeme_counts):
    #initialize lemma dict
    lemma_counts = {}
    #map lexemes onto lemmas/stems
    for lexeme,count in lexeme_counts.items():
        lemma = feature_lem_map[lexeme]
        if lemma in lemma_counts.keys():
            lemma_counts[lemma] += count
        else:
            lemma_counts[lemma] = count
    return lemma_counts

def _counter(df,lang_col,process_col='final_sentence',word_col='response_clean'):
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
            phrase_counts = {phrase : sum(dy[process_col].apply(lambda doc:doc.text.lower().count(phrase)))\
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

def _format_md(d,key):
    if key != 'citation':
        if key in d.keys():
            return d[key]
        else:
            return ''
    else:
        if any(x.startswith('cit_key') for x in d.keys()):
            return '; '.join(['\\citeA{{{}}}'.format(val) for key,val in d.items() if key.startswith('cit_key')])
        else:
            return ''
        
def _lookup_md(keys):
    try:
        d = META_DATA[keys[0]][keys[1]][keys[2]]
        meta_data = {'gloss':_format_md(d,'gloss'),
                     'justification':_format_md(d,'justification'),
                     'citation(s)':_format_md(d,'citation')
                     }
    except KeyError:
        meta_data = {'gloss':'','justification':'','citation(s)':''}
    return meta_data

def _format_citations(df,group_col):
    dfg = df.groupby(group_col)
    store = pd.DataFrame()
    for grp,dx in dfg:
        dx['cits'] = [[i.strip() for i in item.split(";") if not i == ''] for item in dx.loc[:,'citation(s)']]
        cits = [item for sublist in dx.cits for item in sublist]
        cits = pd.Series(cits)
        cits = cits[~cits.duplicated()].to_list()
        ref_map = {cit:"\\textsuperscript{{{}}}".format(no+1) for no,cit in enumerate(cits)}
        cit_list = []
        for idx in dx.index:
            cit_list += ["".join(ref_map[c] for c in dx.loc[idx,"cits"])]
        dx.cits = cit_list
        dx["justification"] = [dx.loc[idx,"justification"]+dx.loc[idx,"cits"] for idx in dx.index]
        cits = [a+b for a,b in zip([ref_map[x] for x in cits],cits)]
        dx["citation(s)"] = "; ".join(cits)
        dx = dx.drop('cits',1)
        store = store.append(dx)
    return store
    
def _merge_md(count_df):
    df = count_df.copy()
    key_cols = ['language','feature','lemma']
    dy = pd.concat([df,df[key_cols].apply(lambda keys:pd.Series(_lookup_md(keys)),axis=1)],axis=1)
    return dy

def count_lemmas(df,lang_col='language',text_col='response',md=True,**kwargs):
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
        df = prepare(df,lang_col,text_col)
    #do the counts
    counts = _counter(df,lang_col,**kwargs)
    counts_df = _make_counts_df(counts,lang_col)
    if md:
        counts_df = _merge_md(counts_df)
    #return
    return counts_df


def format_lemma_df(df_lemmas,
                   droprows=['will_future','go_future','particle','present'],
                   dropcols=['num_responses','num_words'],
                   min_count=1,
                   order = ['language', 'meta category','category', 'word/expression', 'count', 'percent', 
                            'gloss','justification', 'citation(s)'],
                   group_col='language'
                   ):
    dx = df_lemmas.copy()
    dx = dx.loc[~dx.feature.isin(droprows),:]
    dx['percent'] = round(dx['count']/dx['num_responses']*100,2)
    dx.percent = dx.percent.apply(lambda x: str(x)+'\\%')
    dx = dx.loc[dx['count'] >min_count,:]
    dx['meta category'] = dx.feature.apply(lambda x: META_FEATURE_MAP[x])
    dx['category'] = dx.feature.apply(lambda x: FEATURE_NAME_MAP[x])
    dx.lemma = dx.lemma.apply(lambda x: x.replace('_','\\textsubscript{')+'}' if x.endswith('_IND') or x.endswith('_SUBJ') else x)
    dx['word/expression'] = dx.lemma
    dx = dx.sort_values(by=['language','meta category','category','count'],ascending=False)
    dx = dx.drop(dropcols,1)
    dx = dx[order]
    dx = _format_citations(dx,group_col=group_col)
    return dx


