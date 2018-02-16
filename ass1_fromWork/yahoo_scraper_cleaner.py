#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exract price and time for the stock
"""

from bs4 import BeautifulSoup as bs
import requests
import re

('Which stock would you like to trade?\n a - Camden Property Trust / CPT\n b - Delta Airlines / DAL\n c- Apache / APC\n d - Con Edison / ED\n e - Citigroup / C\n')

#stock1 CPT
class scrapy(object):
    def __init__(self):
        self.uni_dic={'CPT':'https://finance.yahoo.com/quote/CPT?p=CPT','ed':'https://finance.yahoo.com/quote/ED?p=ED','DAL':'https://finance.yahoo.com/quote/CPT?p=CPT','APC':'https://finance.yahoo.com/quote/APC?p=APC','C':'https://finance.yahoo.com/quote/C?p=C'}
        #universe of stocks for our purposes
        def rtYhoDats(self,stocks=self.uni_dic):
    #retrieve Yahoo data; function should work with a dictionary
            yahoo_dict={}
            for k,v in stocks.items():
                yahoo_pg=requests.get(v)
                stock_html=yahoo_pg.text
                stock_soup =bs(stock_html,'html.parser')
            #remember that dictionaries do not maintain
                quote=stock_soup.find_all(class_='quote-header-section')
                yahoo_dict[k]=re.search(r'(.*?)(\+|-)',quote[0]).group(0)[:-1]
            return(yahoo_dict)
            
result_list=[]
for i in quote[0]:
    #if 'Trsdu(0.3s)' in i.class_:
    if i.find_all('span',class_='Trsdu(0.3s)'):
        #select for only the element I need
        result_list.append(i.contents)

ma=[g.text for g in result_list[0]]
ma[0]
#this works
re.search(r'(.*?)(\+|-)',ma[0]).group(0)[:-1]
re.match(r'[0-9](?:-)',ma[0])
re.match('(.*?)-|+',ma[0])
re.match('(.*)',ma[0])
#h("(.*?):",string).group()

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
