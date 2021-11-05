from Neural_Network import Layer
from Neural_Network import NeuralNetwork
from Neural_Network import Activation
import numpy as np
#  Creating our neural network, we called it Net. Now we can do whatever we want with it !
Net = NeuralNetwork(24, 4, Layer(18, Activation.relu))
Net.add_layer(18, Activation.sigmoid)
Net.add_layer(4, Activation.softmax)

# We will create an input layer totally random, it's just to see if forward propagation works
input_vector = np.round(np.random.uniform(-1, 1, 24), 2)
result = Net.forward_propagation(input_vector)

decision = np.argmax(result)
