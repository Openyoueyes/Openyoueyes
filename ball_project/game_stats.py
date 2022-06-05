class GameStats():
   # """Отслеживание статистики для игры Ball project."""
    def __init__(self, ai_settings):
       # """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_stats()


    def reset_stats(self):
   # """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.puck_left = self.ai_settings.fault_limit
        self.game_active = True