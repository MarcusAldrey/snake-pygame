import pygame, random

# Game settings

# Snake cell and food size
WIDTH = 25
HEIGHT = 25

GAME_SPEED = 20


SCREENX = 40 * WIDTH
SCREENY = 30 * HEIGHT


# Directions
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

# set snake with initial position
def reset_snake():
    snake = [
        pygame.Rect(SCREENX // 2, SCREENY // 2, WIDTH, HEIGHT),
        pygame.Rect((SCREENX // 2) - WIDTH, SCREENY // 2, WIDTH, HEIGHT),
        pygame.Rect((SCREENX // 2) - WIDTH, SCREENY // 2, WIDTH, HEIGHT),
    ]
    return snake


def get_value_on_grid(x, y):
    return (x // WIDTH) * WIDTH, (y // HEIGHT) * HEIGHT


def generate_new_food():
    x, y = get_value_on_grid(random.randint(0, SCREENX), random.randint(0, SCREENY))
    return pygame.Rect(x, y, WIDTH, HEIGHT)


def reset_game():
    snake = reset_snake()
    food = generate_new_food()
    direction = RIGHT
    return snake, food, direction


snake, food, direction = reset_game()

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

    # show score
    score_font = pygame.font.SysFont("monospace", 20)
    score_text = score_font.render(f"Score: {len(snake)-3}", True, (255, 255, 255))


    # check food collision
    if snake[0].colliderect(food):
        snake.insert(0, snake[0].move(direction))
        food = generate_new_food()

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

    # draw the snake
    for rect in snake:
        pygame.draw.rect(screen, (255, 255, 255), rect)

    screen.blit(score_text, (30, 30))

    pygame.draw.rect(screen, (255, 0, 0), food)
