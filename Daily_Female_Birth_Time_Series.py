# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:57:59 2020

@author: Dipta Das
"""

import pandas as pd
import numpy as np

dt = pd.read_csv('datasets/daily-total-female-births.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
dt1 = pd.read_csv()

print(dt.head())
print(dt.size)
print(dt['1959-01'])
print(dt.describe())