""" This module set up the main menu """

# ! /usr/bin/env python3
# coding: utf-8

from display import config_display as cg
import pygame as pg


class MainMenu(pg.sprite.Sprite):
    """ This class setup the main menu display when game is lauched """

    def __init__(self):

        super().__init__()
        self.background = pg.image.load(cg.BACKGROUND_DIS).convert_alpha()
        self.pbut = pg.image.load(cg.PLAY_DIS).convert_alpha()
        self.pbut_rect = self.pbut.get_rect()
        self.pbut_rect.x = cg.PLAY_BUTTON_RECT_X
        self.pbut_rect.y = cg.PLAY_BUTTON_RECT_Y
