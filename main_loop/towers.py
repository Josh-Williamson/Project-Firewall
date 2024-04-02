import pygame

TOWER_TYPES = 1


class Tower(pygame.sprite.Sprite):
  def __init__(self, pos, image, cost, projectile):
    pygame.sprite.Sprite.__init__(self)
    cost = 0
    projectile = 0
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def draw(self, screen):
      screen.blit(self.image, self.rect)