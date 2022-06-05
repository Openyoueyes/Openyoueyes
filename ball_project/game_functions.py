import sys
from puck import Puck
from time import sleep
import pygame
#реагирует на нажатие
def check_keydown_event(event,player):
    if event.key == pygame.K_RIGHT:
    # Переместить корабль вправо.
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
#реагирует на отпускание
def check_keyup_event(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False

def check_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,player)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, player)
def update_puck(ai_settings,stats,screen,player,pucks):
    pucks.update()
    if pygame.sprite.spritecollideany(player, pucks):
        pucks.remove(pucks)
        create_puck(ai_settings,screen,pucks)
    else:
        for puck in pucks.copy():
            if puck.rect.y >= ai_settings.screen_height:
                pucks.remove(pucks)
                create_puck(ai_settings, screen, pucks)
                ship_hit(stats)



def ship_hit(stats):
    #"""Обрабатывает столкновение корабля с пришельцем."""
    # счеттчик ships_left.
    if stats.puck_left != 2:
        stats.puck_left += 1
        print(stats.puck_left)
    else:
        stats.game_active = False





def create_puck(ai_settings, screen,pucks):
    #"""Создает шайбу и размещает его в ряду."""
    puck = Puck(ai_settings, screen)
    puck_width = puck.rect.width
    puck.x = puck_width
    puck.rect.x = puck.x
    pucks.add(Puck(ai_settings, screen))


def update_screen(BackGround,screen,player,pucks):
    screen.fill([255,255,255])
    screen.blit(BackGround.image, BackGround.rect)
    player.blitme()
    pucks.draw(screen)
    pygame.display.flip()
