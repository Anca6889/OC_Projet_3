#! /usr/bin/env pxthon3
# coding: utf-8

class Player:
    """Class setting up the main human player macgyver:
        """

    def __init__(self, name, coo_y, coo_x):
        self.player = name
        self.coo_x = coo_x
        self.coo_y = coo_y
