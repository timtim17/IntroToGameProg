# Austin Jenchi
# 2/5/2015
# 8th Period
# Splash Screen

import pygame
from pygame import QUIT
from pygame import KEYDOWN
from Tkinter import Tk as getScreen

pygame.init()

# COLORS
BG_COLOR = [255, 152, 0]
FG_COLOR = [0, 0, 0]

# IMAGES
CHROME = pygame.image.load("chrome.png")
chromeAngle = 0
chromeAngleInterval = 0.01

# FONTS
SYSFONT = pygame.font.Font(None, 48)

# WINDOW
DONE = False
FULLSCREEN = False
CLOCK = pygame.time.Clock()
SIZE = (700, 500)
SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Splash Screen")
STAGE = 0

monitor = getScreen()

counter = 0

# http://www.pygame.org/wiki/RotateCenter?parent=CookBook
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

while not DONE:
    SCREEN.fill(BG_COLOR)

    if STAGE == 0 or STAGE == 1:
        text = SYSFONT.render("Aa Games", True, FG_COLOR)
        SCREEN.blit(text,
                    [SCREEN.get_width() / 2 - text.get_width() // 2, SCREEN.get_height() / 2 - text.get_height() // 2])
    elif STAGE == 2:
        SCREEN.blit(rot_center(CHROME, chromeAngle),
                    [SCREEN.get_width() / 2 - CHROME.get_width() // 2, SCREEN.get_height() / 2 - CHROME.get_height() // 2])

        chromeAngle += chromeAngleInterval

        if chromeAngleInterval <= 50:
            chromeAngleInterval += 0.1

    pygame.display.flip()

    if STAGE == 0:
        counter += 1

        if counter > 100:
            STAGE = 1
    elif STAGE == 1:
        if BG_COLOR[0] < 224:
            BG_COLOR[0] += 1
        elif BG_COLOR[0] > 224:
            BG_COLOR[0] -= 1
        if BG_COLOR[1] < 224:
            BG_COLOR[1] += 1
        elif BG_COLOR[1] > 224:
            BG_COLOR[1] -= 1
        if BG_COLOR[2] < 224:
            BG_COLOR[2] += 1
        elif BG_COLOR[2] > 224:
            BG_COLOR[2] -= 1

        if FG_COLOR[0] < 224:
            FG_COLOR[0] += 1
        elif FG_COLOR[0] > 224:
            FG_COLOR[0] -= 1
        if FG_COLOR[1] < 224:
            FG_COLOR[1] += 1
        elif FG_COLOR[1] > 224:
            FG_COLOR[1] -= 1
        if FG_COLOR[2] < 224:
            FG_COLOR[2] += 1
        elif FG_COLOR[2] > 224:
            FG_COLOR[2] -= 1

        if BG_COLOR[0] == 224 and BG_COLOR[1] == 224 and BG_COLOR[2] == 224 and FG_COLOR[0] == 224 and FG_COLOR[1] == 224 and FG_COLOR[2] == 224:
            STAGE = 2

    for event in pygame.event.get():
        type = event.type
        if type == QUIT:
            DONE = True
        elif type == KEYDOWN:
            if event.key == 292:  # F11
                if not FULLSCREEN:
                    screen = pygame.display.set_mode((monitor.winfo_screenwidth(), monitor.winfo_screenheight()),
                                                     pygame.FULLSCREEN)
                    FULLSCREEN = True
                else:
                    SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
                    FULLSCREEN = False
            elif event.key == 27:  # Esc
                SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
                FULLSCREEN = False

    CLOCK.tick(60)

pygame.quit()