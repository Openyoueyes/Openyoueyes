import pygame
class Ship():
    def __init__(self, ai_settings, screen):
#"""Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings
# Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load(
            '/Users/ilaglotov/Desktop/test_fire/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
# Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centery = self.screen_rect.centery
        self.center = float(self.rect.centery)
    # Флаг перемещени
        self.moving_up = False
        self.moving_down = False
    def update(self):
       #Обновляется атрибут center, не rect.
        if self.moving_up and self.rect.top > 0:
           self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor

 # Обновление атрибута rect на основании self.center.
        self.rect.centery = self.center


    def blitme(self):
#"""Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)