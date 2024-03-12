import pygame
from attributes import Create_and_Return_window, UpdateWindowAttributes
from update_methods import updateDisplayScreen


pygame.init()

window = Create_and_Return_window()
color = "red"
UpdateWindowAttributes(window, color)

pygame.display.set_caption("Project Firewall")

keep_game_running = True

while keep_game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_game_running = False

    UpdateWindowAttributes(window, color="green")
    updateDisplayScreen()


else:
    pygame.quit()
