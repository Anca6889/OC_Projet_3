#! /usr/bin/env pxthon3
# coding: utf-8

from display import config_display
import pygame


class LevelDisplay(pygame.sprite.Sprite):
    """ This class setup the level display """

    def __init__(self):

        super().__init__()
        self.walls = pygame.image.load(
            config_display.WALLS_DIS).convert_alpha()
        self.path = pygame.image.load(config_display.PATH_DIS).convert_alpha()
        self.ether = pygame.image.load(
            config_display.ETHER_DIS).convert_alpha()
        self.ether_rect = self.ether.get_rect()
        self.needle = pygame.image.load(
            config_display.NEEDLE_DIS).convert_alpha()
        self.needle_rect = self.needle.get_rect()
        self.tube = pygame.image.load(config_display.TUBE_DIS).convert_alpha()
        self.tuber_rect = self.tube.get_rect()
        self.guardian = pygame.image.load(
            config_display.GUARDIAN_DIS).convert_alpha()
        self.macgyver = pygame.image.load(
            config_display.MACGYVER_DIS).convert_alpha()
        self.macgyver_rect = self.macgyver.get_rect()
        self.door = pygame.image.load(config_display.DOOR_DIS).convert_alpha()
