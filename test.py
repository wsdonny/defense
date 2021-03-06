from keras.models import Sequential, Input, Model
from keras.layers import Dense
import numpy as np

inputs = Input(shape=(2,))
x = Dense(units=4)(inputs)
x = Dense(units=4)(x)
predictions1 = Dense(units=1)(x)
predictions2 = Dense(units=1)(x)
model1 = Model(inputs=inputs, outputs=predictions1)
model2 = Model(inputs=inputs, outputs=predictions2)
model1.compile(loss='mean_squared_error', optimizer='adam')
model2.compile(loss='mean_squared_error', optimizer='adam')
model1.summary()
model2.summary()

# model = Sequential()
# model.add(Dense(units=4, input_dim=1))
# model.add(Dense(units=4))
# model.add(Dense(units=2))
# model.compile(loss='mean_squared_error', optimizer='adam')

# model.summary()

# from keras.utils import plot_model
# plot_model(model, to_file='model.png')

# from IPython.display import SVG
# from keras.utils.vis_utils import model_to_dot
# SVG(model_to_dot(model).create(prog='dot', format='svg'))

# x_train = np.fromfunction(lambda i: i, (10000,), dtype=int)
# y_train1 = np.fromfunction(lambda i: 3 * i + 8, (10000,), dtype=int)
# y_train2 = np.fromfunction(lambda i: 3 * i + 18, (10000,), dtype=int)
# x_train = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]]
# print(np.array([1,1]))
# print(np.array([1,1]).shape)
x_train = np.array([np.array([i,i]) for i in range(3)])
# x_train = np.array([[0,0], [1,1], [2,2]])
print(x_train)
print(x_train.shape)
# x_train1 = np.array([0,1,2,3,4,5,6,7,8,9])
# x_train2 = np.array([0,1,2,3,4,5,6,7,8,9])
y_train1 = [0,1,2]
y_train2 = [1,2,3]
model1.fit(x_train, y_train1, epochs=10000, batch_size=32)
model2.fit(x_train, y_train2, epochs=10000, batch_size=32)

# x_test = np.fromfunction(lambda i: i, (10099,), dtype=int)[10000:]
# y_test1 = np.fromfunction(lambda i: 3 * i + 8, (10099,), dtype=int)[10000:]
# y_test2 = np.fromfunction(lambda i: 3 * i + 18, (10099,), dtype=int)[10000:]
# loss_and_metrics1 = model1.evaluate(x_test, y_test1, batch_size=128)
# loss_and_metrics2 = model1.evaluate(x_test, y_test2, batch_size=128)
#
# print(loss_and_metrics1)
# print(loss_and_metrics2)

print(model1.predict(x_train))
print(model2.predict(x_train))