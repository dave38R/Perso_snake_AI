import numpy as np


# Defining the Neuron class
class Neuron:
    def __init__(self, input_size, activation):
        self.weights = np.round(100 * np.random.rand(input_size + 1), 2)
        self.activation = activation


# Defining the activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Putting neurons in neural networks layers
hidden_layer_1 = [Neuron(24, sigmoid) for _ in range(18)]
hidden_layer_2 = [Neuron(18, sigmoid) for _ in range(18)]

# Define the input layer
input_layer = np.append(1, np.round(10 * np.random.rand(24)))

# Computing the outputs of each layer
weights_neuron_1 = hidden_layer_1[0].weights


def computing_neuron(input, neuron):
    return round(sum(input * neuron), 2)


a = np.array([1, 2, 3, 4])
b = np.array([0, 1, 0, 1])

nb1 = 4
nb2 = 5


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rec = Rectangle(1, 2)
print(rec.area())