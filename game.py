import pygame

pygame.init()

# Set screen resolution
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Set up colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Set up the player
player_x = 30
player_y = 100
player_size = 25
speed = 3

# Set up the enemy
enemy_x = 30
enemy_y = 5
enemy_size = 25
enemy_speed = 1

# Create the exit
exit_rect = pygame.Rect(540, 340, 30, 30)

# Create the maze walls
walls = [
    pygame.Rect(100, 0, 20, 300),
    pygame.Rect(200, 100, 20, 300),
    pygame.Rect(300, 0, 20, 250),
    pygame.Rect(400, 100, 20, 300),
    pygame.Rect(500, 0, 20, 250)
]

# Set up the game
clock = pygame.time.Clock()
running = True
won = False

# Main game loop
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    if not won:

        # Move left
        if keys[pygame.K_LEFT]:
            player_x -= speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            for wall in walls:
                if player.colliderect(wall):
                    font = pygame.font.SysFont(None, 48)
                    message = font.render("YOU LOSE!", True, RED)
                    screen.blit(message, (220, 180))
                    pygame.display.flip()
                    pygame.time.wait (2000)
                    running = False
        # Move right
        if keys[pygame.K_RIGHT]:
            player_x += speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            for wall in walls:
                if player.colliderect(wall):
                    font = pygame.font.SysFont(None, 48)
                    message = font.render("YOU LOSE!", True, RED)
                    screen.blit(message, (220, 180))
                    pygame.display.flip()
                    pygame.time.wait (2000)
                    running = False


        # Move up
        if keys[pygame.K_UP]:
            player_y -= speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            for wall in walls:
                if player.colliderect(wall):
                    font = pygame.font.SysFont(None, 48)
                    message = font.render("YOU LOSE!", True, RED)
                    screen.blit(message, (220, 180))
                    pygame.display.flip()
                    pygame.time.wait (2000)
                    running = False

        # Move down
        if keys[pygame.K_DOWN]:
            player_y += speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            for wall in walls:
                if player.colliderect(wall):
                    font = pygame.font.SysFont(None, 48)
                    message = font.render("YOU LOSE!", True, RED)
                    screen.blit(message, (220, 180))
                    pygame.display.flip()
                    pygame.time.wait (2000)
                    running = False

        # Keep the player inside the screen
        if player_x < 0:
            player_x = 0

        if player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size

        if player_y < 0:
            player_y = 0

        if player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size

        # Update the player rectangle
        player = pygame.Rect(player_x, player_y, player_size, player_size)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
        # Check if the player touches the enemy
        if player.colliderect(enemy_rect):
            font = pygame.font.SysFont(None, 48)
            message = font.render("YOU LOSE!", True, RED)
            screen.blit(message, (220, 180))
            pygame.display.flip()
            pygame.time.wait (2000)
            running = False

        # Makes enemy collide with wall
        if enemy_x < player_x:
            enemy_x += enemy_speed
        elif enemy_x > player_x:
            enemy_x -= enemy_speed
        if enemy_y < player_y:
            enemy_y += enemy_speed
        elif enemy_y < player_y:
            enemy_y -= enemy_speed
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_speed)
    for wall in walls:
        if enemy_rect.colliderect(wall):
            enemy_y = enemy_x


        # Makes enemy chase player
    if enemy_x < player_x:         
        enemy_x += enemy_speed     
    elif enemy_x > player_x:         
        enemy_x -= enemy_speed     
    if enemy_y < player_y:         
        enemy_y += enemy_speed     
    elif enemy_y > player_y:         
        enemy_y -= enemy_speed  

        # Check if the player reaches the exit
        if player.colliderect(exit_rect):
            won = True

    # Draw the background
    screen.fill(WHITE)

    # Draw the maze walls
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

    # Draw the exit
    pygame.draw.rect(screen, GREEN, exit_rect)

    # Draw the player and enemy
    player = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, RED, player)
    enemy = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    pygame.draw.rect(screen, BLACK, enemy)

    # Display the winning message
    if won:
        font = pygame.font.SysFont(None, 48)
        message = font.render("YOU WIN!", True, GREEN)
        screen.blit(message, (220, 180))
        


    # Update the display
    pygame.display.flip()

    # Limit the game to 60 FPS
    clock.tick(60)

# Close Pygame
pygame.quit()