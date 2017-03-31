from recurrentshop import *
from keras.models import *
from keras.layers import *

x = Input((5,))
h_tm1 = Input((10,))
h = add([Dense(10)(x), Dense(10, use_bias=False)(h_tm1)])
h = Activation('tanh')(h)

cell_model = Model([x, h_tm1], [h, h])

rnn_cell = RNNCellFromModel(cell_model)

rnn = RecurrentSequential()
rnn.add(rnn_cell)

a = Input((7, 5))
b = rnn(a)

model = Model(a, b)

model.compile(loss='mse', optimizer='sgd')
model.fit((np.random.random((32, 7, 5))), np.random.random((32, 10)))
model.predict(np.zeros((32, 7, 5)))
