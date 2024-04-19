import json
import math

from enemy_wave_data import *
from base import *
from enemy_wave_data import *

TILE_TYPES = 1
ENEMY_TYPES = 3
spawn_rate = 80

ENEMY_IMAGE_LIST = []
ENEMY_ATTRIBUTE_LIST = []
ENEMY_SPRITE_GROUP = pygame.sprite.RenderUpdates()
ENEMY_SPRITE_GROUP.__init__()



class Enemy(pygame.sprite.Sprite):

    def __init__(self, gridmap, type_id):

        pygame.sprite.Sprite.__init__(self, ENEMY_SPRITE_GROUP)
        self.type_ID = type_id
        ##row == y, column == x
        self.gridpos = gridmap.pathWaypointList[0]
        self.grid_row = self.gridpos[1]
        self.grid_column = self.gridpos[0]

        self.tile_size = 30

        self.truepos = self.convertTiletoTruePosition(self.gridpos)
        self.truepos_vector = pygame.Vector2(self.truepos)
        self.truepos_x = self.truepos[0]
        self.truepos_y = self.truepos[1]


        self.path_index = 1

        attributes = ENEMY_ATTRIBUTE_LIST[self.type_ID]

        self.name = attributes[1]
        self.hp = attributes[2]
        self.damage = attributes[3]
        self.speed = attributes[4]

        self.image = ENEMY_IMAGE_LIST[self.type_ID - 1]
        self.rect = self.getSpriteRect()
        self.rect_center = self.rect.center

    def update(self, gridmap):
        if self.hp == 0:
            self.kill()
        self.followPath(gridmap.pathWaypointList)
        self.rect = self.getSpriteRect()

    def createEnemy(self, spawn_location, gridmap):
        self.path_index = 1
        ENEMY_SPRITE_GROUP.update(gridmap)

    def addToGroup(self):
        pygame.sprite.Sprite.add(self, ENEMY_SPRITE_GROUP)

    def getSpriteRect(self):
        left = self.truepos[0]
        top = self.truepos[1]
        width = self.tile_size
        height = self.tile_size
        return pygame.Rect(left, top, width, height)

    # NEED TO REWORK FOLLOWPATH WITH VECTORS LIKE PROJECTILE - WAY EASIER
    def followPath(self, pathWaypointList):

        if self.path_index == len(pathWaypointList):
            self.dealBaseDamage()
            return

        if self.path_index > len(pathWaypointList):
            print("Path index is out of range: ", self.path_index)
            return

        waypoint = pathWaypointList[self.path_index]
        distance_to_waypoint = self.getDistanceToWaypoint(waypoint)

        if distance_to_waypoint > self.speed/30:
            self.move(waypoint, self.speed/30)

        elif distance_to_waypoint <= self.speed/30:
            self.move(waypoint, distance_to_waypoint)
            self.path_index += 1

    def move(self, waypoint, move_distance):
        move_vector = self.getMovementVector(waypoint)
        move_vector.scale_to_length(move_distance)
        self.truepos += move_vector

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

    def dealBaseDamage(self):
        BASE_SPRITE_GROUP.update(self.damage)
        self.kill()
        print("Base Damaged by: ", self.name)

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    def convertTiletoTruePosition(self, gridpos):
        holdpos = (gridpos[1] * self.tile_size, gridpos[0] * self.tile_size)
        return holdpos

    def scaleTruetoTilePosition(self, gridpos):
        holdpos = (gridpos[1] / self.tile_size, gridpos[0] / self.tile_size)
        return holdpos


def loadEnemyImageList(tile_size):
    for x in range(ENEMY_TYPES + 1):

        image = pygame.image.load(f'assets/enemy/enemy_1.png').convert_alpha()
        image = pygame.transform.scale(image, (tile_size, tile_size))
        ENEMY_IMAGE_LIST.append(image)

def loadEnemyAttributeList():
    file_name = open("sprite_attributes/enemy_attributes.json")
    attributes = json.load(file_name)

    for i in attributes["enemy_attributes"]:
        ENEMY_ATTRIBUTE_LIST.append((i["type_id"], i["name"], i["hp"], i["damage"], i["speed"]))



def collisionDamageHandler(collision_dict):
    for enemy in ENEMY_SPRITE_GROUP:
        if enemy in collision_dict:
            damage = 0
            collision_projectile_list = collision_dict[enemy]
            for projectile in collision_projectile_list:
                damage += projectile.getDamage()
            enemy.takeDamage(damage)

def enemyWaveSpawn(spawn_timer, gridmap, level):
    if len(ENEMY_WAVE_LIST[level]) == 0:
        return False
    elif spawn_timer >= spawn_rate:
        Enemy(gridmap, ENEMY_WAVE_LIST[level].pop(0))
        return True
