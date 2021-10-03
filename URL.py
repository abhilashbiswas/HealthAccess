#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:38:36 2021

@author: anchalchaudhary
"""

import requests
from bs4 import BeautifulSoup
 
 
url = 'https://www.upmc.com/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    urls.append((link.get('href')))
    print(urls)
    
    
    pattern = r'appointment'
    import re
    for k in urls:
        if re.search(pattern,k) != None:
            print(k)
            