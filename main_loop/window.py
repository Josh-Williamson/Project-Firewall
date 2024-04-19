import pygame


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Window():
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.color = pygame.Color(255, 0, 255)
        self.caption = "Project Firewall"
        self.display = pygame.display.set_mode((self.width, self.height))

        self.surface = pygame.surface.Surface([self.width, self.height])

        self.image = self.getBackground(1)
        

    def updateBackground(self):
        self.display.blit(self.image, (0,0))

    def getBackground(self, level):
        background_image = pygame.image.load(f"assets/backgrounds/{level}.png").convert_alpha()
        image = pygame.transform.scale(background_image, (self.width, self.height))
        return image
