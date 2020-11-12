#! /usr/bin/env pxthon3
# coding: utf-8

import pygame

from display.config_display import macgyver_dis
from display.config_display import walls_dis
from display.config_display import path_dis
from display.config_display import ether_dis
from display.config_display import needle_dis
from display.config_display import tube_dis
from display.config_display import guardian_dis
from display.config_display import door_dis



class LevelDisplay(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.walls = pygame.image.load(walls_dis).convert_alpha()
        self.path = pygame.image.load(path_dis).convert_alpha()
        self.ether = pygame.image.load(ether_dis).convert_alpha()
        self.ether_rect = self.ether.get_rect()
        self.needle = pygame.image.load(needle_dis).convert_alpha()
        self.needle_rect = self.needle.get_rect()
        self.tube = pygame.image.load(tube_dis).convert_alpha()
        self.tuber_rect = self.tube.get_rect()
        self.guardian = pygame.image.load(guardian_dis).convert_alpha()
        self.macgyver = pygame.image.load(macgyver_dis).convert_alpha()
        self.macgyver_rect = self.macgyver.get_rect()
        self.door = pygame.image.load(door_dis).convert_alpha()       
        
        