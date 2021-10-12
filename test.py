import numpy as np
import math as m


class Neuron:
    def __init__(self, input_size, activation):
        self.weights = np.round(np.random.rand(1, input_size + 1))
        self.activation = activation


def sigmoid(x):
    sig = 1 / (1 + m.exp(-x))
    return sig


neuron = Neuron(24, sigmoid)
print(neuron.activation(0.5))