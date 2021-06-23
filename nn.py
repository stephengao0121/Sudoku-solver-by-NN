"""
nn.py: The neural network model settings for sudoku solving.
"""

import numpy as np
import tensorflow.keras as kr


class SudokuNN(object):

    def __init__(self, input_shape, layer_num, mid_num):
        self._input = kr.Input(shape=input_shape)
        self._layers = [self._input]
        for i in range(1, layer_num):
            layer = kr.layers.Dense(mid_num, activation='relu')(self._layers[-1])
            self._layers.append(layer)
            self._layers.append(kr.layers.Dropout(0.4)(layer))
        self._layers.append(kr.layers.Flatten()(self._layers[-1]))
        self._output = [
            kr.layers.Dense(input_shape[0], activation='softmax')(self._layers[-1])
            for i in range(input_shape[0] * input_shape[1])]
        self._model = kr.Model(self._input, self._output)

    def compile(self):
        self._model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def get_solver(self):
        return self._model

    def fit(self, x, y, batch_size, epochs):
        self._model.fit(x, y, batch_size=batch_size, epochs=epochs)

    def predict(self, x) -> np.array:
        prediction = self._model.predict(x)
        return prediction
