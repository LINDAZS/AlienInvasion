#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, alien_setting, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('./images/ship.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 青蛙图片位于游戏屏幕的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False
        self.alien_setting = alien_setting
        self.center = float(self.rect.centerx)


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.alien_setting.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.alien_setting.ship_speed_factor
        self.rect.centerx = self.center


    def center_ship(self):
        self.center = self.screen_rect.centerx


