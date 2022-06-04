import sys

import pygame
from settings import Settings
from Rocket import Rocket

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Rocket project")
    bg_color = (255,168,0)
    rocket = Rocket(ai_settings,screen)
# запуск основного цикла игры
    while True:
    # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
             sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = True
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = False
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
        rocket.update()
        screen.fill(ai_settings.bg_color)
        rocket.blitme()
    # Отображение последнего прорисованного экрана.
        pygame.display.flip()
run_game()
