#! /usr/bin/env python3
# coding: utf-8

from level import level

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
        
        newplayer_position = self.player_position[0], self.player_position[1]+1
        
        if newplayer_position in level.coord:
            for key, val in level.coord.items():
                if newplayer_position == key:
                    if val == "#":
                        newplayer_position = self.player_position[0], self.player_position[1]
                        print("la destination est un mur, je n'avance pas")   
                    
        else:
            newplayer_position = self.player_position[0], self.player_position[1]
            print("la destination est hors jeu")
        
        self.player_position = newplayer_position
        return self.player_position

    def moove_left(self):

        newplayer_position = self.player_position[0], self.player_position[1]-1

        if newplayer_position in level.coord:
            for key, val in level.coord.items():
                if newplayer_position == key:
                    if val == "#":
                        newplayer_position = self.player_position[0], self.player_position[1]
                        print("la destination est un mur, je n'avance pas")

        else:
            newplayer_position = self.player_position[0], self.player_position[1]
            print("la destination est hors jeu")

        self.player_position = newplayer_position
        return self.player_position

    def moove_up(self):

        newplayer_position = self.player_position[0]-1, self.player_position[1]

        if newplayer_position in level.coord:
            for key, val in level.coord.items():
                if newplayer_position == key:
                    if val == "#":
                        newplayer_position = self.player_position[0], self.player_position[1]
                        print("la destination est un mur, je n'avance pas")

        else:
            newplayer_position = self.player_position[0], self.player_position[1]
            print("la destination est hors jeu")

        self.player_position = newplayer_position
        return self.player_position

    def moove_down(self):

        newplayer_position = self.player_position[0]+1, self.player_position[1]

        if newplayer_position in level.coord:
            for key, val in level.coord.items():
                if newplayer_position == key:
                    if val == "#":
                        newplayer_position = self.player_position[0], self.player_position[1]
                        print("la destination est un mur, je n'avance pas")

        else:
            newplayer_position = self.player_position[0], self.player_position[1]
            print("la destination est hors jeu")

        self.player_position = newplayer_position
        return self.player_position
        

            

player1 = Player("Macgyver")

print("\n\n","start position : ", player1.start_pos(), "\n")
print("new position (right) : ", player1.moove_right(),"\n")
print("new position (right) : ", player1.moove_right(),"\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (left) : ", player1.moove_left(), "\n")
print("new position (down) : ", player1.moove_down(), "\n")
print("new position (down) : ", player1.moove_down(), "\n")
print("new position (right) : ", player1.moove_right(), "\n")
print("new position (up) : ", player1.moove_up(), "\n")

