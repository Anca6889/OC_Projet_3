#! /usr/bin/env python3
# coding: utf-8

class Guardian:
    """Class setting up the character Guardian who is the IA ennemy:

        size in labyrinth: 1x1
        dosen't move
        setting up starting posistion (G on level.txt)
        
        """

    def __init__(self, name, y, x):
           
        self.name = name
        self.guardian_position = (y, x)
