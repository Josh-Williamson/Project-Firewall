import json
import math

import pygame

from enemies import ENEMY_SPRITE_GROUP
from projectiles import Projectile

TOWER_TYPES = 1
TOWER_IMAGE_LIST = []
TOWER_ATTRIBUTE_LIST = []

TOWER_SPRITE_GROUP = pygame.sprite.RenderUpdates()
TOWER_SPRITE_GROUP.__init__()


class Tower(pygame.sprite.Sprite):

    def __init__(self, truepos, type_id, tile_size):
        pygame.sprite.Sprite.__init__(self, TOWER_SPRITE_GROUP)

        self.type_id = type_id
        self.truepos = truepos

        attributes = TOWER_ATTRIBUTE_LIST[type_id]

        self.cost = attributes[1]
        self.fire_rate = attributes[2]
        self.range = attributes[3] * tile_size

        self.shot_timer = 0
        self.tile_size = tile_size
        self.image = TOWER_IMAGE_LIST[type_id]
        self.rect = self.getSpriteRect()

    def getSpriteRect(self):
        left = self.truepos[0]
        top = self.truepos[1]
        width = self.tile_size
        height = self.tile_size
        return pygame.Rect(left, top, width, height)

    def update(self):
        target = self.checkEnemyInRange()
        if target is not None and self.fireRateTimer():
            self.createProjectile(target)
            return

    # iterated from the oldest (furthest along) to newest enemy, break at first in range
    # which should maintain targeting on the furthest along that is still in range
    def checkEnemyInRange(self):
        if len(ENEMY_SPRITE_GROUP) == 0:
            return None
        tower_center = self.rect.center
        for enemy in ENEMY_SPRITE_GROUP:
            enemy_center = enemy.rect.center
            diff_x = enemy_center[0] - tower_center[0]
            diff_y = enemy_center[1] - tower_center[1]
            if math.hypot(diff_x, diff_y) <= self.range:
                return enemy

    def fireRateTimer(self):
        self.shot_timer += 1
        if self.shot_timer < self.fire_rate:
            return False
        elif self.shot_timer >= self.fire_rate:
            self.shot_timer = 0
            return True

    def createProjectile(self, target):
        Projectile(self.rect.center, self.type_id, self.tile_size, target, self.range)


def loadTowerImageList(gridmap):
    for x in range(TOWER_TYPES+1):
        image = pygame.image.load(f'assets/tower/tower_{x}.png').convert_alpha()
        image = pygame.transform.scale(image, (gridmap.tileSize, gridmap.tileSize))
        TOWER_IMAGE_LIST.append(image)
    return

def loadTowerAttributeList():
    file_name = open("sprite_attributes/tower_attributes.json")
    attributes = json.load(file_name)

    for i in attributes["tower_attributes"]:
        TOWER_ATTRIBUTE_LIST.append((i["type_id"], i["cost"], i["fire_rate"], i["tile_range"]))
    print("TOWER_ATTRIBUTE_LIST: ", TOWER_ATTRIBUTE_LIST)




