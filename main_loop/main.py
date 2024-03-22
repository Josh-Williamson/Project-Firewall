import pygame
from pygame import event
from classes import *
from render import *
from method import *



pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)
LEVEL = 0

window = Window()
window.CreateWindow()

gridmap = GridMap()
gridmap.InitiateGridMap()

textbox = TextBox()
textbox.CreateTextBox()
#window.UpdateBackground(LEVEL)

keep_game_running = True
while keep_game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False
        if event.type == pygame.KEYDOWN:
            window.color = pygame.Color(255, 0, 0)
            pygame.display.get_surface().fill(window.color)


    #purplePulse(window)

    #RenderTextBox()
    gridmap.DrawGrid(window)
    gridmap.LoadImageList()
    gridmap.DrawTileImage()


    updateDisplayScreen()

else:
    pygame.quit()
