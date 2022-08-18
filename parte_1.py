import pygame

# Game settings

# Snake cell and food size
WIDTH = 25
HEIGHT = 25

SNAKE_COLOR = (255, 255, 255)

GAME_SPEED = 20

SCREENX = 40 * WIDTH
SCREENY = 30 * HEIGHT

pygame.init()
pygame.display.set_caption("Snake")

# create game clock
clock = pygame.time.Clock()

# create the screen
screen = pygame.display.set_mode((SCREENX, SCREENY))


# create the game loop
while True:
    clock.tick(GAME_SPEED)

    # update the screen
    pygame.display.flip()

    snake = [
        pygame.Rect(80, 30, WIDTH, HEIGHT),
        pygame.Rect(55, 30, WIDTH, HEIGHT),
        pygame.Rect(30, 30, WIDTH, HEIGHT),
    ]

    # snake = [
    #     pygame.Rect(SCREENX // 2, SCREENY // 2, WIDTH, HEIGHT),
    #     pygame.Rect((SCREENX // 2) - WIDTH, SCREENY // 2, WIDTH, HEIGHT),
    #     pygame.Rect((SCREENX // 2) - (WIDTH*2), SCREENY // 2, WIDTH, HEIGHT),
    # ]


    for rect in snake:
        pygame.draw.rect(screen,SNAKE_COLOR, rect)

    

    if pygame.event.get(pygame.QUIT):
        break

