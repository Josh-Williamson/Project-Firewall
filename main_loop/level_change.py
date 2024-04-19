import pygame
from gridmap import GridMap
from enemies import Enemy
from towers import TOWER_SPRITE_GROUP
from projectiles import PROJECTILE_SPRITE_GROUP

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
    for tower in TOWER_SPRITE_GROUP:
        tower.kill()
    for projectile in PROJECTILE_SPRITE_GROUP:
        projectile.kill()


    gridmap.drawPath()
    gridmap.drawGrid(window)

    Enemy(gridmap, 1)

    pygame.display.flip()
    return gridmap