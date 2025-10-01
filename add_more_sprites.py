import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Simple Shooter Game")

# Colors
WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 200, 0)
ENEMY_COLOR = (200, 0, 0)
BULLET_COLOR = (0, 0, 0)

# Player setup
player = pygame.Rect(230, 350, 40, 20)
player_speed = 5

# Bullet setup
bullet = pygame.Rect(-10, -10, 5, 10)  # Start off-screen
bullet_speed = 7
bullet_active = False

# Enemy setup
enemies = []
for _ in range(7):
    x = random.randint(0, 460)
    y = random.randint(20, 150)
    enemies.append(pygame.Rect(x, y, 40, 20))

score = 0
font = pygame.font.SysFont(None, 32)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < 500:
        player.x += player_speed

    # Fire bullet
    if keys[pygame.K_SPACE] and not bullet_active:
        bullet.x = player.x + player.width // 2 - bullet.width // 2
        bullet.y = player.y
        bullet_active = True

    # Move bullet
    if bullet_active:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullet_active = False

    # Check collision with enemies
    for enemy in enemies[:]:
        if bullet.colliderect(enemy) and bullet_active:
            enemies.remove(enemy)
            bullet_active = False
            score += 1

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, PLAYER_COLOR, player)
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, enemy)
    if bullet_active:
        pygame.draw.rect(screen, BULLET_COLOR, bullet)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()