#! /usr/bin/env pxthon3
# coding: utf-8

import random
from player import Player
from objects import Objects
from inventory import Inventory

class Level:

    """Class setting up the level map 15x15 cells,
    Draw of the level is on level.txt file with following parameters:

    # = Wall
    - = Path
    0 = Start (and Mcgaxver initial position)
    1 = End
    G = Guardian position """

    def __init__(self):
        self.coord = {}
        self.path = []
        self.walls = []
        self.player_map_pos = ()
        self.objects_places = {}

    def grid_gen(self):

        y, x = 1, 0 # y désigne les lignes et x désigne les colonnes
        with open("level.txt", "r") as file:
            for line in file:  # pour chaque ligne dans le fichier
                for element in line:  # pour chaque element dans chaque ligne
                    if element != '\n': # sauf si l'élément n'est pas un retour à la ligne
                        x = x + 1 # rajoute +1 à la valeur x pour chaque élément.
                        self.coord[(y, x)] = element # rajoute au dico les coordonnées y et x en clé avec la valeur élément de chaque cell
                    if element == '-': # si l'élément est un chemin
                        self.path.append((y, x)) #rajoute à la liste des chemins les coordonnées du chemin
                    if element == '#':
                        self.walls.append((y,x))
                y, x = y + 1, 0 # rajoute +1 à la valeur y pour chaque ligne.

    def print_grid(self): # print la grille self.coord de manière représentative sur 15x15

        count = 0
        for val in self.coord.values():
            print(val, end='') #end = '' permet de print sur une seule ligne
            count = count + 1 
            if count % 15 == 0:
                print("\n")

     
    def place_objects(self):

        for name in objects.names: 
            number_of_choices = 1
            random.shuffle(self.path)
            self.objects_places[name] = self.path[number_of_choices]

        for obj_key, obj_val in self.objects_places.items():
            for key, val in self.coord.items():
                if obj_val == key:
                    self.coord[key] = obj_key

        return self.objects_places


    def moove_on_map(self):

        # if macgyver.player_position in self.objects_places:
        #     for val in self.objects_places.values():
        #         if macgyver.player_position == val:
        #             inventory.stock.append("quelque chose")
        #             print("player a rammassé un objet")

        if macgyver.player_newposition in self.walls:
            macgyver.player_newposition = False
            print("la destination est un mur, je n'avance pas")

        elif macgyver.player_position in self.coord:
            for key, val in self.coord.items():
                if macgyver.player_position == key:
                    self.coord[key] = macgyver.player
                elif macgyver.player == val:
                    self.coord[key] = "-"

        else:
            macgyver.player_newposition = False
            print("la destination est hors jeu")

        self.player_map_pos = macgyver.player_newposition
        return self.player_map_pos

level = Level()
level.grid_gen()
macgyver = Player("MG",1,1)
objects = Objects(("ether", "tube", "needle"))
inventory = Inventory()

if __name__ == "__main__":

    # print("\n\nlevel : \n\n", level.coord, "\n\npath : \n\n",
    #       level.path, "\n\nwalls : \n\n", level.walls)

  
    print("\n start position: ", macgyver.player_position, "\n")

    print("place objects: ", level.place_objects(),"\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")
    
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("up"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("right"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("down"), "\n")

    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")
    print("new position: ", level.moove_on_map(), macgyver.moove("left"), "\n")

    print(level.print_grid())
    print(inventory.stock)
