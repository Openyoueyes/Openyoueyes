import sys

import pygame

from drop import Drop

def get_number_rows(ai_settings, drop_height):
    #Определяет количество рядов, помещающихся на экране."""
    available_space_y = (ai_settings.screen_height -  (3 * drop_height))
    number_rows = int(available_space_y / (2 * drop_height))
    return number_rows

def get_number_drops_x(ai_settings, drop_width):
    #"""Вычисляет количество пришельцев в ряду."""
    available_space_x = ai_settings.screen_width - 2 * drop_width
    number_drops_x = int(available_space_x / (2 * drop_width))
    return number_drops_x
def create_drop(ai_settings, screen, drops, drop_number,row_number):
    #Создает каплю и размещает ее в ряду."""
    drop = Drop(ai_settings, screen)
    drop_width = drop.rect.width
    drop.x = drop_width + 2 * drop_width * drop_number
    drop.rect.x = drop.x
    drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number
    drop.y = drop.rect.height + 2 * drop.rect.height * row_number
    drop.rect.y = drop.y
    drops.add(drop)


def check_keydown_events(event):
    #Реагирует на нажатие клавиш."""
   if event.key == pygame.K_q:
      sys.exit()

def check_events(ai_settings, screen):
    #Обрабатывает нажатия клавиш и события мыши."""
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
      elif event.type == pygame.KEYDOWN:
         check_keydown_events(event, ai_settings, screen)


def update_screen(ai_settings, screen,drops):
    # Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
   screen.fill(ai_settings.bg_color)
   drops.draw(screen)
# Отображение последнего прорисованного экрана.
   pygame.display.flip()

def check_fleet_edges(ai_settings,drops):
#Реагирует на достижение капли края экрана."""
    flag = False
    for drop in drops.sprites():
        if drop.check_edges():
           drop.remove(drops)
           flag = True
    if flag:
        create_drop()
        print("new drop create")


def update_drops(ai_settings,drops):
#Обновляет позиции всех капель в ряду.
    check_fleet_edges(ai_settings,drops)
    drops.update()
