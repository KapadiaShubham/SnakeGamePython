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
green = (0,255,0)

# Game specific varaibles
exit_game = False
game_over = False
snake_x = 40
snake_y = 50
init_velocity = 5
velocity_x = init_velocity
velocity_y = 0
food_x = random.randint(20,screen_width-20)
food_y = random.randint(20,screen_height-20)
score = 0
snake_size = 10
fps = 60

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

snk_list = []
snk_length = 1


# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and velocity_x != -init_velocity:
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_LEFT and velocity_x != init_velocity:
                velocity_x = -init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP and velocity_y != init_velocity:
                velocity_x = 0
                velocity_y = -init_velocity
            if event.key == pygame.K_DOWN and velocity_y != -init_velocity:
                velocity_x = 0
                velocity_y = init_velocity

    snake_x += velocity_x
    snake_y += velocity_y
    if snake_x==(-10):
        snake_x = screen_width -10
    elif snake_x==(screen_width+10):
        snake_x = 10
    elif snake_y==(-10):
        snake_y = screen_height - 10
    elif snake_y==(screen_height+10):
        snake_y = 10

    # print(snake_x,snake_y)
    if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
        score += 1
        # init_velocity += 1
        snk_length += 5
        # print("Score :",score*10)
        food_x = random.randint(20, screen_width - 20)
        food_y = random.randint(20, screen_height - 20)
    gameWindow.fill(white)
    text_screen("Score :" + str(score * 10), green, 5, 5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10])

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]
    # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])

    plot_snake(gameWindow, black, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
