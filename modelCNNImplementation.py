from keras import Sequential
from keras.layers import Dense, Embedding, Dropout
from keras.models import Sequential
from keras.layers import Bidirectional
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers import GlobalMaxPooling1D
from keras.optimizers import Adam


def compileCNNModel(num_words=15000, max_tokens=317, lr=1e-3):
    optimizer = Adam(lr)
    model_cnn = Sequential()
    parameters = Embedding(num_words, 200, input_length=max_tokens) 
    model_cnn.add(parameters)
    model_cnn.add(Conv1D(filters=100, kernel_size=2, padding='valid', activation='relu', strides=1))
    model_cnn.add(GlobalMaxPooling1D())
    model_cnn.add(Dense(256, activation='relu'))
    model_cnn.add(Dense(1, activation='sigmoid'))
    model_cnn.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model_cnn
