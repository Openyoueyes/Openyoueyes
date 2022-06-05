import sys
import pygame
from drop import Drop
from settings import Settings

class DropGame():
    def __init__(self):
# Инициализирует игру и создает объект экрана.
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Project Drops")
        self.drops = pygame.sprite.Group()
        self.create_fleet()

    def run_game(self):
# Запуск основного цикла программы.
        while True:
            self.check_events()
            self.update_drops()
            self.update_screen()

    def create_fleet(self):
        # Создает ряд капель
        # Создание капли и вычисление количества пкапель в ряду.
        drop = Drop(self)
        drop_width,drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - (2 * drop_width)
        number_drops_x = available_space_x // (2 * drop_width)

        available_space_y = self.settings.screen_height - (2 * drop_height)
        number_rows = available_space_y // (2 * drop_height)
        # Создание флота пришельцев.
        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self.create_drop(drop_number,row_number)
    def create_row(self):
        drop = Drop(self)
        drop_width,drop_height = drop.rect.size
        available_space_x = self.settings.screen_width - (2 * drop_width)
        number_drops_x = available_space_x // (2 * drop_width)

        available_space_y = self.settings.screen_height - (2 * drop_height)
        number_rows = available_space_y // (2 * drop_height)

        # Создание флота пришельцев.
        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self.create_drop(drop_number,0)

    def create_drop(self, drop_number, row_number):
        drop = Drop(self)
        drop_width = drop.rect.width
        drop.x = drop_width + 2 * drop_width * drop_number
        drop.rect.x = drop.x
        drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number
        drop.y = drop.rect.height + 2 * drop.rect.height * row_number
        drop.rect.y = drop.y
        self.drops.add(drop)

    def update_drops(self):
        # Обновляет позиции всех капель в ряду.
        self.check_fleet_edges()
        self.drops.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def update_screen(self):
        # Обновляет изображения на экране и отображает новый экран."""
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

    def check_fleet_edges(self):
        # Реагирует на достижение капли края экрана."""
        flag = False
        for drop in self.drops.sprites():
            if drop.check_edges():
                drop.remove(self.drops)
                flag = True
        if flag:
            self.create_row()
            print("new drop create")

sg = DropGame()
sg.run_game()