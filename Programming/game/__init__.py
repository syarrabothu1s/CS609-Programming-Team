import pygame
import sys
from game.constants import Constants

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font('assets/Kenney_Future_Square.ttf',16)

        self.bg_color = pygame.Color("black")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_color)