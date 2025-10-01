import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Change Rectangle Colors")

rect1 = pygame.Rect(50, 50, 100, 60)
rect2 = pygame.Rect(200, 150, 120, 80)

color1 = (255, 0, 0)   # Start with red
color2 = (0, 0, 255)   # Start with blue

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Change colors on key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Swap colors when space is pressed
                color1, color2 = color2, color1
            if event.key == pygame.K_c:
                # Set random colors when 'c' is pressed
                import random
                color1 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    screen.fill((200, 200, 200))
    pygame.draw.rect(screen, color1, rect1)
    pygame.draw.rect(screen, color2, rect2)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()