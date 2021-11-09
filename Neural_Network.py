import numpy as np


# We want to build a neural network that has an input and an output vector, and two hidden layers. input is size (24, 1)
# We define 2 layers, each initialized randomly between 0 and 100
# The input layer will be given by the situation of the board, for now we define it randomly to test the code

class Neuron:
    def __init__(self, input_size):
        self.size = input_size
        self.weights = np.random.normal(0, 1, input_size + 1)  # The +1 corresponds to the bias


# It's hard to say if we should say 10* or 100* or 0.1*, check that with the np.exp error that we get if we use the relu

class Layer:
    def __init__(self, size, activation):
        self.activation = activation
        self.size = size
        self.neurons = []

    def forward_layer(self, input_vector):
        input_size = len(input_vector)
        self.neurons = [Neuron(input_size) for _ in range(self.size)]
        output_vector = np.array([])

        for neuron in self.neurons:
            temp_output = sum(neuron.weights * np.append(1, input_vector))  # This is the computation for each neuron
            output_vector = np.append(output_vector, temp_output)

        return np.array(self.activation(output_vector))


class NeuralNetwork:
    def __init__(self, input_size, output_size, first_layer):
        self.input_size = input_size
        self.output_size = output_size
        self.layers = [first_layer]

    def add_layer(self, size, activation):
        self.layers.append(Layer(size, activation))

    def forward_propagation(self, input_vector):
        if input_vector.size != self.input_size:
            print('Error, input_vector is not the right size. Right size is : ', self.input_size)
            return None
        elif self.layers[-1].size != self.output_size:
            print('Error, last_layer is not the right size. Right size is : ', self.output_size)
            return None
        else:
            input_1 = input_vector
            output_1 = 0
            for layer in self.layers:
                output_1 = layer.forward_layer(input_1)
                input_1 = output_1
            return output_1


#  Here is the website from which I got all the activation functions :
#  https://medium.com/ai%C2%B3-theory-practice-business/a-beginners-guide-to-numpy-with-sigmoid-relu-and-softmax-activation-functions-25b840a9a272

class Activation:

    def softmax(X):
        expo = np.exp(X)
        expo_sum = np.sum(np.exp(X))
        return expo / expo_sum

    def relu(X):
        return np.maximum(0, X)

    def sigmoid(X):
        return 1 / (1 + np.exp(-X))


# here is some doc about the overflow in exp warning:
# https://www.statology.org/runtimewarning-overflow-encountered-in-exp/


Net = NeuralNetwork(10, 4, Layer(18, Activation.sigmoid))  # Using the relu gives out problems with the np.exp...
Net.add_layer(18, Activation.sigmoid)
Net.add_layer(4, Activation.softmax)
