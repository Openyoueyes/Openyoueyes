class Settings():  
       #"""Класс для хранения всех настроек игры Alien Invasion."""
       def __init__(self):
           #"""Инициализирует настройки игры."""
           # Параметры экрана
           self.screen_width = 1024
           self.screen_height = 768
           self.bg_color = (230,230,230)
           #параметры карабля
           self.ship_speed_factor = 4.5
           self.bullet_limit = 2
           # Параметры пули
           self.bullet_speed_factor = 7
           self.bullet_width = 15
           self.bullet_height = 3
           self.bullet_color = 60, 60, 60
           self.bullets_allowed = 3
           #настройки пришельцев
           self.alien_speed_factor = 7
           self.fleet_drop_speed = 10
           # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
           self.fleet_direction = 1
