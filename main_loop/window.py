import pygame
from enemy_wave_data import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Window():
    def __init__(self):
        self.level = 1
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.color = pygame.Color(255, 0, 255)
        self.caption = "Project Firewall"
        self.display = pygame.display.set_mode((self.width, self.height))

        self.surface = pygame.surface.Surface([self.width, self.height])

        self.image = self.getBackground(1)
        self.enemy_list = []
        self.spawned_enemies = 0
        self.killed_enemies = 0
        self.missed_enemies = 0

    def updateBackground(self):
        self.display.blit(self.image, (0,0))

    def getBackground(self, level):
        background_image = pygame.image.load(f"assets/backgrounds/{level}.png").convert_alpha()
        image = pygame.transform.scale(background_image, (self.width, self.height))
        return image

    def process_enemies(self):
        enemies = ENEMY_WAVE_DATA[self.level - 1]
        for enemy_type in enemies:
          enemies_to_spawn = enemies[enemy_type]
          for enemy in range(enemies_to_spawn):
            self.enemy_list.append(enemy_type)