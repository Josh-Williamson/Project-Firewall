import pygame



class Window():
    def __init__(window):
        window.width = 400
        window.height = 600
        window.color = pygame.Color(255, 0, 255)
        window.caption = "Project Firewall"
        window.display = pygame.display.set_mode((window.width, window.height))


    def CreateWindow(window):
        window.__init__()
        window.display = pygame.display.set_mode((window.width, window.height))
        window.display.fill(window.color)


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

    def CreateTextBox(self, window):
        self.__init__()
        self.renderText = self.font.render(self.text, True, self.textColor)
        self.textRectangle = self.renderText.get_rect()
        self.textRectangle.center = (window.width / 2, window.height / 2)
        renderTextList.append(self.renderText)
        textRectangleList.append(self.textRectangle)

    def RemoveTextBox(textBox):
        if renderTextList and textRectangleList:
            renderTextList.remove(textBox.renderText)
            textRectangleList.remove(textBox.textRectangle)
        else:
            return

"""global """
def RenderTextBox(window):
    for text in renderTextList:
        for rect in textRectangleList:
            window.display.blit(text, rect)






