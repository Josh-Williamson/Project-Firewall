import pygame
import json

TOWER_TYPES = 1
TOWER_IMAGE_LIST = []
TOWER_ATTRIBUTE_LIST = []

TOWER_SPRITE_GROUP = pygame.sprite.RenderUpdates()
TOWER_SPRITE_GROUP.__init__()


class Tower(pygame.sprite.Sprite):

    def __init__(self, truepos, type_id, TILE_SIZE):
        pygame.sprite.Sprite.__init__(self, TOWER_SPRITE_GROUP)
        attributes = TOWER_ATTRIBUTE_LIST[type_id]
        self.type_id = type_id

        self.truepos = truepos

        self.cost = attributes[1]

        self.image = TOWER_IMAGE_LIST[type_id]
        self.rect = self.getSpriteRect(TILE_SIZE)

    def update(self):
        return

    def getSpriteRect(self, TILE_SIZE):
        left = self.truepos[0]
        top = self.truepos[1]
        width = TILE_SIZE
        height = TILE_SIZE
        return pygame.Rect(left, top, width, height)

def loadTowerImageList(gridmap):
    for x in range(TOWER_TYPES+1):
        image = pygame.image.load(f'assets/tower/tower_{x}.png').convert_alpha()
        image = pygame.transform.scale(image, (gridmap.tileSize, gridmap.tileSize))
        TOWER_IMAGE_LIST.append(image)
        print("image loaded", x)
    return

def loadTowerAttributeList():
    file_name = open("tower_types/tower_attributes.json")
    attributes = json.load(file_name)

    for i in attributes["tower_attributes"]:
        TOWER_ATTRIBUTE_LIST.append((i["type_id"], i["cost"]))
    print(TOWER_ATTRIBUTE_LIST)




