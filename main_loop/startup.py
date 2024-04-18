from enemies import loadEnemyImageList, loadEnemyAttributeList
from gridmap import loadGridmapImageList, TILE_SIZE
from projectiles import loadProjectileImageList, loadProjectileAttributeList
from towers import loadTowerImageList, loadTowerAttributeList

def loadImageLists():

    loadGridmapImageList(TILE_SIZE)
    loadEnemyImageList(TILE_SIZE)
    loadTowerImageList(TILE_SIZE)
    loadProjectileImageList(TILE_SIZE)


def loadAttributeLists():
    loadEnemyAttributeList()
    loadTowerAttributeList()
    loadProjectileAttributeList()
