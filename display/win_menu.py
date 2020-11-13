#! /usr/bin/env python3
# coding: utf-8

from display import config_display
import pygame


class Win(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.youwin = pygame.image.load(
            config_display.YOUWIN_DIS).convert_alpha()
        self.button = pygame.image.load(
            config_display.TRYAGAIN_DIS).convert_alpha()
        self.button_rect = self.button.get_rect()
        self.button_rect.x = config_display.BUTTON_RECT_X
        self.button_rect.y = config_display.BUTTON_RECT_Y
        self.descript_text = pygame.font.SysFont(
            config_display.TEXT_POLICE, config_display.POLICE_SIZE_TITTLE)
        self.descript_text_surface = self.descript_text.render(
            " YOU'VE WIN! ", True, config_display.COLOR_WHITE)
        self.descript_text_rect = self.descript_text_surface.get_rect()
        self.descript_text_rect.center = config_display.BUTTON_RECT_CENTER
