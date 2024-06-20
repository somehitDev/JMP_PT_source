# -*- coding: utf-8 -*-
import os, sqlite3, pandas as pd

conn = sqlite3.connect(os.path.join(gdd, "chzzk_gather", "streams.db"))

# get all categories
df_category_match = pd.read_sql("select distinct `LiveCategory` from `streams`;", conn)
cat_type = pd.CategoricalDtype(df_category_match["LiveCategory"].unique(), ordered = True)
df_category_match["CategoryCode"] = df_category_match["LiveCategory"].astype(cat_type).cat.codes

# get source range
df_streams_source = pd.read_sql("select * from `streams` where `SearchTime` between '2024-05-18T00:00:00Z' and '2024-05-27T23:59:59Z' and `LiveCategory`!='' and `LiveCategory` is not null;", conn)
# get predict range
df_streams_predict = pd.read_sql("select * from `streams` where `SearchTime` between '2024-05-28T00:00:00Z' and '2024-06-01T00:00:00Z' and `LiveCategory`!='' and `LiveCategory` is not null;", conn)

# string to datetime
df_streams_source["SearchTime"] = pd.to_datetime(df_streams_source["SearchTime"], format = "%Y-%m-%dT%H:%M:%SZ")
df_streams_predict["SearchTime"] = pd.to_datetime(df_streams_predict["SearchTime"], format = "%Y-%m-%dT%H:%M:%SZ")

# fill category code from match info
source_code_list = []
for category in df_streams_source["LiveCategory"].values:
    source_code_list.append(df_category_match.query(f"`LiveCategory`=='{category}'")["CategoryCode"].unique()[0])

df_streams_source["CategoryCode"] = source_code_list

predict_code_list = []
for category in df_streams_predict["LiveCategory"].values:
    predict_code_list.append(df_category_match.query(f"`LiveCategory`=='{category}'")["CategoryCode"].unique()[0])

df_streams_predict["CategoryCode"] = predict_code_list

conn.close()
