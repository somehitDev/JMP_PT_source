# -*- coding: utf-8 -*-
import os, pandas as pd, torch, numpy as np
from sklearn.preprocessing import MinMaxScaler

train_window = 100
epochs = 150
scaler = MinMaxScaler(feature_range = (0, 1))
model_file = os.path.join(gdd, "model", "custom.pth")

if not os.path.exists(model_file):
    # open data
    df_train = pd.read_csv(os.path.join(gdd, "train.csv"), engine = "python", encoding = "utf-8")

    # scale data
    data_train = scaler.fit_transform(df_train.values)
    x_train, y_train =\
        [ row[:2] for row in data_train ], [ row[2:] for row in data_train ]

    # create input
    train_input = []
    for idx in range(len(x_train) - train_window - 1):
        xi = torch.Tensor(np.array(x_train[idx:idx + train_window]))
        yi = torch.Tensor(np.array(y_train[idx + train_window + 1]))

        train_input.append(( xi, yi ))

    # define model class
    class CustomModel(torch.nn.Module):
        def __init__(self, n_input = 1, n_output = 1, n_layer = 1, n_hidden_layer = 100, nonlinearity = "tanh"):
            super().__init__()

            self.rnn = torch.nn.RNN(n_input, n_hidden_layer, num_layers = n_layer, nonlinearity = nonlinearity)
            self.linear = torch.nn.Linear(n_hidden_layer, n_output)

        def forward(self, x:np.ndarray):
            xt = torch.Tensor(x)
            out, _ = self.rnn(xt.view(len(xt), 1, 2))
            return self.linear(out.view(len(xt), -1))[-1]

    # define model
    model = CustomModel(n_input = 2, n_layer = 2, n_hidden_layer = 150)
    loss_func = torch.nn.MSELoss()
    opt = torch.optim.Adam(model.parameters(), lr = 0.001)

    # train
    for step in range(epochs):
        for xi, yi in train_input:
            opt.zero_grad()

            pred = model(xi)

            loss = loss_func(pred, yi)

            opt.zero_grad()
            loss.backward()
            opt.step()

        model.eval()
        torch.save(model, model_file)
    else:
        model = torch.load(model_file)
        model.eval()


## predict
# open data
df_predict = pd.read_csv(os.path.join(gdd, "predict.csv"), engine = "python", encoding = "utf-8")

# scale data
data_predict = scaler.fit_transform(df_train.values)
x_predict = [ row[:2] for row in data_predict ]

# predict
y_predict = []
for xi in x_predict:
    with torch.no_grad():
        y_predict.append(model(np.array([ xi ])).item())

# denormalize result
pred_result = scaler.inverse_transform(np.array([
    xi.tolist() + [ yi ]
    for xi, yi in zip(x_predict, y_predict)
]))

# append result to dataframe
df_predict["YPredict"] = [
    item[2]
    for item in pred_result
]
