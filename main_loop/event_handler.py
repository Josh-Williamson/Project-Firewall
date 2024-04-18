import pygame

HANDLED_INPUT_LIST = [1,2,3]


def getKeyPressedValue(event):
    key_value = pygame.key.name(event.key)
    if int(key_value) in HANDLED_INPUT_LIST:
        return int(key_value)
    else:
        return None
