""" This module set up the game-over menu """

# ! /usr/bin/env python3
# coding: utf-8

from display import config_display as cg
import pygame as pg


class GameOver(pg.sprite.Sprite):
    """ This class setup the game-over display when player lose the game """

    def __init__(self):

        super().__init__()
        self.background = pg.image.load(cg.GOBACK_DIS).convert_alpha()
        self.gbut = pg.image.load(cg.TRYAGAIN_DIS).convert_alpha()
        self.gbut_rect = self.gbut.get_rect()
        self.gbut_rect.x = cg.BUTTON_RECT_X
        self.gbut_rect.y = cg.BUTTON_RECT_Y
