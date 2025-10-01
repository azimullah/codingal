import pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Two Rectangles Example")

# Rectangle positions and sizes
rect1 = pygame.Rect(50, 50, 100, 60)      # This one will move
rect2 = pygame.Rect(200, 150, 120, 80)    # This one stays still

speed = 5  # Movement speed

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.x -= speed
    if keys[pygame.K_RIGHT]:
        rect1.x += speed
    if keys[pygame.K_UP]:
        rect1.y -= speed
    if keys[pygame.K_DOWN]:
        rect1.y += speed

    screen.fill((200, 200, 200))  # Fill background with light gray

    # Draw rectangles
    pygame.draw.rect(screen, (255, 0, 0), rect1)   # Movable rectangle (red)
    pygame.draw.rect(screen, (0, 0, 255), rect2)   # Static rectangle (blue)

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit to 60 FPS

pygame.quit()