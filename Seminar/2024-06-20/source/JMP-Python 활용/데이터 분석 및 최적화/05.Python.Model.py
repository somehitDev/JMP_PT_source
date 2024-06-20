# -*- coding: utf-8 -*-
import os, sys, jmp, joblib
from sklearn.ensemble import GradientBoostingRegressor

sys.path.append(os.path.join(jmp.SAMPLE_SCRIPTS, "Python"))
from dt2pandas import to_pandas

df_stream_channel = to_pandas(dtStreamChannel)

model = GradientBoostingRegressor().fit(df_stream_channel[[ "StreamTime", "CategoryCode" ]].values, df_stream_channel[[ "Viewers" ]].values)
joblib.dump(model, os.path.join(gdd, "models", f"{channelId}.model"))
