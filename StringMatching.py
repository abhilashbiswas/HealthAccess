#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:52:53 2021

@author: anchalchaudhary
"""

import urllib.request
import html2text
from bs4 import BeautifulSoup


soup = BeautifulSoup(urllib.request.urlopen('https://www.upmc.com/').read(),'html.parser')

txt = soup.find('div', {'class' : 'body'})

#print(html2text.html2text(txt).get_text())


#soup = BeautifulSoup(html)
print(soup.get_text())
