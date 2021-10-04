# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:52:29 2021

@author: vidisha
"""

"""
STEP 1: Identify 8-10 relevant keywords:
    1) Ortho
    2) Dent
    3) Mental
    4) Pharma
    5) Ear
    6) Counsel
    
STEP 2: Look for categories that match each of these keywords
    
    
"""

import pandas as pd
import re

categories = pd.read_csv("hospital_categories.csv")

keywords = ["Orthop", "Dent", "Mental", "Pharma", "Hear", "Counsel", "Nutri"]

for k in keywords:
    for i in categories['Category']:
        if re.search(k, i, flags = re.IGNORECASE) != None:
            print(k + ' : ' + i)
        
    
    