#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:42:36 2021

@author: anchalchaudhary
"""
"""Step 1: Identifying the categories:
    
    1. Surgery: surge
    2. Dental Care: Dent|prostho
    3. Mental Health and Rehabilitation: mental|psch|rehab 
    4. Pharmacies: Pharma 
    5. Eye and Ear Care: Hear|eye|opti|Audio 
    6. Preventive Care: Preventive 
    7. Women & Reproductive Care: Gynec
    8. Radiology: Radio
   
STEP 2: Look for categories that match each of these keywords"""    
    
import pandas as pd
import re

categories = pd.read_csv("hospital_categories.csv")

keywords = ["surge", "(^Dent|prostho)", "(mental|psch|rehab)","Pharma", "(Hear|eye|opti|Audio)", "Preventive", "Gynec", "Radio"]

for k in keywords:
    for i in categories['Category']:
        if re.search(k, i, flags = re.IGNORECASE) != None:
            print(k + ' : ' + i)

dict = {'surge': 'Surgery', 'Dent|prostho': 'Dental Care', 'mental|psch|rehab' : 'Mental Health and Rehabilitation', 'Pharma':'Pharmacy','Hear|eye|opti|Audio': 'Eye and Ear Care', 'Preventive': 'Preventive Care', 'Gynec': 'Women & Reproductive Care', 'Radio': 'Radiology'  }

print(dict)    