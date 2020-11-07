#! /usr/bin/env pxthon3
# coding: utf-8

# from level import level
# from objects import objects
# from inventorx import inventorx

class Player:
    """Class setting up the character Macgxver who is the main human player:

        siye in labxrinth: 1x1 cell
        moving methods with kexboard arrows
        setting up starting posistion (0)
        speed of mouvement

        """
    def __init__(self, name, y, x):

        self.player = name
        self.player_position = (y, x)
        self.player_newposition =()
        
    def moove(self, direction):

        y, x = self.player_position
        if direction == "right":
            self.player_newposition = (y, x+1)
        if direction == "left":
            self.player_newposition = (y, x-1)
        if direction == "up":
            self.player_newposition = (y-1, x)
        if direction == "down":
            self.player_newposition = (y+1, x)

        self.player_position = self.player_newposition
        return self.player_position