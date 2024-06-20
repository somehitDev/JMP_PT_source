# -*- coding: utf-8 -*-
import sys, pathlib, torch, numpy as np

# gdd = pathlib.Path(gdd).resolve()
# if not gdd in sys.path:
#     sys.path.append(str(gdd))

# import jmp
# sys.path.append(os.path.join(jmp.SAMPLE_SCRIPTS, "Python"))
# from dt2pandas import to_pandas
from torch_model import create_model, create_scaler, load_model

# df_streams = to_pandas(dtStreams)
# df_streams_predict = to_pandas(dtStreamsPredict)
# df_extracts = to_pandas(dtExtracts)

gdd = pathlib.Path(__file__).resolve().parent
import pandas as pd
df_streams = pd.read_excel(str(gdd.joinpath("datas", "Streams.xlsx")), engine = "openpyxl")
df_streams_predict = pd.read_excel(str(gdd.joinpath("datas", "StreamsPredict.xlsx")), engine = "openpyxl")
df_extracts = pd.read_excel(str(gdd.joinpath("datas", "Extracts.xlsx")), engine = "openpyxl")

if df_extracts.shape[1] > 10:
    channel_ids = df_extracts.query(f"`CategoryLength` > {df_extracts['CategoryLength'].mean()}")["ChannelID"].unique()
else:
    channel_ids = df_extracts["ChannelID"].unique()

# # do predict per channel
# for channel_id in channel_ids:
#     df_stream_channel = df_streams.query(f"`ChannelID`=='{channel_id}'")
#     df_predict_channel = df_streams_predict.query(f"`ChannelID`=='{channel_id}'")

#     # check model file exists
#     model_file = gdd.joinpath("models", f"{channel_id}.pth")
#     if model_file.exists():
#         # load model
#         model = load_model(str(model_file), 2, 1)

#         # create scaler
#         scaler = create_scaler(df_stream_channel, [ "StreamTime", "CategoryCode" ], [ "Viewers" ])[0]
#     else:
#         # create model
#         model, scaler = create_model(df_stream_channel, [ "StreamTime", "CategoryCode" ], [ "Viewers" ], epochs = 200)
#         torch.save(model.state_dict(), str(model_file))

#     # scale predict datas
#     data_predict = scaler.fit_transform(df_predict_channel[["StreamTime", "CategoryCode", "Viewers"]])
#     x_predict = [ row[:2] for row in data_predict ]

#     # predict
#     y_predict_raw = []
#     for xi in x_predict:
#         with torch.no_grad():
#             y_predict_raw.append(model(np.array([ xi ])).item())

#     # denormalize result
#     pred_result = scaler.inverse_transform(np.array([
#         xi.tolist() + [ yi ]
#         for xi, yi in zip(x_predict, y_predict_raw)
#     ]))

#     # append result to data
#     df_predict_channel["ViewersPredictTorch"] = [
#         row[2]
#         for row in pred_result
#     ]
#     # append diff
#     df_predict_channel["PredictErrorTorch"] = df_predict_channel.eval("Viewers - ViewersPredictTorch")
#     df_predict_channel["PredictErrorTorch"] = df_predict_channel["PredictErrorTorch"].apply(abs)
#     # append rate
#     df_predict_channel["PredictErrorRateTorch"] = [
#         round(predict_error / viewer * 100) if viewer > viewer_predict else round(predict_error / viewer_predict * 100)
#         for viewer, viewer_predict, predict_error in df_predict_channel[[ "Viewers", "ViewersPredictTorch", "PredictErrorTorch" ]].values
#     ]

#     # send dataframe to jmp
#     jmp.run_jsl(f"""
# dt = PythonGet("df_predict_channel") << NewDataView; Wait(0);
# dt << SetWindowTitle("Predict of {channel_id} by Torch");
# dt << Hide Columns(1, """ + "{ :SearchTime, :StreamTime, :LiveID, :LiveTitle, :LiveCategory, :ChannelID, :CategoryCode" + """ });
# """)

# do predict all
df_predict_all = df_streams_predict.copy()
model_file = gdd.joinpath("models", "All.pth")
if model_file.exists():
    # load model
    model = load_model(str(model_file), 2, 1)

    # create scaler
    scaler = create_scaler(df_streams, [ "StreamTime", "CategoryCode" ], [ "Viewers" ])[0]
else:
    from datetime import datetime
    start_time = datetime.now()

    # create model
    model, scaler = create_model(df_streams, [ "StreamTime", "CategoryCode" ], [ "Viewers" ], epochs = 200)
    torch.save(model.state_dict(), str(model_file))

    print(f"elapsed: {datetime.now() - start_time}")

# # scale predict datas
# data_predict = scaler.fit_transform(df_predict_all[["StreamTime", "CategoryCode", "Viewers"]])
# x_predict = [ row[:2] for row in data_predict ]

# # predict
# y_predict_raw = []
# for xi in x_predict:
#     with torch.no_grad():
#         y_predict_raw.append(model(np.array([ xi ])).item())

# # denormalize result
# pred_result = scaler.inverse_transform(np.array([
#     xi.tolist() + [ yi ]
#     for xi, yi in zip(x_predict, y_predict_raw)
# ]))

# # append result to data
# df_predict_all["ViewersPredictTorch"] = [
#     row[2]
#     for row in pred_result
# ]
# # append diff
# df_predict_all["PredictErrorTorch"] = df_predict_all.eval("Viewers - ViewersPredictTorch")
# df_predict_all["PredictErrorTorch"] = df_predict_all["PredictErrorTorch"].apply(abs)
# # append rate
# df_predict_all["PredictErrorRateTorch"] = [
#     round(predict_error / viewer * 100) if viewer > viewer_predict else round(predict_error / viewer_predict * 100)
#     for viewer, viewer_predict, predict_error in df_predict_all[[ "Viewers", "ViewersPredictTorch", "PredictErrorTorch" ]].values
# ]

# # send dataframe to jmp
# jmp.run_jsl("""
# dt = PythonGet("df_predict_all") << NewDataView; Wait(0);
# dt << SetWindowTitle("Predict of All");
# dt << Hide Columns(1, { :SearchTime, :StreamTime, :LiveID, :LiveTitle, :LiveCategory, :ChannelID, :CategoryCode });
# """)
