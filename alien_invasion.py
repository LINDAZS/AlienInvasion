#!/usr/bin/env python
# coding=utf-8

import sys
import pygame
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化屏幕对象
    pygame.init()
    alien_setting = Setting()
    screen = pygame.display.set_mode((alien_setting.screen_width,\
                                      alien_setting.screen_height)) # 屏幕 
    ship = Ship(alien_setting, screen)
    # 子弹集合
    bullets = Group()
    # 外星人集合，
    aliens = Group()
    # 描述状态
    stats = GameStats(alien_setting)
    # 创建一群外星
    gf.create_feet(alien_setting, screen, ship, aliens)
    sb = Scoreboard(alien_setting, screen, stats)
    start_button = Button(alien_setting, screen, "Start")
    pygame.display.set_caption('王尼玛大作战') # 游戏标题
    while True:
        # 监听鼠标键盘事件
        gf.check_events(alien_setting, stats, sb, start_button, screen, ship,bullets, aliens)
        # 时刻刷新王尼玛的位置
        if stats.game_active:
            ship.update()
            gf.update_bullet(alien_setting, screen, stats, sb, aliens, bullets, ship)
            gf.update_aliens(alien_setting, stats, sb, screen, ship, aliens, bullets)
        # 最近绘制的图像屏幕可见
        gf.update_screen(alien_setting, screen, stats, sb, ship, aliens, bullets, start_button)
run_game()

