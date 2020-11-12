#! /usr/bin/env python3
# coding: utf-8

import pygame
from display.config_display import gameover_dis
from display.config_display import tryagain_dis

class GameOver(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.gameover = pygame.image.load(gameover_dis).convert_alpha()
        self.tryagain_button = pygame.image.load(tryagain_dis).convert_alpha()
        self.tryagain_button_rect = self.tryagain_button.get_rect()
        self.tryagain_button_rect.x = 125
        self.tryagain_button_rect.y = 400
        self.descript_text = pygame.font.SysFont('freesansbold.ttf', 60)
        self.descript_text_surface = self.descript_text.render(
            " YOU'VE LOST! ", True, (255, 255, 255))
        self.descript_text_rect = self.descript_text_surface.get_rect()
        self.descript_text_rect.center = (320, 250)
