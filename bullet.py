#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """对子弹管理的类"""

    def __init__(self, alien_setting, screen, ship):
        """在飞船所处的位置创建子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,alien_setting.bullet_width, \
                                alien_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = alien_setting.bullet_color
        self.speed_factor = alien_setting.bullet_speed_factor


    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



