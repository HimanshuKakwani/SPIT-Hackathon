import string
import time
import datetime
import pandas as pd

ticker = '^NSEI'
period1 = int(time.mktime(datetime.datetime(2016, 1, 28, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 1, 28, 23, 59).timetuple()))
interval = '1d' 

ticker = str(input())
period1 = int(time.mktime(datetime.datetime(2016, 1, 28, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022, 1, 28, 23, 59).timetuple()))
interval = '1d'

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)
print(df)
# df.to_csv()
# df.to_excel()