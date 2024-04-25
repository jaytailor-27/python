import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the size of the snake and the food
BLOCK_SIZE = 20

# Set the speed of the snake
SNAKE_SPEED = 10

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control the game's speed
clock = pygame.time.Clock()

# Function to display text on the screen
def display_text(text, color, x, y):
    font = pygame.font.SysFont(None, 25)
    text_surface = font.render(text, True, color)
    window.blit(text_surface, (x, y))

# Function to draw the snake
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(window, GREEN, [x, y, BLOCK_SIZE, BLOCK_SIZE])

# Function to display the game over message
def game_over_message():
    window.fill(BLACK)
    display_text("Game Over! Press Q to quit or C to play again", RED, WINDOW_WIDTH // 4, WINDOW_HEIGHT // 2)

# Main function to run the game
def game():
    # Initial position of the snake
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2

    # Initial speed of the snake
    x_speed = 0
    y_speed = 0

    # Initial length of the snake
    snake_list = []
    snake_length = 1

    # Initial position of the food
    food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # Flag to control game over
    game_over = False

    # Game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -BLOCK_SIZE
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = BLOCK_SIZE
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = BLOCK_SIZE

        # Update snake's position
        x += x_speed
        y += y_speed

        # Check if snake has eaten food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WINDOW_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, WINDOW_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1

        # Create the snake list
        head = []
        head.append(x)
        head.append(y)
        snake_list.append(head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake has collided with itself or with the window edges
        if head in snake_list[:-1] or x < 0 or x >= WINDOW_WIDTH or y < 0 or y >= WINDOW_HEIGHT:
            game_over = True

        # Clear the window
        window.fill(BLACK)

        # Draw the snake and food
        draw_snake(snake_list)
        pygame.draw.rect(window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Display the score
        display_text("Score: " + str(snake_length - 1), WHITE, 10, 10)

        # Refresh the window
        pygame.display.update()

        # Set the game speed
        clock.tick(SNAKE_SPEED)

    # Display game over message
    game_over_message()

    # Loop to handle game over
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    game()

# Start the game
game()
