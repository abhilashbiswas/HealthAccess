# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:52:29 2021

@author: vidisha
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

keywords = ["surge", r"^Dent|prostho", "mental|psch|rehab","Pharma",\
            "Hear|eye|opti|Audio", "Preventive", "Gynec", "Radio"]
mapping = {}

for k in keywords:
    for i in categories["Category"]:
        if re.search(k, i, flags = re.IGNORECASE) != None:
            print(k + ' : ' + i)
            if i in mapping.keys() and k not in mapping[i]:
                mapping[i].append(k)
            if i not in mapping.keys():
                mapping[i] = [k]
            
hospital_data = pd.read_csv("hospital_list.csv")

# Final categories visible to users
final_cat = {'surge' : 'Surgery',  r"^Dent|prostho" : 'Dental Care',\
        'mental|psch|rehab' : 'Mental Health and Rehabilitation',\
            'Pharma':'Pharmacy','Hear|eye|opti|Audio': 'Eye and Ear Care',\
                'Preventive': 'Preventive Care', \
                    'Gynec': 'Women & Reproductive Care',\
                        'Radio': 'Radiology'  }

    

for i in mapping.keys():
    a = hospital_data["Category"] == i
    hospital_data.loc[a,"Keywords"] = ", ".join([final_cat[mapping[i][j]] \
                                                for j in range(len(mapping[i]))])
        

    

hospital_data.to_csv('hospital_list_with_keywords.csv', index = False)









    
