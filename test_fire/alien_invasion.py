import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from alien import Alien
from ship import Ship
from button import Button
from game_stats import GameStats
def run_game():
# Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
# Создание корабля.
    ship = Ship(ai_settings, screen)
    aliens = Group()
# Создание группы для хранения пуль.
    bullets = Group()
    aliens.add(Alien(ai_settings,screen))
# Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens,
        bullets)
        if stats.game_active:
            ship.update()
           # bullets.update()
            # Удаление пуль, вышедших за край экрана.
            gf.update_bullets(ai_settings,screen,stats,bullets,aliens)
            gf.update_aliens(ai_settings, aliens)
        #"""Обновляет изображения на экране и отображает новый экран."""
        gf.update_screen(ai_settings, screen, stats, ship, aliens,
             bullets,play_button)
run_game()
