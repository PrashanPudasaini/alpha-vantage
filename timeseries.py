#-------------------------------------------------------------------------------
#@file: timeseries.py
#@Date: 01/12/19 11:46:00
#@Desc: Python wrapper for Alpha Vantage API to collect financial data
#-------------------------------------------------------------------------------

import numpy
import pandas as pd
import json
import urllib.request
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries

class StockTimeSeries:
    QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}&outputsize={OUTPUTSIZE}&interval={INTERVAL}"
    API_KEY = 'Your API KEY'
    outputsize = 'full'
    output_format = 'pandas'
    interval = '1min'
    def __init__(self, req_type, symbol):
        self.req_type = req_type
        self.symbol = symbol
        
    def _request(self):
        with urllib.request.urlopen(StockTimeSeries.QUERY_URL.format(KEY=StockTimeSeries.API_KEY, OUTPUTSIZE=StockTimeSeries.outputsize, INTERVAL=StockTimeSeries.interval, REQUEST_TYPE=self.req_type, SYMBOL=self.symbol)) as req:
            data = req.read().decode("UTF-8")
            return data

    def get_time_series_intraday(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_intraday_data = pd.DataFrame.from_dict(jsondata['Time Series (1min)'], orient="index")
        return df_intraday_data

    def get_time_series_daily(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_daily_data = pd.DataFrame.from_dict(jsondata['Time Series (Daily)'], orient="index")
        return df_daily_data

    def get_time_series_daily_adjusted(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_daily_adjusted_data = pd.DataFrame.from_dict(jsondata['Time Series (Daily)'], orient="index")
        return df_daily_adjusted_data

    def get_time_series_weekly(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_weekly_data = pd.DataFrame.from_dict(jsondata['Weekly Time Series'], orient="index")
        return df_weekly_data

    def get_time_series_weekly_adjusted(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_weekly_adjusted_data = pd.DataFrame.from_dict(jsondata['Weekly Adjusted Time Series'], orient="index")
        return df_weekly_adjusted_data

    def get_time_series_monthly(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_monthly_data = pd.DataFrame.from_dict(jsondata['Monthly Time Series'], orient="index")
        return df_monthly_data

    def get_time_series_monthly_adjusted(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_monthly_adjusted_data = pd.DataFrame.from_dict(jsondata['Monthly Adjusted Time Series'], orient="index")
        return df_monthly_adjusted_data

    def get_quote_endpoint(self):
        TimeSeries(key=StockTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_quote_endpoint = pd.DataFrame.from_dict(jsondata['Global Quote'], orient='index')
        return df_quote_endpoint

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

class SearchTimeSeries:
    QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&keywords={KEYWORDS}"
    API_KEY = "WCQZIHBU4CDFXNI0"
    output_format = 'pandas'

    def __init__(self, req_type, keywords):
        self.req_type = req_type
        self.keywords = keywords

    def _request(self):
        with urllib.request.urlopen(SearchTimeSeries.QUERY_URL.format(REQUEST_TYPE=self.req_type, KEY=StockTimeSeries.API_KEY, KEYWORDS=self.keywords)) as req:
            data = req.read().decode("UTF-8")
            return data

    def get_search_endpoint(self):
        TimeSeries(key=SearchTimeSeries.API_KEY, output_format=self.output_format)
        jsondata = json.loads(self._request())
        df_search_endpoint = pd.DataFrame.from_dict(jsondata['bestMatches'])
        return df_search_endpoint[['1. symbol', '2. name']]

ins_search_endpoint=SearchTimeSeries('SYMBOL_SEARCH', 'A')
ins_search_endpoint.get_search_endpoint()
print(ins_search_endpoint)
