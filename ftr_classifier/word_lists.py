#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""

# =============================================================================
# Features 
# =============================================================================
LANGUAGES = ['english','dutch','german']

META_FEATURE_MAP = {'future':'future',
       'present':'present',
       'future_dom':'future',
       'go_future_dom':'future',
       'will_future_dom':'future',
       'particle':'',
       'present_dom':'present',
       'adv_adj_poss':'lexical uncertain',
       'adv_adj_cert':'lexical certain',
       'mental_poss':'lexical uncertain',
       'mental_cert':'lexical certain',
       'particle_poss':'lexical uncertain',
       'particle_cert':'lexical certain',
       'verb_poss':'verbal uncertain',
       'verb_cert':'verbal certain'
       }
FEATURE_NAME_MAP = {'future':"grammar book ``futures''",
                    'present':"present tense response",
                    'future_dom':"grammar book ``futures''",
                    'go_future_dom':"grammar book ``future'' using ``be going to/gaan'' constructions",
                    'will_future_dom':"grammar book ``future'' auxilaries ``will/shall'',``zullen'', ``werden''",
                    'particle':"modal particles with no epistemic valance",
                    'present_dom':"present tense response",
                    'adv_adj_poss':"adverbs/adjectives/nouns",
                    'adv_adj_cert':"adverbs/adjectives/nouns",
                    'mental_poss':"mental state predicates",
                    'mental_cert':"mental state predicates",
                    'particle_poss':"modal particles",
                    'particle_cert':"modal particles",
                    'verb_poss':"modal verbs",
                    'verb_cert':"modal verbs"
                    }

SUBMISSIVE_FEATURES = ['present','future','will_future','go_future']

DOMINANT_FEATURES = ['verb_poss','verb_cert',
                     'adv_adj_poss','adv_adj_cert',
                     'mental_poss',
                     'particle_poss','particle',
                     'particle_cert']

DOMINATED_FEATURES = ['future_dom','present_dom',
                     'go_future_dom','will_future_dom']

SUMMARY_FEATURES = ['lexi_poss','lexi_cert','uncertain','certain']

EXTRA_FEATURES = ['negated','no_code']

MAIN_FEATURES = ['lexi_poss','lexi_cert','future_dom',
                  'present_dom','verb_poss','verb_cert','uncertain','certain']

FEATURES = DOMINANT_FEATURES + SUBMISSIVE_FEATURES
ALL_FEATURES = FEATURES + DOMINATED_FEATURES + SUMMARY_FEATURES + EXTRA_FEATURES

# =============================================================================
# English word lists
# =============================================================================
english = {'present':([' i s ',
                       ' im '],#typos
                      ["'m",
                       "'re",
                       "'s",
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
                       'congradulate',
                       'congradulates',#typo
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
    
    'future':(['about to','is going','are going','am going','going to','theyll'],
              ['will',
               'wil',
               'shall',
               "'ll",
               "ll"]
            ),
    
    'verb_poss':([],
                 ['can',
                  'may',
                  'could',
                  'might',
                  'should',
                  'sould',#typo
                  'ought',
                  'would'#used epistemically in the 'what your brother would do... question, i.e. as a conditional 
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
                'indubitable',
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
                   
    'particle_poss':([],
                     []
                     ),
    
    'particle_cert':([],
                     []
                     ),
    'particle':([],
                []
                ),
    
    'will_future':(['theyll'],
                   ['will',
                    'wil',
                    "'ll",
                    "ll"]
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
                     'valt om','storten in','storten inen',
                     'kom an','komt an','komen an','knap op',
                     'kom ik',
                     'knapt op','knappen op','uit eten','uit eet',
                     'kom op','komt op','komen op','ik ik',#typo
                     'zwel op','zwelt op','zwellen op'],
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
                     'hen',#heb typo
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
                     'laten',
                     'latten',#typo
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
                     'resit',#misspelled
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
                     'verlijten',#common typo
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
                     'word',#could indicate future marking, but sentences in frames use  it not as such (i.e. I become fat...)
                     'worden',
                     'wordt',
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
                     'zwelt',
                     'zeg', #say, and though can be used as mental state pred use (Nuyts, 2000), it is not in our frames, i.e. "I {SAY} no this time..."
                     'zeggen',
                     'zegt']
                    ),
    
          'future':(['staat op'],#about to
                   ['ga',
                    'gaat',
                    'gat',#common typo
                    'gaan',
                    'zal', 
                    'zullen',
                    'zult', 
                    'zul',
                    'economie.zal',#typo
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
                      'vermoogd',
                      'zou',#past tense form of zullen, translated as 'should'/indicates epistemic modality in Broekhuis (2014) + coders/informants agree 
                      'zouden'
                      ] #i.e. mogen + prefix ver-
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
                         'waarschijnlijk',
                         'wellicht',#probably
                         ]
                        ),
        'adv_adj_cert':(['wel degelijk',
                         '100%',#expresses certainty in some (1) response
                         'twijfel er niet'#no doubt
                         ],
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
                         'logisch',
                         'natuurlijk',
                         'nodig',
                         'noodzakelijk',
                         'normaal',
                         'ondenkbaar',
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
                         'zeker',
                         'ongetwijfeld']#undoubtedly]
                        ),
        'mental_poss':(['houden voor',
                        'niet weten',
                        'neit weet'],
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
                         'verwacht',
                         #'zeg', #say, and though can be used as mental state pred use (Nuyts, 2000), it is not in our frames
                         #'zeggen',
                         #'zegt',                         
                         ]
                        ),
        'particle_poss':(['wel eens'],
                         ['wel']
                         ),
        
        'particle_cert':([],
                         ['toch'] #indicates certainty according to coders, informants
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
                     'nu']
                    ),
        'will_future':([],
                       ['zal', 
                        'zult',
                        'zul',
                        'zullen',
                        'economie.zal'#typo
                        ]
                       ),
        'go_future':([],
                     ['ga',
                      'gaat',
                      'gaan',
                      'gat',#typo
                      'gaanverliezen']#typo
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
                      'gehen auf',
                      'breche zusammen',
                      'brichst zusammen',
                      'bricht zusammen',
                      'brechen zusammen',
                      'brecht zusammen'],
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
                      'leben',
                       ]),
    'future': ([],
               ['werde',
                'wirst',
                'wird',
                'werden',
                'werdet',
                'werden',
                'wirdt'#typo
                ]
               ),
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
                  
                  #konjunktiv ii
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
                  
                  ##konjuntiv of werden, i.e. 'would' with epistemic uses: according to informant/coder
                  'würde',
                  'würdest',
                  'würden',
                  'würdet',
                  
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
                     'wahrscheinlichkeit',#probability -- informant coder
                     'möglich',
                     'möglicherweise',
                     'offenbar',
                     'scheinbar',#seemingly
                     #'vielleicht',
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
                    #'sage',#while this can be used epistemically, none of the question frames do so
                    #'sagst',# and do use 'to say' in non epistemic ways
                    #'sagt',
                    #'sagen',
                    'erwarte',
                    'erwartest',
                    'erwartet',
                    'erwarten'
                    ]
                    ),
    
    'particle_poss':([],
                     ['wohl',
                      'vielleicht']
                      ),
    
    'particle_cert':([],
                     []
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