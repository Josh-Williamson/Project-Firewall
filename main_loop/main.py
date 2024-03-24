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

gridmap = GridMap()
gridmap.InitiateGridMap(1)
gridmap.LoadImageList()


textbox = TextBox()
textbox.CreateTextBox()
window.UpdateBackground(LEVEL)

enemy_group = pygame.sprite.Group()

enemy_image1 = pygame.image.load("assets/enemy/enemy_1.png").convert_alpha()

enemy_1 = Enemy((200, 200), enemy_image1, 0, 0, 0)
enemy_group.add(enemy_1)

projectile_image1 = pygame.image.load("assets/projectile/projectile_1.png").convert_alpha()
projectile_1 = Projectile((400,400), projectile_image1, 0, 0)

tower_image1 = pygame.image.load("assets/tower/tower_1.png").convert_alpha()
tower_1 = Tower((400, 200) , tower_image1, 0, projectile_1)

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



        #Event(window, textbox, gridmap)


    #purplePulse(window)

    #RenderTextBox()
    gridmap.DrawTileImage()
    gridmap.DrawGrid(window)
    #gridmap.LoadImageList()


    enemy_group.draw(window.display)
    projectile_1.draw(window.display)
    tower_1.draw(window.display)

    pygame.event.pump()
    pygame.display.flip()

else:
    pygame.quit()
