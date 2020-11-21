"""" This module generate the map and the characters /objects on the map """

# ! /usr/bin/env python3
# coding: utf-8

import random
from classes.player import Player
from classes.guardian import Guardian
from classes.config_classes import OBJECTS


class Level:
    """ Class setting up the level map 15x15 cells, spawning the objects on
        random position and managing the movements of the player
        draw of the level is on level.txt file with following parameters:

        # = Wall
        - = Path
        M = Macgyver position
        1 = End
        G = Guardian position
        """

    def __init__(self):

        self.coord = {}
        self.path = []
        self.macgyver = None
        self.guardian = None
        self.inventory = []
        self.grid_gen()
        self.set_objects()
        self.getters = {}
        self.get_info()

    def grid_gen(self):
        """ Generate a virtual grid with map_x and map_y coordonates
            and stock them in a dictionary.
            Create the guardian and the player objects
            isolate the coordonates of the paths
            """

        map_y, map_x = 0, 0
        with open("ressource/level.txt", "r") as file:
            for line in file:
                for element in line:
                    if element != '\n':
                        map_x = map_x + 1
                        self.coord[(map_y, map_x)] = element
                    if element == '-':
                        self.path.append((map_y, map_x))
                    if element == 'M':
                        self.macgyver = Player("macgyver", map_y, map_x)
                    if element == 'G':
                        self.guardian = Guardian("guardian", map_y, map_x)
                map_y, map_x = map_y + 1, 0

    def set_objects(self):
        """ Spawn the objects to random positions on the paths """

        random.shuffle(self.path)
        for key, obj in enumerate(OBJECTS):
            self.coord[self.path[key]] = obj

    def get_info(self):
        """ This fonctions setup bolean values for get informations
            in the game script, pickobject and killguardian are
            used for play a mini sound, gamewined and gamelost
            will be used for switch to win or game-over menus """

        self.getters = {"gamewined": False, "gamelost": False,
                        "pickobject": False, "killguardian": False}

    def move(self, direction):
        """ Control the movements of the player on the map
            check what each cell contain and alow or not
            the player to moove, pick object, pass or not
            the guardian, win or loose the game """

        # Move the player:
        if direction == "right":
            new_coo = (self.macgyver.coo_y, self.macgyver.coo_x+1)
        if direction == "left":
            new_coo = (self.macgyver.coo_y, self.macgyver.coo_x-1)
        if direction == "up":
            new_coo = (self.macgyver.coo_y-1, self.macgyver.coo_x)
        if direction == "down":
            new_coo = (self.macgyver.coo_y+1, self.macgyver.coo_x)

        # check what cell contain :
        if new_coo in self.coord:
            new_cell_content = self.coord[new_coo]

            if new_cell_content == '-':
                self.coord[(self.macgyver.coo_y, self.macgyver.coo_x)] = "-"
                self.coord[new_coo] = 'M'
                self.macgyver.coo_y = new_coo[0]
                self.macgyver.coo_x = new_coo[1]
                self.getters["pickobject"] = False

            if new_cell_content in OBJECTS:
                self.coord[(self.macgyver.coo_y, self.macgyver.coo_x)] = "-"
                self.inventory.append(new_cell_content)
                self.coord[new_coo] = 'M'
                self.macgyver.coo_y = new_coo[0]
                self.macgyver.coo_x = new_coo[1]
                self.getters["pickobject"] = True

            if new_cell_content == 'G':
                if len(self.inventory) == 3:
                    self.coord[(self.macgyver.coo_y,
                                self.macgyver.coo_x)] = "-"
                    self.coord[new_coo] = 'M'
                    self.macgyver.coo_y = new_coo[0]
                    self.macgyver.coo_x = new_coo[1]
                    self.getters["pickobject"] = False
                    self.getters["killguardian"] = True
                else:
                    self.getters["gamelost"] = True

            if new_cell_content == '1':
                self.coord[(self.macgyver.coo_y, self.macgyver.coo_x)] = "-"
                self.coord[new_coo] = 'M'
                self.macgyver.coo_y = new_coo[0]
                self.macgyver.coo_x = new_coo[1]
                self.getters["pickobject"] = False
                self.getters["gamewined"] = True
        else:
            pass
