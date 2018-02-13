#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
I will need to connect to a profit calc engine
"""
import sys
#these paths will later need to be edited and matched with the imported/downloaded git folder
sys.path.append('/home/lechuza/Documents/CUNY/data_607/assignment1')
#import ass1_acountsClass as acct

class EquityTrade():
    
    def __init__(self,trade_dic,acctSnapshot):
        #trade_dic is the dictionary/json object scraped from yahoo
        self.ticker=trade_dic['ticker']
        self.price=trade_dic['price']
        self.shares=trade_dic['shares']
        self.timestamp=trade_dic['timestamp']
        self.tradetype=trade_dic['tradetype'] #buy, sell, short
        self.original_trade_type=trade_dic['original_tradetype']
        #self.currentPortfolio=acctSnapshot #ass1_accountsClass
        
    
    def qaTrade(self):
        #ensure that the trade makes sense given the current holdings in the portfolio... return a True or False... True will allow the transaction to make all the proper updates, while a False should prompt the user that the transaction is not allowed given the current holdings
        return True
    def tradeType(self):
        #call the appropriate function, determined by trade type i.e. short, long, sell from long
        if self.tradetype=='short':
            if self.qaTrade():
                result_set=self.shortTrade()
            else: print('trade is not legal')
        elif self.tradetype=='buy':
            if self.qaTrade():
                result_set=self.longTrade()
            else: print('trade is not legal')
            #don't need to send this through the qaTrade
        elif self.tradetype=='sell to close':
            if self.qaTrade():
                result_set=self.sellToClose()
            else: print('trade is not legal')
        elif self.tradetype=='buy to close':
            #don't need to send through qa
            if self.qaTrade():
                result_set=self.buyToClose()
            else: print('trade is not legal')
        
        return result_set
    
    def shortTrade(self):
        #no drawdown of cash, update portfolio w/negative shares
        notional_delta=self.shares*self.price
        position_delta=self.shares*-1
        cash_delta=0
        
        result_set={'notional_delta':notional_delta,'cash_delta':cash_delta,'position_delta':position_delta,'ticker':self.ticker,'original_tradetype':'short'}
        return(result_set)
        
    def buyToClose(self):
        #no drawdown of cash, update portfolio w/negative shares
        notional_delta=-1*self.shares*self.price
        position_delta=self.shares*-1
        cash_delta=notional_delta
        
        result_set={'notional_delta':notional_delta,'cash_delta':cash_delta,'position_delta':position_delta,'ticker':self.ticker,'original_tradetype':'short'}
        return(result_set)
        
    def longTrade(self):
        #cash drawdown, increase number of shares, increase in notional...
        notional_delta=self.shares*self.price
        cash_delta=notional_delta*-1 #cash debit
        position_delta=self.shares
        
        result_set={'notional_delta':notional_delta,'cash_delta':cash_delta,'position_delta':position_delta,'ticker':self.ticker,'original_tradetype':'long'}
        return(result_set)
        
    def sellToClose(self):
        #decrease #of shares held, increase cash, record realized g/l... realized g/l could be outsourced to a g/l calculator
        notional_delta=-1*self.shares*self.price
        position_delta=self.shares*-1
        cash_delta=self.shares*self.price #cash increase
        
        result_set={'notional_delta':notional_delta,'cash_delta':cash_delta,'position_delta':position_delta,'ticker':self.ticker,'original_tradetype':'long'}
        return(result_set)
        
        #call the proft calc engine and calculate realized profit
    
    def updatePortfolio(self):
        #interact with the portfolio dictionary from the ass1_accountsClass.py file... I can either make the update via the account class or this trade class - perhaps not both
        #this function could serve as the argument to ass1_acountsClass.updateAccount()
        return
    

