#load libraries
import pandas as pd
import spacy

#local imports 
from ftr_word_lists import WORD_LISTS,FEATURES

#fuck off pandas
pd.options.mode.chained_assignment = None  # default='warn'

#load MODELS
en = spacy.load('en')
de = spacy.load('de')
nl = spacy.load('nl')

#make MODELS dictionary
MODELS = {'english':en,
          'dutch':nl,
          'german':de}

#define missing data flag
MISSING = '-999'

#import data
df = pd.read_excel('/Users/cole/Dropbox/FTR2Share/chen_1/cleanedData/chenMasterExp1_uncoded.xlsx')

# =============================================================================
# #subset for test
# gdf = df.groupby('textLang')
# dxt = pd.DataFrame()
# for lang,dx in gdf:
#     dx = dx[:40]
#     dxt = dxt.append(dx)
# 
# =============================================================================
#drop duplicates
df = df.dropna(subset=['response'])
#dxt = dxt.dropna(subset=['response'])
#df=dxt


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

def _clean_spacy(df):
    df = df.copy()
    df['response_clean'] = df.final_sentence.apply(lambda x: _tok_return(x))
    df = df.drop(['final_sentence','spacy_doc'],1)
    return df

def _clean_non_applicable(df,lang_col='textLang'):
    #create new dataframe
    dx = pd.DataFrame()
    #group by language
    df_group = df.groupby(lang_col)
    for lang,dy in df_group:
        if lang == 'english':
            cols = [x for x in dy.columns if 'particle' in x]
            dy[cols] = MISSING
        elif lang == 'german':
            dy['go_future'] = MISSING
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
    other_features = [x for x in FEATURES if x not in futures and x != 'present']
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

def _check_words(response):
    scores = []
    for feature,w_list in word_list.items():
        if any(phrase in response.text for phrase in w_list[0]):
            scores += [1]
        elif any(word in _tok_return(response) for word in w_list[1]):
            scores += [1]
        else:
            scores += [0]
    return dict(zip(FEATURES, scores))
            

def prepare(df,**kwargs):
    df = df.copy()
    #clean docs with spacy
    df = _append_spacy_docs(df,**kwargs)
    df = _append_last_sentence(df,**kwargs)
    return df


def score(df,lang_col='textLang',doc_col='final_sentence',clean_spacy=True):
    #initiate a new dataframe
    dx = pd.DataFrame()
    
    #make word lists a global var
    global word_list
    
    #group by language
    df_groups = df.groupby(lang_col)
    
    #iterate and apply
    for lang,dy in df_groups:
        #assign lang_specific word list
        word_list = WORD_LISTS[lang]        
       
        #apply function to lang-specific group
        dy[FEATURES] = dy[doc_col].apply(lambda doc: pd.Series(_check_words(doc)))
        
        #append together
        dx = dx.append(dy)
    #remove memory hungry spacy docs
    if clean_spacy == True:
        dx = _clean_spacy(dx)        
    return dx

def apply_dominance(df):
    df = df.copy()
    df = _present_dom(df)
    df = _future_dom(df)
    df = _make_lexi_vars(df)
    return df
    
def process_dataframe(df,**kwargs):
    df = df.copy()
    df = prepare(df,**kwargs)
    df = score(df,**kwargs)
    df = apply_dominance(df)
    return df 
    
if __name__ == '__main__':
    df = process_dataframe(df)







