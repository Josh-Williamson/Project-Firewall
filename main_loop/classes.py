import pygame

TILE_TYPES = 1
ENEMY_TYPES = 1
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


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

    def get_renderTextList(self=None):
        return renderTextList

    def get_textRectangleList(self=None):
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
