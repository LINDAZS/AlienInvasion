#!/usr/bin/env python
# coding=utf-8

class Setting(object):

    def __init__(self):
        # 王尼玛
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # 子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_speed_factor = 1
        self.bullet_allowed = 4
        # 外星人
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #1 右 -1左
        self.speed_scale = 1.1
        self.initialize_dynamic_setting()
        self.alien_point = 50
        self.alien_scale =1.5


    def initialize_dynamic_setting(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1


    def increase_speed(self):
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_point  = int(self.alien_point * self.alien_scale)

