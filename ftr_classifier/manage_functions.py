#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:03:29 2019

@author: cole
"""
# =============================================================================
# imports
# =============================================================================
from copy import deepcopy
import pickle
import os
from ftr_classifier.word_lists import WORD_LISTS
#from word_lists import WORD_LISTS
import pandas as pd
#from word_lists import WORD_LISTS

# =============================================================================
# #set localle
# =============================================================================
DIR = os.path.dirname(os.path.realpath(__file__))
LOCAL_PATH ='/data/'

# =============================================================================
# collection of general CRUD functions for metadata and lemmatizing
# =============================================================================
def _load_obj(obj_name):
    load_path = DIR+LOCAL_PATH+obj_name
    #open
    with open(load_path,'rb') as handle:
        obj = pickle.load(handle)
    return obj

#save map function
def _save_obj(obj,obj_name):
    save_path = DIR+LOCAL_PATH+obj_name
    #open
    with open(save_path,'wb') as handle:
        pickle.dump(obj,handle,protocol=pickle.HIGHEST_PROTOCOL)
    print('{} saved to {}'.format(obj_name,save_path))

def _add_feature_to_lemma_map(lemma_map,feature_name,**kwargs):
    for key,val in lemma_map.items():
        val[feature_name] = ({},{})
    _save_obj(lemma_map,'lemma_map')

def _update_md_keys(lemma_map,new=False,drop = ['present','will_future','go_future']):
    lm = lemma_map.copy()
    #create blank MD db if new == True
    if new:
        d = {}
        for language in lm:
            d[language] = {}
            for feature in lm[language]:
                if not feature in drop:
                    d[language][feature] = {}
    else:
        d = _load_obj('meta_data')
    #splice new keys together 
    for language in lm:
        for feature in lm[language]:
            if not feature in drop:
                if feature not in d[language].keys():
                    d[language][feature] = {}
                for dic in lm[language][feature]:
                    vals = {val:{} for val in set(dic.values())}
                    d[language][feature] = {**vals,**d[language][feature]}
    #save
    _save_obj(d,'meta_data')
    
def _load_bibtex(path):
    import bibtexparser
    with open(path) as bibtex_file:
        db = bibtexparser.load(bibtex_file)
    bib_dic = {ent['ID']:ent for ent in db.entries}
    return bib_dic

def _write_bibtex():
    from bibtexparser.bwriter import BibTexWriter
    from bibtexparser.bibdatabase import BibDatabase
    db = BibDatabase()
    writer = BibTexWriter()
    path = DIR+LOCAL_PATH+'bibtex.bib'
    ents = {}
    md = _load_obj('meta_data')
    for language in md:
        for feature in md[language]:
            for metadata in md[language][feature].values():
                cits = {value['ID']:value for key,value in metadata.items() if key.startswith('citation')}
                if len(cits) > 0:
                    ents = {**ents,**cits}
    db.entries=list(ents.values())
    with open(path, 'w') as bibfile:
        bibfile.write(writer.write(db))
        
def _show_prog(md,language,cat):
    print('done:')
    print([key for key,val in md[language][cat].items() if len(val) > 0])
    print('')
    print('not done:')
    print([key for key,val in md[language][cat].items() if len(val) ==0])

#some cruddy functions to get the strings formatting correctly
def _format_str(s,replace_chars=['"'],sub1="``",sub2="''"):
    count = 0
    s = s.replace('“','"').replace('”','"')
    new = ""
    for ch in s:
        if ch == "%":
            new += "\\%"
        elif ch in replace_chars and count == 0:
            new += sub1
            count += 1
        elif ch in replace_chars and count == 1:
            new += sub2
            count += 1
        else:
            new += ch
    return new
    
def _format_md(md,key):
    mdn = deepcopy(md)
    for language in mdn:
        for feature in mdn[language]:
            for lemma in mdn[language][feature].keys():
                if key in mdn[language][feature][lemma].keys():
                    mdn[language][feature][lemma][key] = _format_str(mdn[language][feature][lemma][key])
    return mdn


def _split(x,split_on=']'):
    return x.split(split_on)[-1]

def _get_verb(x,start='{',end='}'):
    return x[x.index(start)+1:x.index(end)].lower().strip()

def _get_set(x):
    return list(set(x))

def _apply_func(store,func=None,kind='by_item'):
    store = deepcopy(store)
    for key,val in store.items():
        if kind == 'by_item':
            store[key] = list(map(func,val))
        elif kind == 'as_list':
            store[key] = func(val)
        elif kind == 'filter':
            store[key] = list(filter(lambda x: x not in WORD_LISTS[key]['present'][0] and x not in WORD_LISTS[key]['present'][1],val))
    return store

def get_new_verbs(questions_path='../../ftr_questionnaire/new_questions/ftr_questions/questionnaire_long.xlsx',
                   lang_col='language',
                   text_col='question'):
    questions = pd.read_excel(questions_path)
    store = {}
    for lang,dx in questions.groupby(lang_col):
        store[lang] = dx.loc[:,text_col].to_list()
    store = _apply_func(store,_split)
    store = _apply_func(store,_get_verb)
    store = _apply_func(store,_get_set,kind='as_list')
    store = _apply_func(store,kind='filter')
    store = {'language':[lang for lang,val in store.items() for word in val],
                         'word':[word for lang,val in store.items() for word in val]}
    store = pd.DataFrame(store)
    return store

def check_add_lemmas(add_lemmas=True,**kwargs):
    safe = True
    if add_lemmas is True:
        LEMMA_MAP = _load_obj('lemma_map')
        new_map = deepcopy(LEMMA_MAP)
    #iterate through and add/check
    for lang,lang_dict in WORD_LISTS.items():
        for feature,phrase_word_tuple in lang_dict.items():
            #add new features if necessary
            try:
                new_map[lang][feature]
            except KeyError:
                print('adding new feature')
                new_map[lang][feature] = ({}, {})
                LEMMA_MAP[lang][feature] = ({}, {})
            #iterate through phrases
            for phrase in phrase_word_tuple[0]:
                if phrase not in LEMMA_MAP[lang][feature][0]:
                    safe = False
                    if add_lemmas is False:
                        print('The phrase "{}" from the {} feature "{}" is not in the corresponding lemma_map'.format(phrase,lang,feature))
                    elif add_lemmas is True:
                        new_lemma = input('Please enter the phrase "{}" will be lemmatized as in the {} language feature {}.\n\n Enter "no_new_lemma" to continue with no change:\n\n'.format(phrase,lang,feature))
                        if not new_lemma == 'no_new_lemma':
                            new_map[lang][feature][0][phrase] = new_lemma
                            print('New lemma "{}" added to new lemma_map for "{}"'.format(new_lemma,phrase))
                    else:
                        pass
            #iterate through words
            for word in phrase_word_tuple[1]:
                if word not in LEMMA_MAP[lang][feature][1]:
                        safe = False
                        if add_lemmas is False:
                            print('The word "{}" from the {} feature "{}" is not in the corresponding lemma_map'.format(word,lang,feature))
                        elif add_lemmas is True:
                            new_lemma = input('Please enter the word "{}" will be lemmatized as in the {} language feature "{}":\n\nEnter "no_new_lemma" to continue with no change:\n\n'.format(word,lang,feature))
                            if not new_lemma == 'no_new_lemma':
                                new_map[lang][feature][1][word] = new_lemma
                                print('New lemma "{}" added to new lemma_map for "{}"'.format(new_lemma,word))
                        else:
                            pass
    if safe is True:
        print("All phrases and words are in the lemma map")
        return LEMMA_MAP
    elif add_lemmas is True and new_map != LEMMA_MAP:
        _save_obj(new_map,'lemma_map')
        return new_map
    else:
        return LEMMA_MAP

def add_md(lemma,justification,language,feature,bib,citation_key=None,**kwargs):
    md = _load_obj('meta_data')
    if len(md[language][feature][lemma]) > 0:
        from pprint import pprint
        pprint(md[language][feature][lemma])
        y = input('{} already has associated metadata. press y to continue: '.format(lemma))
        if y!= 'y':
            print('no changes were made')
            return md
    if 'justification' in md[language][feature][lemma].keys():
        y = input('justification is already "{}", press o to overwrite, anything else to add'.format(md[language][feature][lemma]['justification']))
        if y == 'o':
            md[language][feature][lemma]['justification'] = justification
        else:
            md[language][feature][lemma]['justification'] += ', '+justification
    else:
        md[language][feature][lemma]['justification'] = justification
    print('Added "{}" as justification for "{}"'.format(justification,lemma))
    print('Justification is now "{}"'.format(md[language][feature][lemma]['justification']))
    if citation_key:
        if isinstance(citation_key,str):
            citation_keys = [citation_key]
        else:
            citation_keys = citation_key
        prev_cits = len([x for x in md[language][feature][lemma] if x.startswith('citation')])
        for idx,key in enumerate(citation_keys):
            cit = 'citation_{}'.format(idx+prev_cits+1)
            cit_key = 'cit_key_{}'.format(idx+prev_cits+1)
            md[language][feature][lemma][cit] = bib[key]
            md[language][feature][lemma][cit_key] = key
            print('Added "{}" as reference'.format(key))
    if kwargs:
        for key,value in kwargs.items():
            md[language][feature][lemma][key] = value 
            print('"{}" added as "{}" for "{}"'.format(value,key,lemma))
    _save_obj(md,'meta_data')
    return md

# =============================================================================
# #load map
# META_DATA = _load_obj('meta_data')
# LEMMA_MAP = _load_obj('lemma_map')
# 
# ### add data to metadata
# bib = _load_bibtex('/Users/cole/Documents/BibTex/library.bib')
# _update_md_keys(LEMMA_MAP)
# 
# md = add_md(lemma='mogen',
#             justification='primarily deontic/dynamic modal, but review of our data indicate peripheral epistemic uses are possible (rare)',
#             language='dutch',
#             feature='verb_poss',
#             bib=bib,
#             citation_key=['Nuyts2000'],
#             gloss='may'
#             )
# 
# md = _load_obj('meta_data')
# mdn = _format_md(md,'gloss')
# _write_bibtex()
# _save_obj(md,'meta_data')
# =============================================================================

#run and save changes to lemma map
if __name__ == "__main__":
    LEMMA_MAP = check_add_lemmas()
    pass
