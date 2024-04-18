import pygame

from base import Base
from enemies import ENEMY_SPRITE_GROUP, Enemy, collisionDamageHandler
from gridmap import GridMap
from projectiles import PROJECTILE_SPRITE_GROUP
from towers import TOWER_SPRITE_GROUP
from window import Window
from startup import loadImageLists, loadAttributeLists
from level_change import levelInitialize

pygame.init()

window = Window()

SURFACE = pygame.display.get_surface()
LEVEL = 1

loadImageLists()
loadAttributeLists()

FPS = pygame.time.Clock()
FPS.tick(60)

gridmap = GridMap()
gridmap.initiateGridMap(1)

base = Base()

enemy_1 = Enemy(gridmap, 1)

ENEMY_SPRITE_GROUP.draw(SURFACE)

levelInitialize(LEVEL, gridmap)

keep_game_running = True

while keep_game_running:

    if ENEMY_SPRITE_GROUP.sprites() is None:
        LEVEL += 1
        gridmap = levelInitialize(LEVEL, gridmap, window)



    window.updateBackground()
    gridmap.drawPath()


    mouse_pressed = pygame.mouse.get_pressed(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False


        if event.type == pygame.MOUSEBUTTONUP:
            LMB = mouse_pressed[0]
            RMB = mouse_pressed[2]
            if (LMB or RMB):
                gridmap.clickTile(LMB, RMB)


    ENEMY_SPRITE_GROUP.update(gridmap)
    TOWER_SPRITE_GROUP.update()
    PROJECTILE_SPRITE_GROUP.update()

    collision_dict = pygame.sprite.groupcollide(
        ENEMY_SPRITE_GROUP, PROJECTILE_SPRITE_GROUP,
        False, True)
    collisionDamageHandler(collision_dict)

    gridmap.drawGrid(window)

    update_list = []
    update_list.extend(ENEMY_SPRITE_GROUP.draw(SURFACE))
    update_list.extend(TOWER_SPRITE_GROUP.draw(SURFACE))
    pygame.display.update(update_list)
    #second update list iteration to put projectiles on top of towers
    update_list = []
    update_list.extend(PROJECTILE_SPRITE_GROUP.draw(SURFACE))
    pygame.display.update(update_list)

    pygame.event.pump()
    FPS.tick(60)
    print(FPS.get_fps())

else:
    pygame.quit()
