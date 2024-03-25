import pygame
import csv
from classes import *

pygame.init()

"""Demo method for GameLoop functionality"""
def purplePulse(window):
    if window.color != (255, 0, 255):
        """If the Clock.tick is not set high, pulse is a fast strobe"""
        pygame.time.Clock().tick(200)
        window.color = window.color + pygame.Color(1, 0, 1)
        window.display.fill(window.color)
        return
    else:
        window.color = pygame.Color(0,0,0)
        window.display.fill(window.color)
        return













