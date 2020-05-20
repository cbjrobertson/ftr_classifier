#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""
#load libraries
import pandas as pd

#local imports
from ftr_classifier.word_lists import FEATURES,WORD_LISTS,ALL_FEATURES
from ftr_classifier.models import MODELS


#fuck off pandas
pd.options.mode.chained_assignment = None  # default='warn'

#define missing data flag
_MISSING = '-999'

#functions
def _append_spacy_docs(df,lang_col,text_col):
    #create new dataframe
    dx = pd.DataFrame()
    #group by language
    df_group = df.groupby(lang_col)
    for lang,dy in df_group:
        #pull a model
        nlp = MODELS[lang]
        #apply model to language
        dy['spacy_doc'] = dy[text_col].apply(lambda x:  nlp(x) if isinstance(x,str) else nlp(""))
        #append together
        dx = dx.append(dy)
    return dx

def _clean_non_applicable(df,lang_col):
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

def _future_dom(df):
    df = df.copy()
    futures = ['go_future','will_future','future']
    exclude = ['present','particle','past','present_perfect','past_perfect']
    other_features = [x for x in FEATURES if x not in futures and x not in exclude]
    for future in futures:
        df[future+'_dom'] = [0 if any(feature == 1 for feature in df.loc[x,other_features])\
                              else 1 if df[future][x] == 1 else 0\
                              for x in df.index]
    return df

def _aspect_dom(df,lang_col='language'):
    dfg = df.groupby(lang_col)
    store = pd.DataFrame()
    for lang,dx in dfg:
        if lang == 'english':
            dx['present_perfect'] = [1 if dx.present_perfect[x] == 1 and dx.past[x] == 1 and dx.future[x] == 0 else 0 for x in dx.index]
            dx['past_perfect'] = [1 if dx.past_perfect[x] == 1 and dx.past[x] == 1 and dx.future[x] == 0 else 0 for x in dx.index]
            store = store.append(dx)
        elif lang == 'dutch':
            dx['present_perfect'] = [1 if dx.present_perfect[x] == 1 and dx.past_participle[x] == 1 and dx.future[x] == 0 else 0 for x in dx.index]
            dx['past_perfect'] = [1 if dx.past_perfect[x] == 1 and dx.past_participle[x] == 1 and dx.future[x] == 0 else 0 for x in dx.index]
            store = store.append(dx)
        else:
            store = store.append(dx)
    store.index = range(store.shape[0])
    return store

def _past_dom(df):
    df = df.copy()
    other_features = ['verb_cert','verb_poss','future','verb_des_int','present_perfect']
    df['past'] = [0 if any(feature == 1 for feature in df.loc[x,other_features])\
                          else 1 if df.past[x] == 1 else 0\
                          for x in df.index]
    return df

def _present_dom(df):
    df = df.copy()
    #other features not pres
    other_features = [x for x in FEATURES if x != 'present' and x not in ['particle','past_perfect']]
    #apply
    df['present_dom'] = [0 if any(feature == 1 for feature in df.loc[x,other_features])\
                          else 1 if df.present[x] == 1 \
                          else 0\
                          for x in df.index]
    return df

def _modal_exclude(df):
    df = df.copy()
    posses = [x for x in FEATURES if x.endswith('poss')]
    certs = [x for x in FEATURES if x.endswith('cert')]
    new_val = "mixed_modality"
    df[new_val] = [new_val if any(feature == 1 for feature in df.loc[x,certs]) and \
          any(feature == 1 for feature in df.loc[x,posses]) else "unmixed_modality" for x in df.index]
    return df

def _make_lexi_vars(df):
    df = df.copy()
    #make features lists
    poss_features = [x for x in FEATURES  if x.endswith('poss')]
    cert_features = [x for x in FEATURES if x.endswith('cert')]
    
    #lexi_sumary
    lexi_poss_features = [x for x in poss_features if not x.startswith('verb')]
    lexi_cert_features = [x for x in cert_features if not x.startswith('verb')]
    
    #apply
    df['uncertain'] = [1 if any(feature == 1 for feature in df.loc[x,poss_features])\
                       else "mixed_modality" if any(feature == "mixed_modality" for feature in df.loc[x,poss_features])
                       else 0 for x in df.index]
    df['certain'] = [1 if any(feature == 1 for feature in df.loc[x,cert_features])\
                      else "mixed_modality" if any(feature == "mixed_modality" for feature in df.loc[x,cert_features])
                       else 0 for x in df.index]
    
    df['lexi_poss'] = [1 if any(feature == 1 for feature in df.loc[x,lexi_poss_features])\
                      else "mixed_modality" if any(feature == "mixed_modality" for feature in df.loc[x,poss_features])
                       else 0 for x in df.index]
    df['lexi_cert'] = [1 if any(feature == 1 for feature in df.loc[x,lexi_cert_features])\
                      else "mixed_modality" if any(feature == "mixed_modality" for feature in df.loc[x,cert_features])
                       else 0 for x in df.index]
    return df

def _make_no_code(df):
    df = df.copy()
    #apply
    df['no_code'] = ['coded' if any(feature == 1 for feature in df.loc[x,FEATURES])\
                       else 'uncoded' for x in df.index]
    return df

def _tok_return(doc):
    toks =  [token.text.lower() for token in doc if\
            not token.is_punct]
    toks = [stok for tok in toks for stok in tok.split("'")]
    return toks

