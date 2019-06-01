#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""

# =============================================================================
# Features 
# =============================================================================
FEATURES = ['present','future',
            'verb_poss','verb_cert',
            'adv_adj_poss','adv_adj_cert',
            'mental_poss','mental_cert',
            'particle_poss','particle',
            'will_future','go_future']


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
                       'congradulates',
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
                       'indists',
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
                    ['probably',
                     'probable'
                     'probability',
                     'possibly',
                     'possibility',
                     'possible',
                     'likely',
                     'somewhat',
                     'maybe',
                     'perhaps',
                     'apparently',
                     'dubiously',
                     'expectably',
                     'expectedly',
                     'improbably',  
                     'mayhap',
                     'perchance',   
                     'potentially',
                     'presumably',
                     'questionably',
                     'seemingly',
                     'supposedly',
                     'supposed'
                     'uncertainly']
                    ),
    
    'adv_adj_cert':(['for sure'],
               ['definitely','definetly',#missspelling
                'definite',
                'certainly',
                'certain',
                'certainty'
                'assuredly'
                'assured',
                'clearly',
                'doubtless',
                'indubitably',
                'inevitably',
                'infallibly',
                'irrefutably',
                'irrefutable'
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
                    'believe',
                    'believing'
                    'reckon',
                    'reckoning',
                    'expect',
                    'expecting'
                    'planning',
                    'plan']
                   ),
    
    'mental_cert':([],
                   ['know']),
                   
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
dutch = {'present':(['is het','vallen om','storten in'
                     'en ik in au','het stoort',
                     'contact opnemen','leuk vindt',
                     'ze halen het','val om','stort in',
                     'valt om','storten in'],
                    ['.is',#typo
                     'accepteer',
                     'accepteert',
                     'accepteeren',
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
                     'danken'
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
                     'resi',
                     'resideer',
                     'resideert',
                     'resideren',
                     'resit',
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
                     'verhuis',
                     'verhuist',
                     'verhuizen',
                     'verlies',
                     'verliest',
                     'verliezen',
                     'verlslijten',
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
                     'zeg',
                     'zeggen',
                     'zegt',
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
                      'mogen' #doesn't have primary epistemic uses, more deontic, Nuyts 2000, but included anyway for exploratory pusposes 
                      'vermogen',
                      'vermoogd'] #i.e. mogen + prefix ver-
                     ),
        'verb_cert':([],
                     ['moeten',
                      'moet',
                      'moest',
                      'gemoeten',
                      'moesten',
                      'wil',
                      'wilt',
                      'willen']#no real epistemic use, i.e. "to want" but included for exploratory purposes, see Nuyts 2000
                     ),
        'adv_adj_poss':(['in aanmerking komend'
                         'niet zeker',
                         'is er een kans',
                         'te komen'],
                        ['horen',
                         'gehoord', #to hear, possible epistemic use? Check data
                         'waarschijnlijk',
                         'vermoedelijk',
                         'aannemelijk',
                         'mogelijk',
                         'misschien',
                         'mogelijkerwijs',
                         'geschiktlijkend',
                         'veelbelovend',
                         'verwacht',
                         'bedenkelijk',
                         'blijkbaar',
                         'denkelijk',
                         'hypothetisch',
                         'ongeveer',
                         'onzeker',
                         'schijnbaar',
                         'twijfelachtig',
                         'wellicht',
                         'word',
                         'worden',
                         'wordt']#unclear worden "becomes" is a futuroid, but is in the present tense. from a cognitive/pragmatic perspective, it is somewhat modal/marked
                        ),
        'adv_adj_cert':(['wel degelijk'],
                        ['definitief',
                         'voorgoed',
                         'beslist',
                         'zeker',
                         'stellig',
                         'vast',
                         'bepaald',
                         'wis',
                         'gedwongen',
                         'nodig',
                         'ongetwijfeld',
                         'verplicht',
                         'absoluut',
                         'alleszins',
                         'allicht',
                         'doorgans'
                         'duidelijk',
                         'echt',
                         'eenvoudigweg',
                         'eigenlijk',
                         'essentieel',
                         'evident',
                         'fietelijk',
                         'gegarandeerd',
                         'glashelder',
                         'hoogstwaarschijnlijk',
                         'inderdaad',
                         'kennelijk',   
                         'klaarblijkelijk', 
                         'logisch',
                         'natuurlijk',
                         'noodzakelijk',
                         'normaal',
                         'ondenkbaar',
                         'ongetwijfeld',
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
                         'uiteraard',
                         'vanzelfsprekend',
                         'werkelijk']
                        ),
        'mental_poss':(['jij denkt',
                        'hij denkt',
                        'wij denken',
                        'zij denken'],
                        ['denk']
                        ),
        'mental_cert':([],
                       []
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
                      'kaputt',
                      'zusammen',
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
                      'nutzen',
                      'mache',
                      'machst',
                      'macht',
                      'machen',
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
                      'sage',
                      'sagst',
                      'sagt',
                      'sagen',
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
                      'lebe', 
                      'liebe', 
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
                  'könne'
                  'könnte',
                  'könntest',
                  'könnten',
                  'könntet',
                  
                  #may have some epistemic use, but not typical (Nuyts 2000). Both konjunctiv ii and indicative included    
                  'sollen',
                  'soll',
                  'sollst',
                  'sollt',
                  
                  #konjunktiv ii uncelar if I should include ???
                  'sollte',
                  'solltest',
                  'sollten',
                  'soltet',
                  
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
                    ['wahrscheinlich',
                     'möglicherweise',
                     'vielleicht',
                     'eventuell',
                     'gegebenenfalls',
                     'womöglich',
                     'möglich']
                    ),
    
    'adv_adj_cert':(['auf jeden fall'],
                    ['definitiv',
                     'sicher',
                     'aufjedenfall',
                     'jedenfalls',
                     'gewiss',
                     'bestimmt',
                     'sicherlich']
                    ),
    
    'mental_poss':(['ich denke',
                    'du denkst',
                    'er denkt',
                    'wer denken',
                    'ihr denkt',
                    'sie denken'],
                    []
                    ),
    
    'mental_cert':([],
                   []
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
# Create master dictionary
# =============================================================================
WORD_LISTS = {
        'english':english,
        'dutch':dutch,
        'german':german
            }

 