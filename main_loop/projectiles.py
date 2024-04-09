import pygame
from pygame import Vector2
import json
import math

from enemies import ENEMY_SPRITE_GROUP


PROJECTILE_TYPES = 1

PROJECTILE_IMAGE_LIST = []
PROJECTILE_ATTRIBUTE_LIST = []
PROJECTILE_SPRITE_GROUP = pygame.sprite.RenderUpdates()
PROJECTILE_SPRITE_GROUP.__init__()


class Projectile(pygame.sprite.Sprite):
    def __init__(self, position, type_id, tile_size):
        pygame.sprite.Sprite.__init__(self, PROJECTILE_SPRITE_GROUP)
        self.type_id = type_id
        self.position = position
        self.move_vector = Vector2(0,0)

        attributes = PROJECTILE_ATTRIBUTE_LIST[self.type_id]

        self.name = attributes[0]
        self.damage = attributes[1]
        self.speed = attributes[2] * 0.05  #multiplier for more manageable type/attribute development

        self.tile_size = tile_size
        self.image = PROJECTILE_IMAGE_LIST[self.type_id]
        self.rect = self.getSpriteRect()
        self.rect_center = self.rect.center

    def update(self):
        self.chaseTarget()


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def getSpriteRect(self):
        left = self.position[0]
        top = self.position[1]
        width = self.tile_size * 0.2
        height = self.tile_size * 0.2
        return pygame.Rect(left, top, width, height)

    def chaseTarget(self):
        self.getMovementVector()
        self.position = (
            self.position[0] + self.move_vector[0],
            self.position[1] + self.move_vector[1]
        )


    def getMovementVector(self):
        target_enemy = ENEMY_SPRITE_GROUP.sprites()[0]
        target_point = target_enemy.rect.center
        x_comp = target_point[0] - self.rect_center[0]
        y_comp = target_point[1] - self.rect_center[1]
        raw_vector = pygame.Vector2(x_comp, y_comp)
        self.move_vector = raw_vector.scale_to_length(self.speed)
        return


def loadProjectileImageList(gridmap):
    for x in range(0, PROJECTILE_TYPES + 1):
        image = pygame.image.load(f'assets/projectile/projectile_{x}.png').convert_alpha()
        image = pygame.transform.scale(image, (gridmap.tileSize/4, gridmap.tileSize/4))
        PROJECTILE_IMAGE_LIST.append(image)
    return

def loadProjectileAttributeList():
    file_name = open("sprite_attributes/projectile_attributes.json")
    attributes = json.load(file_name)

    for i in attributes["projectile_attributes"]:
        PROJECTILE_ATTRIBUTE_LIST.append((i["type_id"], i["name"], i["damage"], i["speed"]))
    print(PROJECTILE_ATTRIBUTE_LIST)
