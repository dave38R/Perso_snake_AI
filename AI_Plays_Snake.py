# This code is from this website : https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/

import pygame
import random
from Neural_Network import Net
import numpy as np

pygame.font.init()
pygame.init()

# Window size
window_x = 450
window_y = 300
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialise game window
pygame.display.set_caption("David's Snake Game !")
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]
snake_speed = 15
# defining first 4 blocks of snake
# body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]
# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# setting default snake direction
# towards right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0


def spawn_a_fruit(snake_body):  # We can't have a fruit spawn ON the snake.
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]
    while fruit_position in snake_body:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
    return fruit_position


# displaying Score function
def show_score(score, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the
    # text surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)


# game over function
def game_over(gameOver, score):
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit wil draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    gameOver = True

    # setup the quit possibility
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


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


def get_info(body_list=None, fruit_position=None):
    if fruit_position is None:
        fruit_position = fruit_list
    if body_list is None:
        body_list = snake_body
    head = body_list[0]
    info_vector = []
    info_vector.append(head[0])  # Distance to left wall
    info_vector.append(window_x - head[0])  # Distance to right wall
    info_vector.append(head[1])  # Distance to bottom wall
    info_vector.append(window_y - head[1])  # Distance to top wall
    info_vector.append(fruit_position[0] - head[0])  # Distance to fruit along the x axis
    info_vector.append(fruit_position[1] - head[1])  # Distance to fruit along the y axis
    info_vector.append(get_info_body(body_list)[0][0])  # Distance to body on the bottom
    info_vector.append(get_info_body(body_list)[0][1])  # Distance to body on the top
    info_vector.append(get_info_body(body_list)[1][0])  # Distance to body on the left
    info_vector.append(get_info_body(body_list)[1][1])  # Distance to body on the right

    return info_vector


# Main Function

def play_game(change_to='RIGHT', direction='RIGHT', fruit_list=fruit_position, fruit_spawn=True):
    score = 0
    gameOver = False

    while not gameOver:

        # handling key events
        input_vector = 0.1 * np.array(get_info(snake_body, fruit_list))
        result = Net.forward_propagation(input_vector)  # Right now, the AI has random weights
        decision = np.argmax(result)
        AI_choice = decision  # here, the AI chooses randomly a direction everytime

        if AI_choice == 1:
            change_to = 'UP'
        if AI_choice == 2:
            change_to = 'DOWN'
        if AI_choice == 3:
            change_to = 'LEFT'
        if AI_choice == 4:
            change_to = 'RIGHT'

        # we don't want snake to start going backwards and die
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_list[0] and snake_position[1] == fruit_list[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            # Put a function spawn_a_fruit(snake_body) to prevent a fruit from spawning on the snake body
            fruit_list = spawn_a_fruit(snake_body)

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(
                pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, blue, pygame.Rect(
            snake_body[0][0], snake_body[0][1], 10, 10))

        pygame.draw.rect(game_window, red, pygame.Rect(
            fruit_list[0], fruit_list[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over(gameOver, score)
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over(gameOver, score)

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(gameOver, score)

        # displaying score continuously
        show_score(score, white, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)

    return score

b = 3
a = play_game()
print(a, b)

