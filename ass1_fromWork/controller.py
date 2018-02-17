#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Controller class for the trading application
"""

import sys
sys.path.append('/home/tio/Documents/CUNY/advancedProgramming/ass1_fromWork')
import tradeClass as trade
import ass1_acountsClass as accts
import datetime as datetime
import tradeManager as tm
import engageUser as eu
import yahoo_scraper_cleaner as scraper
from imp import reload

reload(trade)
reload(accts)
reload(eu)

act=accts.Account()

#4 pieces of information needed: ticker, timestamp, price, trade type and original trade type
buy_trade={'ticker':'CPT','price':98.108,'shares':1000,'timestamp':datetime.datetime.today(),'tradetype':'buy','original_tradetype':'long'}

buy_trade_2={'ticker':'HD','price':78.108,'shares':1000000,'timestamp':datetime.datetime.today(),'tradetype':'buy','original_tradetype':'long'}
sell_trade_dic={'ticker':'HD','price':102.108,'shares':1000,'timestamp':datetime.datetime.today(),'tradetype':'sell to close','original_tradetype':'long'}

short_trade_dic={'ticker':'RLS','price':67.108,'shares':1000,'timestamp':datetime.datetime.today(),'tradetype':'short','original_tradetype':'short'}
btc_trade_dic={'ticker':'RLS','price':69.108,'shares':1000,'timestamp':datetime.datetime.today(),'tradetype':'buy to close','original_tradetype':'short'}

#initiate trading day object and pass all trades through the object in order to log it
todayTrading=tm.TradingDay()

#using the new tradeManager framework
buy_test_today=todayTrading.makeTrade(buy_trade,act)

#following along the tradeClass object... instantiation does not affect the portfolio
buy_test=trade.EquityTrade(buy_trade,act)
buy_test_2=trade.EquityTrade(buy_trade_2,act)
sell_test=trade.EquityTrade(sell_trade_dic,act)
short_test=trade.EquityTrade(short_trade_dic,act)
short_test.tradetype

#testing only the tradeClass class and circumventing tradeManager class
buy_test_dict=buy_test.tradeType()
buy_test_dict2=buy_test_2.tradeType()
sell_test_dict=sell_test.tradeType()
#nothing is being returned here
short_test_dict=short_test.tradeType()

#update the portfolio
act.postEquityTrade(buy_test_dict)
act.postEquityTrade(short_test_dict)
act.getPortfolio()
act.cash_bal

buy_dict=buy_test_today.tradeType()
buy_dict2=buy_test_2.tradeType()
sell_dict=sell_test.tradeType()
short_dict=short_test.tradeType()

act.postEquityTrade(buy_dict)
act.postEquityTrade(buy_dict2)
act.postEquityTrade(short_dict)

act.getPortfolio()
act.cash_bal
cashAfterPurchase=act.getCash()

''' building console interaction '''
engage=eu.Dialogue()
engage.engageUser()

''' test the scraper function '''
s=scraper.scrapy()
