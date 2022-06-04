import pygame
from pygame.sprite import Sprite
class Drop(Sprite):
#Класс, представляющий одну каплю.
    def __init__(self, sg_game):
#Инициализирует каплю и задает ее начальную позицию.
        super().__init__()
        self.screen = sg_game.screen
        self.settings = sg_game.settings
# Загрузка изображения капли и назначение атрибута rect.
        self.image = pygame.image.load('/Users/ilaglotov/Desktop/drop_Project/image/drop.bmp')
        self.rect = self.image.get_rect()
# Каждый новая капля появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
 # Сохранение точной позиции капли.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
   #Перемещает  капли вниз."""
        self.y += self.settings.drop_speed_factor
        self.rect.y = self.y



    def check_edges(self):
    #"""Возвращает True, если капли находятся внизу экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True


