import pygame
from base import *

TILE_TYPES = 1
ENEMY_TYPES = 1

ENEMY_IMAGE_LIST = []
ENEMY_SPRITE_GROUP = pygame.sprite.RenderUpdates()
ENEMY_SPRITE_GROUP.__init__()



class Sprite(pygame.sprite.Sprite):


    def update(self, gridmap, base):
        return


class Enemy(Sprite):
    def __init__(self, gridmap, base):

        pygame.sprite.Sprite.__init__(self, ENEMY_SPRITE_GROUP)
        self.type_ID = 1
        ##row == y, column == x
        self.gridpos = gridmap.pathWaypointList[0]
        self.grid_row = self.gridpos[1]
        self.grid_column = self.gridpos[0]

        self.tile_size = 30

        self.truepos = self.convertTiletoTruePosition(self.gridpos)
        self.truepos_x = self.truepos[0]
        self.truepos_y = self.truepos[1]


        self.path_index = 0

        self.hp = 0
        self.damage = 1
        self.speed = 35

        self.image = ENEMY_IMAGE_LIST[0]
        self.rect = self.getSpriteRect()
        Sprite.update(self, gridmap, base)

    def update(self, gridmap, base):
        self.followPath(gridmap.pathWaypointList, base)
        self.rect = self.getSpriteRect()

    def createEnemy(self, spawn_location, gridmap, base):
        self.position = spawn_location
        Sprite.rect = self.rect
        ENEMY_SPRITE_GROUP.update(gridmap, base)

    def addToGroup(self):
        pygame.sprite.Sprite.add(self, ENEMY_SPRITE_GROUP)

    def getSpriteRect(self):
        left = self.truepos[0]
        top = self.truepos[1]
        width = self.tile_size
        height = self.tile_size
        return pygame.Rect(left, top, width, height)

    def followPath(self, pathWaypointList, base):

        waypoint = pathWaypointList[self.path_index]
        self.gridpos = waypoint
        self.truepos = self.convertTiletoTruePosition(self.gridpos)

        if self.path_index >= len(pathWaypointList):
            print("Path index is out of range: ", self.path_index)
            return

        elif self.path_index == len(pathWaypointList) - 1:
            self.dealBaseDamage(base)

        else:
            self.path_index += 1
            return

    def dealBaseDamage(self, base):
        base.hp -= self.damage
        self.kill()
        print("kill")
        return

    def convertTiletoTruePosition(self, gridpos):
        holdpos = (gridpos[1] * self.tile_size, gridpos[0] * self.tile_size)
        return holdpos

    def scaleTruetoTilePosition(self, gridpos):
        holdpos = (gridpos[1] / self.tile_size, gridpos[0] / self.tile_size)
        return holdpos

def loadEnemyImageList(gridmap):
    for x in range(0, 2):
        image = pygame.image.load(f'assets/enemy/enemy_1.png').convert_alpha()
        image = pygame.transform.scale(image, (gridmap.tileSize, gridmap.tileSize))
        ENEMY_IMAGE_LIST.append(image)

