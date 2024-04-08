import pygame

BASE_SPRITE_GROUP = pygame.sprite.RenderUpdates()
BASE_SPRITE_GROUP.__init__()
class Base(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, BASE_SPRITE_GROUP)
        self.hp = 10

    def get_hp(self):
        return self.hp

    def update(self, damage):
        self.hp -= damage
        return


