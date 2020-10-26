#! /usr/bin/env pxthon3
# coding: utf-8

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

    def grid_gen(self):
        """ Generate a virtual grid with level.txt file.
            Give y and x coordonates for each cell
            Get the all the paths in a separate list """

        y, x = 1, 0 # y désigne les lignes et x désigne les colonnes
        with open("level.txt", "r") as file: 
            for line in file:  # pour chaque ligne dans le fichier
                for element in line:  # pour chaque element dans chaque ligne
                    if element != '\n': # sauf si l'élément n'est pas un retour à la ligne
                        x = x + 1 # rajoute +1 à la valeur x pour chaque élément.
                        self.coord[(y, x)] = element # rajoute au dico les coordonnées y et x en clé avec la valeur élément de chaque cell
                    if element == '-': # si l'élément est un chemin
                        self.path.append((y, x)) #rajoute à la liste des chemins les coordonnées du chemin
                y, x = y + 1, 0 # rajoute +1 à la valeur y pour chaque ligne.


level = Level()
level.grid_gen()
print("\n\nlevel : \n\n", level.coord, "\n\npath : \n\n", level.path)
