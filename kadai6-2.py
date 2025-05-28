#alphavantageからIBMの日別の開始価格、最高値、最安値、終値、取引数を取得し、表示する。
#エンドポイント:https://www.alphavantage.co/query
#paramsのsymbolを変更することで世界中の各社の株価、為替データの取得が可能
#一定回数実行するとapi制限がかかる

import requests
import pandas as pd

APP_ID = "5487O9EK7H412D6N"
API_URL  = "https://www.alphavantage.co/query"

params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "IBM",
        "apikey": APP_ID,
        "datatype": "json"
    }

response = requests.get(API_URL, params=params)

data = response.json()
data = data['Time Series (Daily)']

df = pd.DataFrame()
for i in data:
    df = df._append(pd.Series([data[i]["1. open"],data[i]["2. high"],data[i]["3. low"],data[i]["4. close"],data[i]['5. volume']],name=i))

##省略しないで表示するように
pd.set_option('display.max_rows', None)
print(df)
