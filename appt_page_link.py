#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 10:22:54 2021

@author: abhilashbiswas
"""

import requests
from bs4 import BeautifulSoup
import re

urls = 'https://www.ahn.org'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
 
# opening a file in write mode
f = open("test2.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
   data = link.get('href')
   if data!=None:
       f.write(data)
       f.write("\n")
 
f.close()

pattern = r'appointment'
#extracting the appt extension
with open('test2.txt','r') as f:
    for line in f:
        if re.search(pattern,line) != None:
            text = line


#Correcting the extension
if text[-1] == '\n':
    text = text[:-1]

       
appt_link = urls + text

#Checking if the webpage exists (since we are constructing by adding strings)
import requests

response = requests.get(appt_link)
if response.status_code == 200:
    website_exists =1
else:
    website_exists=0
    
    
