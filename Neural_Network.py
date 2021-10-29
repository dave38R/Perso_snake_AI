import random

import numpy as np
import tensorflow as tf

# We want to build a neural network that has an input and an output vector, and two hidden layers. input is size (24, 1)
# We define 2 layers, each initialized randomly between 0 and 100
# The input layer will be given by the situation of the board, for now we define it randomly to test the code
input_layer = np.append(1, np.round(np.random.rand(24), 2))


class Neuron:
    def __init__(self, input_vector, weights):
        self.weights = weights
        self.input_vector = input_vector

    def ComputeNeuron(self):
        return self.weights * self.input_vector


class Layer:
    def __init__(self, size, input_vector, activation):
        self.neurons = [Neuron(input_vector,
                               np.round(10 * random.uniform(-1, 1), 2))
                        for i in range(size)]
        self.activation = activation


class NeuralNetwork:
    def __init__(self, input_size, output_size, first_layer):
        self.input_size = input_size
        self.output_size = output_size
        self.layers = [first_layer]

    def ouput_layer(self, layer):
        output_1 = [layer.input_vector * neuron for neuron in layer.neurons]
        output_2 = layer.activation(output_1)
        return output_2

    def add_layer(self, size, activation):
        self.layers.append(Layer(size, NeuralNetwork.ouput_layer(self.layers[-1]), activation))


# here is some doc about the overflow in exp warning:
# https://www.statology.org/runtimewarning-overflow-encountered-in-exp/


# The output layer will be computed by what happens in the two hidden layers
def computing_neuron(input_layer, neuron, activation):
    return round(activation(sum(input_layer * neuron)), 2)


directions = ['Up', 'Down', 'Left', 'Right']
decision = directions[np.argmax(output)]
print(decision)
