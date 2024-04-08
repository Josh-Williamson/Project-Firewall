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



LEVEL = 0

window = Window()
window.createWindow()
SURFACE = pygame.display.get_surface()

gridmap = GridMap()
gridmap.initiateGridMap(1)

loadGridmapImageList(gridmap)
loadEnemyImageList(gridmap)
loadEnemyAttributeList()
loadTowerImageList(gridmap)
loadTowerAttributeList()
loadProjectileImageList(gridmap)

base = Base()

enemy_1 = Enemy(gridmap, 1)
enemy_1.createEnemy((gridmap.getPathStart()), gridmap)
enemy_1.addToGroup()

#basic proof of concept that is drawn on lines 73-74
projectile_1 = Projectile()

ENEMY_UPDATE_EVENT = pygame.event.custom_type()
TOWER_UPDATE_EVENT = pygame.event.custom_type()
pygame.time.set_timer(ENEMY_UPDATE_EVENT, 500)
ENEMY_SPRITE_GROUP.draw(SURFACE)


window.updateBackground(LEVEL)
gridmap.drawTileImage()
gridmap.drawGrid(window)

keep_game_running = True

while keep_game_running:

    window.updateBackground(LEVEL)
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






    projectile_1.draw(window.display)

    TOWER_SPRITE_GROUP.draw(SURFACE)
    gridmap.drawGrid(window)
    ENEMY_SPRITE_GROUP.draw(SURFACE)

    pygame.event.pump()
    pygame.display.flip()

    FPS.tick()
    print(FPS.get_fps())

else:
    pygame.quit()
