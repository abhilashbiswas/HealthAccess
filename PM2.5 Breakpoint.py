#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:25:04 2021

@author: yuxuansheng
"""

import pandas as pd

AQI = pd.read_csv('aqi_breakpoints.csv')
print(AQI)

Breakpoint = AQI[['AQI Category', 'Low Breakpoint', 'High Breakpoint']]
print(Breakpoint)

PM_AQI = Breakpoint.loc[0:15]
print(PM_AQI)

