# This code is from this website : https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/

import pygame
import random

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


# Main Function

def play_game(change_to='RIGHT', direction='RIGHT', fruit_list=fruit_position, fruit_spawn=True):
    score = 0
    gameOver = False
    while not gameOver:

        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
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

print(play_game())