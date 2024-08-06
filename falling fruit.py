import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
BASKET_WIDTH, BASKET_HEIGHT = 100, 30
FRUIT_SIZE = 30
FRUIT_SPEED = 5
BASKET_SPEED = 10
NUM_FRUITS = 5
TARGET_SCORE = 10


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
FRUIT_COLORS = [RED, GREEN, BLUE, YELLOW]


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Fruits")

def draw_objects(basket, fruits, score):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, basket)
    for fruit in fruits:
        pygame.draw.ellipse(screen, fruit['color'], fruit['rect'])
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()

   
    basket = pygame.Rect(WIDTH // 2 - BASKET_WIDTH // 2, HEIGHT - BASKET_HEIGHT - 10, BASKET_WIDTH, BASKET_HEIGHT)

    
    fruits = [{'color': random.choice(FRUIT_COLORS), 'rect': pygame.Rect(random.randint(0, WIDTH - FRUIT_SIZE), random.randint(-HEIGHT, -FRUIT_SIZE), FRUIT_SIZE, FRUIT_SIZE)} for _ in range(NUM_FRUITS)]

   
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.left > 0:
            basket.x -= BASKET_SPEED
        if keys[pygame.K_RIGHT] and basket.right < WIDTH:
            basket.x += BASKET_SPEED

       
        for fruit in fruits:
            fruit['rect'].y += FRUIT_SPEED

       
        for fruit in fruits[:]:
            if fruit['rect'].colliderect(basket):
                score += 1
                fruits.remove(fruit)
                new_fruit = {'color': random.choice(FRUIT_COLORS), 'rect': pygame.Rect(random.randint(0, WIDTH - FRUIT_SIZE), random.randint(-FRUIT_SIZE, -FRUIT_SIZE), FRUIT_SIZE, FRUIT_SIZE)}
                fruits.append(new_fruit)
            elif fruit['rect'].top > HEIGHT:
                fruits.remove(fruit)
                new_fruit = {'color': random.choice(FRUIT_COLORS), 'rect': pygame.Rect(random.randint(0, WIDTH - FRUIT_SIZE), random.randint(-FRUIT_SIZE, -FRUIT_SIZE), FRUIT_SIZE, FRUIT_SIZE)}
                fruits.append(new_fruit)

        
        if score >= TARGET_SCORE:
            print("You Win!")
            running = False

       
        draw_objects(basket, fruits, score)

        clock.tick(30)  

    pygame.quit()

if __name__ == "__main__":
    main()
