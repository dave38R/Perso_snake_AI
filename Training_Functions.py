from Neural_Network import Net
import numpy as np


def get_genetic_representation(net):
    genrep = np.array([])
    for layer in net.layers:
        for neuron in layer.neurons:
            for weight in neuron.weights:
                np.append(genrep, weight)
    return genrep

genetic_representation = get_genetic_representation(Net)

