# -*- coding: utf-8 -*-
import torch, pandas as pd, numpy as np
from typing import Tuple
from sklearn.preprocessing import MinMaxScaler


class _CustomModel(torch.nn.Module):
    def __init__(self, n_input:int, n_output:int, n_layer:int, n_hidden_layer:int, nonlinearity:str):
        super().__init__()

        self.__n_input, self.__n_output = n_input, n_output
        self.rnn = torch.nn.RNN(n_input, n_hidden_layer, n_layer, nonlinearity)
        self.linear = torch.nn.Linear(n_hidden_layer, n_output)

    def forward(self, x:np.ndarray):
        xt = torch.Tensor(x)
        out, _ = self.rnn(xt.view(len(xt), self.__n_output, self.__n_input))
        return self.linear(out.view(len(xt), -1))[-1]

def create_scaler(source_data:pd.DataFrame, x_cols:list[str], y_cols:list[str]) -> Tuple[MinMaxScaler, list, list]:
    scaler = MinMaxScaler(feature_range = (0, 1))
    data_train = scaler.fit_transform(source_data[x_cols + y_cols].values)
    train_x, train_y =\
        [ row[:len(x_cols)] for row in data_train ], [ row[len(x_cols):] for row in data_train ]
    print("scale train datas")

    return scaler, train_x, train_y

def create_model(source_data:pd.DataFrame, x_cols:list[str], y_cols:list[str], train_window:int = 100, n_layer:int = 1, n_hidden_layer:int = 100, nonlinearity:str = "tanh", lr:float = 0.001, epochs:int = 150) -> Tuple[torch.nn.Module, MinMaxScaler]:
    # scaler
    scaler, train_x, train_y = create_scaler(source_data, x_cols, y_cols)

    # create input
    train_input = []
    for idx in range(len(train_x) - train_window - 1):
        xi = torch.Tensor(np.array(train_x[idx:idx + train_window]))
        yi = torch.Tensor(np.array(train_y[idx + train_window + 1]))

        train_input.append(( xi, yi ))
    print("create train datas")

    # define model
    model = _CustomModel(len(x_cols), len(y_cols), n_layer, n_hidden_layer, nonlinearity)
    fn_loss = torch.nn.MSELoss()
    opt = torch.optim.Adam(model.parameters(), lr = lr)
    print("define model, loss function, opt")

    # train
    print("start training")
    for step in range(epochs):
        for xi, yi in train_input:
            opt.zero_grad()

            pred = model(xi)
            loss = fn_loss(pred, yi)

            opt.zero_grad()
            loss.backward()
            opt.step()

        model.eval()
        print(f"step {step + 1}: {loss}")

    # return model
    return model, scaler

def load_model(model_file:str, n_input:int, n_output:int, n_layer:int = 1, n_hidden_layer:int = 100, nonlinearity:str = "tanh") -> torch.nn.Module:
    model = _CustomModel(n_input, n_output, n_layer, n_hidden_layer, nonlinearity)
    model.load_state_dict(torch.load(model_file))
    model.eval()

    return model
