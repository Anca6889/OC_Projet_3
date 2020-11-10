#! /usr/bin/env pxthon3
# coding: utf-8

import pygame
from display.config_display import background_dis
from display.config_display import play_dis


class Main_menu(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        self.background = pygame.image.load(background_dis).convert_alpha()
        self.play_button = pygame.image.load(play_dis).convert_alpha()
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = 200
        self.play_button_rect.y = 400
        self.title_text = pygame.font.SysFont('freesansbold.ttf', 60)
        self.title_text_surface = self.title_text.render("Help MacGyver to escape !",True,(255,255,255))
        self.title_text_rect = self.title_text_surface.get_rect()
        self.title_text_rect.center = (320, 50)
        self.descript_text = pygame.font.SysFont('freesansbold.ttf', 23)
        self.descript_text_surface = self.descript_text.render("Pick the 3 items 'ether, needle and tube' to build a syringe and defeat the guardian ! ", True, (255, 255, 255))
        self.descript_text_rect = self.descript_text_surface.get_rect()
        self.descript_text_rect.center = (320, 100)
        self.click_text = pygame.font.SysFont('freesansbold.ttf', 23)
        self.click_text_surface = self.click_text.render("click here to play", True, (255, 255, 255))
        self.click_text_rect = self.click_text_surface.get_rect()
        self.click_text_rect.center = (320, 380)
