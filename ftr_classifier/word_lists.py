#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""
# =============================================================================
# imports
# =============================================================================
from copy import deepcopy
import os
import pickle

#set constants
DIR = os.path.dirname(os.path.realpath(__file__))
LOCAL_PATH ='/lemma_map/lemma_map'
# =============================================================================
# CRUD functions
# =============================================================================

def _load_map():
    import pickle
    load_path = DIR+LOCAL_PATH
    with open(load_path,'rb') as handle:
        lemma_map = pickle.load(handle)
    return lemma_map   

#save map function
def _save_map(lemma_map,filepath='/lemma_map/lemma_map'):
    #save
    save_path = DIR+LOCAL_PATH
    with open(save_path,'wb') as handle:
        pickle.dump(lemma_map,handle,protocol=pickle.HIGHEST_PROTOCOL)
    print('lemma_map saved to {}'.format(save_path))
    
def check_add_lemmas(add_lemmas=True,**kwargs):
    safe = True
    if add_lemmas is True:
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
        _save_map(new_map,**kwargs)
        return new_map
    else:
        return LEMMA_MAP

# =============================================================================
# Features 
# =============================================================================
FEATURES = ['present','future',
            'verb_poss','verb_cert',
            'adv_adj_poss','adv_adj_cert',
            'mental_poss','mental_cert',
            'particle_poss','particle',
            'will_future','go_future']

LANGUAGES = ['english','dutch','german']
# =============================================================================
# English word lists
# =============================================================================
english = {'present':([],
                      ["'m",
                       "'re",
                       'allow',
                       'allows',
                       'am',
                       'are',
                       'arrives',
                       'arrive',
                       'be',
                       'break',
                       'breaks',
                       'buy',
                       'buys',
                       'call',
                       'calls',
                       'cause',
                       'causes',
                       'climb',
                       'climbs',
                       'collapse',
                       'collapses',
                       'come',
                       'comes',
                       'congratulate',
                       'congratulates',
                       'crash',
                       'crashes',
                       'decline',
                       'declines',
                       'develop',
                       'develops',
                       'die',
                       'dies',
                       'do',
                       'does',
                       'drop',
                       'drops',
                       'fall',
                       'falls',
                       'fly',
                       'flies',
                       'forecast',
                       'forecasts',
                       'gain',
                       'gains',
                       'garden',
                       'gardens',
                       'get',
                       'gets',
                       'go',
                       'goes',
                       'help',
                       'helps',
                       'increase',
                       'increases',
                       'insist',
                       'insists',
                       'is',
                       'live',
                       'lives',
                       'make',
                       'makes',
                       'plan',
                       'plans',
                       'plummet',
                       'plummets',
                       'potter',
                       'potters',
                       'praise',
                       'praises',
                       'puts',
                       'put',
                       'rain',
                       'rains',
                       'receive',
                       'receives',
                       'rise',
                       'rises',
                       'risk',
                       'risks',
                       'say',
                       'says',
                       'sit',
                       'sits',
                       'spend',
                       'spends',
                       'stay',
                       'stays',
                       'suggest',
                       'suggests',
                       'thank',
                       'thanks',
                       'travel',
                       'travels',
                       'work',
                       'works']
                          ),
    
    'future':(['about to','is going','are going','am going','going to'],
              ['will',
               'wil',
               'shall',
               "'ll",
               "theyll"]
            ),
    
    'verb_poss':([],
                 ['can',
                  'may',
                  'could',
                  'might',
                  'should',
                  'sould',
                  'ought'
                  ]
                 ),
    
    'verb_cert':(['have to','got to','has to'],
                 ['must']
                 ),
    
    'adv_adj_poss':([],
                   ['apparently',
                    'dubiously',
                    'expectably',
                    'expectedly',
                    'improbably',
                    'likely',
                    'maybe',
                    'mayhap',
                    'perchance',
                    'perhaps',
                    'possibility',
                    'possible',
                    'possibly',
                    'potentially',
                    'presumably',
                    'probable',
                    'probability',
                    'probably',
                    'improbable',
                    'improbability',
                    'improbably',
                    'questionably',
                    'seemingly',
                    'somewhat',
                    'supposedly',
                    'supposed',
                    'uncertainly']
                    ),
    
    'adv_adj_cert':(['for sure'],
               ['definitely','definetly',#missspelling
                'definite',
                'certainly',
                'certain',
                'certainty',
                'assuredly',
                'assured',
                'clearly',
                'doubtless',
                'indubitably',
                'inevitably',
                'infallibly',
                'irrefutably',
                'irrefutable',
                'necessarily',
                'necessary',
                'obviously',
                'obvious',
                'surely',
                'sure',
                'unavoidably',
                'unavoidable',
                'undeniably',
                'undeniable',
                'undoubtedly',
                'undoubted',
                'unquestionably',
                'unquestionable']
               ),
    'mental_poss':(['feel like'],
                   ['think',
                    'thinking',
                    'thinks',
                    'believe',
                    'believes',
                    'believing',
                    'reckon',
                    'reckons',
                    'reckoning',
                    'expect',
                    'expects',
                    'expecting',
                    'planning',
                    'plan',
                    'plans',
                    'doubt',
                    'doubts',
                    'doubting',
                    'suppose',
                    'supposes',
                    'supposing',
                    'guess',
                    'guesses',
                    'guessing']
                   ),
    
    'mental_cert':([],
                   ['know',
                    'knows']#certaintly strongest of mental state preds, enough for certain category?
                   ),
                   
    'particle_poss':([],
                     []
                     ),
    'particle':([],
                []
                ),
    'will_future':([],
                   ['will',
                    'wil',
                    "'ll",
                    "theyll"]
                   ),
    'go_future':(['is going','are going',
                   'am going','going to'],
                 []
                 )
    }


