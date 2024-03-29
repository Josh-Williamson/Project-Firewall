import pygame

class Projectile(pygame.sprite.Sprite):
  def __init__(self, pos, image, damage, speed):
    pygame.sprite.Sprite.__init__(self)
    damage = 0
    speed = 0
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def draw(self, screen):
      screen.blit(self.image, self.rect)
