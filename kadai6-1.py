#e-statから景気指数の値を取得し表示する
#エンドポイント:https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
#"statsDataId":"0003446461"とすることで景気指数のデータを指定している
import requests
import pandas as pd

APP_ID = "a85bf133eea52a338ba4db8cd68b025546cf999b"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "cdTab":"100",
    "cdCat01":"110",
    "statsDataId":"0003446461",##景気指数のデータ
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}

response = requests.get(API_URL, params=params)

data = response.json()

values = data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']
df = pd.DataFrame(values)

##不要な項目を削除
df = df.drop(["@tab","@cat01","@unit"],axis=1)

##列名を書き換え

df = df.rename(columns={"@time":"年月","$":"景気指標"})
##年月を日時形式に
for index, row in df.iterrows():
    row["年月"] = row["年月"][0:4]+"/"+row["年月"][6:8]
    
##省略しないで表示するように
pd.set_option('display.max_rows', None)
print(df)
