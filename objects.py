#! /usr/bin/env python3
# coding: utf-8
import random
from level import level

class Objects:
    """ Class creating the objectss needle, ether, syringe
        with following attributes:
            name
            position on the map """

    def __init__(self, name):
        self.name = name
        self.position = random.choice(level.path)
        # ne trouve pas comment faire pour ne pas avoir deux fois la même clé
        
    def get_position(self):
        return self.position

    # def destroy(self):
    #     self.destroy = pop(self.position)


ether = Objects("ether")
needle = Objects("needle")
syringe = Objects("syringe")

print("\n\nether position : \n\n", ether.get_position(),
      "\n\nneedle position : \n\n", needle.get_position(), 
      "\n\nsyringe position : \n\n", syringe.get_position())
