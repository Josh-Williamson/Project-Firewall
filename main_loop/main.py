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

LEVEL = 0

window = Window()
window.CreateWindow()
SURFACE = pygame.display.get_surface()

gridmap = GridMap()
gridmap.InitiateGridMap(1)
gridmap.LoadImageList()
gridmap.writePathWaypointList()

loadEnemyImageList(gridmap)
loadProjectileImageList(gridmap)

base = Base()

enemy_1 = Enemy(gridmap)
enemy_1.CreateEnemy((255, 15), gridmap, base)
enemy_1.type_ID = 1
enemy_1.addToGroup()

#basic proof of concept that is drawn on lines 73-74
projectile_1 = Projectile()

tower_image1 = pygame.image.load("assets/tower/tower_1.png").convert_alpha()
tower_1 = Tower((400, 200), tower_image1, 0, projectile_1)



ENEMY_UPDATE_EVENT = pygame.event.custom_type()
pygame.time.set_timer(ENEMY_UPDATE_EVENT, 500)
ENEMY_SPRITE_GROUP.draw(SURFACE)



keep_game_running = True

while keep_game_running:
    window.UpdateBackground(LEVEL)
    gridmap.DrawTileImage()
    gridmap.DrawGrid(window)
    mouse_pressed = pygame.mouse.get_pressed(3)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False


        LMB = mouse_pressed[0]
        RMB = mouse_pressed[2]
        if (LMB or RMB):
            gridmap.clickTile(LMB, RMB)
        if event.type == ENEMY_UPDATE_EVENT:
            ENEMY_SPRITE_GROUP.update(gridmap, base)



    ENEMY_SPRITE_GROUP.draw(SURFACE)

    print(ENEMY_SPRITE_GROUP.sprites())
    print(base.hp)



    #ENEMY_SPRITE_GROUP.update(gridmap)
    #ENEMY_SPRITE_GROUP.draw(SURFACE)


    tower_1.draw(window.display)
    projectile_1.draw(window.display)



    pygame.event.pump()
    pygame.display.flip()
    FPS.tick_busy_loop(60)

else:
    pygame.quit()
