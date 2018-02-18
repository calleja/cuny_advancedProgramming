#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This class interacts with the tradeClass and stores a log of all the trades. This facilitates p+l calculation and the trade log.

Blotter requirements:
    side (Buy/Sell), Ticker
    Qty, Executed Price
    Timestamp, Money In/Out
    
P/L:
    Ticker, current position (can be 0),
    Current Market Price, VWAP,
    Unrealized p/l, realized p/l
"""
import sys
sys.path.append('/home/lechuza/Documents/CUNY/data_607/assignment1')
import tradeClass as trade

class TradingDay(object):
    
    def __init__(self):
        self.tradeLogTup=()
        
    def makeTrade(self,rawTradeDict,act):
        #log the trade and make the trade object available for passing to the account object... Call the yahoo finance scraper. trade.EquityTrade requires fewer attributes than what is to be retrieved from the scraper and what we need to record here on the log.
        #TODO parameter specificTradeDict contains an entry for the timestamp, but this is not persisted by the 'trade' object; this is needed for the trade log
        specificTrade=trade.EquityTrade(rawTradeDict,act)
        #an instantiation of EquityTrade class... no processing done yet
        
        #TODO ensure that illegal trades are not logged... this logic is contained within tradeClass.qaTrade() function
        try:
            specificTradeResult=specificTrade.tradeType()
            formattedDic=self.prepDict(specificTradeResult,rawTradeDict)
            self.logTrade(formattedDic)
            print('your trade has been logged')
            return(specificTradeResult)
        except ValueError:
            #TODO ensure this breaks out of the function
            print('trade was not executed')
            raise ValueError #pass the ValueError to the calling function in engageUser class
        #a dictionary of scrubbed and processed trade attributes... unfortunately, this does not handle an errant trade
        #TODO ensure that illegal trades are not logged... this logic is contained within tradeClass.qaTrade() function... this function does not and should not handle errant trades... need to ensure that the application breaks and that prepDic() is not called
        
        
    def prepDict(self,tradeClassDict,rawDict):        
        #take elements from both dictionaries and create a third one for logging
        formattedDict={'side':rawDict['tradetype'],'ticker':rawDict['ticker'],'quantity':rawDict['shares'],'executed price':rawDict['price'],'execution timesestamp':rawDict['timestamp'],'money in/out':tradeClassDict['cash_delta']}
        return(formattedDict)
        
    def logTrade(self,tradeObject):
        #store all the records onto a large dictionary that needs to persist throughout the trading day... we need to store timestamp, money in/out (available via the "specificTrade" reference variable in "makeTrade"), qty, ticker and direction (buy/sell)
        #normalize the tradeObject and fit into a list of dictionaries
        self.tradeLogTup=self.tradeLogTup+(tradeObject,)
        #create another function to format the trade list, unless this method is light
        return
    def profitCalc(self):
        #handle the p+l... will need to decide either LIFO, FIFO or average trade cost... may require pandas or numpy... and even its own class
        return
    
    def prettyPrintTradeLog(self):
        return print(self.tradeLogTup)

