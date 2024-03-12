import pygame
from update_methods import updateDisplayScreen

def Create_and_Return_window():
    window = pygame.display.set_mode((400, 500))
    return window

def UpdateWindowAttributes(window, color):
    setWindowColor(window, color)

def setWindowColor(window, color):
    window.fill(color)
