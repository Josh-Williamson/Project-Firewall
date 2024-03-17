import pygame


def Create_and_Return_window():
    window = pygame.display.set_mode((400, 500))
    return window


def setWindowColor(display, color):
    display.fill(color)
