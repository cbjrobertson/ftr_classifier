#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 00:17:04 2019

@author: cole
"""
import importlib as iml
import pandas as pd
import ftr_classify as ftr

ftr = iml.reload(ftr)

dx = pd.read_pickle('test.pkl')


dx = ftr.prepare(dx)
dx = ftr.score(dx)
dx = ftr.apply_dominance(dx)
dx = ftr.process_dataframe(dx)
