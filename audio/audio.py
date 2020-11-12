#! /usr/bin/env python3
# coding: utf-8

import pygame
from audio.audio_config import menu_music
from audio.audio_config import level_music
from audio.audio_config import pick_up_sound
from audio.audio_config import gameover_music
from audio.audio_config import allobjects_sound
from audio.audio_config import punch_sound
from audio.audio_config import win_fanfare
from audio.audio_config import win_menu_music

class Audio:
    def __init__(self):

        super().__init__()
        self.menu_music = menu_music
        self.level_music = level_music
        self.pick_up_sound = pick_up_sound
        self.allobjects_sound = allobjects_sound
        self.gameover_music = gameover_music
        self.win_menu_music = win_menu_music
        self.win_fanfare = win_fanfare
        self.punch_sound = punch_sound
