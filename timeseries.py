#-------------------------------------------------------------------------------
#@file: timeseries.py
#@author: Prashan Pudasaini
#@Date: 01/12/19 11:46:00
#@Desc: Python wrapper for Alpha Vantage API to collect financial data
#-------------------------------------------------------------------------------

import numpy
import pandas as pd
import json
import urllib.request
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries

#--------------------------------Class StockTimeSeries--------------------------
#Supports US and most International Markets
#var QUERY_URL: the url to query for data
#var API_KEY: unique API KEY provided by Alpha Vantage
#var outputsize = full: get all rows | outputsize=compact: get first 100 rows
#var output_format: get data as python pandas | accepted format:pandas csv, json
#var interval: time interval for intraday data | accepted intervals: 1min, 5min, 15min, 30min, 60min
#-------------------------------------------------------------------------------
class StockTimeSeries:
    QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}&outputsize={OUTPUTSIZE}&interval={INTERVAL}"
    API_KEY = 'Your API KEY'
    outputsize = 'full'
    output_format = 'pandas'
    interval = '1min'

#------------------------------------MEMBER FUNCTION----------------------------
#@param req_type: API request type
#@param symbol: ticker
#pre: valid ticker and req type
#post: initialized
#-------------------------------------------------------------------------------
    def __init__(self, req_type, symbol):
        self.req_type = req_type
        self.symbol = symbol

#------------------------------------MEMBER FUNCTION----------------------------
#pre: none
#post: returned query url
#-------------------------------------------------------------------------------
    def _request(self):
        with urllib.request.urlopen(StockTimeSeries.QUERY_URL.format(KEY=StockTimeSeries.API_KEY, OUTPUTSIZE=StockTimeSeries.outputsize, INTERVAL=StockTimeSeries.interval, REQUEST_TYPE=self.req_type, SYMBOL=self.symbol)) as req:
            data = req.read().decode("UTF-8")
            return data

