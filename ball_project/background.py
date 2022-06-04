import pygame
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load('/Users/ilaglotov/Desktop/ball_project/background.bmp')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location