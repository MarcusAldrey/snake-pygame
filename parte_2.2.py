import pygame

# Game settings

# Snake cell and food size
WIDTH = 25
HEIGHT = 25

SNAKE_COLOR = (255, 255, 255)

GAME_SPEED = 20

SCREENX = 40 * WIDTH
SCREENY = 30 * HEIGHT


UP = (0, -1 * HEIGHT)
DOWN = (0, 1 * HEIGHT)
LEFT = (-1 * WIDTH, 0)
RIGHT = (1 * WIDTH, 0)

direction = RIGHT

pygame.init()
pygame.display.set_caption("Snake")

# create game clock
clock = pygame.time.Clock()

# create the screen
screen = pygame.display.set_mode((SCREENX, SCREENY))

snake = [
    pygame.Rect(SCREENX // 2, SCREENY // 2, WIDTH, HEIGHT),
    pygame.Rect((SCREENX // 2) - WIDTH, SCREENY // 2, WIDTH, HEIGHT),
    pygame.Rect((SCREENX // 2) - (WIDTH*2), SCREENY // 2, WIDTH, HEIGHT),
]

# create the game loop
while True:
    clock.tick(GAME_SPEED)

    # update the screen
    pygame.display.flip()

    if pygame.event.get(pygame.QUIT):
        break
    
    # input handling
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        direction = UP
    elif pressed[pygame.K_DOWN]:
        direction = DOWN
    elif pressed[pygame.K_LEFT]:
        direction = LEFT
    elif pressed[pygame.K_RIGHT]:
        direction = RIGHT

    # move the snake
    snake.insert(0, snake[0].move(direction))
    snake.pop()

     # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for rect in snake:
        pygame.draw.rect(screen,SNAKE_COLOR, rect)

