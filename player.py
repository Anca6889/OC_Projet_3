#! /usr/bin/env python3
# coding: utf-8

class Player:
    """Class setting up the character Macgyver who is the main human player:

        size in labyrinth: 1x1 cell
        moving methods with keyboard arrows
        setting up starting posistion (0)
        speed of mouvement

        """
    def __init__(self, size, position, speed ):

        self.size = size
        self.position = position
        self.speed = speed


