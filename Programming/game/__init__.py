import pygame
import sys
from game.constants import Constants
from game.player import Player
from game.ball import Ball
from game.bricks import Bricks

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font('assets/Kenney_Future_Square.ttf',16)
        self.bg_color = pygame.Color("black")

        self.player = Player()
        self.ball = Ball()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player,self.ball)

        self.bricks = Bricks(self.all_sprites)


    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pass

    def update(self):
        if self.ball.is_off_screen():
            self.player.lose_life()
            self.ball.reset()
        self.ball.check_collide_paddle(self.player)
        self.all_sprites.update()
        pygame.display.update()
        self.clock.tick(120)



    def draw(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)