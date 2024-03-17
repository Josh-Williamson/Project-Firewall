"""All rendering functions can go here.
If we gotta draw it on the screen, we should do it here if possible.

"""
import pygame
from classes import Window
from update_methods import updateDisplayScreen
from method import purplePulse


def renderAll(window):
    Window.UpdateWindowAttributes(window)
    purplePulse(window)
    ...
    ...
    ...
    updateDisplayScreen()
