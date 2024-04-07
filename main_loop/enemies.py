import pygame
from base import *
import json
import math


TILE_TYPES = 1
ENEMY_TYPES = 1

ENEMY_IMAGE_LIST = []
ENEMY_ATTRIBUTE_LIST = []
ENEMY_SPRITE_GROUP = pygame.sprite.RenderUpdates()
ENEMY_SPRITE_GROUP.__init__()



class Sprite(pygame.sprite.Sprite):


    def update(self, gridmap):
        return


class Enemy(Sprite):
    def __init__(self, gridmap, type_id):

        pygame.sprite.Sprite.__init__(self, ENEMY_SPRITE_GROUP)
        self.type_ID = type_id
        ##row == y, column == x
        self.gridpos = gridmap.pathWaypointList[0]
        self.grid_row = self.gridpos[1]
        self.grid_column = self.gridpos[0]

        self.tile_size = 30

        self.truepos = self.convertTiletoTruePosition(self.gridpos)
        self.truepos_x = self.truepos[0]
        self.truepos_y = self.truepos[1]


        self.path_index = 0

        attributes = ENEMY_ATTRIBUTE_LIST[self.type_ID]

        self.name = attributes[1]
        self.hp = attributes[2]
        self.damage = attributes[3]
        self.speed = attributes[4]

        self.image = ENEMY_IMAGE_LIST[0]
        self.rect = self.getSpriteRect()
        self.rect_center = self.rect.center
        Sprite.update(self, gridmap)

    def update(self, gridmap, base):
        if self.hp == 0:
            self.kill()
        self.followPath(gridmap.pathWaypointList, base)
        self.rect = self.getSpriteRect()

    def createEnemy(self, spawn_location, gridmap, base):
        self.position = spawn_location
        self.path_index = 1
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

        if self.path_index == len(pathWaypointList):
            self.dealBaseDamage(base)
            return

        if self.path_index > len(pathWaypointList):
            print("Path index is out of range: ", self.path_index)
            return

        waypoint = pathWaypointList[self.path_index]
        distance_to_waypoint = self.getDistanceToWaypoint(waypoint)

        if distance_to_waypoint > self.speed/30:
            move_vector = self.getMovementVector(waypoint)
            move_vector.scale_to_length(self.speed/30)
            self.truepos += move_vector

        elif distance_to_waypoint <= self.speed/30:
            move_vector = self.getMovementVector(waypoint)
            move_vector.scale_to_length(distance_to_waypoint)
            self.truepos += move_vector
            self.path_index += 1
            return

    def getDistanceToWaypoint(self, waypoint):
        true_wp = self.convertTiletoTruePosition(waypoint)
        x_comp = true_wp[0] - self.truepos[0]
        y_comp = true_wp[1] - self.truepos[1]

        return math.hypot(x_comp, y_comp)

    def getMovementVector(self, waypoint):
        true_wp = self.convertTiletoTruePosition(waypoint)
        x_comp = true_wp[0] - self.truepos[0]
        y_comp = true_wp[1] - self.truepos[1]
        return pygame.Vector2(x_comp, y_comp)

    def dealBaseDamage(self, base):
        base.hp -= self.damage
        self.kill()
        print("Base Damaged by: ", self.name)
        return

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
            print("Enemy destroyed")
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

def loadEnemyAttributeList():
    file_name = open("sprite_attributes/enemy_attributes.json")
    attributes = json.load(file_name)

    for i in attributes["enemy_attributes"]:
        ENEMY_ATTRIBUTE_LIST.append((i["type_id"], i["name"], i["hp"], i["damage"], i["speed"]))
    print(ENEMY_ATTRIBUTE_LIST)

