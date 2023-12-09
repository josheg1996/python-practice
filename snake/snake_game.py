import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.size = 20
        self.head_pos = [width // 2, height // 2]
        self.body = [self.head_pos.copy()]
        self.direction = [1, 0]

    def move(self):
        self.head_pos[0] += self.direction[0] * self.size
        self.head_pos[1] += self.direction[1] * self.size

    def check_boundary(self):
        return self.head_pos[0] < 0 or self.head_pos[0] >= width or \
               self.head_pos[1] < 0 or self.head_pos[1] >= height

    def check_collision(self):
        return self.head_pos in self.body[1:]

    def update_body(self):
        self.body.insert(0, self.head_pos.copy())
        if len(self.body) > 1:
            self.body.pop()

# Food class
class Food:
    def __init__(self):
        self.size = 20
        self.pos = [random.randrange(0, width, self.size),
                    random.randrange(0, height, self.size)]

    def respawn(self):
        self.pos = [random.randrange(0, width, self.size),
                    random.randrange(0, height, self.size)]

# Create instances of Snake and Food
snake = Snake()
food = Food()

# Set up the font for the score
font = pygame.font.Font(None, 36)

# Main game loop
clock = pygame.time.Clock()
score = 0

while True:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
           # pygame.quit()
           # sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and not snake.direction[0] == 1:
        snake.direction = [-1, 0]
    elif keys[pygame.K_RIGHT] and not snake.direction[0] == -1:
        snake.direction = [1, 0]
    elif keys[pygame.K_UP] and not snake.direction[1] == 1:
        snake.direction = [0, -1]
    elif keys[pygame.K_DOWN] and not snake.direction[1] == -1:
        snake.direction = [0, 1]

    snake.move()

    if snake.head_pos == food.pos:
        score += 1
        food.respawn()
        snake.update_body()

    if snake.check_boundary() or snake.check_collision():
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(black)

    for segment in snake.body:
        pygame.draw.rect(screen, white, (segment[0], segment[1], snake.size, snake.size))

    pygame.draw.rect(screen, red, (food.pos[0], food.pos[1], food.size, food.size))

    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(10)  # Adjust the value to control the speed of the game
