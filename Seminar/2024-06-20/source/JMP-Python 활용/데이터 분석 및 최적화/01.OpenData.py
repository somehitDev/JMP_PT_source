# -*- coding: utf-8 -*-
import os, sqlite3, pandas as pd

conn = sqlite3.connect(os.path.join(gdd, "chzzk_gather", "streams.db"))

# get source range
df_streams = pd.read_sql("select * from `streams` where `LiveCategory` is not null;", conn)

# string to datetime
df_streams["SearchTime"] = pd.to_datetime(df_streams["SearchTime"], format = "%Y-%m-%dT%H:%M:%SZ")

# sort by datetime
df_streams = df_streams.sort_values(by = [ "SearchTime" ])

# add category code
cat_type = pd.CategoricalDtype(df_streams["LiveCategory"].unique(), ordered = True)
df_streams["CategoryCode"] = df_streams["LiveCategory"].astype(cat_type).cat.codes

# split code match dataframe from origin
df_category_match = df_streams[[ "LiveCategory", "CategoryCode" ]].drop_duplicates()

conn.close()
