#KERAS - WandB
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

df = pd.read_csv('baitap.csv')
x = df.drop('y',axis=1)
y = df.drop('x',axis=1)

import wandb
from wandb.integration.keras import WandbMetricsLogger

wandb.login()

# KERAS
import datetime
from tensorflow.keras.callbacks import TensorBoard
run = wandb.init(project='baitap',
                 config={
                     "learning_rate": 0.01,
                     "epochs": 1000,
                     "batch_size": 32
                 })

model = Sequential([Dense(units=1, input_shape=[1])])

curr = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')

log_dir = 'logs/fit/' + curr
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

model.compile(loss='mean_squared_error',optimizer = Adam(learning_rate=0.03))
model.fit(x,y,epochs =1000, verbose=0, callbacks=[WandbMetricsLogger(), tensorboard_callback])
y_pred = model.predict(x)

plt.scatter(x,y)
plt.plot(x, y_pred, color='red')
fig = plt.gcf()

run.log({"Biểu đồ": wandb.Image(fig)})
run.finish()

#PYTORCH

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.utils.tensorboard import SummaryWriter

run1 = wandb.init(project='torch',
                 config={
                     "learning_rate": 0.01,
                     "epochs": 1000,
                     "batch_size": 32
                 })

x_train = torch.tensor(x.to_numpy()).view(-1,1)
y_train = torch.tensor(y.to_numpy()).view(-1,1)

x_train = x_train.float()
y_train = y_train.float()

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


model = LinearRegressionModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.03)

wandb.watch(model, log_freq=100)
epochs = 1000
for epoch in range(epochs):
    model.train()
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
       run1.log({'loss': loss.item()})

model.eval()
y_pred = model(x_train)
plt.scatter(x_train,y_train)
plt.plot(x_train, y_pred.detach().numpy(), color='red')
fig = plt.gcf()
wandb.log({"Biểu đồ": wandb.Image(fig)})

wandb.finish()
