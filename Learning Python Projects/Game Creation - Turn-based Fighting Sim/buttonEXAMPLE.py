###example buttons in pygame code:


import pygame


pygame.init()

display_width= 1280
display_height = 720

gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

# Use uppercase names for constants that should never be changed.
DARK_GRAY = pygame.Color('gray13')
BACKGROUND1 = pygame.Surface((display_width, display_height))
BACKGROUND1.fill((30, 150, 90))
BACKGROUND2 = pygame.Surface((display_width, display_height))
BACKGROUND2.fill((140, 50, 0))
BACKGROUND3 = pygame.Surface((display_width, display_height))
BACKGROUND3.fill((0, 80, 170))

states = {
    'scene1': {'background': BACKGROUND1, 'left_scene': 'scene2', 'right_scene': 'scene3'},
    'scene2': {'background': BACKGROUND2, 'left_scene': 'scene1', 'right_scene': 'scene3'},
    'scene3': {'background': BACKGROUND3, 'left_scene': 'scene1', 'right_scene': 'scene2'},
    }

def game_loop():
    # The buttons are just pygame.Rects.
    left_button = pygame.Rect(440, 450, 60, 40)
    right_button = pygame.Rect(740, 450, 60, 40)
    # The current_scene is a dictionary with the relevant data.
    current_scene = states['scene1']

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the left button is clicked we switch to the 'left_scene'
                # in the `current_scene` dictionary.
                if left_button.collidepoint(event.pos):
                    current_scene = states[current_scene['left_scene']]
                    print(current_scene)
                # If the right button is clicked we switch to the 'right_scene'.
                elif right_button.collidepoint(event.pos):
                    current_scene = states[current_scene['right_scene']]
                    print(current_scene)

        # Blit the current background.
        gameDisplay.blit(current_scene['background'], (0, 0))
        # Always draw the button rects.
        pygame.draw.rect(gameDisplay, DARK_GRAY, left_button)
        pygame.draw.rect(gameDisplay, DARK_GRAY, right_button)
        pygame.display.update()
        clock.tick(30)  # 30 FPS feels more responsive.


game_loop()
pygame.quit()