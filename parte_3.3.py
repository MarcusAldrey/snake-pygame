import pygame, random

# Game settings

# Snake cell and food size
WIDTH = 25
HEIGHT = 25

SNAKE_COLOR = (255, 255, 255)
FOOD_COLOR = (255, 0, 0)

GAME_SPEED = 15

SCREENX = 40 * WIDTH
SCREENY = 30 * HEIGHT


UP = (0, -1 * HEIGHT)
DOWN = (0, 1 * HEIGHT)
LEFT = (-1 * WIDTH, 0)
RIGHT = (1 * WIDTH, 0)



pygame.init()
pygame.display.set_caption("Snake")

# create game clock
clock = pygame.time.Clock()

# create the screen
screen = pygame.display.set_mode((SCREENX, SCREENY))

def reset_game():
    snake = [
        pygame.Rect(SCREENX // 2, SCREENY // 2, WIDTH, HEIGHT),
        pygame.Rect((SCREENX // 2) - WIDTH, SCREENY // 2, WIDTH, HEIGHT),
        pygame.Rect((SCREENX // 2) - (WIDTH*2), SCREENY // 2, WIDTH, HEIGHT),
    ]
    direction = RIGHT
    food = pygame.Rect(random.randint(0, SCREENX), random.randint(0, SCREENY),WIDTH, HEIGHT)
    return snake, food, direction

snake, food, direction = reset_game()

# create the game loop
while True:
    clock.tick(GAME_SPEED)

    if pygame.event.get(pygame.QUIT):
        break

    # update the screen
    pygame.display.flip()

    # input handling
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if direction != DOWN:
            direction = UP
    elif pressed[pygame.K_DOWN]:
        if direction != UP:
            direction = DOWN
    elif pressed[pygame.K_LEFT]:
        if direction != RIGHT:
            direction = LEFT
    elif pressed[pygame.K_RIGHT]:
        if direction != LEFT:
            direction = RIGHT

    # move the snake
    snake.insert(0, snake[0].move(direction))
    snake.pop()

    # check food collision
    if snake[0].colliderect(food):
        snake.insert(0, snake[0].move(direction))
        food = pygame.Rect(random.randint(0, SCREENX), random.randint(0, SCREENY),WIDTH, HEIGHT)

    # check if the snake hit the wall
    if (
        snake[0].x < 0
        or snake[0].x > SCREENX - WIDTH
        or snake[0].y < 0
        or snake[0].y > SCREENY - HEIGHT
    ):
        snake, food, direction = reset_game()

    # check if the snake hit itself
    if pygame.Rect.collidelist(snake[0], snake[1:]) != -1:
        snake, food, direction = reset_game()
    
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    for rect in snake:
        pygame.draw.rect(screen,SNAKE_COLOR, rect)

    pygame.draw.rect(screen,FOOD_COLOR, food)