#------------------------------------MEMBER FUNCTION----------------------------
#get intraday timeseries data from the API (1 min interval)
#accepted intervals: 1min, 5min, 15min, 30min, 60min
#pre: valid key in json dict
#post: return intraday timeseries data
#-------------------------------------------------------------------------------
    def get_time_series_intraday(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_intraday_data = pd.DataFrame.from_dict(jsondata['Time Series (1min)'], orient="index")
        return df_intraday_data

#------------------------------------MEMBER FUNCTION----------------------------
#get daily timeseries data from the API
#pre: valid key in json dict
#post: return daily timeseries data
#-------------------------------------------------------------------------------
    def get_time_series_daily(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_daily_data = pd.DataFrame.from_dict(jsondata['Time Series (Daily)'], orient="index")
        return df_daily_data

#------------------------------------MEMBER FUNCTION----------------------------
#get daily_adjusted timeseries data from the API
#pre: valid key in json dict
#post: return daily_adjusted timeseries data
#-------------------------------------------------------------------------------
    def get_time_series_daily_adjusted(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_daily_adjusted_data = pd.DataFrame.from_dict(jsondata['Time Series (Daily)'], orient="index")
        return df_daily_adjusted_data

#------------------------------------MEMBER FUNCTION----------------------------
#get weekly timeseries data from the API
#pre: valid key in json dict
#post: return weekly timeseries data
#-------------------------------------------------------------------------------
    def get_time_series_weekly(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_weekly_data = pd.DataFrame.from_dict(jsondata['Weekly Time Series'], orient="index")
        return df_weekly_data

#------------------------------------MEMBER FUNCTION----------------------------
#get weekly_adjusted timeseries data from the API
#pre: valid key in json dict
#post: return weekly_adjusted timeseries data
#-------------------------------------------------------------------------------
    def get_time_series_weekly_adjusted(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_weekly_adjusted_data = pd.DataFrame.from_dict(jsondata['Weekly Adjusted Time Series'], orient="index")
        return df_weekly_adjusted_data

#------------------------------------MEMBER FUNCTION----------------------------
#get monthly timeseries data from the API
#pre: valid key in json dict
#post: return monthly timeseries data
#-------------------------------------------------------------------------------
    def get_time_series_monthly(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_monthly_data = pd.DataFrame.from_dict(jsondata['Monthly Time Series'], orient="index")
        return df_monthly_data

#------------------------------------MEMBER FUNCTION----------------------------
#get monthly_adjusted timeseries data from the API
#pre: valid key in json dict
#post: return monthly_adjusted timeseries data
#-------------------------------------------------------------------------------
    def get_time_series_monthly_adjusted(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_monthly_adjusted_data = pd.DataFrame.from_dict(jsondata['Monthly Adjusted Time Series'], orient="index")
        return df_monthly_adjusted_data

#-----------------------------------MEMBER FUNCTION-----------------------------
#get global quote data from the API
#pre: valid key in json dict
#post: return global quote data
#-------------------------------------------------------------------------------
    def get_quote_endpoint(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_quote_endpoint = pd.DataFrame.from_dict(jsondata['Global Quote'], orient='index')
        return df_quote_endpoint

#--------------------------------------CALLS------------------------------------
# US and some International Stock markets
#-------------------------------------------------------------------------------
ins_intraday=StockTimeSeries('TIME_SERIES_INTRADAY', 'IBM')
ins_intraday.get_time_series_intraday()
print(ins_intraday)

ins_daily=StockTimeSeries('TIME_SERIES_DAILY', 'LMT')
ins_daily.get_time_series_daily()
print(ins_daily)

ins_daily_adjusted=StockTimeSeries('TIME_SERIES_DAILY_ADJUSTED', 'GLNCY')   #swiss
ins_daily_adjusted.get_time_series_daily_adjusted()
print(ins_daily_adjusted)

ins_weekly=StockTimeSeries('TIME_SERIES_WEEKLY', 'BA')
ins_weekly.get_time_series_weekly()
print(ins_weekly)

ins_weekly_adjusted=StockTimeSeries('TIME_SERIES_WEEKLY_ADJUSTED', 'AAPL')
ins_weekly_adjusted.get_time_series_weekly_adjusted()
print(ins_weekly_adjusted)

ins_monthly=StockTimeSeries("TIME_SERIES_MONTHLY", 'GOOG')
ins_monthly.get_time_series_monthly()
print(ins_monthly)

ins_monthly_adjusted=StockTimeSeries('TIME_SERIES_MONTHLY_ADJUSTED', 'AMZN')
ins_monthly_adjusted.get_time_series_monthly_adjusted()
print(ins_monthly_adjusted)
#-------------------------------END CALLS---------------------------------------

#-------------------------------Class SearchTimeSeries--------------------------
#Supports US and most International Markets
#var QUERY_URL: the url to query for data
#var API_KEY: unique API KEY provided by Alpha Vantage
#var output_format: get data as python pandas | accepted format:pandas csv, json
#-------------------------------------------------------------------------------
class SearchTimeSeries:
    QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&keywords={KEYWORDS}"
    API_KEY = "WCQZIHBU4CDFXNI0"
    output_format = 'pandas'

#------------------------------------MEMBER FUNCTION----------------------------
#@param req_type: API request type
#@param keywords: ticker
#pre: valid ticker and req type
#post: initialized
#-------------------------------------------------------------------------------
    def __init__(self, req_type, keywords):
        self.req_type = req_type
        self.keywords = keywords

#------------------------------------MEMBER FUNCTION----------------------------
#pre: none
#post: returned query url
#-------------------------------------------------------------------------------
    def _request(self):
        with urllib.request.urlopen(SearchTimeSeries.QUERY_URL.format(REQUEST_TYPE=self.req_type, KEY=StockTimeSeries.API_KEY, KEYWORDS=self.keywords)) as req:
            data = req.read().decode("UTF-8")
            return data

#------------------------------------MEMBER FUNCTION----------------------------
#get search endpoint data from the API
#pre: valid key in json dict
#post: Return best match "symbol" and "name" only. Can ignore "type", "region", etc...
#accepted keys: '1. symbol', '2. name', '3. type', '4. region', '5. marketOpen', '6. marketClose', '7. timezone', '8. currency', '9. matchScore'
#-------------------------------------------------------------------------------
    def get_search_endpoint(self):
        TimeSeries(key=SearchTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_search_endpoint = pd.DataFrame.from_dict(jsondata['bestMatches'])
        return df_search_endpoint[['1. symbol', '2. name']]

#--------------------------------------CALLS------------------------------------
#Prints stocks starting with A
#-------------------------------------------------------------------------------
ins_search_endpoint=SearchTimeSeries('SYMBOL_SEARCH', 'A')
ins_search_endpoint.get_search_endpoint()
print(ins_search_endpoint)
#--------------------------------------END CALLS--------------------------------
