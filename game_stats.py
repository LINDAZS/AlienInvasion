#!/usr/bin/env python
# coding=utf-8

class GameStats(object):

    def __init__(self,alien_setting):
        self.alien_setting = alien_setting
        self.reset_stats()
        self.game_active = False
        with open('./high_score.txt') as fp:
            self.hight_score = int(fp.read())


    def reset_stats(self):
        self.ship_left = self.alien_setting.ship_limit
        self.score = 0
        self.level = 1

