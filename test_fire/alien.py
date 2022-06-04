import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
#"""Класс, представляющий одного пришельца."""
    def __init__(self, ai_settings, screen):
#"""Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
# Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('/Users/ilaglotov/Desktop/test_fire/images/target1.bmp').convert()
        self.image.set_colorkey((255,255,255))
        self.image.set_colorkey((254,254,254))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
# Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.right = self.screen_rect.right
        self.rect.y = randint(0,705)
 # Сохранение точной позиции пришельца.
        self.y = float(self.rect.y)


    def check_edges(self):
    #"""Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def update(self):
        self.y += (self.ai_settings.alien_speed_factor *
            self.ai_settings.fleet_direction)
        self.rect.y = self.y

    def blitme(self):
 # """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)


