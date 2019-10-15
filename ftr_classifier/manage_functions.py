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

# =============================================================================
# locals imports
# =============================================================================
from ftr_classifier.word_lists import WORD_LISTS

# =============================================================================
# #set constants
# =============================================================================
DIR = os.path.dirname(os.path.realpath(__file__))
LOCAL_PATH ='/data/'

# =============================================================================
# collection of general functions
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

  
def check_add_lemmas(add_lemmas=True,**kwargs):
    safe = True
    if add_lemmas is True:
        LEMMA_MAP = _load_obj('lemma_map')
        new_map = deepcopy(LEMMA_MAP)
    #iterate through and add/check
    for lang,lang_dict in WORD_LISTS.items():
        for feature,phrase_word_tuple in lang_dict.items():
            for phrase in phrase_word_tuple[0]:
                if phrase not in LEMMA_MAP[lang][feature][0]:
                    safe = False
                    if add_lemmas is False:
                        print('The phrase "{}" from the {} feature "{}" is not in the corresponding lemma_map'.format(phrase,lang,feature))
                    elif add_lemmas is True:
                        new_lemma = input('Please enter the phrase "{}" will be lemmatized as in the {} language feature {}.\n\n Enter "pass" to continue with no change:\n\n'.format(phrase,lang,feature))
                        if not new_lemma == 'pass':
                            new_map[lang][feature][0][phrase] = new_lemma
                            print('New lemma "{}" added to new lemma_map for "{}"'.format(new_lemma,phrase))
                    else:
                        pass
            for word in phrase_word_tuple[1]:
                if word not in LEMMA_MAP[lang][feature][1]:
                        safe = False
                        if add_lemmas is False:
                            print('The word "{}" from the {} feature "{}" is not in the corresponding lemma_map'.format(word,lang,feature))
                        elif add_lemmas is True:
                            new_lemma = input('Please enter the word "{}" will be lemmatized as in the {} language feature "{}":\n\nEnter "pass" to continue with no change:\n\n'.format(word,lang,feature))
                            if not new_lemma == 'pass':
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
   
def add_feature_to_lemma_map(lemma_map,feature_name,**kwargs):
    for key,val in lemma_map.items():
        val[feature_name] = ({},{})
    _save_obj(lemma_map,'lemma_map')

def update_md_keys(lemma_map,new=False,drop = ['present','will_future','go_future']):
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

def _write_bibtex(md):
    from bibtexparser.bwriter import BibTexWriter
    writer = BibTexWriter()
    path = LOCAL_PATH+'bib_file.bib'
    ents = []
    for language in md:
        for feature in md[language]:
            for metadata in md[language][feature].values():
                cits = [value for key,value in md.items() if key.startswith('citation')]
                if len(cits) > 0:
                    ents += cits
    return ents
    #with open(path, 'w') as bibfile:
    #    bibfile.write(writer.write(ents))
        


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
    
def show_prog(md,language,cat):
    print('done:')
    print([key for key,val in md[language][cat].items() if len(val) > 0])
    print('')
    print('not done:')
    print([key for key,val in md[language][cat].items() if len(val) ==0])
    
#load map
META_DATA = _load_obj('meta_data')

#run and save changes to lemma map
if __name__ == '__main__':
    LEMMA_MAP = _load_obj('lemma_map')
    LEMMA_MAP = check_add_lemmas()