def _is_negated(doc):
    if any(tok.dep_ == 'neg' or tok.dep_ == 'ng' for tok in doc):
        return 1
    else:
        return 0
    
def _append_last_sentence(df):
    df = df.copy()
    df['final_sentence'] = df.spacy_doc #pointless step implementing to test for better accuracy
    #df['final_sentence'] = df.spacy_doc.apply(lambda doc: [sent for sent in doc.sents][-1])
    return df

def _check_words(response):
    scores = {}
    for feature,w_list in _word_list.items():
        if any(phrase in response.text.lower() for phrase in w_list[0]):
            scores[feature] = 1
        elif any(word in _tok_return(response) for word in w_list[1]):
            scores[feature] = 1
        else:
            scores[feature] = 0
    return scores

def _debug_check_words(response,raw_text=False,lang='dutch'):
    #set _word_list to global
    global _word_list
    if raw_text == True:
        doc = MODELS[lang](response)
        response = [sent for sent in doc.sents][-1]
        _word_list = WORD_LISTS[lang]
    scores = {}
    for feature,w_list in _word_list.items():
        if any(phrase in response.text.lower() for phrase in w_list[0]):
            scores[feature+'_debug'] = [phrase for phrase in w_list[0] if phrase in response.text.lower()]
        elif any(word in _tok_return(response) for word in w_list[1]):
            scores[feature+'_debug'] = [word for word in w_list[1] if word in _tok_return(response)]
        else:
            scores[feature+'_debug'] = ''
    return scores

def add_suffix(df,suffix):
    df = df.copy()
    for feature in ALL_FEATURES:
        df[[feature+suffix]] = df[[feature]]
    df = df.drop(ALL_FEATURES,1)
    return df

def prepare(df,lang_col,text_col):
    """ append two columns to a pandas dataframe containing at least two columns, one
    definining language in ['english','dutch','german'], the second containing str 
    natural language responses. Appended columns are 'spacy_doc', which is a
    spaCy document, and 'final_sentence' which is the last sentence in each spaCy document object.
    :param df: a pandas.DataFrame() object
    :param text_col: str, name of the df column containing natural language strings to be processed using spacy.nlp() models for languages in df[lang_col] default == 'response'
    :param lang_col: str, name of df column indexing language, default == 'language'. df[lang_col] must contain only ['english','dutch','german'], or a subset thereof
    :return: pd.DataFrame() with spaCy documents appended to df.spacy_doc., and last sentence to df.final_sentence
    """
    df = df.copy()
    #clean docs with spacy
    df = _append_spacy_docs(df,lang_col,text_col)
    df  = _append_last_sentence(df)
    df['response_clean'] = df.final_sentence.apply(lambda x: _tok_return(x))
    return df


def score(df,lang_col,debug,process_col='final_sentence'):
    """ Append columns for each of the features in ftr.word_lists._FEATURES. Columns are in [0,1], and define whether ftr.word_lists._FEATURES_i is present in df[process_col]
    :param df: a pandas.DataFrame() object
    :param clean_spacy: boolean, default == True. If True, spacy docs in df.final_sentence and df.spacy_doc will be dropped from df, if False, these will be kept.
    :param process_col: str, name of the df column containing spacy classified, default == 'final_sentence', must contain spacy.doc objects
    :param lang_col: str, name of df column indexing language, default == 'language'. df[lang_col] must contain only ['english','dutch','german'], or a subset thereof
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
        dy = pd.concat([dy,dy[process_col].apply(lambda doc: pd.Series(_check_words(doc)))],axis=1)
        dy['negated'] = dy[process_col].apply(lambda doc: _is_negated(doc))
        #add lists of hit words to debug if necessary
        if debug:
            dy = pd.concat([dy,dy[process_col].apply(lambda doc: pd.Series(_debug_check_words(doc)))],axis=1)
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
    df = _future_dom(df)
    df = _aspect_dom(df)
    df = _past_dom(df)
    df = _present_dom(df)
    df = _modal_exclude(df)
    df = _make_lexi_vars(df)
    df = _make_no_code(df)
    return df
    
def classify_df(df,lang_col='language',text_col='response',suffix=None,debug=False,**kwargs):
    """ Sequentially call prepare(df), score(df), and apply_dominance(df)
    :param df: a pandas.DataFrame() object which MUST match criteria described in prepare() description.
    :param **kwargs: any key_word arguments passable to prepare() or score(), 
    i.e. defining non-default values for text_col,lang_col,clean_spacy,and process_col, though if process_col is changed without adjusting _append_last_sentence for agreement, an error will result
    :return: pd.Dataframe()
    """
    df = df.copy()
    df = prepare(df,lang_col,text_col)
    #debug by returning the 'hit' words
    df = score(df,lang_col,debug,**kwargs)
    #apply dominance
    df = apply_dominance(df)
    if suffix:
        df = add_suffix(df,suffix)
    df = _clean_non_applicable(df,lang_col)
    df.index = range(len(df.index))
    return df
    
def clean_spacy(df):
    '''
    :param df: pd.DataFrame
    :return: df with cols 'final_sentence' and 'spacy_doc' dropped
    '''
    df = df.copy()
    df = df.drop(['final_sentence','spacy_doc'],1)
    return df
