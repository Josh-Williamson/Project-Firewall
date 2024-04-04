import pygame
from pygame import Vector2

PROJECTILE_TYPES = 1

PROJECTILE_IMAGE_LIST = []
PROJECTILE_SPRITE_GROUP = pygame.sprite.RenderUpdates()
PROJECTILE_SPRITE_GROUP.__init__()



class Projectile(pygame.sprite.Sprite):
    def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.position = (0, 0)
      self.velocity = (0, 0)
      self.damage = 0
      self.speed = 0
      self.type_id = 0
      self.vector = Vector2(0, 0)
      self.image = PROJECTILE_IMAGE_LIST[self.type_id]
      self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def loadProjectileImageList(gridmap):
    for x in range(0, 1):
      image = pygame.image.load(f'assets/projectile/projectile_{x}.png').convert_alpha()
      image = pygame.transform.scale(image, (gridmap.tileSize, gridmap.tileSize))
      PROJECTILE_IMAGE_LIST.append(image)
      return