import pygame
from classes import *
from render import *

pygame.init()
FPS = pygame.time.Clock()
FPS.tick(60)



window = Window()
Window.CreateWindow(window)

keep_game_running = True

while keep_game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False

    renderAll(window)

else:
    pygame.quit()
