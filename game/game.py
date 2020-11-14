#! /usr/bin/env python3
# coding: utf-8

from classes.level import Level
from display.level_display import LevelDisplay
from display.inventory_display import InventoryDisplay
from display.main_menu import Main_menu
from display.gameover_menu import GameOver
from display.win_menu import Win
from audio.audio import Audio
from game import config_game
import pygame


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

    def launch_game(self):
        """ Method running the game """

        pygame.init()

        # Creating the display 640x600 pixels :
        pygame.display.set_caption(config_game.WINDOWTITLE)
        screen = pygame.display.set_mode(config_game.RES)

        # Instancy all the necessaries classes :
        level = Level()
        main_menu_dis = Main_menu()
        level_dis = LevelDisplay()
        inventory_dis = InventoryDisplay()
        gameover_dis = GameOver()
        win_dis = Win()
        audio = Audio()

        # Initialise main menu music:
        pygame.mixer.init()
        pygame.mixer.music.load(audio.menu_music)
        pygame.mixer.music.play(-1)

        # Creating 4 diffrent while loops to keep game running:
        game_running = False
        main_menu_running = True
        gameover_menu_running = False
        win_menu_running = False

        # Main menu while loop running the main menu till player clik on start
        # button, when player click on start, the game while loop start:
        while main_menu_running is True:

            screen.blit(main_menu_dis.background, config_game.MAIN_MENU_POS)
            screen.blit(main_menu_dis.play_button,
                        (main_menu_dis.play_button_rect))
            screen.blit(main_menu_dis.title_text_surface,
                        (main_menu_dis.title_text_rect))
            screen.blit(main_menu_dis.descript_text_surface,
                        (main_menu_dis.descript_text_rect))
            screen.blit(main_menu_dis.click_text_surface,
                        (main_menu_dis.click_text_rect))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    main_menu_running = False
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if main_menu_dis.play_button_rect.collidepoint(event.pos):
                        pygame.mixer.music.stop()
                        pygame.mixer.init()
                        pygame.mixer.music.load(audio.level_music)
                        pygame.mixer.music.play(-1)
                        main_menu_running = False
                        game_running = True

            pygame.display.flip()

        # Game while loop running the game till player win or lose:
        while game_running is True:

            # play littles sounds for these conditions:
            if level.pickobject is True:
                sound_obj = pygame.mixer.Sound(audio.pick_up_sound)
                sound_obj.play()

            if level.killgardian is True:
                pygame.mixer.music.stop()
                sound_obj = pygame.mixer.Sound(audio.punch_sound)
                sound_obj.play(1)

            # Display the inventory on the left side with
            # transparents objects (unpicked):
            screen.blit(inventory_dis.inventory, config_game.INVENTORY_POS)
            screen.blit(inventory_dis.ethertrans, config_game.ETHER_POS)
            screen.blit(inventory_dis.needletrans, config_game.NEEDLE_POS)
            screen.blit(inventory_dis.tubetrans, config_game.TUBE_POS)
            screen.blit(inventory_dis.startrans, config_game.STAR_SYRINGE_POS)

            # Generate all the display of the map on cells of 40x40px
            # based on the level.txt file:
            for key, val in level.coord.items():

                if val == "M":
                    screen.blit(
                        level_dis.path, (key[1] * config_game.SPRITEPX,
                                         key[0] * config_game.SPRITEPX))
                    screen.blit(
                        level_dis.macgyver, (key[1] * config_game.SPRITEPX,
                                             key[0] * config_game.SPRITEPX))
                if val == "#":
                    screen.blit(
                        level_dis.walls, (key[1] * config_game.SPRITEPX,
                                          key[0] * config_game.SPRITEPX))
                if val == "-":
                    screen.blit(
                        level_dis.path, (key[1] * config_game.SPRITEPX,
                                         key[0] * config_game.SPRITEPX))
                if val == "ether":
                    screen.blit(
                        level_dis.path, (key[1] * config_game.SPRITEPX,
                                         key[0] * config_game.SPRITEPX))
                    screen.blit(
                        level_dis.ether, (key[1] * config_game.SPRITEPX,
                                          key[0] * config_game.SPRITEPX))
                if val == "needle":
                    screen.blit(
                        level_dis.path, (key[1] * config_game.SPRITEPX,
                                         key[0] * config_game.SPRITEPX))
                    screen.blit(
                        level_dis.needle, (key[1] * config_game.SPRITEPX,
                                           key[0] * config_game.SPRITEPX))
                if val == "tube":
                    screen.blit(
                        level_dis.path, (key[1] * config_game.SPRITEPX,
                                         key[0] * config_game.SPRITEPX))
                    screen.blit(
                        level_dis.tube, (key[1] * config_game.SPRITEPX,
                                         key[0] * config_game.SPRITEPX))
                if val == "G":
                    screen.blit(
                        level_dis.path, (key[1] * config_game.SPRITEPX,
                                         key[0] * config_game.SPRITEPX))
                    screen.blit(
                        level_dis.guardian, (key[1] * config_game.SPRITEPX,
                                             key[0] * config_game.SPRITEPX))
                if val == "1":
                    screen.blit(
                        level_dis.path, (key[1] * config_game.SPRITEPX,
                                         key[0] * config_game.SPRITEPX))
                    screen.blit(
                        level_dis.door, (key[1] * config_game.SPRITEPX,
                                         key[0] * config_game.SPRITEPX))

            # When an object is picked, add the colourfull picture of
            # the object on the transparent picture (picked)
            # If all objects are picked, add a bonus picture of the syringe:
            if "ether" in level.inventory:
                screen.blit(level_dis.ether, config_game.ETHER_POS)

            if "needle" in level.inventory:
                screen.blit(level_dis.needle, config_game.NEEDLE_POS)

            if "tube" in level.inventory:
                screen.blit(level_dis.tube, config_game.TUBE_POS)

            if len(level.inventory) == 3:
                screen.blit(inventory_dis.star, config_game.STAR_SYRINGE_POS)
                screen.blit(inventory_dis.syringe,
                            config_game.STAR_SYRINGE_POS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    pygame.quit()

                # Control the mooves of the player with keyboard arrows:
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        level.move("right")
                    elif event.key == pygame.K_LEFT:
                        level.move("left")
                    elif event.key == pygame.K_UP:
                        level.move("up")
                    elif event.key == pygame.K_DOWN:
                        level.move("down")

            # Switch to Game-Over or Win menu with these conditions:
            if level.gamelost is True:
                pygame.mixer.music.stop()
                pygame.mixer.init()
                pygame.mixer.music.load(audio.gameover_music)
                pygame.mixer.music.play(-1)
                game_running = False
                gameover_menu_running = True
                break

            if level.gamewined is True:
                pygame.mixer.music.stop()
                pygame.mixer.init()
                pygame.mixer.music.load(audio.win_fanfare)
                pygame.mixer.music.play()
                game_running = False
                win_menu_running = True
                break

            pygame.display.flip()

        while gameover_menu_running is True:

            screen.blit(main_menu_dis.background, config_game.MAIN_MENU_POS)
            screen.blit(gameover_dis.gameover, config_game.GAMEOVER_POS)
            screen.blit(gameover_dis.descript_text_surface,
                        (gameover_dis.descript_text_rect))
            screen.blit(gameover_dis.gobutton,
                        (gameover_dis.gobutton_rect))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover_menu_running = False
                    pygame.quit()

                # Add a tryagain button if human player want to play again:
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if gameover_dis.gobutton_rect.collidepoint(event.pos):
                        gameover_menu_running = False
                        main_menu_running = True
                        self.launch_game()

                pygame.display.flip()

        while win_menu_running is True:

            screen.blit(main_menu_dis.background, config_game.MAIN_MENU_POS)
            screen.blit(win_dis.youwin, config_game.YOUWIN_POS)
            screen.blit(win_dis.descript_text_surface,
                        (win_dis.descript_text_rect))
            screen.blit(win_dis.winbutton,
                        (win_dis.winbutton_rect))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover_menu_running = False
                    pygame.quit()

                # Add a tryagain button if human player want to play again:
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if win_dis.winbutton_rect.collidepoint(event.pos):
                        win_menu_running = False
                        main_menu_running = True
                        self.launch_game()

            pygame.display.flip()
