#! /usr/bin/env python3
# coding: utf-8

from level import level
from objects import ether
from objects import needle
from objects import syringe
from inventory import inventory

class Player:
    """Class setting up the character Macgyver who is the main human player:

        size in labyrinth: 1x1 cell
        moving methods with keyboard arrows
        setting up starting posistion (0)
        speed of mouvement

        """
    def __init__(self, player):

        self.player = player
        self.player_position = ()
    
        
        #Pour mouvements:

        #rappel (y,x)= éléments
        #si déplacement à droite = x+1
        #si déplacement à gauche = x-1
        #si déplacement en haut = y-1
        #si déplacement à bas = y+1

    def start_pos(self):
        for key, val in level.coord.items():
            if val == "0":
                self.player_position = key
        return self.player_position

    def moove_right(self):
        
        player_newposition = self.player_position[0], self.player_position[1]+1
        
        if player_newposition in level.coord:
            for key, val in level.coord.items():
                if player_newposition == key:
                    if val == "#":
                        player_newposition = self.player_position[0], self.player_position[1]
                        print("la destination est un mur, je n'avance pas")

                    elif player_newposition == ether.position:
                        inventory.stock.append(ether.name)
                        print("player a rammassé l'éther")
                        

                    elif player_newposition == needle.position:
                        inventory.stock.append(needle.name)
                        print("player a rammassé l'aguille")

                    elif player_newposition == syringe.position:
                        inventory.stock.append(syringe.name)
                        print("player a rammassé la sereingue")

        else:
            player_newposition = self.player_position[0], self.player_position[1]
            print("la destination est hors jeu")
        
        self.player_position = player_newposition
        return self.player_position
        return inventory.stock

    def moove_left(self):

        player_newposition = self.player_position[0], self.player_position[1]-1

        if player_newposition in level.coord:
            for key, val in level.coord.items():
                if player_newposition == key:
                    if val == "#":
                        player_newposition = self.player_position[0], self.player_position[1]
                        print("la destination est un mur, je n'avance pas")

                    elif player_newposition == ether.position:
                        inventory.stock.append(ether.name)
                        print("player a rammassé l'éther")

                    elif player_newposition == needle.position:
                        inventory.stock.append(needle.name)
                        print("player a rammassé l'aguille")

                    elif player_newposition == syringe.position:
                        inventory.stock.append(syringe.name)
                        print("player a rammassé la sereingue")

        else:
            player_newposition = self.player_position[0], self.player_position[1]
            print("la destination est hors jeu")

        self.player_position = player_newposition
        return self.player_position
        return inventory.stock

    def moove_up(self):

        player_newposition = self.player_position[0]-1, self.player_position[1]

        if player_newposition in level.coord:
            for key, val in level.coord.items():
                if player_newposition == key:
                    if val == "#":
                        player_newposition = self.player_position[0], self.player_position[1]
                        print("la destination est un mur, je n'avance pas")

                    elif player_newposition == ether.position:
                        inventory.stock.append(ether.name)
                        print("player a rammassé l'éther")

                    elif player_newposition == needle.position:
                        inventory.stock.append(needle.name)
                        print("player a rammassé l'aguille")
                        
                    elif player_newposition == syringe.position:
                        inventory.stock.append(syringe.name)
                        print("player a rammassé la sereingue")

        else:
            player_newposition = self.player_position[0], self.player_position[1]
            print("la destination est hors jeu")

        self.player_position = player_newposition
        return self.player_position
        return inventory.stock

    def moove_down(self):

        player_newposition = self.player_position[0]+1, self.player_position[1]

        if player_newposition in level.coord:
            for key, val in level.coord.items():
                if player_newposition == key:
                    if val == "#":
                        player_newposition = self.player_position[0], self.player_position[1]
                        print("la destination est un mur, je n'avance pas")

                    elif player_newposition == ether.position:
                        inventory.stock.append(ether.name)
                        print("player a rammassé l'éther")

                    elif player_newposition == needle.position:
                        inventory.stock.append(needle.name)
                        print("player a rammassé l'aguille")

                    elif player_newposition == syringe.position:
                        inventory.stock.append(syringe.name)
                        print("player a rammassé la sereingue")

        else:
            player_newposition = self.player_position[0], self.player_position[1]
            print("la destination est hors jeu")

        self.player_position = player_newposition
        return self.player_position
        return inventory.stock

    def get_ether(self):
        return ether.position
    def get_needle(self):
        return needle.position
    def get_syringe(self):
        return syringe.position

#####################################################################################
#################################### TESTS ##########################################
#####################################################################################

player1 = Player("Macgyver")

# On génère le player sur sa case de départ:
print("\n\n","start position : ", player1.start_pos(), "\n")

# on test le bloquage bordures et murs:
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (right) : ", player1.moove_right(),"\n")
print("new position (right) : ", player1.moove_right(),"\n")

# on parcourt la moitié haute la map pour tester de (1,1) à (7,15):
print("new position (down) : ", player1.moove_down(), "\n")
print("new position (down) : ", player1.moove_down(), "\n")
print("new position (down) : ", player1.moove_down(), "\n")

print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")

print("new position (up) : ", player1.moove_up(), "\n")
print("new position (up) : ", player1.moove_up(), "\n")
print("new position (up) : ", player1.moove_up(), "\n")

print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")

print("new position (down) : ", player1.moove_down(), "\n")
print("new position (down) : ", player1.moove_down(), "\n")

print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")

print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")

print("new position (up) : ", player1.moove_up(), "\n")
print("new position (up) : ", player1.moove_up(), "\n")

print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")

print("new position (down) : ", player1.moove_down(), "\n")
print("new position (down) : ", player1.moove_down(), "\n")

print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")

print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")

print("new position (down) : ", player1.moove_down(), "\n")

print("new position (left) : ", player1.moove_left(), "\n")

print("new position (down) : ", player1.moove_down(), "\n")
print("new position (down) : ", player1.moove_down(), "\n")
print("new position (down) : ", player1.moove_down(), "\n")

print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")

print("new position (up) : ", player1.moove_up(), "\n")
print("new position (up) : ", player1.moove_up(), "\n")

print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")

print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")

print("new position (down) : ", player1.moove_down(), "\n")
print("new position (down) : ", player1.moove_down(), "\n")

print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")


# on vérifie la position des objects:
print("ether position:", player1.get_ether())
print("needle position:", player1.get_needle())
print("syringe position:", player1.get_syringe())

print("Inventory: ", inventory.stock)
