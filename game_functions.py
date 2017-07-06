#!/usr/bin/env python
# coding=utf-8

# 创建这个文件，主要存储大量的飞船需要的函数，避免在alien...py里文件过大，保证清晰的逻辑

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_fleet_edges(alien_setting, aliens):
    for alien in aliens:
        if alien.check_edges():
            check_fleet_direction(alien_setting, aliens)
            break


def check_fleet_direction(alien_setting, aliens):
    for aline in aliens:
        aline.rect.y += alien_setting.fleet_drop_speed
    alien_setting.fleet_direction *= -1


def ship_hit(alien_setting, stats, screen, sb, ship, aliens, bullets):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_feet(alien_setting, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(alien_setting, stats, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom :
            ship_hit(alien_setting, stats, screen, sb, ship, aliens, bullets)
            break


def update_aliens(alien_setting, stats, sb, screen, ship, aliens, bullets):
    check_fleet_edges(alien_setting, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(alien_setting, stats, screen, sb, ship, aliens, bullets)
    check_aliens_bottom(alien_setting, stats, screen, sb, ship, aliens, bullets)


def get_number_rows(alien_setting, ship_height, alien_height):
    available_space_y = (alien_setting.screen_height - \
                        (3 * alien_height) - ship_height)
    return int(available_space_y/(2 * alien_height))


def get_number_aliens_x(alien_setting, alien_width):
    available_space_x = alien_setting.screen_width - \
            2 * alien_width
    return int(available_space_x/(2 * alien_width))


def create_alien(alien_setting, screen, aliens, alien_numer, row_number):
    alien = Alien(alien_setting, screen)
    alien_width = alien.rect.width
    alien.x = (2 * alien_numer + 1) * alien_width
    alien.rect.x = alien.x
    alien.rect.y = (2 * row_number + 1) * alien.rect.height
    aliens.add(alien)


def create_feet(alien_setting, screen, ship, aliens):
    alien = Alien(alien_setting, screen)
    number_alien_x = get_number_aliens_x(alien_setting, \
                                         alien.rect.width)
    number_rows = get_number_rows(alien_setting, ship.rect.height, \
                                  alien.rect.height)

    for number in range(number_rows):
        for alien_numer in range(number_alien_x):
            create_alien(alien_setting, screen, aliens, alien_numer, number)



def check_keydown_events(event, alien_setting, screen, ship, bullets, stats):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    # 空格发子弹
    elif event.key == pygame.K_SPACE:
        fire_bullet(alien_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        with open('./high_score.txt','w') as fp:
            fp.write(str(stats.hight_score))
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False


def fire_bullet(alien_setting, screen, ship, bullets):
    if len(bullets) < 4:
        new_bullet = Bullet(alien_setting, screen, ship)
        bullets.add(new_bullet)


def check_events(alien_setting, stats, sb, start_button, screen, ship, bullets, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, alien_setting, screen, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_start_button(alien_setting, screen, stats, sb, start_button, mouse_x, mouse_y, \
                               aliens, bullets, ship)


def check_start_button(alien_setting, screen, stats, sb, start_button,\
                       mouse_x, mouse_y, aliens, bullets, ship):
    if start_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        # 点击开始数据重新设置
        sb.prep_score()
        sb.prep_hight_score()
        sb.prep_level()
        sb.prep_ships()
        alien_setting.initialize_dynamic_setting()
        pygame.mouse.set_visible(False)
        create_feet(alien_setting, screen, ship, aliens)
        ship.center_ship()


def update_screen(alien_setting, screen, stats, sb, ship, aliens, bullets, start_button):
    screen.fill(alien_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        start_button.draw_button()
    pygame.display.flip()


def check_high_score(stats, sb):
    if stats.score > stats.hight_score:
        stats.hight_score = stats.score
        sb.prep_hight_score()


def check_bullets_aliens_collisions(alien_setting, screen, stats, sb, aliens, bullets, ship):
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += alien_setting.alien_point* len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        alien_setting.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_feet(alien_setting, screen, ship, aliens)


def update_bullet(alien_setting, screen, stats, sb, aliens, bullets, ship):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullets_aliens_collisions(alien_setting, screen, stats, sb, aliens, bullets, ship)

