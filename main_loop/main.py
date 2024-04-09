import pygame
from pygame import event

from window import *
from gridmap import *
from base import *
from towers import *
from projectiles import *
from enemies import *


pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)


TILE_SIZE = 30
LEVEL = 1

window = Window(LEVEL)
SURFACE = pygame.display.get_surface()

gridmap = GridMap()
gridmap.initiateGridMap(1)

loadGridmapImageList(gridmap)
loadEnemyImageList(gridmap)
loadEnemyAttributeList()
loadTowerImageList(gridmap)
loadTowerAttributeList()
loadProjectileImageList(gridmap)
loadProjectileAttributeList()

base = Base()

enemy_1 = Enemy(gridmap, 1)




ENEMY_UPDATE_EVENT = pygame.event.custom_type()
TOWER_UPDATE_EVENT = pygame.event.custom_type()
pygame.time.set_timer(ENEMY_UPDATE_EVENT, 500)
ENEMY_SPRITE_GROUP.draw(SURFACE)


window.updateBackground()
gridmap.drawTileImage()
gridmap.drawGrid(window)
pygame.display.flip()

keep_game_running = True

while keep_game_running:


    gridmap.drawTileImage()

    mouse_pressed = pygame.mouse.get_pressed(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False


        LMB = mouse_pressed[0]
        RMB = mouse_pressed[2]
        if (LMB or RMB):
            gridmap.clickTile(LMB, RMB)

    ENEMY_SPRITE_GROUP.update(gridmap)

    projectile_1 = Projectile((200, 200), 1, gridmap.tileSize)





    TOWER_SPRITE_GROUP.draw(SURFACE)
    gridmap.drawGrid(window)

    update_list = []
    update_list.extend(ENEMY_SPRITE_GROUP.draw(SURFACE))
    update_list.extend(PROJECTILE_SPRITE_GROUP.draw(SURFACE))
    update_list.extend(TOWER_SPRITE_GROUP.draw(SURFACE))

    pygame.display.update(update_list)

    pygame.event.pump()
    FPS.tick(60)
    print(FPS.get_fps())

else:
    pygame.quit()
