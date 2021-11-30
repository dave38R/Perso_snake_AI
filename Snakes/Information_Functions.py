from .Game_Parameters import *
# Here are the functions to get the information we want to feed our algorithm

def get_distance(body_list, bit):
    head = body_list[0]
    checkpoints = []

    for pos in body_list:
        if head[bit] == pos[bit]:
            checkpoints.append(pos[1 - bit] - head[1 - bit])  # We add all the distances that we get, pos or neg

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


def get_info(body_list=None, fruit_list=None):
    if fruit_list is None:
        fruit_list = fruit_position
    if body_list is None:
        body_list = snake_body
    head = body_list[0]
    info_vector = []

    info_vector.append(head[0])  # Distance to left wall
    info_vector.append(window_x - head[0])  # Distance to right wall
    info_vector.append(head[1])  # Distance to bottom wall
    info_vector.append(window_y - head[1])  # Distance to top wall
    info_vector.append(fruit_list[0] - head[0])  # Distance to fruit along the x axis
    info_vector.append(fruit_list[1] - head[1])  # Distance to fruit along the y axis
    info_vector.append(get_info_body(body_list)[0][0])  # Distance to body on the bottom
    info_vector.append(get_info_body(body_list)[0][1])  # Distance to body on the top
    info_vector.append(get_info_body(body_list)[1][0])  # Distance to body on the left
    info_vector.append(get_info_body(body_list)[1][1])  # Distance to body on the right
# Should display 10 (or -10) for the second body part (let's call it the neck)
    return info_vector

