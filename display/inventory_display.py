#! /usr/bin/env pxthon3
# coding: utf-8

import pygame
from display.config_display import inventory_dis
from display.config_display import syringe_dis
from display.config_display import star_dis
from display.config_display import ethertrans_dis
from display.config_display import needletrans_dis
from display.config_display import tubetrans_dis
from display.config_display import startrans_dis


class InventoryDisplay(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.inventory = pygame.image.load(inventory_dis).convert_alpha()
        self.syringe = pygame.image.load(syringe_dis).convert_alpha()
        self.star = pygame.image.load(star_dis).convert_alpha()
        self.ethertrans = pygame.image.load(ethertrans_dis).convert_alpha()
        self.needletrans = pygame.image.load(needletrans_dis).convert_alpha()
        self.tubetrans = pygame.image.load(tubetrans_dis).convert_alpha()
        self.startrans = pygame.image.load(startrans_dis).convert_alpha()
