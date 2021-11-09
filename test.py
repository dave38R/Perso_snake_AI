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

print(result)
print("decision :", decision)

def get_distance(body_list, bit):
    head = body_list[0]
    checkpoints = []

    for pos in body_list:

        if head[bit] == pos[bit]:
            checkpoints.append(head[1 - bit] - pos[1 - bit])  # We add all the distances that we get, pos or neg

    pos_checkpoints = [distance for distance in checkpoints if distance > 0]  # Neg part ==> left or down parts
    if len(pos_checkpoints) == 0:
        pos_checkpoints.append(0)  # 0 means that there are no snake parts in that direction

    neg_checkpoints = [distance for distance in checkpoints if distance < 0]  # Pos part ==> right or up parts
    if len(neg_checkpoints) == 0:
        neg_checkpoints.append(0)  # 0 means that there are no snake parts in that direction

    distance_to_body = [max(neg_checkpoints), min(pos_checkpoints)]  # We have the pos and neg closest to the snake

    return distance_to_body


def get_info_body(body_list):
    distance_to_body_x = get_distance(body_list, 0)
    distance_to_body_y = get_distance(body_list, 1)

    return distance_to_body_x, distance_to_body_y


body = [[50, 50], [50, 100], [50, 25]]
print(get_info_body(body))

