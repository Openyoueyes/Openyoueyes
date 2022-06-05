import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,ai_settings,screen):
        pygame.sprite.Sprite.__init__(self)
#"""Инициализирует и и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings
# Загрузка изображения игрока и получение прямоугольника.
        self.image = pygame.image.load('/Users/ilaglotov/Desktop/ball_project/player_helm.bmp').convert_alpha()
        self.image.set_colorkey((145, 191, 218))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
# Каждый новый игрок появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
    # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
    def update(self):
       #Обновляется атрибут center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.player_speed_factor
        if self.moving_left and self.rect.left >0:
            self.rect.centerx -= self.ai_settings.player_speed_factor
 # Обновление атрибута rect на основании self.center.

    def blitme(self):
#"""Рисует игрока в текущей позиции."""
        self.screen.blit(self.image, self.rect)