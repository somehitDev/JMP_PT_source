# -*- coding: utf-8 -*-
import os, sys, jmp, pandas as pd

sys.path.append(os.path.join(jmp.SAMPLE_SCRIPTS, "Python"))
from dt2pandas import to_pandas

df_streams = to_pandas(dtStreams)

# get factors
factors = []
for channel_id in df_streams["ChannelID"].unique():
    df_stream_split = df_streams.query(f"`ChannelID`=='{channel_id}'")

    factors.append({
        "ChannelID": channel_id,
        "StreamLength": df_stream_split["SearchTime"].unique().shape[0],
        "CategoryLength": df_stream_split["LiveCategory"].unique().shape[0],
        "MinViewers": int(df_stream_split["Viewers"].min()),
        "MaxViewers": int(df_stream_split["Viewers"].max()),
        "MeanViewers": int(df_stream_split["Viewers"].mean())
    })

df_weights = pd.DataFrame.from_dict(factors)\
    .query("(`CategoryLength`>1) and (`MeanViewers`>=10) and (`MinViewers`>0)")\
    [[ "ChannelID", "StreamLength", "CategoryLength", "MeanViewers" ]]

# calculate weights
weights = []
describes = {
    column: df_weights[column].describe()
    for column in ( "StreamLength", "CategoryLength", "MeanViewers" )
}

for channel_id, stream_length, category_length, mean_viewers in df_weights[[ "ChannelID", "StreamLength", "CategoryLength", "MeanViewers" ]].values:
    channel_weight = 0

    # stream length
    if stream_length >= describes["StreamLength"]["max"]:
        channel_weight += 4
    elif stream_length >= describes["StreamLength"]["mean"]:
        channel_weight += 3
    elif stream_length > describes["StreamLength"]["min"]:
        channel_weight += 2
    elif stream_length == describes["StreamLength"]["min"]:
        channel_weight += 1

    # category length
    if category_length >= describes["CategoryLength"]["max"]:
        channel_weight += 4
    elif category_length >= describes["CategoryLength"]["mean"]:
        channel_weight += 2
    elif category_length > describes["CategoryLength"]["min"]:
        channel_weight += 0
    elif category_length == describes["CategoryLength"]["min"]:
        channel_weight += -1

    # mean viewers
    if mean_viewers >= describes["MeanViewers"]["max"]:
        channel_weight += 4
    elif mean_viewers >= describes["MeanViewers"]["mean"]:
        channel_weight += 2
    elif mean_viewers > describes["MeanViewers"]["min"]:
        channel_weight += -1
    elif mean_viewers == describes["MeanViewers"]["min"]:
        channel_weight += -2

    if describes["MeanViewers"]["max"] - describes["MeanViewers"]["min"] >= 30:
        channel_weight += 4

    weights.append(channel_weight)

df_weights["Weights"] = weights
df_weights = df_weights.query("`Weights`>0")\
    .sort_values(by = [ "Weights", "StreamLength", "CategoryLength", "MeanViewers" ], ascending = False)\
    [[ "ChannelID", "Weights" ]]
