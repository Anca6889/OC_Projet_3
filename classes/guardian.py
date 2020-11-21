""" This module set up the ennemy of the game """

# ! /usr/bin/env python3
# coding: utf-8


class Guardian:
    """Class setting up the guardian who is the ennemy """

    def __init__(self, name, y, x):

        self.name = name
        self.guardian_position = (y, x)
