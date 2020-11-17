#! /usr/bin/env python3
# coding: utf-8

""" This module generate Macgyver """


class Player:
    """Class setting up the main human player macgyver:
        """

    def __init__(self, name, coo_y, coo_x):
        self.player = name
        self.coo_x = coo_x
        self.coo_y = coo_y
