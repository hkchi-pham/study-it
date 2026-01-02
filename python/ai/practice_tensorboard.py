#KERAS - tensorboard
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import Callback, TensorBoard
import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('baitap.csv')
x = df['x'].values
y = df['y'].values

model = Sequential([Dense(units=1, input_shape=[1])])
model.compile(optimizer=Adam(learning_rate=0.03), loss='mean_squared_error')


class call_back(Callback):
  def on_epoch_end(self, epoch, logs=None):
     if epoch % 100 == 0:
       print(f"Epoch {epoch}, Loss: {logs['loss']}")

logs_dir = 'logs/fit/' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
tensorboard_callback = TensorBoard(log_dir=logs_dir, histogram_freq=1)


model.fit(x,y,epochs =1000, verbose=0, callbacks=[tensorboard_callback])

y_pred = model.predict(x)

img = "keras.png"
raw_img = tf.io.read_file(img)
img_tensor = tf.image.decode_image(raw_img)
img_tensor = tf.expand_dims(img_tensor, 0)
tf.summary.image("keras", img_tensor, step=0)
plt.scatter(x,y)
plt.plot(x, y_pred, color='red')
plt.show()


# Pytorch - Tensorboard
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.utils.tensorboard import SummaryWriter

df = pd.read_csv('baitap.csv')
x = df['x'].values
y = df['y'].values
x_train = torch.tensor(x).view(-1,1)
y_train = torch.tensor(y).view(-1,1)

x_train = x_train.float()
y_train = y_train.float()

class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


model = LinearRegressionModel()
writer = SummaryWriter(log_dir="/content/logs")
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.03)

epochs = 1000
for epoch in range(epochs):
    model.train()
    y_pred = model(x_train)
    loss = criterion(y_pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        writer.add_scalar('Loss', loss.item(), epoch)

    for i, (x,pred) in enumerate(zip(x_train,y_pred)):
      writer.add_scalar(f'Prediction_{i}', pred.detach().item(), x.detach().item())

model.eval()
y_pred = model(x_train)
plt.scatter(x_train,y_train)
plt.plot(x_train, y_pred.detach().numpy(), color='red')
fig = plt.gcf()
fig.canvas.draw()
writer.add_figure('Prediction', fig, 0)
plt.show()


writer.flush()
