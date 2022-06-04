import sys
from alien import Alien
import pygame
from bullet import Bullet
from time import sleep
def check_events(ai_settings, screen, stats, play_button, ship, aliens,
        bullets):
  # """Обрабатывает нажатия клавиш и события мыши."""
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
         sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        check_play_button(ai_settings, screen, stats, play_button, ship,
        aliens, bullets, mouse_x, mouse_y)
    elif event.type == pygame.KEYDOWN:
         check_keydown_events(event, ai_settings, screen,stats, ship, aliens,bullets)
    elif event.type == pygame.KEYUP:
         check_keyup_events(event, ship)
def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
           bullets, mouse_x, mouse_y):
   # """Запускает новую игру при нажатии кнопки Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, aliens,
            bullets)

def start_game(ai_settings, screen, stats, aliens,bullets):
    pygame.mouse.set_visible(False)
    # Сброс игровой статистики.
    stats.reset_stats()
    stats.game_active = True
    # Очистка списков пришельцев и пуль.
    aliens.empty()
    bullets.empty()
    create_alien(ai_settings, screen, aliens)

def bullets_hit(stats):
  #  """Обрабатывает столкновение корабля с пришельцем."""
    # Уменьшение ships_left.
    if stats.bullets_left > 0:
      stats.bullets_left -= 1
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    # Очистка списков пришельцев и пуль.


def check_keydown_events(event, ai_settings, screen,
                         stats, ship, aliens,bullets):
#"""Реагирует на нажатие клавиш."""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    # Создание новой пули и включение ее в группу bullets.
    elif event.key == pygame.K_p:
        start_game(event,ai_settings, screen, stats, aliens,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
#"""Реагирует на отпускание клавиш."""
   if event.key == pygame.K_UP:
      ship.moving_up = False
   elif event.key == pygame.K_DOWN:
      ship.moving_down = False


def update_bullets(ai_settings,screen,stats,bullets,aliens):
   # """Обновляет позиции пуль и уничтожает старые пули."""
    # Обновление позиций пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left >= ai_settings.screen_width:
            bullets.remove(bullet)
            bullets_hit(stats)
    check_bullet_alien_collisions(ai_settings, screen,aliens, bullets)



def check_bullet_alien_collisions(ai_settings, screen,aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
    # Уничтожение существующих пуль и создание нового флота.
        create_alien(ai_settings, screen, aliens)
def create_alien(ai_settings, screen,aliens):
    #"""Создает шайбу и размещает его в ряду."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width
    alien.rect.x = alien.x
    aliens.add(Alien(ai_settings, screen))

def check_alien_edges(ai_settings, aliens):
 #   """Реагирует на достижение пришельцем края экрана."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_alien_direction(ai_settings)
            break

def change_alien_direction(ai_settings):
  #  """Опускает весь флот и меняет направление флота."""
        ai_settings.fleet_direction *= -1


def update_aliens(ai_settings,aliens):
   # """Обновляет позиции всех пришельцев во флоте."""
   check_alien_edges(ai_settings, aliens)
   aliens.update()





def update_screen(ai_settings, screen, stats, ship, aliens, bullets,
           play_button):
#"""Обновляет изображения на экране и отображает новый экран."""
# При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
           play_button.draw_button()
# Отображение последнего прорисованного экрана.
    pygame.display.flip()
