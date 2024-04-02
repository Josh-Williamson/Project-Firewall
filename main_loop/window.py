import pygame
from pygame import event
import csv

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class Window:
    def __init__(window):

        window.width = SCREEN_WIDTH
        window.height = SCREEN_HEIGHT
        window.color = pygame.Color(255, 0, 255)
        window.caption = "Project Firewall"
        window.display = pygame.display.set_mode((window.width, window.height))

        window.surface = pygame.surface.Surface([window.width, window.height])


    def CreateWindow(window):
        window.__init__()
        window.display = pygame.display.set_mode((window.width, window.height))
        window.display.fill(window.color)

    def UpdateBackground(window, level):
        backgroundImage = pygame.image.load(f"assets/backgrounds/0.png")
        window.display.blit(backgroundImage, (0,0))

