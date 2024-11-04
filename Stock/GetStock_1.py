"""
Web:
    https://medium.com/renee0918/python-%E7%88%AC%E5%8F%96%E5%80%8B%E8%82%A1%E6%AD%B7%E5%B9%B4%E8%82%A1%E5%83%B9%E8%B3%87%E8%A8%8A-b6bc594c8a95
Code:
    https://gist.github.com/circle81918/a58bbb0db93acde63701119325e2c1c1#file-stock4-ipynb

"""

# import package
from dateutil import rrule
import urllib.request
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np
import json
import time
import ssl

stock = "0050"
begin_date = "2010-01-01"
stock = "2330"
begin_date = "1994-09-05"

#matplotlib inline
end_date = datetime.datetime.now().strftime("%Y-%m-%d")
end_date = "1994-12-01"


# 爬取每月股價的目標網站並包裝成函式
def craw_one_month(stock_number,date):
    print(f"... craw_one_month: {stock} {date}")
    url = (
        "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date="+
        date.strftime('%Y%m%d')+
        "&stockNo="+
        stock_number
    )
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    ssl._create_default_https_context = ssl._create_unverified_context
    req = urllib.request.Request(url, headers=headers)
    data = json.loads(urllib.request.urlopen(req).read())
    print(f"... ... got!")
    if 'data' in data:
        return pd.DataFrame(data['data'],columns=data['fields'])
    else:
        return None
    
    
    
    
# 根據使用者輸入的日期，以月為單位，重複呼叫爬取月股價的函式
def craw_stock(stock_number, start_month, end_date):
    b_month = datetime.date(*[int(x) for x in start_month.split('-')])
    # now = datetime.datetime.now().strftime("%Y-%m-%d")         # 取得現在時間
    e_month = datetime.date(*[int(x) for x in end_date.split('-')])
    
    result = pd.DataFrame()
    for dt in rrule.rrule(rrule.MONTHLY, dtstart=b_month, until=e_month):
        query = craw_one_month(stock_number,dt)
        result = pd.concat([result,query],ignore_index=True)
        # result = pd.concat([result,craw_one_month(stock_number,dt)],ignore_index=True)
        time.sleep(5/3+0.2)
    
    return result

df = craw_stock(stock, begin_date, end_date)
df.set_index("日期", inplace=True)
df.to_csv(f"Stock_{stock}__Begin_{begin_date}__End_{end_date}.csv", encoding='utf_8_sig')





# 將爬取到的歷年股價資訊繪成圖表
# df['收盤價']=df['收盤價'].astype(float)
# df.loc[:]['收盤價'].plot(figsize=(18, 8))
# plt.xlabel('month')
# plt.ylabel('stock')
# plt.savefig("test.png")