import pygame
from pygame import event
from classes import *
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

enemy_group = pygame.sprite.Group()

enemy_image1 = pygame.image.load("../assets/enemy/enemy_1.png").convert_alpha()

enemy_1 = Enemy((200, 200), enemy_image1, 0, 0, 0)
enemy_group.add(enemy_1)

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

    enemy_group.draw(window.display)

    pygame.display.flip()

else:
    pygame.quit()
