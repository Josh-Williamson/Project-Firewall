import pygame
from attributes import setWindowColor


class Window():
    def __init__(window):
        window.width = 400
        window.height = 600
        window.color = pygame.Color(255, 0, 255)
        window.caption = "Project Firewall"
        window.display = pygame.display

    def CreateWindow(window):
        window.display = pygame.display.set_mode((window.width, window.height))
        pygame.display.set_caption(window.caption)
        setWindowColor(window.display, window.color)

    def UpdateWindowAttributes(window):
        setWindowColor(window.display, window.color)