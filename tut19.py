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
pink = (255, 0, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)



def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])




# Creating a game loop
def gameloop():
    # Game specific varaibles
    exit_game = False
    game_over = False
    snake_x = 40
    snake_y = 50
    init_velocity = 5
    velocity_x = init_velocity
    velocity_y = 0
    snk_list = []
    snk_length = 1

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)
    score = 0
    snake_size = 10
    fps = 60

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue",red,(screen_width/2)-300,(screen_height/2)-35)
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
                text_screen("You made a High Score",green,(screen_width/2)-200,(screen_height/2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
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
                score += 10
                # init_velocity += 1
                snk_length += 5
                # print("Score :",score)
                if score>int(highscore):
                    highscore = score
                food_x = random.randint(20, screen_width - 20)
                food_y = random.randint(20, screen_height - 20)
            gameWindow.fill(white)
            text_screen("Score : " + str(score), pink, 5, 5)
            text_screen("HighScore : "+str(highscore),green,5,35)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, 10, 10])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True

            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    with open("highscore.txt", "w") as f:
        f.write(str(highscore))
    pygame.quit()
    quit()

gameloop()