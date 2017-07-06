#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, alien_setting, screen):
        super(Alien, self).__init__()
        self.image = pygame.image.load('./images/alien.jpg')
        self.screen = screen
        self.alien_setting = alien_setting
        self.rect = self.image.get_rect()
        # 外星人出现的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left  <= 0 :
            return True


    def update(self):
        # 带方向的移动
        self.x += (self.alien_setting.alien_speed_factor * self.alien_setting.fleet_direction)
        self.rect.x = self.x
