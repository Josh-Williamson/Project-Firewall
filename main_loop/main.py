import pygame
from pygame import event
from classes import *
from render import *
from method import *
from attributes import setWindowColor

pygame.init()
keep_game_running = True
FPS = pygame.time.Clock()
FPS.tick(60)

window = Window()
window.CreateWindow()

textbox = TextBox()
textbox.CreateTextBox(window)


while keep_game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False

    """little test function for funsies and sanity.
    press DOWN ARROW key to remove textbox from screen"""
    if event.type == pygame.KEYDOWN:
        textbox.RemoveTextBox()

    purplePulse(window)
    RenderTextBox(window)


    updateDisplayScreen()

else:
    pygame.quit()
