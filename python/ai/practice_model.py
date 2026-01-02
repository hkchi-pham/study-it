#1 - kmean

from sklearn.cluster import KMeans

join_matrix = tf.concat([tensor_a,tensor_b],0)
join_matrix_np = join_matrix.numpy()

kmeans = KMeans(n_clusters=3, random_state = 42)
kmeans.fit(join_matrix_np)

label = kmeans.labels_
center = tf.convert_to_tensor(kmeans.cluster_centers_)

print(label)
print(center)

#2 - linear regression

from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('baitap.csv').to_numpy()
x, y = np.hsplit(data,2)
x = x.reshape(15,)
y = y.reshape(15,)


x = x.reshape(-1,1)
y = y.reshape(-1,1)

model = LinearRegression()
model.fit(x,y)

y_pred_sk = model.predict(x)
plt.title('Linear Regression')
plt.scatter(x,y, color='red')
plt.plot(x,y_pred_sk, color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#3 - TensorFlow Sequential
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import Callback
model = Sequential([Dense(1,input_shape=[x.shape[1]])])

model.compile(loss='mse', optimizer=keras.optimizers.Adam(learning_rate=0.01))

class call_back(Callback):
  def on_epoch_end(self, epoch, logs=None):
    if epoch%100==0:
      print(f'epoch: {epoch}, loss: {logs["loss"]}')
model.fit(x,y, epochs=1000, verbose=0, callbacks=[call_back()])
y_pred_tf = model.predict(x)

plt.scatter(x,y)
plt.plot(x,y_pred_tf, color='red')
plt.show()

#4 - pytorch
import torch
import torch.nn as nn
import torch.optim as optim

class LinearRegressionModel(nn.Module):
  def __init__(self, input_dim, output_dim):
    super(LinearRegressionModel, self).__init__()
    self.linear = nn.Linear(input_dim, output_dim)

  def forward(self, x):
    return self.linear(x)


model = LinearRegressionModel(input_dim=1,output_dim=1)

criterion = nn.MSELoss()
optimiser = optim.SGD(model.parameters(), lr=0.01)

x = torch.tensor(x, dtype=torch.float32).view(-1, 1)
y = torch.tensor(y, dtype=torch.float32).view(-1, 1)
epochs = 1000
for epoch in range(epochs):

  y_pred = model(x)
  loss = criterion(y_pred, y)

  optimiser.zero_grad()
  loss.backward()
  optimiser.step()

  if epoch%10==0:
    print(f'epoch: {epoch}, loss: {loss.item()}')

plt.title('Linear Regression')
plt.scatter(x,y, color='red')
plt.plot(x,y_pred.detach().numpy(), color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
