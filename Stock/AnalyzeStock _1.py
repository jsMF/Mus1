"""


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



# Read File
df = pd.DataFrame()
df = pd.read_csv(file_name)
# print(f"{df.loc[1][:]}")
# print("\n")
# print("%s" % (df.loc[1]["日期"]))
# print("\n")
# df.to_csv(f"Stock_{stock}__Begin_{begin_date}__End_{now}__test.csv", encoding='utf_8_sig')


