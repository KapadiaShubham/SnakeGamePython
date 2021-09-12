import random

import pygame
pygame.init()
screen_width = 900
screen_height = 600

# Creating window
gameWindow = pygame.display.set_mode((screen_width,screen_height))
# Game Title
pygame.display.set_caption("Snakes with Harry")
pygame.display.update() # whenever you want to see the change in your window

# Colors - RGB
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# Game specific varaibles
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 5
velocity_y = 0
food_x = random.randint(0,screen_width)
food_y = random.randint(0,screen_height)
snake_size = 10
fps = 30

clock = pygame.time.Clock()

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and velocity_x != -5:
                velocity_x = 5
                velocity_y = 0
            if event.key == pygame.K_LEFT and velocity_x != 5:
                velocity_x = -5
                velocity_y = 0
            if event.key == pygame.K_UP and velocity_y != 5:
                velocity_x = 0
                velocity_y = -5
            if event.key == pygame.K_DOWN and velocity_y != -5:
                velocity_x = 0
                velocity_y = 5
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         print("You have pressed right arrow key")
    snake_x += velocity_x
    snake_y += velocity_y
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
