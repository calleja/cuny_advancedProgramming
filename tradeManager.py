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
        self.tradeLogDict={}
        
    def makeTrade(self,specificTradeDict,act):
        #log the trade and make the trade object available for passing to the account object... Call the yahoo finance scraper. trade.EquityTrade requires fewer attributes than what is to be retrieved from the scraper and what we need to record here on the log.
        specificTrade=trade.EquityTrade(specificTradeDict,act)
        self.logTrade(specificTrade)
        return specificTrade
        
    def logTrade(self,tradeObject):
        #store all the records onto a large dictionary... we need to store timestamp, money in/out (available via the "specificTrade" reference variable in "makeTrade"), qty, ticker and direction (buy/sell)
        #normalize the tradeObject and fit into a list of dictionaries
        #create another function to format the trade list, unless this method is light
        return
    def profitCalc(self):
        #handle the p+l... will need to decide either LIFO, FIFO or average trade cost... may require pandas or numpy... and even its own class

