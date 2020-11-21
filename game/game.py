""" This module run the all game """

# ! /usr/bin/env python3
# coding: utf-8

from classes.level import Level
from display.level_display import LevelDisplay
from display.inventory_display import InventoryDisplay
from display.main_menu import MainMenu
from display.gameover_menu import GameOver
from display.win_menu import Win
from audio.audio import Audio
from game import config_game as cg
import pygame as pg


class Game:

    """ Class running the game with the following instructions:
        1) Display the main menu with the menu music
        2) Launch game when human player click on start button
        3) Run the game with game music
        4) Win the game if player reach the exit door
        4a) If game winned, diplay the win menu with win music
        5) Lose the game if collision with guardian without all objetcs
        5a) If game losed, diplay game-over menu with game-over music
        """

    def __init__(self):
        self.launch_game()
        self.data = {}
        self.screen = None
        self.loops = {}

    def data_gen(self):
        """ Instancy all the necessaries classes """

        self.data = {"menu": MainMenu(),
                     "audio": Audio(),
                     "level": Level(),
                     "map": LevelDisplay(),
                     "inventory": InventoryDisplay(),
                     "win": Win(),
                     "go": GameOver()}

    def display_gen(self):
        """ Creating the display 640x600 pixels"""

        pg.display.set_caption(cg.WINDOWTITLE)
        self.screen = pg.display.set_mode(cg.RES)

    def loop_conditions(self):
        """ Conditions variables maintaining the game running """

        self.loops = {"main_menu_running": True,
                      "game_running": True,
                      "win_menu_running": True,
                      "gameover_menu_running": True}

    def all_set_fonctions(self):
        """ play the 3 previous fonctions in one they are all necessary in
        each display
        """

        self.display_gen()
        self.data_gen()
        self.loop_conditions()

    def main_menu_gen(self):
        """ Generate the main menu display """

        self.screen.blit(
            self.data["menu"].background, cg.MAIN_MENU_POS)
        self.screen.blit(self.data["menu"].pbut,
                         (self.data["menu"].pbut_rect))

    def gameover_menu_gen(self):
        """ Generate the game-over menu display """

        self.screen.blit(
            self.data["go"].background, cg.MAIN_MENU_POS)
        self.screen.blit(self.data["go"].gbut,
                         (self.data["go"].gbut_rect))

    def win_menu_gen(self):
        """ Generate the win menu display """

        self.screen.blit(
            self.data["win"].background, cg.MAIN_MENU_POS)
        self.screen.blit(self.data["win"].wbut,
                         (self.data["win"].wbut_rect))

    def game_gen(self):
        """ Generate the game display """

        # Generate all the display of the map on cells of 40x40px
        # based on the level.txt file:
        for key, val in self.data["level"].coord.items():

            if val == "M":
                self.screen.blit(
                    self.data["map"].data["path"], (key[1] * cg.SPRITEPX,
                                                    key[0] * cg.SPRITEPX))
                self.screen.blit(
                    self.data["map"].data["macgyver"], (key[1] * cg.SPRITEPX,
                                                        key[0] * cg.SPRITEPX))
            if val == "#":
                self.screen.blit(
                    self.data["map"].data["walls"], (key[1] * cg.SPRITEPX,
                                                     key[0] * cg.SPRITEPX))
            if val == "-":
                self.screen.blit(
                    self.data["map"].data["path"], (key[1] * cg.SPRITEPX,
                                                    key[0] * cg.SPRITEPX))
            if val == "ether":
                self.screen.blit(
                    self.data["map"].data["path"], (key[1] * cg.SPRITEPX,
                                                    key[0] * cg.SPRITEPX))
                self.screen.blit(
                    self.data["map"].data["ether"], (key[1] * cg.SPRITEPX,
                                                     key[0] * cg.SPRITEPX))
            if val == "needle":
                self.screen.blit(
                    self.data["map"].data["path"], (key[1] * cg.SPRITEPX,
                                                    key[0] * cg.SPRITEPX))
                self.screen.blit(
                    self.data["map"].data["needle"], (key[1] * cg.SPRITEPX,
                                                      key[0] * cg.SPRITEPX))
            if val == "tube":
                self.screen.blit(
                    self.data["map"].data["path"], (key[1] * cg.SPRITEPX,
                                                    key[0] * cg.SPRITEPX))
                self.screen.blit(
                    self.data["map"].data["tube"], (key[1] * cg.SPRITEPX,
                                                    key[0] * cg.SPRITEPX))
            if val == "G":
                self.screen.blit(
                    self.data["map"].data["path"], (key[1] * cg.SPRITEPX,
                                                    key[0] * cg.SPRITEPX))
                self.screen.blit(
                    self.data["map"].data["guardian"], (key[1] * cg.SPRITEPX,
                                                        key[0] * cg.SPRITEPX))
            if val == "1":
                self.screen.blit(
                    self.data["map"].data["path"], (key[1] * cg.SPRITEPX,
                                                    key[0] * cg.SPRITEPX))
                self.screen.blit(
                    self.data["map"].data["door"], (key[1] * cg.SPRITEPX,
                                                    key[0] * cg.SPRITEPX))

    def inventory_gen(self):
        """ Generate the inventory display """

        # Display the inventory on the left side with
        # transparents objects (unpicked):
        self.screen.blit(self.data["inventory"].inventory,
                         cg.INVENTORY_POS)
        self.screen.blit(
            self.data["inventory"].ethertrans, cg.ETHER_POS)
        self.screen.blit(
            self.data["inventory"].needletrans, cg.NEEDLE_POS)
        self.screen.blit(
            self.data["inventory"].tubetrans, cg.TUBE_POS)
        self.screen.blit(self.data["inventory"].startrans,
                         cg.STAR_SYRINGE_POS)

        # When an object is picked, add the colourfull picture of
        # the object on the transparent picture (picked)
        # If all objects are picked, add a bonus picture of the syringe:
        if "ether" in self.data["level"].inventory:
            self.screen.blit(
                self.data["map"].data["ether"], cg.ETHER_POS)

        if "needle" in self.data["level"].inventory:
            self.screen.blit(
                self.data["map"].data["needle"], cg.NEEDLE_POS)

        if "tube" in self.data["level"].inventory:
            self.screen.blit(
                self.data["map"].data["tube"], cg.TUBE_POS)

        if len(self.data["level"].inventory) == 3:
            self.screen.blit(
                self.data["inventory"].star, cg.STAR_SYRINGE_POS)
            self.screen.blit(self.data["inventory"].syringe,
                             cg.STAR_SYRINGE_POS)

    def mini_sounds(self):
        """ Play mini sounds when object is picked and guardian killed """

        if self.data["level"].getters["pickobject"] is True:
            sound_obj = pg.mixer.Sound(self.data["audio"].pick_up_sound)
            sound_obj.play()

        if self.data["level"].getters["killguardian"] is True:
            pg.mixer.music.stop()
            sound_obj = pg.mixer.Sound(self.data["audio"].punch_sound)
            sound_obj.play(1)

    def launch_game(self):
        """ This method will lauch the game and setup the main_menu"""

        pg.init()
        self.all_set_fonctions()

        # Initialise main menu music:
        pg.mixer.init()
        pg.mixer.music.load(self.data["audio"].menu_music)
        pg.mixer.music.play(-1)

        # Main menu while loop running the main menu till player clik on start
        # button, when player click on start, the game while loop start:
        while self.loops["main_menu_running"] is True:

            self.main_menu_gen()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.data["menu"].pbut_rect.collidepoint(event.pos):
                        pg.mixer.music.load(self.data["audio"].level_music)
                        pg.mixer.music.play(-1)
                        self.run_game()

            pg.display.flip()

    def run_game(self):
        """ This method will run the game """

        self.all_set_fonctions()

        # Game while loop running the game till player win or lose:
        while self.loops["game_running"] is True:

            self.game_gen()
            self.inventory_gen()
            self.mini_sounds()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.loops["game_running"] = False
                    pg.quit()

                # Control the mooves of the player with keyboard arrows:
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        self.data["level"].move("right")
                    elif event.key == pg.K_LEFT:
                        self.data["level"].move("left")
                    elif event.key == pg.K_UP:
                        self.data["level"].move("up")
                    elif event.key == pg.K_DOWN:
                        self.data["level"].move("down")

            # Switch to Game-Over or Win menu with these conditions:
            if self.data["level"].getters["gamelost"] is True:
                pg.mixer.music.stop()
                pg.mixer.init()
                pg.mixer.music.load(self.data["audio"].gameover_music)
                pg.mixer.music.play(-1)
                self.run_game_over()

            if self.data["level"].getters["gamewined"] is True:
                pg.mixer.music.stop()
                pg.mixer.init()
                pg.mixer.music.load(self.data["audio"].win_fanfare)
                pg.mixer.music.play()
                self.run_win_menu()

            pg.display.flip()

    def run_game_over(self):
        """ This method setup the game over menu"""

        self.all_set_fonctions()

        while self.loops["gameover_menu_running"] is True:

            self.gameover_menu_gen()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                # Add a tryagain button if human player want to play again:
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.data["go"].gbut_rect.collidepoint(event.pos):
                        self.launch_game()

                pg.display.flip()

    def run_win_menu(self):
        """ This method setup the win menu """

        self.all_set_fonctions()

        while self.loops["win_menu_running"] is True:

            self.win_menu_gen()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                # Add a tryagain button if human player want to play again:
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.data["win"].wbut_rect.collidepoint(event.pos):
                        self.launch_game()

            pg.display.flip()
