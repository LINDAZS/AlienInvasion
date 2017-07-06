#!/usr/bin/env python
# coding=utf-8

import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scoreboard(object):

    def __init__(self, alien_setting, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.alien_setting = alien_setting
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_hight_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, \
                                            self.alien_setting.bg_color)
        # 设置于分数的背景颜色重合与屏幕
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_hight_score(self):
        high_score = int(round(self.stats.hight_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, \
                                                self.alien_setting.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top


    def prep_level(self):
        self.level_str_image = self.font.render(str(self.stats.level), True, self.text_color, \
                                               self.alien_setting.bg_color)
        self.level_image_rect = self.level_str_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10


    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.alien_setting, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_str_image, self.level_image_rect)
        self.ships.draw(self.screen)


