#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exract price and time for the stock

Which stock would you like to trade?\n a - Camden Property Trust / CPT\n b - Delta Airlines / DAL\n c- Apache / APC\n d - Con Edison / ED\n e - Citigroup / C\n
"""

from bs4 import BeautifulSoup as bs
import requests
import re

#stock1 CPT
class Scrapy(object):
    
    def __init__(self):
        
        self.uni_dic={'CPT':'https://finance.yahoo.com/quote/CPT?p=CPT','ED':'https://finance.yahoo.com/quote/ED?p=ED','DAL':'https://finance.yahoo.com/quote/DAL?p=DAL','APC':'https://finance.yahoo.com/quote/APC?p=APC','C':'https://finance.yahoo.com/quote/C?p=C'}
        #universe of stocks for our purposes
        
    def rtYhoDats(self,stocks=None):
    #retrieve Yahoo data; function should work with a dictionary... yahoo_dict is a dictionary of dictionaries... stocks is a ticker, I'll use that to index the dictionary
        if stocks is None:
            #facilitate a dictionary if something else is passed
            stocks=self.uni_dic
        else: #make a dictionary with a singleton
            stocks={stocks:self.uni_dic[stocks]}
        yahoo_dict={}
        for k,v in stocks.items():
            yahoo_pg=requests.get(v)
            stock_html=yahoo_pg.text
            stock_soup =bs(stock_html,'html.parser')
                
            #remember that dictionaries do not maintain
            quote=stock_soup.find_all('div',{'id':'quote-header'})
            yahoo_dict.setdefault(k,{})
                #k is a ticker
                #call the parser, which returns a dictionary of bid and ask for the stock
            yahoo_dict[k]=self.parseText(quote)
        return(yahoo_dict)
            
    def parseText(self,extract):
            #parse the price text and return a dictionary of the bid and ask... this dictionary will be nested into the ticker dictionary
        mini_dict={}
        for i in extract:
            mini_dict['ASK']=self.lowerParse(i.find('td',{'data-test':'ASK-value'}).get_text())
            mini_dict['BID']=self.lowerParse(i.find('td',{'data-test':'BID-value'}).get_text())
        return(mini_dict)
        
    def lowerParse(self,price_text):
        price=re.search(r'.*?(?: )',price_text)
        price_float=float(price.group(0))
        return(price_float)
            
