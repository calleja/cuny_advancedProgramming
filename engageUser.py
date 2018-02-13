#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Client dialogue
"""
import sys
sys.path.append('/home/lechuza/Documents/CUNY/data_607/assignment1')
import tradeClass as trade
import ass1_acountsClass as accts
import datetime as datetime
import tradeManager as tm
import engageUser as eu

class Dialogue(object):
    def __init__(self):
        self.todayTrading=tm.TradingDay()
        #create a new account/portfolio
        self.act=accts.Account()
    
    def engageUser(self):
        menuSelection=input('Please select from the list of options below.\n a -Trade\n b - Show Blotter\n c- Show P/L\n d - Quit\n')
        if menuSelection=='a':
            stockTrade=input('Which stock would you like to trade?\n a - Camden Property Trust / CPT\n b - Delta Airlines / DAL\n c- Apache / APC\n d - Con Edison / ED\n e - Citigroup / C\n')
            stock_dic={'a':'CPT','b':'DAL','c':'APC','d':'ED','e':'C'}
            ticker=stock_dic[stockTrade]
            
            #call the yahoo scraper... then call TradeManager which calls TradeClass... actually - have the option to call the yahoo scraper from the TradeManager object.
            self.tradeWorkflow()
            #arguments will probably be the dictionary from the yahoo scrape
        elif menuSelection=='b':
            #call the blotter from the tradeManager class - may need rendering in this class, and the return value from either this function or another in this class can be handled at the controller level
            print('call blotter function')
            #the blotter function will return a list of dictionaries, or perhaps a pandas dataframe, that I'll then print... if extensive formating is required, I'll do it in this class
            return
        elif menuSelection=='c':
            #call the yahoo scraper on all stocks (a list)
            stock_universe=['CPT','APC','DAL','ED','C']
            print('send stock universe to yahoo scraper')
            return
        else:
            print('please select an option')
            self.engageUser()
    
    def tradeWorkflow(self):
        buy_trade={'ticker':'CPT','price':98.108,'shares':1000,'timestamp':datetime.datetime.today(),'tradetype':'buy','original_tradetype':'long'}
        buy_test_today=self.todayTrading.makeTrade(buy_trade,self.act)
        buy_dict=buy_test_today.tradeType()
        self.act.postEquityTrade(buy_dict)
        print(self.act.getPortfolio())
        print(self.act.cash_bal)
        
    def blotterWorkflow(self):
        return
    def portfolioStatementWorkflow(self):
        #extract the current price for all stocks in the universe... or the portfolio
        stock_universe=['CPT','APC','DAL','ED','C']
        return