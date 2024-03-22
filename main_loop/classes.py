import pygame

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

    def InitiateGridMap(self):
        self.gridMap.clear()
        for row in range(self.rows):
            row = [-1] * self.columns
            self.gridMap.append(row)

    def LoadImageList(self):
        for x in range(TILE_TYPES):
            image = pygame.image.load(f'assets/tile/{x}.png').convert_alpha()
            image = pygame.transform.scale(image, (self.tileSize, self.tileSize))
            self.imageList.append(image)

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
                if tile >= 0:
                    pygame.display.get_surface().blit(self.imageList[tile], (x * self.tileSize, y * self.tileSize))

    #use in placement events and map drawing for tile locations
    def updateTile(self, x, y, value):
        for tile in range(0, self.rows):
            self.gridMap[x - 1][y] = value
        print(self.gridMap)














