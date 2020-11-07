#! /usr/bin/env pxthon3
# coding: utf-8

# from level import level
# from objects import objects
# from inventorx import inventorx

class Player:
    """Class setting up the character Macgxver who is the main human player:
        """

    def __init__(self, name, coo_y, coo_x):
        self.player = name
        self.coo_x = coo_x
        self.coo_y = coo_y
