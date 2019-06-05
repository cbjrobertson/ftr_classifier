#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""
#load libraries
import pandas as pd

#local imports
from ftr_classifier.word_lists import FEATURES, WORD_LISTS
from ftr_classifier.models import MODELS


#fuck off pandas
pd.options.mode.chained_assignment = None  # default='warn'

#define missing data flag
_MISSING = '-999'

#functions
def _append_spacy_docs(df,lang_col='textLang',text_col='response'):
    #create new dataframe
    dx = pd.DataFrame()
    #group by language
    df_group = df.groupby(lang_col)
    for lang,dy in df_group:
        #pull a model
        nlp = MODELS[lang]
        #apply model to language
        dy['spacy_doc'] = dy[text_col].apply(lambda x: nlp(x))
        #append together
        dx = dx.append(dy)
    return dx

def _append_last_sentence(df):
    df = df.copy()
    df['final_sentence'] = df.spacy_doc.apply(lambda doc: [sent for sent in doc.sents][-1])
    return df

def _clean_non_applicable(df,lang_col='textLang'):
    #create new dataframe
    dx = pd.DataFrame()
    #group by language
    df_group = df.groupby(lang_col)
    for lang,dy in df_group:
        if lang == 'english':
            cols = [x for x in dy.columns if 'particle' in x]
            dy[cols] = _MISSING
        elif lang == 'german':
            dy['go_future'] = _MISSING
        else:
            pass
        #append
        dx = dx.append(dy)
    return dx

def _present_dom(df):
    df = df.copy()
    #other features not pres
    other_features = [x for x in FEATURES if x != 'present']
    #apply
    df['present_dom'] = [0 if any(feature == 1 for feature in df.loc[x,other_features])\
                  else 1 if df.present[x] == 1 else 0\
                  for x in df.index]
    return df

def _future_dom(df):
    df = df.copy()
    futures = ['go_future','will_future','future']
    exclude = ['present','particle']
    other_features = [x for x in FEATURES if x not in futures and x not in exclude]
    for future in futures:
        df[future+'_dom'] = [0 if any(feature == 1 for feature in df.loc[x,other_features])\
                              else 1 if df[future][x] == 1 else 0\
                              for x in df.index]
    return df

def _make_lexi_vars(df):
    df = df.copy()
    #make features lists
    poss_features = [x for x in FEATURES  if x.endswith('poss')]
    cert_features = [x for x in FEATURES if x.endswith('cert')]
    #apply
    df['lexi_poss'] = [1 if any(feature == 1 for feature in df.loc[x,poss_features])\
                       else 0 for x in df.index]
    df['lexi_cert'] = [1 if any(feature == 1 for feature in df.loc[x,cert_features])\
                       else 0 for x in df.index]
    return df

def _tok_return(doc):
    toks =  [token.text for token in doc if\
            not token.lemma_ == '-PRON-' and \
            not token.is_punct]
    return toks

def _is_negated(doc):
    if any(tok.dep_ == 'neg' or tok.dep_ == 'ng' for tok in doc):
        return 1
    else:
        return 0
    
def _check_words(response):
    scores = []
    for feature,w_list in _word_list.items():
        if any(phrase in response.text for phrase in w_list[0]):
            scores += [1]
        elif any(word in _tok_return(response) for word in w_list[1]):
            scores += [1]
        else:
            scores += [0]
    return dict(zip(FEATURES, scores))




def prepare(df,*args,**kwargs):
    """ append two columns to a pandas dataframe containing at least two columns, one
    definining language in ['english','dutch','german'], the second containing str 
    natural language responses. Appended columns are 'spacy_doc', which is a
    spaCy document, and 'final_sentence' which is the last sentence in each spaCy document object.
    :param df: a pandas.DataFrame() object
    :param text_col: str, name of the df column containing natural language strings to be processed using spacy.nlp() models for languages in df[lang_col] default == 'response'
    :param lang_col: str, name of df column indexing language, default == 'textLang'. df[lang_col] must contain only ['english','dutch','german'], or a subset thereof
    :return: pd.DataFrame() with spaCy documents appended to df.spacy_doc., and last sentence to df.final_sentence
    """
    df = df.copy()
    #clean docs with spacy
    df = _append_spacy_docs(df,*args,**kwargs)
    df = _append_last_sentence(df)
    df['response_clean'] = df.final_sentence.apply(lambda x: _tok_return(x))
    return df


def score(df,lang_col='textLang',process_col='final_sentence'):
    """ Append columns for each of the features in ftr.word_lists._FEATURES. Columns are in [0,1], and define whether ftr.word_lists._FEATURES_i is present in df[process_col]
    :param df: a pandas.DataFrame() object
    :param clean_spacy: boolean, default == True. If True, spacy docs in df.final_sentence and df.spacy_doc will be dropped from df, if False, these will be kept.
    :param process_col: str, name of the df column containing spacy classified, default == 'final_sentence', must contain spacy.doc objects
    :param lang_col: str, name of df column indexing language, default == 'textLang'. df[lang_col] must contain only ['english','dutch','german'], or a subset thereof
    :return: pd.DataFrame() with columns for each feature in ftr.word_lists._FEATURES, 1 indicates feature present, 0 indicates feature not present
    """
    #initiate a new dataframe
    dx = pd.DataFrame()
    
    #make word lists a global var
    global _word_list
    
    #group by language
    df_groups = df.groupby(lang_col)
    
    #iterate and apply
    for lang,dy in df_groups:
        #assign lang_specific word list abd language
        _word_list = WORD_LISTS[lang]  
       
        #apply function to lang-specific group
        dy[FEATURES] = dy[process_col].apply(lambda doc: pd.Series(_check_words(doc)))
        dy['negated'] = dy[process_col].apply(lambda doc: _is_negated(doc))
        
        #append together
        dx = dx.append(dy)       
    return dx

def apply_dominance(df):
    """ Apply dominance scoring hierarchy described in Robertson et al. (TKTK), columns subjected to the dominance 
    relationship are appended to df with a "_dom" suffix. Additionally appends two columns: 
        1) df['lexi_cert'] indicating  whether ANY certainty expression is used
        2) df['lexi_poss'] indicating  whether ANY possibility expression is used, see Robertson et al. (TKTK) for description.
    :param df: a pandas.DataFrame() object which MUST have been passed to score() and contain columns for all values in ftr.word_lists._FEATURES, and containing values in [0,1] 
    :return: pd.DataFrame()
    """
    df = df.copy()
    df = _present_dom(df)
    df = _future_dom(df)
    df = _make_lexi_vars(df)
    return df
    
def classify_df(df,**kwargs):
    """ Sequentially call prepare(df), score(df), and apply_dominance(df)
    :param df: a pandas.DataFrame() object which MUST match criteria described in prepare() description.
    :param **kwargs: any key_word arguments passable to prepare() or score(), 
    i.e. defining non-default values for text_col,lang_col,clean_spacy,and process_col, though if process_col is changed without adjusting _append_last_sentence for agreement, an error will result
    :return: pd.Dataframe()
    """
    df = df.copy()
    df = prepare(df,**kwargs)
    df = score(df,**kwargs)
    df = apply_dominance(df)
    return df
    
def clean_spacy(df):
    df = df.copy()
    df = df.drop(['final_sentence','spacy_doc'],1)
    return df
