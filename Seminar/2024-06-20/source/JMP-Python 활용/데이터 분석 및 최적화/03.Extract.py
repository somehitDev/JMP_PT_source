# -*- coding: utf-8 -*-
import os, sys, jmp, pandas as pd

sys.path.append(os.path.join(jmp.SAMPLE_SCRIPTS, "Python"))
from dt2pandas import to_pandas

df_streams = to_pandas(dtStreams)

extracts = []
for channel_id in channelIds:
    df_stream_channel = df_streams.query(f"`ChannelID`=='{channel_id}'").dropna(subset = [ "LiveCategory", "Viewers" ])
    df_stream_channel["CategoryLength"] = df_stream_channel["LiveCategory"].unique().shape[0]

    extracts.extend(
        df_stream_channel.query(f"`Viewers`=={df_stream_channel['Viewers'].max()}")\
            .drop_duplicates(subset = [ "ChannelID", "Viewers" ])\
            .sort_values(by = [ "Viewers" ], ascending = False)\
            [[ "ChannelID", "CategoryLength" ]].to_dict(orient = "records")
    )

# df_extracts = pd.DataFrame.from_dict(extracts).sort_values(by = [ "CategoryLength", "Viewers" ], ascending = False)
df_extracts = pd.DataFrame.from_dict(extracts).sort_values(by = [ "ChannelID", "CategoryLength" ], ascending = False)
