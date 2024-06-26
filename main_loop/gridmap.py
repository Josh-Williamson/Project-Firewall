import csv

from towers import *

TILE_TYPES = 1
ENEMY_TYPES = 1
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

PATH = 900
SPAWN = 901
BASE = 902

GRIDMAP_IMAGE_LIST = []
TILE_SIZE = 30

class GridMap:

    def __init__(self, level):
        self.tileSize = TILE_SIZE
        self.rows = pygame.display.get_surface().get_height() // self.tileSize
        self.columns = pygame.display.get_surface().get_width() // self.tileSize
        self.gridMap = []
        self.pathWaypointList = []
        self.imageList = []
        self.level = level

        #self.highlighted = []
        #self.highlightSprite = pygame.sprite.Sprite()

    def initiateGridMap(self, level):
        self.gridMap.clear()
        file_name = "level_data/{level_num}.csv".format(level_num=level)
        with open(file_name, "r") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                for i in range(0, len(row)):
                    if row[i] == "0":
                        row[i] = 0
                    else:
                        row[i] = int(row[i])
                    i += 1
                self.gridMap.append(row)
        self.writePathWaypointList()



    def drawGrid(self, window):
        update_list = []
        for row in range(self.rows):
            update_list.append(pygame.rect.Rect(pygame.draw.line(window.display, (0, 0, 0), (0, row * self.tileSize),
                                                                 (window.width, row * self.tileSize))))

        for column in range(self.columns):
            update_list.append(pygame.rect.Rect(pygame.draw.line(window.display, (0, 0, 0), (column * self.tileSize, 0),
                                                                 (column * self.tileSize, window.height))))
        return update_list

#added 'path', 'spawn', and 'base' handling, need images and function for spawn and base"""
    def drawTileImage(self):
        for y, row in enumerate(self.gridMap):
            for x, tile in enumerate(row):
                if tile == PATH:
                    image = GRIDMAP_IMAGE_LIST[0]
                    pygame.display.get_surface().blit(image, (x * self.tileSize, y * self.tileSize))
                elif tile == SPAWN:
                    image = GRIDMAP_IMAGE_LIST[1]
                    pygame.display.get_surface().blit(image, (x * self.tileSize, y * self.tileSize))
                elif tile == BASE:
                    image = GRIDMAP_IMAGE_LIST[2]
                    pygame.display.get_surface().blit(image, (x * self.tileSize, y * self.tileSize))

    def drawPath(self):
        for i in range(len(self.pathWaypointList)):

            row, column = self.pathWaypointList[i]
            tile_value = self.gridMap[row][column]

            if tile_value == PATH:
                image = GRIDMAP_IMAGE_LIST[0]
                pygame.display.get_surface().blit(image, (column * TILE_SIZE, row * TILE_SIZE))
            elif tile_value == SPAWN:
                image = GRIDMAP_IMAGE_LIST[1]
                pygame.display.get_surface().blit(image, (column * TILE_SIZE, row * TILE_SIZE))
            elif tile_value == BASE:
                image = GRIDMAP_IMAGE_LIST[2]
                pygame.display.get_surface().blit(image, (column * TILE_SIZE, row * TILE_SIZE))

    def getTilePosition(self):
        pos = pygame.mouse.get_pos()
        column = int(pos[0]/self.tileSize)
        row = int(pos[1]/self.tileSize)
        return [row, column]

    def getTileValueAtMousePosition(self):
        pos = self.getTilePosition()
        row = pos[0]
        column = pos[1]
        if row <= self.rows and column <= self.columns:
            tile = self.gridMap[row][column]
        return tile

        #use in placement events and map drawing for tile locations

    def updateTile(self, row, column, value):
        self.gridMap[row][column] = value

    def clickTile(self, left_mouse_button, right_mouse_button, key_pressed):
        pos = self.getTilePosition()
        tile = self.getTileValueAtMousePosition()
        row = pos[0]
        column = pos[1]

        if left_mouse_button and tile == 0 and key_pressed is not None:
            if self.leftClickTile(tile, row, column, key_pressed):
                return True
            else:
                return False
        if right_mouse_button:
            self.rightClickTile(tile, row, column)

    def leftClickTile(self, tile, row, column, tower_type_id):
        if tile != 0:
            return
        elif pygame.MOUSEBUTTONUP:
            self.updateTile(row, column, tower_type_id)
            Tower((column*self.tileSize, row*self.tileSize), tower_type_id, self.tileSize)
            return True

    def rightClickTile(self, tile, row, column):
        if tile != 0 or PATH or SPAWN or BASE:
            self.updateTile(row, column, 0)
            for tower in TOWER_SPRITE_GROUP.sprites():
                if tower.rect.x == column * self.tileSize and tower.rect.y == row * self.tileSize:
                    tower.kill()
                    return tower.rect.x, tower.rect.y
        else:
            return False

    def getPathStart(self):
        found_start = False
        while found_start == False:
            for row in range(self.rows):
                if found_start == True:
                    break
                for column in range(self.columns):
                    if self.gridMap[row][column] == SPAWN:
                        #tried flipping coordinates, and it broke everything
                        found_start = True
                        print("found start")
                        return (row, column)

    def getPathEnd(self):
        found_end = False
        while found_end == False:
            for row in range(self.rows):
                if found_end == True:
                    break
                for column in range(self.columns):
                    if self.gridMap[row][column] == BASE:
                        #tried flipping coordinates, and it broke everything
                        found_start = True
                        print("found end")
                        return (row, column)

    def writePathWaypointList(self):
        previous_position = (0, 0)
        previous_row = previous_position[0]
        previous_column = previous_position[1]

        index = 0
        recursion_counter = 0
        writing_path = True

        self.pathWaypointList.clear()
        self.pathWaypointList.append(self.getPathStart())

        done = False
        while done == False:

            current_position = (self.pathWaypointList[index])
            previous_position = self.pathWaypointList[index - 1]

            next_check_list = self.getAdjacentTiles(current_position)

            for pos in next_check_list:
                if done == True:
                    break
                row = pos[0]
                column = pos[1]

                if pos not in self.pathWaypointList:

                    if self.gridMap[row][column] == 900:
                        #tried flipping coordinates, and it broke everything
                        self.pathWaypointList.append((row, column))
                        index = index + 1

                    elif self.gridMap[row][column] == 902:
                        #tried flipping coordinates, and it broke everything
                        self.pathWaypointList.append((row, column))
                        done = True
                        break

    def getAdjacentTiles(self, current_position):
        row = current_position[0]
        column = current_position[1]

        if row > 0:
            pos_up = (row - 1, column)
        else:
            pos_up = (0, column)

        if row < 19:
            pos_down = (row + 1, column)
        else:
            pos_down = (19, column)

        if column > 0:
            pos_left = (row, column - 1)
        else:
            pos_left = (row, 0)

        if column < 19:
            pos_right = (row, column + 1)
        else:
            pos_right = (row, 19)

        print([pos_up, pos_down, pos_left, pos_right])
        return [pos_up, pos_down, pos_left, pos_right]

