import pygame
from pygame import event
import csv

TILE_TYPES = 1
ENEMY_TYPES = 1
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

PATH = 900
SPAWN = 901
BASE = 902

ENEMY_IMAGE_LIST = []
ENEMY_SPRITE_GROUP = pygame.sprite.RenderUpdates()
ENEMY_SPRITE_GROUP.__init__()

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



class TextBox:

    def __init__(textBox):
        global renderTextList, textRectangleList
        renderTextList = list()
        textRectangleList = list()
        textBox.width = 300
        textBox.height = 100
        textBox.color = pygame.Color(255, 255, 255)
        textBox.font = pygame.font.Font('freesansbold.ttf', 30)
        textBox.text = "Hello World!"
        textBox.textColor = pygame.Color(0, 0, 0)
        textBox.renderText = pygame.surface
        textBox.textRectangle = pygame.rect


    def get_renderTextList(self = None):
        return renderTextList

    def get_textRectangleList(self = None):
        return textRectangleList

    def CreateTextBox(self):
        self.__init__()
        self.renderText = self.font.render(self.text, True, self.textColor)
        self.textRectangle = self.renderText.get_rect()
        self.textRectangle.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        renderTextList.append(self.renderText)
        textRectangleList.append(self.textRectangle)

    def RemoveTextBox(textBox):
        if renderTextList and textRectangleList:
            renderTextList.remove(textBox.renderText)
            textRectangleList.remove(textBox.textRectangle)
        else:
            return

class Sprite(pygame.sprite.Sprite):


    def update(self, gridmap):
        return


class Enemy(Sprite):
    def __init__(self, gridmap):

        pygame.sprite.Sprite.__init__(self, ENEMY_SPRITE_GROUP)
        self.type_ID = 1
        ##row == y, column == x
        self.gridpos = gridmap.pathWaypointList[0]
        self.grid_row = self.gridpos[1]
        self.grid_column = self.gridpos[0]

        self.tile_size = 30

        self.truepos_x = self.grid_column * self.tile_size
        self.truepos_y = self.grid_row * self.tile_size
        self.truepos = [self.truepos_x, self.truepos_y]

        self.path_index = 0

        self.hp = 0
        self.damage = 0
        self.speed = 35

        self.image = ENEMY_IMAGE_LIST[0]
        self.rect = self.getSpriteRect()
        Sprite.update(self, gridmap)

    def update(self, gridmap):
        self.followPath(gridmap.pathWaypointList)
        self.rect = self.getSpriteRect()

    def CreateEnemy(self, spawn_location):
        self.position = spawn_location

        Sprite.rect = self.rect

    def addToGroup(self):
        pygame.sprite.Sprite.add(self, ENEMY_SPRITE_GROUP)

    def getSpriteRect(self):
        left = self.truepos[0]
        top = self.truepos[1]
        width = self.tile_size
        height = self.tile_size
        return pygame.Rect(left, top, width, height)

    def followPath(self, pathWaypointList):
        self.path_index += 1
        waypoint = pathWaypointList[self.path_index]
        self.gridpos = waypoint
        if self.gridpos == pathWaypointList[len(pathWaypointList)-1]:
            #need to manage base hp reduction
            self.kill()
            return
        else:
            self.truepos = self.convertTiletoTruePosition(self.gridpos)
            return

    def convertTiletoTruePosition(self, gridpos):
        holdpos = (gridpos[1] * self.tile_size, gridpos[0] * self.tile_size)
        return holdpos

    def scaleTruetoTilePosition(self, gridpos):
        holdpos = (gridpos[1] / self.tile_size, gridpos[0] / self.tile_size)
        return holdpos

def loadEnemyImageList(gridmap):
    for x in range(0, 2):
        image = pygame.image.load(f'assets/enemy/enemy_1.png').convert_alpha()
        image = pygame.transform.scale(image, (gridmap.tileSize, gridmap.tileSize))
        ENEMY_IMAGE_LIST.append(image)


"""global """
def RenderTextBox():
    for text in renderTextList:
        for rect in textRectangleList:
            pygame.display.get_surface().blit(text, rect)


