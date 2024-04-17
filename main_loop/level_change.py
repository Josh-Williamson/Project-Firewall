import pygame
from gridmap import GridMap

def levelInitialize(level, window, gridmap):
    window.image = window.getBackground(level)
    window.updateBackground()
    #previous_tile_size = gridmap.tileSize
    gridmap = GridMap(level)
    gridmap.initiateGridMap(level)
    #if previous_tile_size !+ gridmap.tileSize:
    #   reload all image lists

    #load LEVEL_ENEMY_LIST
    #rescale image lists when/if dynamic tile sizes are implemented

    gridmap.drawPath()
    gridmap.drawGrid(window)



    pygame.display.flip()
    return gridmap