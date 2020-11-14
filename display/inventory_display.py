#! /usr/bin/env pxthon3
# coding: utf-8

from display import config_display
import pygame


class InventoryDisplay(pygame.sprite.Sprite):
    """ This class setup the inventory display """

    def __init__(self):

        super().__init__()
        self.inventory = pygame.image.load(
            config_display.INVENTORY_DIS).convert_alpha()
        self.syringe = pygame.image.load(
            config_display.SYRINGE_DIS).convert_alpha()
        self.star = pygame.image.load(config_display.STAR_DIS).convert_alpha()
        self.ethertrans = pygame.image.load(
            config_display.ETHERTRANS_DIS).convert_alpha()
        self.needletrans = pygame.image.load(
            config_display.NEEDLETRANS_DIS).convert_alpha()
        self.tubetrans = pygame.image.load(
            config_display.TUBETRANS_DIS).convert_alpha()
        self.startrans = pygame.image.load(
            config_display.STARTRANS_DIS).convert_alpha()
