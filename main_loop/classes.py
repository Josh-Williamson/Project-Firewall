import pygame
from pygame import event
import csv

TILE_TYPES = 1
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600



class Window:
    def __init__(window):
        window.width = SCREEN_WIDTH
        window.height = SCREEN_HEIGHT
        window.color = pygame.Color(255, 0, 255)
        window.caption = "Project Firewall"
        window.display = pygame.display.set_mode((window.width, window.height))


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


class Enemy(pygame.sprite.Sprite):
  def __init__(self, pos, image, hp, damage, speed):
    pygame.sprite.Sprite.__init__(self)
    hp = 0
    damage = 0
    speed = 0
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = pos

class Tower(pygame.sprite.Sprite):
  def __init__(self, pos, image, cost, projectile):
    pygame.sprite.Sprite.__init__(self)
    cost = 0
    projectile = 0
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def draw(self, screen):
      screen.blit(self.image, self.rect)

class Projectile(pygame.sprite.Sprite):
  def __init__(self, pos, image, damage, speed):
    pygame.sprite.Sprite.__init__(self)
    damage = 0
    speed = 0
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def draw(self, screen):
      screen.blit(self.image, self.rect)

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

        i = 0
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



    def LoadImageList(self):
        for x in range(TILE_TYPES + 1):
            image = pygame.image.load(f'assets/tile/{x}.png').convert_alpha()
            image = pygame.transform.scale(image, (self.tileSize, self.tileSize))
            self.imageList.append(image)
            print(x)

    def DrawGrid(self, window):
        for row in range(self.rows):
            pygame.draw.line(window.display, (0,0,0), (0, row * self.tileSize),
                             (window.width, row * self.tileSize))
        for column in range(self.columns):
            pygame.draw.line(window.display, (0,0,0), (column * self.tileSize, 0),
                             (column * self.tileSize, window.height))

    def DrawTileImage(self):
        for y, row in enumerate(self.gridMap):
            for x, tile in enumerate(row):
                if tile != 0:
                    image = self.imageList[tile]
                    pygame.display.get_surface().blit(image,
                                                      (x * self.tileSize, y * self.tileSize))

    def getTilePosition(self):
        pos = pygame.mouse.get_pos()
        x = int(pos[0]/self.tileSize)
        y = int(pos[1]/self.tileSize)
        return [x, y]

    def getTileValueAtMousePosition(self):
        pos = self.getTilePosition()
        row = pos[0]
        column = pos[1]
        if row <= self.rows and column <= self.columns:
            tile = self.gridMap[row][column]
        print("getTileValueAtMousePosition", tile)
        return tile




        #use in placement events and map drawing for tile locations
    def updateTile(self, column, row, value):
        print("value = ", value)
        print("x, y=", column, row)
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















