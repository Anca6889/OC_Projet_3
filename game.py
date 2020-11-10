#! /usr/bin/env python3
# coding: utf-8

import pygame
from classes.level import Level
from display.inventory_display import InventoryDisplay
from display.level_display import LevelDisplay

pygame.init()

# Creating the display 600x600 pixels
res = (640, 600)
pygame.display.set_caption("Help Macgyver to escape")
screen = pygame.display.set_mode(res, pygame.RESIZABLE)

level = Level()
level_dis = LevelDisplay()
inventory_dis = InventoryDisplay()



#creating a for loop to keep the game running
running = True
while running:
    screen.blit(inventory_dis.inventory, (0,0))

    for key, val in level.coord.items():
        
        if val == "M":
            screen.blit(level_dis.macgyver, (key[1] * 40, key[0] * 40))
        if val == "#":
            screen.blit(level_dis.walls, (key[1] * 40 , key[0] * 40))
        if val == "-":
            screen.blit(level_dis.path, (key[1] * 40, key[0] * 40))
        if val == "ether" :
            screen.blit(level_dis.ether, (key[1] * 40, key[0] * 40))
        if val == "needle":
            screen.blit(level_dis.needle, (key[1] * 40, key[0] * 40))
        if val == "tube":
            screen.blit(level_dis.tube, (key[1] * 40, key[0] * 40))
        if val == "G":
            screen.blit(level_dis.guardian, (key[1] * 40, key[0] * 40))
        if val == "1":
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

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                level.move("right")
                # macgyver.move("right")
                print("mouvement à droite")
            elif event.key == pygame.K_LEFT:
                level.move("left")
                # macgyver.move("left")
                print("mouvement à gauche")
            elif event.key == pygame.K_UP:
                level.move("up")
                # macgyver.move("up")
                print("mouvement à haut")
            elif event.key == pygame.K_DOWN:
                level.move("down")
                # macgyver.move("down")
                print("mouvement à bas")
        

