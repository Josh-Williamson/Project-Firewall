import pygame

from base import Base
from enemies import ENEMY_SPRITE_GROUP, Enemy, collisionDamageHandler, enemyWaveSpawn
from gridmap import GridMap
from projectiles import PROJECTILE_SPRITE_GROUP
from towers import TOWER_SPRITE_GROUP
from window import Window
from startup import loadImageLists, loadAttributeLists
from level_change import levelInitialize
from event_handler import getKeyPressedValue

pygame.init()

window = Window()

SURFACE = pygame.display.get_surface()
KEY_PRESSED = 0
LEVEL = 1
spawn_timer = 0



loadAttributeLists()
loadImageLists()


FPS = pygame.time.Clock()
FPS.tick(60)

gridmap = GridMap(1)
gridmap.initiateGridMap(1)

base = Base()

ENEMY_SPRITE_GROUP.draw(SURFACE)

levelInitialize(LEVEL, window, gridmap)

keep_game_running = True

while keep_game_running:

    spawn_timer = spawn_timer + 1
    print (spawn_timer)

    if enemyWaveSpawn(spawn_timer, gridmap, LEVEL):
        spawn_timer = 0

    if ENEMY_SPRITE_GROUP.sprites() is None:
        LEVEL += 1
        gridmap = levelInitialize(LEVEL, window, gridmap)

    window.updateBackground()
    gridmap.drawPath()


    mouse_pressed = pygame.mouse.get_pressed(3)
    LMB = mouse_pressed[0]
    RMB = mouse_pressed[2]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False
        if event.type == pygame.KEYDOWN:
            KEY_PRESSED = getKeyPressedValue(event)
        if (LMB or RMB) and event.type == pygame.MOUSEBUTTONUP:
            if gridmap.clickTile(LMB, RMB, KEY_PRESSED):
                KEY_PRESSED = None

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
    #print(FPS.get_fps())

else:
    pygame.quit()
