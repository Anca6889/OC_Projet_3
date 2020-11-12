#! /usr/bin/env python3
# coding: utf-8

import pygame
from display.main_menu import Main_menu
from classes.level import Level
from display.inventory_display import InventoryDisplay
from display.level_display import LevelDisplay
from display.gameover_menu import GameOver
from display.win_menu import Win
from audio.audio import Audio

def launch_game():

    pygame.init()

    # Creating the display 600x600 pixels
    res = (640, 600)
    pygame.display.set_caption("Help Macgyver to escape")
    screen = pygame.display.set_mode(res)


    level = Level()
    main_menu_dis = Main_menu()
    level_dis = LevelDisplay()
    inventory_dis = InventoryDisplay()
    gameover_dis = GameOver()
    win_dis = Win()
    audio = Audio()

    pygame.mixer.init()
    pygame.mixer.music.load(audio.menu_music)
    pygame.mixer.music.play(-1)

    #creating a for loop to keep the game game_running
    
    game_running = False
    main_menu_running = True
    gameover_menu_running = False
    win_menu_running = False 
    
    while main_menu_running:
        
        screen.blit(main_menu_dis.background, (0, 0))
        screen.blit(main_menu_dis.play_button,(main_menu_dis.play_button_rect))
        screen.blit(main_menu_dis.title_text_surface,(main_menu_dis.title_text_rect))
        screen.blit(main_menu_dis.descript_text_surface, (main_menu_dis.descript_text_rect))
        screen.blit(main_menu_dis.click_text_surface,(main_menu_dis.click_text_rect))
        
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

    while game_running:

        # if level_dis.macgyver_rect.colliderect(level_dis.ether_rect):
        #     print("collision ether")
            # soundObj = pygame.mixer.Sound(pick_up_sound)
            # soundObj.play()
            
        screen.blit(inventory_dis.inventory, (0,0))
        screen.blit(inventory_dis.ethertrans, (0, 310))
        screen.blit(inventory_dis.needletrans, (0,370))
        screen.blit(inventory_dis.tubetrans, (0, 430))
        screen.blit(inventory_dis.startrans, (0, 540))

        for key, val in level.coord.items():
        
            if val == "M":
                screen.blit(level_dis.path, (key[1] * 40, key[0] * 40))
                screen.blit(level_dis.macgyver, (key[1] * 40, key[0] * 40))
            if val == "#":
                screen.blit(level_dis.walls, (key[1] * 40 , key[0] * 40))
            if val == "-":
                screen.blit(level_dis.path, (key[1] * 40, key[0] * 40))
            if val == "ether" :
                screen.blit(level_dis.path, (key[1] * 40, key[0] * 40))
                screen.blit(level_dis.ether, (key[1] * 40, key[0] * 40))
            if val == "needle":
                screen.blit(level_dis.path, (key[1] * 40, key[0] * 40))
                screen.blit(level_dis.needle, (key[1] * 40, key[0] * 40))
            if val == "tube":
                screen.blit(level_dis.path, (key[1] * 40, key[0] * 40))
                screen.blit(level_dis.tube, (key[1] * 40, key[0] * 40))
            if val == "G":
                screen.blit(level_dis.path, (key[1] * 40, key[0] * 40))
                screen.blit(level_dis.guardian, (key[1] * 40, key[0] * 40))
            if val == "1":
                screen.blit(level_dis.path, (key[1] * 40, key[0] * 40))
                screen.blit(level_dis.door, (key[1] * 40, key[0] * 40))


        if "ether"in level.inventory:
            screen.blit(level_dis.ether, (0, 310))
            
        if "needle" in level.inventory:
            screen.blit(level_dis.needle, (0, 370))
        
        if "tube" in level.inventory:
            screen.blit(level_dis.tube, (0, 430))
            
        if  len(level.inventory) == 3:
            screen.blit(inventory_dis.star, (0, 540))
            screen.blit(inventory_dis.syringe, (0, 540))

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    level.move("right")
                    print("mouvement à droite")
                elif event.key == pygame.K_LEFT:
                    level.move("left") 
                    print("mouvement à gauche")
                elif event.key == pygame.K_UP:
                    level.move("up") 
                    print("mouvement à haut")
                elif event.key == pygame.K_DOWN:
                    level.move("down")
                    print("mouvement à bas")

        if level.gamelost == True:
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load(audio.gameover_music)
            pygame.mixer.music.play(-1)
            game_running = False
            gameover_menu_running = True
            break
            
        if level.gamewined == True:
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load(audio.win_menu_music)
            pygame.mixer.music.play(-1)
            game_running = False
            win_menu_running = True
            break


        pygame.display.flip()

            
    while gameover_menu_running:

        screen.blit(main_menu_dis.background, (0, 0))
        screen.blit(gameover_dis.gameover, (170, 0))
        screen.blit(gameover_dis.descript_text_surface,
                    (gameover_dis.descript_text_rect))
        screen.blit(gameover_dis.tryagain_button,
                    (gameover_dis.tryagain_button_rect))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover_menu_running = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if gameover_dis.tryagain_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.init()
                    pygame.mixer.music.load(audio.level_music)
                    pygame.mixer.music.play(-1)
                    gameover_menu_running = False
                    main_menu_running = True
                    launch_game()
                    

            pygame.display.flip()
    
    while win_menu_running:

        screen.blit(main_menu_dis.background, (0, 0))
        screen.blit(win_dis.youwin, (100, 0))
        screen.blit(win_dis.descript_text_surface,
                    (win_dis.descript_text_rect))
        screen.blit(win_dis.tryagain_button,
                    (win_dis.tryagain_button_rect))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover_menu_running = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if win_dis.tryagain_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.init()
                    pygame.mixer.music.load(audio.level_music)
                    pygame.mixer.music.play(-1)
                    win_menu_running = False
                    main_menu_running = True
                    launch_game()

        pygame.display.flip()
