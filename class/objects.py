#! /usr/bin/env python3
# coding: utf-8
import random
# from level import level

class Objects:
    """ Class creating the objectss needle, ether, tube
        with following attributes:
            name
            position on the map """

    def __init__(self, names):
        self.names = (names)