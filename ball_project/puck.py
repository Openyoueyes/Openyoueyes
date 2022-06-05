import pygame
from random import randint
class Puck(pygame.sprite.Sprite):
#"""Класс, представляющий одного пришельца."""
    def __init__(self, ai_settings, screen):
#"""Инициализирует пришельца и задает его начальную позицию."""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.ai_settings = ai_settings
# Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('/Users/ilaglotov/Desktop/ball_project/hockey_puck.bmp')
        self.image.set_colorkey((145, 193, 218))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #self.add(group)
# Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.screen_rect.top
        self.rect.y = self.screen_rect.top
        self.rect.x = randint(0,740)

           # Сохранение точной позиции пришельца.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def update(self):
        if self.y < self.screen_rect.bottom:
            self.y += self.ai_settings.puck_speed_factor
            self.rect.y = self.y

    def blitme(self):
 #          """Выводит пришельца в текущем положении."""
        self.screen.blit(self.image, self.rect)