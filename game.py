import pygame, sys
from button import Button

pygame.init()

# Set screen resolution
SCREEN = pygame.display.set_mode((800,600))
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


JUMPSCARE_IMG = pygame.image.load("assets/Brimley.png")
JUMPSCARE_IMG = pygame.transform.scale(JUMPSCARE_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))

def trigger_jumpscare():
    if JUMPSCARE_IMG:
        SCREEN.blit(JUMPSCARE_IMG, (0, 0))
    else:
        SCREEN.fill(RED)
        
    pygame.display.update()
    pygame.time.delay(2000)

def game():
    # Records Time
    ticks = pygame.time.get_ticks()

    # Set up the player
    player_x = 30
    player_y = 150
    player_size = 25
    speed = 3

    # Set up the enemy
    enemy_x = 30
    enemy_y = 20
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
        pygame.Rect(600, 425, 20, 100),
        pygame.Rect(600, 425, 100, 20),
        pygame.Rect(680, 500, 100, 20),
        pygame.Rect(520, 525, 100, 20),
        pygame.Rect(520, 495, 20, 30),
        pygame.Rect(680, 425, 100, 20),
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
                        trigger_jumpscare()
                        pygame.display.flip()
                        running = False
                if not lever_activated:
                    for o_walls in orange_walls:
                        if player.colliderect(o_walls):
                            font = pygame.font.SysFont(None, 48)
                            message = font.render("YOU LOSE!", True, RED)
                            screen.blit(message, (220, 180))
                            trigger_jumpscare()
                            pygame.display.flip()
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
                        trigger_jumpscare()
                        pygame.display.flip()
                        running = False
                if not lever_activated:
                    for o_walls in orange_walls:
                        if player.colliderect(o_walls):
                            font = pygame.font.SysFont(None, 48)
                            message = font.render("YOU LOSE!", True, RED)
                            screen.blit(message, (220, 180))
                            trigger_jumpscare()
                            pygame.display.flip()
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
                        trigger_jumpscare()
                        pygame.display.flip()
                        running = False
                if not lever_activated:
                        for o_walls in orange_walls:
                            if player.colliderect(o_walls):
                                font = pygame.font.SysFont(None, 48)
                                message = font.render("YOU LOSE!", True, RED)
                                screen.blit(message, (220, 180))
                                trigger_jumpscare()
                                pygame.display.flip()
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
                        trigger_jumpscare()
                        pygame.display.flip()
                        running = False
                if not lever_activated:
                    for o_walls in orange_walls:
                        if player.colliderect(o_walls):
                            font = pygame.font.SysFont(None, 48)
                            message = font.render("YOU LOSE!", True, RED)
                            screen.blit(message, (220, 180))
                            trigger_jumpscare()
                            pygame.display.flip()
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
                trigger_jumpscare()
                pygame.display.flip()
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

#Play screen used youtube video, https://youtu.be/GMBqjxcKogA?si=cQ57FwoG5ois49VM
BG = pygame.image.load("assets/Background.png")
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    pygame.display.set_caption("Play")

    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    pygame.display.set_caption("Options")

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill(BLACK)

        OPTIONS_TEXT = get_font(45).render("Coming Soon.", True, (WHITE))
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(420, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640,460),
                            text_input="BACK", font=get_font(40), base_color="WHITE", hovering_color="GREEN")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        SCREEN.blit(BG, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("MAIN MENU", True,"#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 225),
                            text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="WHITE")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 375),
                            text_input="OPTIONS", font=get_font(50), base_color="#d7fcd4", hovering_color="WHITE")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 525),
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="WHITE")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
main_menu()
