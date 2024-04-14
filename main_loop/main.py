from enemies import *
from gridmap import *
from projectiles import *
from towers import *
from window import *

pygame.init()

FPS = pygame.time.Clock()
FPS.tick(60)

TILE_SIZE = 30
LEVEL = 1

window = Window(LEVEL)
SURFACE = pygame.display.get_surface()

gridmap = GridMap()
gridmap.initiateGridMap(1)

loadGridmapImageList(gridmap)
loadEnemyImageList(gridmap)
loadEnemyAttributeList()
loadTowerImageList(gridmap)
loadTowerAttributeList()
loadProjectileImageList(gridmap)
loadProjectileAttributeList()

base = Base()

enemy_1 = Enemy(gridmap, 1)


ENEMY_SPRITE_GROUP.draw(SURFACE)

window.updateBackground()
gridmap.drawTileImage()
gridmap.drawGrid(window)
pygame.display.flip()

keep_game_running = True

while keep_game_running:

    window.updateBackground()
    gridmap.drawTileImage()

    mouse_pressed = pygame.mouse.get_pressed(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False


        LMB = mouse_pressed[0]
        RMB = mouse_pressed[2]
        if (LMB or RMB):
            gridmap.clickTile(LMB, RMB)

    ENEMY_SPRITE_GROUP.update(gridmap)
    TOWER_SPRITE_GROUP.update()
    PROJECTILE_SPRITE_GROUP.update()

    collision_dict = pygame.sprite.groupcollide(
        ENEMY_SPRITE_GROUP, PROJECTILE_SPRITE_GROUP,
        False, True)
    collisionDamageHandler(collision_dict)

    gridmap.drawGrid(window)

    update_list = []
    update_list.extend(ENEMY_SPRITE_GROUP.draw(SURFACE))
    update_list.extend(TOWER_SPRITE_GROUP.draw(SURFACE))
    pygame.display.update(update_list)
    #second update list iteration to put projectiles on top of towers
    update_list = []
    update_list.extend(PROJECTILE_SPRITE_GROUP.draw(SURFACE))
    pygame.display.update(update_list)

    pygame.event.pump()
    FPS.tick(60)
    print(FPS.get_fps())

else:
    pygame.quit()
