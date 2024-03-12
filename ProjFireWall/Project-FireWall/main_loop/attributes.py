import pygame

def window_Creation():
    window = pygame.display.set_mode((400, 500))
    color = "red"
    window.fill(color)
    return window


def window_Attributes(window):
    color = "red"
    window.fill(color)
    pygame.display.update()
    return "Window adjusted and updated"

