import sys
import pygame
from background import Background
from pygame.sprite import Group
from player import Player
from puck import Puck
from settings import Settings
import game_functions as gf
from game_stats import GameStats

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Ball game")
    BackGround = Background('background.bmp', [0, 0])
    player = Player(ai_settings,screen)
    pucks = pygame.sprite.Group()
    pucks.add(Puck(ai_settings,screen))
    stats = GameStats(ai_settings)

    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(player)
        if stats.game_active:
            player.update()
            gf.update_screen(BackGround, screen, player, pucks)
            gf.update_puck(ai_settings,stats,screen,player,pucks)
       # Отображение последнего прорисованного экрана.


run_game()