# =============================================================================
# Dutch word lists
# =============================================================================
dutch = {'present':(['is het','vallen om','storten in',
                     'en ik in au','het stoort',
                     'contact opnemen','leuk vindt',
                     'ze halen het','val om','stort in',
                     'valt om','storten in'],
                    ['.is',#typo
                     'accepteer',
                     'accepteert',
                     'accepteren',
                     'bedank',
                     'bedanken',
                     'bedankt',
                     'bekijk',
                     'bekijkt',
                     'bekijken',
                     'bel',
                     'bellen',
                     'belt',
                     'ben',
                     'bent',
                     'bereik',
                     'bereiken',
                     'bereikt',
                     'blijf',
                     'blijven',
                     'blijft',
                     'breek',
                     'breekt',
                     'breken',
                     'daal',
                     'daalt',
                     'dalen',
                     'dank',
                     'dankt',
                     'danken',
                     'doe',
                     'doet',
                     'doen',
                     'dood',
                     'doodt',
                     'doden',
                     'doodgaan',
                     'eet',
                     'eten',
                     'explodeer',
                     'explodeert',
                     'exploderen',
                     'haal',
                     'haalt',
                     'halen',
                     'heb',
                     'hebben',
                     'hebt',
                     'heeft',
                     'helen',
                     'heel',
                     'heelt',
                     'ingestort',
                     'instort',
                     'is',
                     'is.',#typo
                     'kijk',
                     'kijken',
                     'kijkt',
                     'knap',
                     'knappen',
                     'knapt',
                     'kom',
                     'komen',
                     'komt',
                     'koop',
                     'koopt',
                     'kopen',
                     'krijg',
                     'krijgen',
                     'krijgt',
                     'laat',
                     'latten',
                     'maak',
                     'maaken',
                     'maakt',
                     'maken',
                     'nemen',
                     'neem',
                     'neemt',
                     'omvalt',
                     'omval',
                     'omvalen',
                     'regen',
                     'regenen',
                     'regent',
                     'reis',
                     'reist',
                     'reizen',
                     'resideer',
                     'resideert',
                     'resideren',
                     'rij',
                     'rijd',
                     'rijden',
                     'rijdt',
                     'slijt',
                     'slijten',
                     'sneeuw',
                     'sneeuwen',
                     'sneeuwt',
                     'sort',
                     'sotrt',
                     'spaar',
                     'spaart',
                     'sparen',
                     'stel',
                     'stellen',
                     'stelt',
                     'sterf',
                     'sterft',
                     'sterven',
                     'stijg',
                     'stijgen',
                     'stijgt',
                     'stjgt',
                     'stort',
                     'storten',
                     'strort',#typo
                     'val',
                     'vallen',
                     'valt',
                     'verdubbel',
                     'verdubbelen',
                     'verdubbelt',
                     'vergangt',
                     'vergang',
                     'vergangen',
                     'verhuis',
                     'verhuist',
                     'verhuizen',
                     'verlies',
                     'verliest',
                     'verliezen',
                     'verslijten',
                     'verslijt',
                     'verminder',
                     'verminderen',
                     'vermindert',
                     'verslijt',
                     'verslijten',
                     'verslitjen',
                     'verspil',
                     'verspillen',
                     'verspilt',
                     'vervang',
                     'vervangen',
                     'vervangt',
                     'vinden',
                     'vind',
                     'vindt',
                     'voel',
                     'voelen',
                     'voelt',
                     'weetblijft',#typo
                     'werk',
                     'werken',
                     'werkt',
                     'wetkt',
                     'win',
                     'winnen',
                     'wint',
                     'wonen',
                     'wonnen',
                     'woon',
                     'woont',
                     'wwon',#typo 
                     'zie',
                     'zien',
                     'ziet',
                     'zij',
                     'zijn',
                     'zinnen',
                     'zit',
                     'zitten',
                     'zwel',
                     'zwellen',
                     'zwelt']
                    ),
    
          'future':(['staat op'],#about to
                   ['ga',
                    'gaat', 
                    'gaan',
                    'zal', 
                    'zullen',
                    'zult', 
                    'zul',
                    'gaanverliezen'] #misspelling of gaan verleizen, "going to lose"
                   ),
        'verb_poss':([],
                     ['kunnen',
                      'gekund',
                      'kan',
                      'kun',
                      'kunt',
                      'kon' ,
                      'kans',
                      'mag',
                      'mogen', #doesn't have primary epistemic uses, more deontic, Nuyts 2000, but included anyway for exploratory pusposes 
                      'vermogen',
                      'vermoogd'] #i.e. mogen + prefix ver-
                     ),
        'verb_cert':([],
                     ['moeten',
                      'moet',
                      'moest',
                      'gemoeten',
                      'moesten'
                      #'wil',
                      #'wilt',
                      #'willen'#no real epistemic use, i.e. "to want", see Nuyts 2000
                      ]
                     ),
        'adv_adj_poss':(['in aanmerking komend'
                         'niet zeker',
                         'is er een kans',
                         'te komen',
                         'naar het schijnt'],#it seems 
                        ['aannemelijk',#predsumably (Nuyts 2000)
                         'allichet',#probably
                         'bedenkelijk',
                         'blijkbaar',
                         'denkelijk',
                         'geschiktlijkend',
                         'hypothetisch',
                         'misschien',#perhaps
                         'mogelijk',#possibly
                         'mogelijkerwijs',#possibly
                         'ongeveer',
                         'onzeker',
                         'ogenschijnlijk',#seemingly/apparently
                         'klaarblijkelijk',
                         'schijnbaar',#seemingly
                         'twijfelachtig',
                         'veelbelovend',
                         'vermoedelijk',
                         'verwacht',
                         'waarschijnlijk',
                         'wellicht',#probably
                         'word',
                         'worden',
                         'wordt']#unclear worden "becomes" is a futuroid, but is in the present tense. from a cognitive/pragmatic perspective, it is somewhat modal/marked
                        ),
        'adv_adj_cert':(['wel degelijk'],
                        ['absoluut',
                         'alleszins',
                         'allicht',
                         'bepaald',
                         'beslist',
                         'definitief',
                         'doorgansduidelijk',
                         'duidelijk',
                         'echt',
                         'eenvoudigweg',
                         'eigenlijk',
                         'essentieel',
                         'evident',
                         'fietelijk',
                         'gedwongen',
                         'gegarandeerd',
                         'glashelder',
                         'hoogstwaarschijnlijk',
                         'helder',
                         'inderdaad',
                         'kennelijk',
                         'klaarblijkelijk',
                         'klaar',
                         'logisch',
                         'natuurlijk',
                         'nodig',
                         'noodzakelijk',
                         'normaal',
                         'ondenkbaar',
                         'ongetwijfeld',#certainly               
                         'onmiskenbaar',
                         'onmogelijk',
                         'onomstotelijk',
                         'ontwijfelbaar',
                         'onvermijdelijk',
                         'onwaarschijnlijk',
                         'onweerlegbaar',
                         'onwrikbaar',
                         'overduidelijk',
                         'overtuigend',
                         'sowieso',
                         'stellig',
                         'uiteraard',
                         'vanzelfsprekend',
                         'vast',#certain
                         'verplicht',
                         'voorgoed',
                         'werkelijk',
                         'wis',
                         'zeker']
                        ),
        'mental_poss':(['houden voor'],
                        ['denk',
                         'denken',
                         'denkt',
                         'geloven',
                         'gelooft',
                         'geloof',
                         'meen',
                         'ment',
                         'menen',
                         'veronderstellen',#to suppose, epistemic use (Nuyts 2000)
                         'veronderstel',
                         'veronderstelt',
                         'vermoed',
                         'vermoedt',
                         'vermoeden',
                         'gehoord',#to hear, possible epistemic/evidential use (Nuyts, 2000)
                         'horen', #to hear, possible epistemic/evidential
                         'hoor',
                         'hoort'
                         'betwijfel',#to doubt, has epistemic use Nuyts (2000)
                         'betwijfelt',
                         'betwijfelen',
                         'annehm',#to assume, but more clear qualificational use than in English (Nuyts 2000)
                         'annehmt',
                         'annehmen',
                         'zeg', #say, but similar to mental state pred use (Nuyts, 2000)
                         'zeggen',
                         'zegt',
                         
                         ]
                        ),
        'mental_cert':([],
                       ['weet',
                        'weten']#not sure if certain or uncertain, certaintly strongest of mental state preds
                       ),
        'particle_poss':(['wel eens'],
                         ['wel']
                         ),
        'particle':(['nou eenmaal',
                     'nu eenmaal'],
                    ['eens'
                     'effe',
                     'es',
                     'even',
                     'entjes',
                     'gewoon',
                     'hoor',
                     'ja',
                     'maar',
                     'nou'
                     'nu',
                     'toch']
                    ),
        'will_future':([],
                       ['zal', 
                        'zult',
                        'zul',
                        'zullen']
                       ),
        'go_future':([],
                     ['ga',
                      'gaat',
                      'gaan',
                      'gaanverliezen']
                     )
        }

