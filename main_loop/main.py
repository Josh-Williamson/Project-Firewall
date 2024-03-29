import pygame
from pygame import event
from classes import *
from method import *


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

enemy_1 = Enemy(gridmap)
enemy_1.CreateEnemy((255, 15))
enemy_1.type_ID = 1
print(enemy_1.type_ID)
enemy_1.addToGroup()

pygame.time.set_timer(pygame.USEREVENT+1, 500)


keep_game_running = True

while keep_game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False
        window.UpdateBackground(LEVEL)
        mouse_pressed = pygame.mouse.get_pressed(3)


        left_mouse_button = mouse_pressed[0]
        right_mouse_button = mouse_pressed[2]
        if (mouse_pressed[0] or mouse_pressed[2]) and event.type == pygame.MOUSEBUTTONDOWN:
            gridmap.clickTile(left_mouse_button, right_mouse_button)

    pygame.time.wait(500)


    print(enemy_1.truepos)


    gridmap.DrawTileImage()
    gridmap.DrawGrid(window)


    ENEMY_SPRITE_GROUP.update(gridmap)
    ENEMY_SPRITE_GROUP.draw(SURFACE)

    pygame.event.pump()
    pygame.display.flip()
    FPS.tick_busy_loop(60)

else:
    pygame.quit()
