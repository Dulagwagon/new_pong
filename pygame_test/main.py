import pygame
from assets import *

pygame.init()

W = 1280
H = 720

gc = pygame.display.set_mode((W, H))
gt = pygame.display.set_caption("Pong Reborn")


def pl1_mv():
    global p1y
    if p1up:
        p1y -= 7
    else:
        p1y +=0
    if p1dw:
        p1y += 7
    else:
        p1y -= 0
    if p1y <= 0:
        p1y = 0
    elif p1y >= 575:
        p1y = 575


def pl2_mv():
    global p2y
    if p2up:
        p2y -= 7
    else:
        p2y +=0
    if p2dw:
        p2y += 7
    else:
        p2y -= 0
    if p2y <= 0:
        p2y = 0
    elif p2y >= 575:
        p2y = 575


def bl_mov():
    global blx
    global bly
    global bl_chdir
    global bl_chdiry
    blx += bl_chdir
    bly += bl_chdiry

    if blx > 1105:
        if p2y < bly + 46:
            if p2y + 146 > bly:
                bl_chdir *= -1

    if blx < 130:
        if p1y < bly + 46:
            if p1y + 146 > bly:
                bl_chdir *= -1

    if bly > 675:
        bl_chdiry *= -1
    elif bly <=0:
        bl_chdiry *= -1

    if blx < -50:
        blx = 617
        bly = 337
        bl_chdiry *= -1
        bl_chdir *= -1
    elif blx >= 1320:
        blx = 617
        bly = 337
        bl_chdiry *= -1
        bl_chdir *= -1


def dr():
    gc.blit(gf, (0, 0))
    gc.blit(p1, (p1x, p1y))
    gc.blit(p2, (p2x, p2y))
    gc.blit(bl, (blx, bly))


gr = True
while gr:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gr = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1up = True
            if event.key == pygame.K_s:
                p1dw = True
            if event.key == pygame.K_UP:
                p2up = True
            if event.key == pygame.K_DOWN:
                p2dw = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1up = False
            if event.key == pygame.K_s:
                p1dw = False
            if event.key == pygame.K_UP:
                p2up = False
            if event.key == pygame.K_DOWN:
                p2dw = False

    dr()
    bl_mov()
    pl1_mv()
    pl2_mv()
    pygame.display.update()
