"""
Ticker Data Collector (TDCollector)

TEST API KEY: 093W2TCOPVD33Z99



"""

import requests
import urllib
import shutil



class TDCollector:
    API_KEY = "093W2TCOPVD33Z99"    #NOTE: Input your own Alpha Vantage key here.
    time_series = "TIME_SERIES_INTRADAY_EXTENDED"
    symbol = "IBM"
    interval = "15min"
    slice = "year1month1"
    apikey = "demo"
    url = f"https://www.alphavantage.co/query?function={time_series}&symbol={symbol}&interval={interval}&slice={slice}&apikey=f{API_KEY}"

    def get_data(self):


        #check to see if a directory for the ticker already already exists

        #check to see if the data for this timeframe exists

        #write the data to the appropriately named file
        

        response = urllib.request.urlopen(self.url)
        file = "Revel-Fin-Lib/Data/test.csv"

        try:
            with open(file, 'w') as out_file:
                shutil.copyfileobj(response,out_file)
        except Exception as e:
            print(e)




TDCollector().get_data()