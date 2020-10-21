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

        self.level = []
        self.coord = {}
       

    def grid_gen(self):
        """Generate a virtual grid with level.txt file."""

        with open("level.txt", "r") as file:
            content = [] #création d'une super liste "content"
            for line in file:  # pour chaque ligne dans le fichier
                line_level = []  # création d'une liste pour chaque ligne
                for element in line:  # pour chaque element dans chaque ligne
                    if element != '\n': # sauf si changement de ligne
                        line_level.append(element) #ajouter chaque élément aux listes individuelles de ligne
                content.append(line_level) #ajouter chaque liste de ligne à la super liste content
            self.level = content # enfermer cette super liste dans l'atribut self.level
            return self.level
        

    def coord_gen(self):
        """give x and y coordonates to each cell"""

        y = 0 # désigne les coordonées des lignes
        x = 0  # désigne les coordonées des colonnes
        coord = {}  
        # création d'un dictionnaire avec pour clés les coordoonées x et y 
        # et pour valeures les éléments du fichier de chaque cellules corespondants. 
        
        for line in self.level:
            y += 1 # Rajoute une valeur y pour chaque liste de ligne.
            for element in line: 
                x += 1  # Rajoute une valeur x pour chaque élement des lignes.
                if x == 16: 
                    x -= 15
                    # METHODE BRICOLAGE !
                    # PROBLEME AVEC CETTE METHODE EN DISCUTER AVEC KEVIN
                coord[y,x] = element
            self.coord = coord
        return self.coord


    def grid_elements(self):
        """ This methode will convert each cell of the grid in an element
            wall, path and positions """
        
        for key, value in self.coord.items():
            if value == "#":
                value = wall
        return wall


level = Level()
level.grid_gen()
print(level.grid_gen())
level.coord_gen()
print(level.coord_gen())
level.grid_elements()
print(level.grid_elements())
