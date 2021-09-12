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
velocity_x = 10
velocity_y = 0
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
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10
            if event.key == pygame.K_UP:
                snake_y = snake_y - 10
            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 10
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         print("You have pressed right arrow key")
    snake_x += velocity_x
    snake_y += velocity_y
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
quit()
