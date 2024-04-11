import json

import pygame
from pygame import Vector2

from enemies import ENEMY_SPRITE_GROUP

PROJECTILE_TYPES = 1

PROJECTILE_IMAGE_LIST = []
PROJECTILE_ATTRIBUTE_LIST = []
PROJECTILE_SPRITE_GROUP = pygame.sprite.RenderUpdates()
PROJECTILE_SPRITE_GROUP.__init__()


class Projectile(pygame.sprite.Sprite):
    def __init__(self, position, type_id, tile_size, target, range):
        pygame.sprite.Sprite.__init__(self, PROJECTILE_SPRITE_GROUP)
        self.type_id = type_id
        self.spawn_position = position
        self.position = position
        self.position_vector = Vector2(position[0], position[1])

        attributes = PROJECTILE_ATTRIBUTE_LIST[self.type_id]

        self.name = attributes[1]
        self.damage = attributes[2]
        self.speed = attributes[3] / 60  # division for per second values in attribute JSON

        self.range = range
        self.target = target
        self.tile_size = tile_size
        self.image = PROJECTILE_IMAGE_LIST[self.type_id]
        self.rect = self.getSpriteRect()

    def update(self):
        if len(ENEMY_SPRITE_GROUP) == 0:
            self.kill()
            return
        if self.position_vector.distance_to(self.spawn_position) >= self.range:
            self.kill()
            return
        self.chaseTarget()
        self.rect = self.getSpriteRect()

    def getDamage(self):
        return int(self.damage)

    def getSpriteRect(self):
        left = self.position[0]
        top = self.position[1]
        width = self.tile_size * 0.2
        height = self.tile_size * 0.2
        return pygame.Rect(left, top, width, height)

    def chaseTarget(self):
        self.getMovementVector()
        self.position = (self.position_vector[0], self.position_vector[1])

    def getMovementVector(self):
        target_enemy = self.target
        target_point = target_enemy.rect.center
        self.position_vector = self.position_vector.move_towards(target_point, self.speed)
        return


def loadProjectileImageList(gridmap):
    for x in range(0, PROJECTILE_TYPES + 1):
        image = pygame.image.load(f'assets/projectile/projectile_{x}.png').convert_alpha()
        image = pygame.transform.scale(image, (gridmap.tileSize * 0.2, gridmap.tileSize / 4))
        PROJECTILE_IMAGE_LIST.append(image)
    return

def loadProjectileAttributeList():
    file_name = open("sprite_attributes/projectile_attributes.json")
    attributes = json.load(file_name)

    for i in attributes["projectile_attributes"]:
        PROJECTILE_ATTRIBUTE_LIST.append((i["type_id"], i["name"], i["damage"], i["speed"]))
    print("PROJECTILE_ATTRIBUTE_LIST: ", PROJECTILE_ATTRIBUTE_LIST)
