from Neural_Network import Layer, Activation
import numpy as np

# We will create an input layer totally random, it's just to see if forward propagation works
input_vector = np.round(0.1 * np.random.uniform(-1, 1, 3), 2)

# Try to work out why it doesn't work
layer = Layer(4, Activation.relu)
o = layer.forward_layer(input_vector)


