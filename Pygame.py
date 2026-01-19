import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
BASKET_WIDTH, BASKET_HEIGHT = 100, 20
APPLE_WIDTH, APPLE_HEIGHT = 20, 20
SPEED = 5
APPLE_FALL_SPEED = 4

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Apples")

# Load basket
basket = pygame.Rect(WIDTH // 2, HEIGHT - 50, BASKET_WIDTH, BASKET_HEIGHT)

# List of apples
apples = []
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket.left > 0:
        basket.move_ip(-SPEED, 0)
    if keys[pygame.K_RIGHT] and basket.right < WIDTH:
        basket.move_ip(SPEED, 0)
    
    # Spawn apples
    if random.randint(1, 50) == 1:
        apple_x = random.randint(0, WIDTH - APPLE_WIDTH)
        apples.append(pygame.Rect(apple_x, 0, APPLE_WIDTH, APPLE_HEIGHT))
    
    # Move apples
    for apple in apples[:]:
        apple.move_ip(0, APPLE_FALL_SPEED)
        if apple.colliderect(basket):
            apples.remove(apple)
            score += 1
        elif apple.top > HEIGHT:
            apples.remove(apple)
    
    # Draw basket
    pygame.draw.rect(screen, GREEN, basket)
    
    # Draw apples
    for apple in apples:
        pygame.draw.rect(screen, RED, apple)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
