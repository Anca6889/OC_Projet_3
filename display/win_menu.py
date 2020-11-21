""" This module set up the win menu """

# ! /usr/bin/env python3
# coding: utf-8

from display import config_display as cg
import pygame as pg


class Win(pg.sprite.Sprite):
    """ This class setup the win display when player win the game """

    def __init__(self):

        super().__init__()
        self.background = pg.image.load(cg.WINBACK_DIS).convert_alpha()
        self.wbut = pg.image.load(cg.TRYAGAIN_DIS).convert_alpha()
        self.wbut_rect = self.wbut.get_rect()
        self.wbut_rect.x = cg.BUTTON_RECT_X
        self.wbut_rect.y = cg.BUTTON_RECT_Y