class GridMap:

    def __init__(self):
        self.tileSize = 30
        self.rows = pygame.display.get_surface().get_height() // self.tileSize
        self.columns = pygame.display.get_surface().get_width() // self.tileSize
        self.gridMap = []
        self.pathWaypointList = []
        self.imageList = []
        self.level = 0

        #self.highlighted = []
        #self.highlightSprite = pygame.sprite.Sprite()

    def InitiateGridMap(self, level):
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
            print(self.gridMap)
        self.writePathWaypointList()

    def LoadImageList(self):
        for x in range(TILE_TYPES + 1):
            image = pygame.image.load(f'assets/tile/{x}.png').convert_alpha()
            image = pygame.transform.scale(image, (self.tileSize, self.tileSize))
            self.imageList.append(image)
            print(x)
        #append path.png
        image = pygame.image.load(f'assets/tile/path.png').convert_alpha()
        image = pygame.transform.scale(image, (self.tileSize, self.tileSize))
        self.imageList.append(image)
        #append spawn.png
        image = pygame.image.load(f'assets/tile/spawn.png').convert_alpha()
        image = pygame.transform.scale(image, (self.tileSize, self.tileSize))
        self.imageList.append(image)
        #append base.png
        image = pygame.image.load(f'assets/tile/base.png').convert_alpha()
        image = pygame.transform.scale(image, (self.tileSize, self.tileSize))
        self.imageList.append(image)

    def DrawGrid(self, window):
        for row in range(self.rows):
            pygame.draw.line(window.display, (0,0,0), (0, row * self.tileSize),
                             (window.width, row * self.tileSize))
        for column in range(self.columns):
            pygame.draw.line(window.display, (0,0,0), (column * self.tileSize, 0),
                             (column * self.tileSize, window.height))

#added 'path', 'spawn', and 'base' handling, need images and function for spawn and base"""
    def DrawTileImage(self):
        for y, row in enumerate(self.gridMap):
            for x, tile in enumerate(row):
                if tile == PATH:
                    image = self.imageList[TILE_TYPES + 1]
                    pygame.display.get_surface().blit(image, (x * self.tileSize, y * self.tileSize))
                elif tile == SPAWN:
                    image = self.imageList[TILE_TYPES + 2]
                    pygame.display.get_surface().blit(image, (x * self.tileSize, y * self.tileSize))
                elif tile == BASE:
                    image = self.imageList[TILE_TYPES + 3]
                    pygame.display.get_surface().blit(image, (x * self.tileSize, y * self.tileSize))
                elif tile != 0:
                    image = self.imageList[tile]
                    pygame.display.get_surface().blit(image,
                                                      (x * self.tileSize, y * self.tileSize))

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
        print("getTileValueAtMousePosition", tile)
        return tile




        #use in placement events and map drawing for tile locations

    def updateTile(self, row, column, value):
        print("value = ", value)
        print("row, column", row, column)
        holder = self.gridMap
        holder[row][column] = value
        self.gridMap = holder
        print("updateTile: ", self.gridMap[row][column])

    def clickTile(self, left_mouse_button, right_mouse_button):
        pos = self.getTilePosition()
        tile = self.getTileValueAtMousePosition()
        row = pos[0]
        column = pos[1]

        if left_mouse_button:
            self.leftClickTile(tile, row, column)
        if right_mouse_button:
            self.rightClickTile(tile, row, column)

    def leftClickTile(self, tile, row, column):
        if tile >= TILE_TYPES:
            return
        elif pygame.MOUSEBUTTONDOWN:
            self.updateTile(row, column, (tile + 1))
            return

    def rightClickTile(self, tile, row, column):
        self.updateTile(row, column, 0)
        print("right_click: ", self.gridMap[row][column])
        return

    def getPathStart(self):
        found_start = False

        self.pathWaypointList.clear()

        while found_start == False:
            for row in range(self.rows):
                if found_start == True:
                    break
                for column in range(self.columns):
                    if self.gridMap[row][column] == SPAWN:
                        #tried flipping coordinates, and it broke everything
                        self.pathWaypointList.append((row, column))
                        found_start = True
                        print("found start")
                        return

    def writePathWaypointList(self):
        previous_position = (0, 0)
        previous_row = previous_position[0]
        previous_column = previous_position[1]

        index = 0
        recursion_counter = 0
        writing_path = True

        self.getPathStart()

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
                        print(done)
                        break

        print("pathWaypointList: ", self.pathWaypointList)

    def getAdjacentTiles(self, current_position):
        row = current_position[0]
        column = current_position[1]

        if row > 0:
            pos1 = (row - 1, column)
        else:
            pos1 = (0, column)
        pos2 = (row + 1, column)

        if column > 0:
            pos3 = (row, column - 1)
        else:
            pos3 = (row, 0)
        pos4 = (row, column + 1)

        return [pos1, pos2, pos3, pos4]

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





















