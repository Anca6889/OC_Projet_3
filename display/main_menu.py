#! /usr/bin/env pxthon3
# coding: utf-8

from display import config_display
import pygame


class Main_menu(pygame.sprite.Sprite):
    """ This class setup the main menu display when game is lauched """

    def __init__(self):

        super().__init__()
        self.background = pygame.image.load(
            config_display.BACKGROUND_DIS).convert_alpha()
        self.play_button = pygame.image.load(
            config_display.PLAY_DIS).convert_alpha()
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = config_display.PLAY_BUTTON_RECT_X
        self.play_button_rect.y = config_display.PLAY_BUTTON_RECT_Y
        self.title_text = pygame.font.SysFont(
            config_display.TEXT_POLICE, config_display.POLICE_SIZE_TITTLE)
        self.title_text_surface = self.title_text.render(
            config_display.TITLE_TEXT, True, config_display.COLOR_WHITE)
        self.title_text_rect = self.title_text_surface.get_rect()
        self.title_text_rect.center = config_display.TITLE_TEXT_RECT_CENTER
        self.descript_text = pygame.font.SysFont(
            config_display.TEXT_POLICE, config_display.POLICE_SIZE_TEXT)
        self.descript_text_surface = self.descript_text.render(
            config_display.DESCRIPT_TEXT, True, config_display.COLOR_WHITE)
        self.descript_text_rect = self.descript_text_surface.get_rect()
        self.descript_text_rect.center = config_display.MAIN_MENU_RECT_CENTER
        self.click_text = pygame.font.SysFont(
            config_display.TEXT_POLICE, config_display.POLICE_SIZE_TEXT)
        self.click_text_surface = self.click_text.render(
            config_display.CLICK_TEXT, True, config_display.COLOR_WHITE)
        self.click_text_rect = self.click_text_surface.get_rect()
        self.click_text_rect.center = config_display.CLICK_TEXT_RECT_CENTER
