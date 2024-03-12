import pygame
from attributes import window_Creation, window_Attributes


pygame.init()

window = window_Creation()

pygame.display.set_caption("Project Firewall")

keepGameRunning = True

while keepGameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGameRunning = False
    window_Attributes(window)
    window.fill("green")
    pygame.display.flip()

