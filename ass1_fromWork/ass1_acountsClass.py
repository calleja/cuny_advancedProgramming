#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Account class...
This object will have attributes like cash and positions and will need to allow for retrieval methods and some minor calculations of each (unless it can be done in the trade/transaction class). This object must persist throughout the trading session.

Positions must store total shares, average price, possibly VWAP
In addition, store cash amount; keep in mind that short positions do not affect cash balance.
"""

class Account:
    def __init__(self):
        self.cash_bal=1000000
        #will be a nested dictionary, the outermost key is the ticker and the value will be a dictionary of total shares, average price and possibly VWAP, realized p/l... ex: {ticker:{'notional':notaionValue,'direction':direction_string, etc...}}
        self.positions={}
        self.tickers_owned=[]
        
    def getCash(self):
        print('cash balance is :'+str(self.cash_bal))
        return self.cash_bal
    
    def getPortfolio(self):
        return(self.positions)
    
    def updateTickersOwned(self):
        #could also just get the keys from the dictionary
        self.tickers=self.position.keys()
            
    def amend_cash(self,amend):
        self.cash=self.cash+amend
        
    def checkIfNew(self,dic):
        #checks whether there is a position in that stock and in the same direction
        if dic['ticker'] in self.positions.keys():
            if self.positions[dic['ticker']]['original_direction']==dic['original_tradetype']:
                return
        else:
            #create an entry/holding in the portfolio for that stock at 0 notional and shares
            self.positions[dic['ticker']]={'shares':0,'notional':0,'original_direction':''}
            print(self.positions)
        
    def postEquityTrade(self,dic):
        #dic will come from the tradeClass
        '''
  the dictionary will contain total number of shares and trade price... conditional statements will qualify whether the trade serves to: 
    a) open a new position - can be long or short
    b) close all or part of an existing position - long or short
    c) augment an existing position - short or long

this function will then instantiate a tradeClass object that will QA the trade (verify whether legal), then subsequently amend the current portfolio
'''
        #if the trade/position is new, create a new entry in the dictionary to not trigger errors
        self.checkIfNew(dic) #really only necessary for buys and shorts
        
        self.positions[dic['ticker']]['notional']=dic['notional_delta']+self.positions[dic['ticker']]['notional']
        self.cash_bal=dic['cash_delta']+self.cash_bal
        self.positions[dic['ticker']]['shares']=dic['position_delta']+self.positions[dic['ticker']]['shares']
        #how to keep track of "new" trades - tracking the genesis trade
        self.positions[dic['ticker']]['original_direction']=dic['original_tradetype']
        #updat self.positions[ticker]['realized_pl'] with another application

    def currentHoldingsDirection(self):
        'add a dictionary element indicating whether the position is long or short - under development and may not be necessary'
        return