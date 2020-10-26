#! /usr/bin/env python3
# coding: utf-8
import random
from level import level

class Object:
    """ Class creating the objects needle, ether, syringe
        with following attributes:
            name
            position on the map """

    def __init__(self, name):
        self.name = name
        self.position = [random.choice(level.path)]
        # ne trouve pas comment faire pour ne pas avoir deux fois la même clé
        
    def get_position(self):
        return self.position

ether = Object("ether")
needle = Object("needle")
syringe = Object("syringe")
ether.get_position()
needle.get_position()
syringe.get_position()
print("\n\nether position : \n\n", ether.get_position(),
      "\n\nneedle position : \n\n", needle.get_position(), 
      "\n\nsyringe position : \n\n", syringe.get_position())
