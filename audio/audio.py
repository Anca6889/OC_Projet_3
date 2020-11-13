#! /usr/bin/env python3
# coding: utf-8

from audio import config_audio


class Audio:
    def __init__(self):

        super().__init__()
        self.menu_music = config_audio.MENU_MUSIC
        self.level_music = config_audio.LEVEL_MUSIC
        self.pick_up_sound = config_audio.PICK_UP_SOUND
        self.allobjects_sound = config_audio.ALLOBJECTS_SOUND
        self.gameover_music = config_audio.GAMEOVER_MUSIC
        self.win_menu_music = config_audio.WIN_MENU_MUSIC
        self.win_fanfare = config_audio.WIN_FANFARE
        self.punch_sound = config_audio.PUNCH_SOUND
