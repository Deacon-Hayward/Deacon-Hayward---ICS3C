import pygame

pygame.init()

# Set screen resolution
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Set up colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
SKYBLUE = (135, 206, 235)
ORANGE = (255, 165, 0)

# Records Time
ticks = pygame.time.get_ticks()

# Set up the player
player_x = 30
player_y = 100
player_size = 25
speed = 3

# Set up the enemy
enemy_x = 30
enemy_y = 30
enemy_size = 25
enemy_speed = 1.5

# Create the exit
exit_rect = pygame.Rect(740, 540, 30, 30)

# Create the lever
lever_rect = pygame.Rect(47, 525, 30, 30)
lever_activated = False


# Create the maze walls
walls = [
    #outside walls
    pygame.Rect(0, 0, 800, 20),
    pygame.Rect(0, 580, 800, 20),
    pygame.Rect(0, 0, 20, 600),
    pygame.Rect(780, 0, 20, 600),

    #inside walls
    pygame.Rect(75, 100, 200, 20),
    pygame.Rect(375, 100, 200, 20),
    pygame.Rect(75, 200, 100, 20),
    pygame.Rect(175, 200, 20, 100),
    pygame.Rect(100, 375, 100, 20),
    pygame.Rect(100, 375, 20, 140),
    pygame.Rect(20, 300, 300, 20),
    pygame.Rect(100, 500, 200, 20),
    pygame.Rect(300, 300, 20, 125),
    pygame.Rect(270, 425, 50, 20),
    pygame.Rect(185, 375, 20, 50),
    pygame.Rect(260, 200, 150, 20),
    pygame.Rect(400, 200, 20, 150),
    pygame.Rect(400, 425, 20, 175),
    pygame.Rect(400, 425, 125, 20),
    pygame.Rect(505, 175, 20, 250),
    pygame.Rect(225, 550, 20, 50),
    pygame.Rect(475, 15, 20, 100),
    pygame.Rect(575, 75, 20, 200),
    pygame.Rect(575, 275, 100, 20),
    pygame.Rect(675, 145, 20, 150),
    pygame.Rect(675, 275, 50, 20),
    pygame.Rect(525, 350, 100, 20),
]

# Walls lever opens
orange_walls = [
    pygame.Rect(505, 120, 20, 75)
]

# Set up the game
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
running = True
won = False
game_over = False
final_time_text = ""

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
            #
            for wall in walls:
                if player.colliderect(wall):
                    font = pygame.font.SysFont(None, 48)
                    message = font.render("YOU LOSE!", True, RED)
                    screen.blit(message, (220, 180))
                    pygame.display.flip()
                    pygame.time.wait (2000)
                    running = False
            if not lever_activated:
                for o_walls in orange_walls:
                    if player.colliderect(o_walls):
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
            if not lever_activated:
                for o_walls in orange_walls:
                    if player.colliderect(o_walls):
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
            if not lever_activated:
                    for o_walls in orange_walls:
                        if player.colliderect(o_walls):
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
            if not lever_activated:
                for o_walls in orange_walls:
                    if player.colliderect(o_walls):
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

        # Enemy wall collison
        old_enemy_x = enemy_x
        if enemy_x < player_x:
            enemy_x += enemy_speed
        elif enemy_x > player_x:
            enemy_x -= enemy_speed

        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
        for wall in walls:
            if enemy_rect.colliderect(wall):
                enemy_x = old_enemy_x


        old_enemy_y = enemy_y
        if enemy_y < player_y:
            enemy_y += enemy_speed
        elif enemy_y > player_y:
            enemy_y -= enemy_speed

        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
        for wall in walls:
            if enemy_rect.colliderect(wall):
                enemy_y = old_enemy_y

        # Check if the player touches the enemy
        if player.colliderect(enemy_rect):
            enemy_y -= enemy_speed
            font = pygame.font.SysFont(None, 48)
            message = font.render("YOU LOSE!", True, RED)
            screen.blit(message, (220, 180))
            pygame.display.flip()
            pygame.time.wait (2000)
            running = False

        # Check if the player reaches the lever
        if player.colliderect(lever_rect):
            lever_activated = True

        # Check if the player reaches the exit
        if player.colliderect(exit_rect):
            won = True

    # Draw the background
    screen.fill(SKYBLUE)

    #  Blue walls
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

    # Orange walls if lever is not flipped
    if not lever_activated:
        for o_walls in orange_walls:
            pygame.draw.rect (screen, ORANGE, o_walls)
        

    # Draw the exit
    pygame.draw.rect(screen, GREEN, exit_rect)

    # Draw the lever if not activated
    if not lever_activated:
        pygame.draw.rect(screen, ORANGE, lever_rect)

    # Draw the player and enemy
    player = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, RED, player)
    enemy = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    pygame.draw.rect(screen, BLACK, enemy)

    # Calculate and display timer
    if not won and not game_over:
        time_passed = (pygame.time.get_ticks() - ticks) // 1000
        minutes = time_passed // 60
        seconds = time_passed % 60
        timer_text = f"Time: {minutes:02d}:{seconds:02d}"
        final_time_text = timer_text
    else:
        timer_text = final_time_text

    text_surface = font.render(timer_text, True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))

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
