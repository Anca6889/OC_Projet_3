""" This module set up the map display """

# ! /usr/bin/env python3
# coding: utf-8

import pygame as pg
from display import config_display as cg


class LevelDisplay(pg.sprite.Sprite):
    """ This class setup the level display """

    def __init__(self):

        super().__init__()
        self.data = {}
        self.data_gen()

    def data_gen(self):
        """ this methode give images to all level elements """

        self.data = {"walls": pg.image.load(
            cg.WALLS_DIS).convert_alpha(),
            "path": pg.image.load(cg.PATH_DIS).convert_alpha(),
            "ether": pg.image.load(
            cg.ETHER_DIS).convert_alpha(),
            "needle": pg.image.load(
            cg.NEEDLE_DIS).convert_alpha(),
            "tube": pg.image.load(cg.TUBE_DIS).convert_alpha(),
            "guardian": pg.image.load(
            cg.GUARDIAN_DIS).convert_alpha(),
            "macgyver": pg.image.load(
            cg.MACGYVER_DIS).convert_alpha(),
            "door": pg.image.load(cg.DOOR_DIS).convert_alpha()}
