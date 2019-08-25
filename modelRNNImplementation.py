from keras import Sequential
from keras.layers import Dense, Embedding, GRU 
from keras.models import Sequential
from keras.optimizers import Adam


def compileRNNModel(num_words=15000, max_tokens=317, lr=1e-3, embedding_size=8*3):
    optimizer = Adam(lr)
    model_rnn = Sequential()
    model_rnn.add(Embedding(input_dim=num_words,output_dim=embedding_size, input_length=max_tokens, name='layer_embedding'))
    model_rnn.add(GRU(units=16, return_sequences=True))
    model_rnn.add(GRU(units=8, return_sequences=True))
    model_rnn.add(GRU(units=4))
    model_rnn.add(Dense(1, activation='sigmoid'))
    model_rnn.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model_rnn
