#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:47:09 2021

@author: anchalchaudhary
"""

import requests
from bs4 import BeautifulSoup

httpString ='https://www.upmc.com/'
print(httpString)
page = requests.get(httpString)

soup = BeautifulSoup(page.content, 'html.parser')

y = soup.find(class_="col-xs-12 col-sm-2")
contact = y.find(class_="rte")
period = contact.find().get_text()
print(contact)




httpString ='https://www.upmc.com'
print(httpString)
page = requests.get(httpString)

soup = BeautifulSoup(page.content, 'html.parser')

z = soup.find(class_="button-container")
x = z.find('href=')
app = z.find().get_text()


url = soup.find("a", {"class":"anchor-link"})["href"]
#print(url)

final_web_path = httpString + url
print(final_web_path)





#print(httpString)

#app = zb.find(href="/contact/appointments")
#print(app)

