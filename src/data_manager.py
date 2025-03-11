class DataManager():
    def __init__(self):
        self.player_manager = None
        self.map_manager = None
        self.puzzle_manager = None
        self.server_save_active = False

    def __local_save(self):
        return
    
    def __server_save(self):
        return
    
    def save_game(self):
        if self.server_save_active:
            self.__local_save()
            self.__server_save()
        else:
            self.__local_save()