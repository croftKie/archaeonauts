import random
import pygame
class MapManager():
    def __init__(self, game):
        self.game = game
        self.tile_size = 64
        self.tilemap = [[0,0,0,1,1], [1,0,1,1,1], [1,0,1,0,1], [1,1,1,0,0]]
        self.tile_one = pygame.image.load("./assets/hidden.png")
        self.tile_two = pygame.image.load("./assets/visible.png")

    def tilemap_generator():
        
        return
    

    def render_map(self):
        for i, r in enumerate(self.tilemap):
            for j, c in enumerate(r):
                x = j * self.tile_size
                y = i * self.tile_size
                if c == 0:
                    self.game.screen.blit(self.tile_one, (x,y))
                elif c == 1:
                    self.game.screen.blit(self.tile_two, (x, y))

