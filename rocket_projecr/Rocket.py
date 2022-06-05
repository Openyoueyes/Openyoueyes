import pygame
class Rocket():
    def __init__(self, ai_settings, screen):
       # """Инициализирует ракету и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения рокеты и получение прямоугольника.
        self.image = pygame.image.load('/Users/ilaglotov/Desktop/rocket_projecr/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый рокеты появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
       # Сохранение вещественной координаты центра рокеты.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

      # флаг перемещения
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    def update(self):
     if self.moving_right and self.rect.right < self.screen_rect.right:
              self.centerx += self.ai_settings.ship_speed_factor
     if self.moving_left and self.rect.left > 0:
              self.centerx -= self.ai_settings.ship_speed_factor

     if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
              self.centery += self.ai_settings.ship_speed_factor
     if self.moving_up and self.rect.top > 0:
              self.centery -= self.ai_settings.ship_speed_factor
     # Обновление атрибута rect на основании self.center
     self.rect.centerx = self.centerx
     self.rect.centery = self.centery
    def blitme(self):
       #"""Рисует рокету в текущей позиции."""
        self.screen.blit(self.image, self.rect)