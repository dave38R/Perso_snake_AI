import pygame
import random

# Window size
window_x = 200  # 450
window_y = 100  # 300

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

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