# =============================================================================
# German word lists
# =============================================================================
german = {'present':(['nutze ab',
                      'nutzt ab',
                      'nutzen ab',
                      'gehe aus',
                      'gehst aus',
                      'geht aus',
                      'gehen aus',
                      'rufe an',
                      'rufst an',
                      'ruft an',
                      'rufen an',
                      'rufe an',
                      'rufst an',
                      'ruft an',
                      'rufen an',
                      'gehe auf',
                      'gehst auf',
                      'geht auf',
                      'gehen auf'],
                     ['bin',
                      'bist', 
                      'ist', 
                      'sind',#typo
                      'seid',#typo
                      'sein',
                      'komme',
                      'kommst',
                      'kommt',
                      'kommen',
                      'steige',
                      'steigst',
                      'steigt',
                      'steigen',
                      'bekomme',
                      'bekommst',
                      'bekommt',
                      'bekommen',
                      'mache',
                      'machst',
                      'macht',
                      'machen',
                      'nutzen',
                      'nutze',
                      'nutzt',
                      'habe',
                      'hast',
                      'hat',
                      'haben',
                      'habt',
                      'arbeite',
                      'arbeitest',
                      'arbeitet',
                      'arbeiten',
                      'fühle',
                      'fühlst',
                      'fühlt',
                      'fühlen',
                      'fuehlst',
                      'gewinne',
                      'gewinnst',
                      'gewinnt',
                      'gewinnen',
                      'regne',
                      'regnest',
                      'regnet',
                      'regnen',
                      'kaufe',
                      'kaufst',
                      'kauft',
                      'kaufen',
                      'sterbe',
                      'stirbst',
                      'stirbt',
                      'sterben',
                      'sterbt',
                      'reise',
                      'reist',
                      'reisen',
                      'ruft',
                      'rufst',
                      'rufe',
                      'rufen',
                      'gehe',
                      'gehst',
                      'geht',
                      'gehen',
                      'liebe',
                      'liebst',
                      'liebt',
                      'lieben',
                      'lebe', 
                      'lebst', 
                      'lebt', 
                      'leben']),
    'future': ([],
               ['werde',
                'wirst',
                'wird',
                'werden',
                'werdet',
                'werden']),
    'verb_poss':([],
                 [#indicative of können
                  'kann',
                  'kannst',
                  'könnt',
                  'können',
                  
                  #konjunktiv ii of können
                  'könnte',
                  'könntest',
                  'könnten',
                  'könntet',
                  
                  #may have some epistemic use, but not typical, as in english ''should' (Nuyts 2000). Both konjunctiv ii and indicative included    
                  'sollen',
                  'soll',
                  'sollst',
                  'sollt',
                  
                  #konjunktiv ii uncelar if I should include ???
                  'sollte',
                  'solltest',
                  'sollten',
                  'solltet',
                  
                  #indicative dürfen cannot have epistemic uses, only deontic (Nuyts, 2000)
                  #'darf',
                  #'darfst',
                  #'dürfen',
                  #'dürft',
                  
                  #konjunktiv ii of ¨dürfen
                  'dürfte',
                  'dürftest',
                  'dürften',
                  'dürftet',
                  
                  #mogen 'may' in the indicative has epistemic uses, but not konjunktiv ii (Nuyts 2000)
                  'mag',
                  'magst',
                  'mögen',
                  'mögt',
                  
                  ##konjunktiv ii
                  #'möchte',
                  #'möchtest',
                  #'möchten',
                  #'möchtet',
                  
                  #konjunktiv ii of müssen has epistemic uses, like 'should' (Mortelmans 2000).
                  'müßte',
                  'müßtest',
                  'müßten',
                  'müßtet',
                  'müsste',
                  'müsstest',
                  'müssten',
                  'müsstet']
                 ),
    
    'verb_cert':([],
                 ['muss',
                  'musst',
                  'müssen',
                  'müsst',
                  'muß',
                  'mußt',
                  'müßen',
                  'müßt']
                 ),
    
    'adv_adj_poss':(['unter umständen'],
                    ['annehmbar',#presumably (Nuyts 2000)
                     'eventuell',
                     'anscheinend',
                     'gegebenenfalls',
                     'möglich',
                     'möglicherweise',
                     'offenbar',
                     'scheinbar',#seemingly
                     'vielleicht',
                     'vermutlich',#presumably (Nuyts 2000)
                     'wahrscheinlich',
                     'womöglich']#maybe
                    ),
    
    'adv_adj_cert':(['auf jeden fall',
                     'klipp und klar'],
                    ['aufjedenfall',
                     'augenscheinlich',#evidently
                     'bestimmt',#certainly
                     'definitiv',
                     'deutlich',#clearly
                     'eindeutig',
                     'gewiss',
                     'klar',
                     'offensichtlich',#obviously
                     'jedenfalls',
                     'sicher',#certainly (Nuyts 2000)
                     'sicherlich',#certainly
                     'zweifelsohne',#certainly
                     'zweifellos',#certainly
                     ]
                    ),
    
    'mental_poss':(['nehme an',
                    'nimmst an',
                    'nimmt an',
                    'nehmen an',
                    'nehmt an'], #assume, but with more clear qualificational use 
                   ['denke',
                    'denkst',
                    'denkt',
                    'denken',
                    'glaube',
                    'glaubst',
                    'glaubt',
                    'glauben',# Nuyts 2000
                    'meine',
                    'meinst',
                    'meint',
                    'meinen', # to mean, no qualificational use in english, but stronger in german, and menen, too in dutch (Nuyts 2000)
                    'vermuten',#to presume (outdated in engish mostly, (Nuyts, 2000))
                    'vermute',
                    'vermutest',
                    'vermutet',
                    'rechne',#reckon, qulaificational use, (Nuyts 2000)
                    'rechnest',
                    'rechnet',
                    'rechnen',
                    'sage',
                    'sagst',
                    'sagt',
                    'sagen',
                    ]
                    ),
    
    'mental_cert':([],
                   ['weiß',
                    'weißt',
                    'wissen',
                    'wisst'] #to know, qualificational use, though whether certain/uncertain unclear (Nuyts 2000)
                   ),
    
    'particle_poss':([],
                     ['wohl']
                      ),
    'particle':([],
                 ['aber',
                  'auch',
                  'bloß',
                  'denn',
                  'doch',
                  'eigentlich',
                  'eben',
                  'etwa',
                  'einfach',
                  'erst',
                  'halt',
                  'ja',
                  'nun',
                  'mal',
                  'nur',
                  'schon',
                  'vielleicht',
                  'ruhig']
                 ),
    
    'will_future': ([],
                  ['werde',
                   'wirst',
                   'wird',
                   'werden',
                   'werdet',
                   'werden']),
    
     'go_future':([],
                  []
                   )
     }

# =============================================================================
# Create master dictionaries
# =============================================================================
WORD_LISTS = {
        'english':english,
        'dutch':dutch,
        'german':german
            }    
#load map
LEMMA_MAP = _load_map()

#run and save changes to lemma map
if __name__ == '__main__':
    LEMMA_MAP = check_add_lemmas(add_lemmas=True)
    
