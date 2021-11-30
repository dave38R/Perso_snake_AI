from Neural_Network import Layer
from Neural_Network import NeuralNetwork
from Neural_Network import Activation
import numpy as np
from Snakes.Information_Functions import get_info

#  Creating our neural network, we called it Net. Now we can do whatever we want with it !
Net = NeuralNetwork(24, 4, Layer(18, Activation.relu))
Net.add_layer(18, Activation.sigmoid)
Net.add_layer(4, Activation.softmax)

# We will create an input layer totally random, it's just to see if forward propagation works
input_vector = np.round(np.random.uniform(-1, 1, 24), 2)
result = Net.forward_propagation(input_vector)

decision = np.argmax(result)

# print(result)
# print("decision :", decision)


body = [[130, 30], [140, 30], [150, 30], [150, 40], [150, 50], [150, 60], [150, 70], [140, 70], [130, 70], [120, 70], [110, 70], [100, 70], [90, 70], [80, 70]]
fruit = [10, 90]
print(get_info(body, fruit))



