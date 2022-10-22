#!/usr/bin/env python3
# -*- coding: utf-8 -*- import random
import pygame
import random

from vec2d import Vec2d
from polyline import Polyline, Knot


SCREEN_DIM = (800, 600)

def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(polyline.steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))

        
pygame.init()
gameDisplay = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption("MyScreenSaver")

working = True
polyline = Polyline(gameDisplay)
show_help = False
pause = True

hue = 0
color = pygame.Color(0)

while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                working = False
            if event.key == pygame.K_r:
                polyline = Polyline(gameDisplay)
            if event.key == pygame.K_p:
                pause = not pause
            if event.key == pygame.K_KP_PLUS:
                polyline.steps += 1
            if event.key == pygame.K_F1:
                show_help = not show_help
            if event.key == pygame.K_KP_MINUS:
                polyline.steps -= 1 if polyline.steps > 1 else 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            polyline.add_point(Vec2d(event.pos[0], event.pos[1]),
                    Vec2d(random.random()*2, random.random()*2))

    gameDisplay.fill((0, 0, 0))
    hue = (hue + 1) % 360
    color.hsla = (hue, 100, 50, 100)
    polyline.draw_points()
    polyline.draw_points("line", 3, color)
    if not pause:
        polyline.set_points()
    if show_help:
        draw_help()

    pygame.display.flip()

pygame.display.quit()
pygame.quit()
exit(0)
