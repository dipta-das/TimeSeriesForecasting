# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:40:18 2020

@author: Dipta Das
"""

import pandas as pd
import numpy as np

dt = pd.read_csv('datasets/daily-min-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
dt1 = pd.read_csv()

print(dt.head())
print(dt.size)
print(dt['1959-01'])
print(dt.describe())