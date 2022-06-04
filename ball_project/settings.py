import pygame
class Settings():
    #"""Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
       # """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        #self.image = pygame.image.load('/Users/ilaglotov/Desktop/ball_project/background.bmp')
        self.bg_color = (145, 193, 218)
        #настройки игрока
        self.player_speed_factor = 3
        self.puck_speed_factor = 5
        self.fault_limit = 0


