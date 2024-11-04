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
begin_date = "2023-11-01"
now = datetime.datetime.now().strftime("%Y-%m-%d")

file_name = f"Stock_{stock}__Begin_{begin_date}__End_{now}.csv"


file_name = "Stock_2330.csv"


#matplotlib inline




df = pd.DataFrame()
df = pd.read_csv(file_name)
print(f"{df.loc[1][:]}")
print("\n")
print("%s" % (df.loc[1]["日期"]))
print("\n")
df.to_csv(f"Stock_{stock}__Begin_{begin_date}__End_{now}__test.csv", encoding='utf_8_sig')




# 將爬取到的歷年股價資訊繪成圖表
# df['收盤價']=df['收盤價'].astype(float)
# df.loc[:]['收盤價'].plot(figsize=(18, 8))
# plt.xlabel('month')
# plt.ylabel('stock')
# plt.savefig("test.png")