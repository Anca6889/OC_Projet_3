#! /usr/bin/env python3
# coding: utf-8

class Level:

    """Class setting up the level map 15x15 cells,
    Draw of the level is on level.txt file with following parameters:

    # = Wall
    - = Path
    0 = Start (and Mcgayver initial position)
    1 = End
    G = Guardian position """

    def __init__(self):
        self.coord = {}
        self.path = []

    def grid_gen(self):
        """ Generate a virtual grid with level.txt file.
            Give x and y coordonates for each cell
            Get the all the paths in a separate list """

        x, y = 1, 0 # x désigne les lignes et y désigne les colonnes
        with open("level.txt", "r") as file: 
            for line in file:  # pour chaque ligne dans le fichier
                for element in line:  # pour chaque element dans chaque ligne
                    if element != '\n': # sauf si l'élément n'est pas un retour à la ligne
                        y = y + 1 # rajoute +1 à la valeur y pour chaque élément.
                        self.coord[(x, y)] = element # rajoute au dico les coordonnées x et y en clé avec la valeur élément de chaque cell
                    if element == '-': # si l'élément est un chemin
                        self.path.append((x, y)) #rajoute à la liste des chemins les coordonnées du chemin
                x, y = x + 1, 0 # rajoute +1 à la valeur x pour chaque ligne.


level = Level()
level.grid_gen()
print("\n\nlevel : \n\n", level.coord, "\n\npath : \n\n", level.path)
