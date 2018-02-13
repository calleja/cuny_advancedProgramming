#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exract price and time for the stock
"""

from bs4 import BeautifulSoup as bs
import requests
import re

#stock1 CPT
cpt='https://finance.yahoo.com/quote/CPT?p=CPT'
#Visa
visa='https://finance.yahoo.com/quote/V?p=V'
#Con Edison
ed='https://finance.yahoo.com/quote/ED?p=ED'

cpt_pg=requests.get(cpt)
cpt_html=cpt_pg.text
cpt_soup = bs(cpt_html,'html.parser')

quote=cpt_soup.find_all(class_='quote-header-section')

result_list=[]
for i in quote[0]:
    #if 'Trsdu(0.3s)' in i.class_:
    if i.find_all('span',class_='Trsdu(0.3s)'):
        #select for only the element I need
        result_list.append(i.contents)

[g.text for g in result_list[0]]

v_pg=requests.get(visa)
v_html=v_pg.text
v_soup = bs(v_html,'html.parser')

quote=v_soup.find_all(class_='quote-header-section')

result_list=[]
for i in quote[0]:
    #if 'Trsdu(0.3s)' in i.class_:
    if i.find_all('span',class_='Trsdu(0.3s)'):
        #select for only the element I need
        result_list.append(i.contents)
g=quote[0].text #this grabs all the text - I can run this through a regular expression... 'g' is of type string
result_list[0]
ma=[g.text for g in result_list[0]]