#path_recursion is a WIP method for generating paths"""
    def path_recursion(self, base, spawn):
        current_row = 0
        current_column = 0
        base_row = base[0]
        base_column = base[1]
        spawn_row = spawn[0]
        spawn_column = spawn[1]
        self.currentIteration = [spawn_row, spawn_column]

        while self.currentIteration != [base_row, base_column]:
            current_row = self.currentIteration[0]
            current_column = self.currentIteration[1]

            for row in enumerate(self.gridMap):
                for column, tile in enumerate(row):
                    if current_row == current_row and current_column +- 1 == current_column\
                            and self.pathWaypointList.index([current_row, current_column]):
                        self.pathWaypointList

def loadGridmapImageList(tile_size):
    #append path.png
    image = pygame.image.load(f'assets/tile/path.png').convert_alpha()
    image = pygame.transform.scale(image, (tile_size, tile_size))
    GRIDMAP_IMAGE_LIST.append(image)
    #append spawn.png
    image = pygame.image.load(f'assets/tile/spawn.png').convert_alpha()
    image = pygame.transform.scale(image, (tile_size, tile_size))
    GRIDMAP_IMAGE_LIST.append(image)
    #append base.png
    image = pygame.image.load(f'assets/tile/base.png').convert_alpha()
    image = pygame.transform.scale(image, (tile_size, tile_size))
    GRIDMAP_IMAGE_LIST.append(image)

def convertTiletoTruePosition(tile_size, gridpos):
    holdpos = (gridpos[1] * tile_size, gridpos[0] * tile_size)
    return holdpos

def scaleTruetoTilePosition(tile_size, gridpos):
    holdpos = (gridpos[1] / tile_size, gridpos[0] / tile_size)
    return holdpos
