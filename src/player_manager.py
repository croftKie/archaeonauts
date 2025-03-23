import pygame
class Player:
    def __init__(self, game, drones):
        self.game = game
        self.level = 0
        self.drones = drones
        self.stats = {
            "reputation": 0,
            "knowledge": 0,
            "creds": 0
        }
        self.active_drone = drones[0]
        self.sprite = pygame.image.load("./assets/ship_E.png")
        self.position_x = 0
        self.position_y = 0

    def update(self, com):
        x = 0
        y = 0
        if "left" in com:
            x = -64
        
        if "right" in com:
            x = 64

        if "up" in com:
            y = -64

        if "down" in com:
            y = 64

        new_pos_x = self.position_x + x
        new_pos_y = self.position_y + y

        if new_pos_x < 0 or new_pos_y < y:
            return
        else:
            self.position_x = new_pos_x
            self.position_y = new_pos_y

    def render_player(self):
        self.game.screen.blit(self.sprite, (self.position_x, self.position_y))


class Drone:
    def __init__(self, isActive):
        self.isActive: isActive
        self.activeFeatures: []
        self.features: []

class DroneFeature:
    def __init__(self, name):
        self.name = name
        self.isActive = False
        self.isUnlocked = False
        self.desc = ""