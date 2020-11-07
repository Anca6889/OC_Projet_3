#! /usr/bin/env python3
# coding: utf-8

import random
from player import Player
from guardian import Guardian
from inventory import Inventory
from config import OBJECTS


class Level:

    """Class setting up the level map 15x15 cells,
    Draw of the level is on level.txt file with following parameters:

    # = Wall
    - = Path
    M = Macgyver position
    1 = End
    G = Guardian position """

    def __init__(self):

        self.coord = {}
        self.path = []
        self.macgyver = None
        self.guardian = None
        self.inventory = []
        self.grid_gen()
        self.set_objects()
       

    def grid_gen(self):
        y, x = 1, 0  # y désigne les lignes et x désigne les colonnes
        with open("level.txt", "r") as file:
            for line in file:  # pour chaque ligne dans le fichier
                for element in line:  # pour chaque element dans chaque ligne
                    if element != '\n':  # sauf si l'élément n'est pas un retour à la ligne
                        # rajoute +1 à la valeur x pour chaque élément.
                        x = x + 1
                        # rajoute au dico les coordonnées y et x en clé avec la valeur élément de chaque cell
                        self.coord[(y, x)] = element
                    if element == '-':  # si l'élément est un chemin
                        # rajoute à la liste des chemins les coordonnées du chemin
                        self.path.append((y, x))
                    if element == 'M':
                        self.macgyver = Player("macgyver", y, x)
                    if element == 'G':
                        self.guardian = Guardian("guardian", y, x)
                y, x = y + 1, 0  # rajoute +1 à la valeur y pour chaque ligne.

    def set_objects(self):
        random.shuffle(self.path)
        for key, obj in enumerate(OBJECTS):
            self.coord[self.path[key]] = obj

    def move(self, direction):
        # récupération des nouvelles coordonnées
        if direction == "right":
            new_coo = (self.macgyver.coo_y, self.macgyver.coo_x+1)
        if direction == "left":
            new_coo = (self.macgyver.coo_y, self.macgyver.coo_x-1)
        if direction == "up":
            new_coo = (self.macgyver.coo_y-1, self.macgyver.coo_x)
        if direction == "down":
            new_coo = (self.macgyver.coo_y+1, self.macgyver.coo_x)

        # est-ce qu'on peut bouger ?
        # est-ce que les coordonnées existent ?
        if self.coord[new_coo]:
            # récupération du contenu de la case
            new_cell_content = self.coord[new_coo]
            # on peut bouger si : new_cell_content est un chemin
            if new_cell_content == '-':
                # on bouge macgyver aux nouvelles coordonnées,
                # et on remplace les anciennes par un chemin
                self.path[(self.macgyver.coo_y, self.macgyver.coo_x)] = "-"
                self.path[new_coo] = 'M'
                # MAJ coo macgyver dans l'objet
                self.macgyver.coo_y = new_coo[0]
                self.macgyver.coo_x = new_coo[1]

            # on peut bouger si : new_cell_content est un objet
            if new_cell_content in OBJECTS:
                # on bouge macgyver aux nouvelles coordonnées,
                # et on remplace les anciennes par un chemin
                self.path[(self.macgyver.coo_y, self.macgyver.coo_x)] = "-"
                # on ramasse l'objet
                self.inventory.append(new_cell_content)
                self.path[new_coo] = 'M'
                # MAJ coo macgyver dans l'objet
                self.macgyver.coo_y = new_coo[0]
                self.macgyver.coo_x = new_coo[1]

            # on peut bouger si : new_cell_content est le gardien et qu'on a tous les objets
            if new_cell_content == 'G':
                # on bouge macgyver aux nouvelles coordonnées,
                # et on remplace les anciennes par un chemin
                if self.inventory.count() == 3:
                    self.path[(self.macgyver.coo_y, self.macgyver.coo_x)] = "-"
                    self.path[new_coo] = '0'
                    # MAJ coo macgyver dans l'objet
                    self.macgyver.coo_y = new_coo[0]
                    self.macgyver.coo_x = new_coo[1]

    def print_grid(self):  # print la grille self.coord de manière représentative sur 15x15
        count = 0
        for val in self.coord.values():
            print(val, end='')  # end = '' permet de print sur une seule ligne
            count = count + 1
            if count % 15 == 0:
                print("\n")

if __name__ == "__main__":

    level = Level()
    print(level.move("right"))
    print(level.print_grid())
    
    # print("\n\nlevel : \n\n", level.coord, "\n\npath : \n\n",
    # #       level.path, "\n\nwalls : \n\n", level.walls)

    # print("\n start position: ", macgyver.player_position, "\n")

    # print("place objects: ", level.place_objects(),"\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    # print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    # print(level.print_grid())
    # print(inventory.stock)
