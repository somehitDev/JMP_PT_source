# -*- coding: utf-8 -*-
import os, sys, jmp

sys.path.append(os.path.join(jmp.SAMPLE_SCRIPTS, "Python"))
from dt2pandas import to_pandas

df_compare = to_pandas(dtOptFormula)
df_opt_sklearn = to_pandas(dtOptSklearn)

df_compare.columns = [ "ChannelID", "StreamTimeFormula", "CategoryCodeFormula", "ViewersFormula" ]

stream_time, category_code, viewers = [], [], []
for channel_id in df_compare["ChannelID"].unique():
    df_opt_sklearn_channel = df_opt_sklearn.query(f"`ChannelID` == '{channel_id}'")

    stream_time.append(df_opt_sklearn_channel["StreamTime"].unique()[0])
    category_code.append(df_opt_sklearn_channel["CategoryCode"].unique()[0])
    viewers.append(df_opt_sklearn_channel["Viewers"].unique()[0])

df_compare["StreamTimeSklearn"] = stream_time
df_compare["CategoryCodeSklearn"] = category_code
df_compare["ViewersSklearn"] = viewers
