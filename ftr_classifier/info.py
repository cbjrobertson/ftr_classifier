#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 22:32:52 2019

@author: cole roberson
"""


INFO = {'version':'1.0.5',
        "long_description" :
        '''This is an implementation of the key-word analysis techniques described in Robertson et al. (TKTK). It is designed to classify future-time-referring sentences in English, Dutch, and German in terms of whether 
        they use the accepted "future" tense morphemes (i.e. will/shall/be going to (English); zullen/gaan (Dutch); or werden (German)),
        use the present tense to refer to future time, or use an expression which specifically marks the probability of the utterance, 
        i.e. "It could rain tomorrow", or "It will probably rain tomorrow." This classifier almost certainly overfit to the data it has
        been built/trained on, and will not perform well out-of-sample. It is designed to be used exclusively with data generated using
        the  Future Time Reference questionnaire described in Robertson et al (TKTK), and available for free to academic researchers,
        downloadable here (to come). 
        
        Any interested researchers should feel free to contact myself (Cole Robertson) at cbjrobertson@gmail.com, or open an issue for discussion
        on the project git repository.
        ''',
        'description':"Classifies English, Dutch and German sentences in terms of how they refer to the future."
        }