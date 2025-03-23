import pygame
import queue
from src.views.map_manager import MapManager
from src.output_manager import OutputManager
from src.input_manager import InputManager
from src.state_manager import StateManager
from src.player_manager import Player, Drone
pygame.init()

class Game:
    def __init__(self, width = 320, height = 256):
        self.width = width
        self.height = height
        self.commands = queue.Queue()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = False
        self.state_manager = StateManager(self)
        self.map_manager = MapManager(self)
        self.output_manager = OutputManager(self)
        self.input_manager = InputManager(self)
        self.player = Player(self, [Drone(True), Drone(True), Drone(True)])

    def update(self, com):




        if "--help" in com:
            self.output_manager.output_help_text()
        elif "Drone:" in com:
            self.player.update(com)
        else:
            self.output_manager.output_unknown_phrase()

        return
    
    def renderer(self):

        ## menu logic
        while not self.running:
            answer = self.input_manager.prompt_list_input()
            if answer["menu"] == "Start New Game":
                # self.input_manager.start_new_game()
                self.running = True

            if answer["menu"] == "About Game":
                self.input_manager.about_game()
            
            if answer["menu"] == "Load Game":
                self.input_manager.load_game()
            
            if answer["menu"] == "Quit Game":
                self.input_manager.quit_game()


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    quit()

            command = input()
            self.commands.put(command)

            com = self.commands.get(False)
        
                    
            self.update(com)

            self.map_manager.render_map()
            self.player.render_player()


            pygame.display.flip()
            self.clock.tick(60)


