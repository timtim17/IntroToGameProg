# Austin Jenchi
# 2/5/2015
# 8th Period
# Animation

import pygame

from pygame import QUIT
from pygame import KEYDOWN
from Tkinter import Tk as getScreen

pygame.init()

# COLORS
WHITE = (255, 255, 255)

# IMAGES
MARIO = [pygame.image.load("mario1.png"),
         pygame.image.load("mario2.png"),
         pygame.image.load("mario3.png")]

# MUSIC
pygame.mixer.music.load("Mario Theme.wav")
pygame.mixer.music.play(-1)

# WINDOW
DONE = False
FULLSCREEN = False
CLOCK = pygame.time.Clock()
SIZE = (700, 500)
SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Animation Test")

monitor = getScreen()

marioImageID = 0
marioCoords = [0, 0]

while not DONE:
    SCREEN.fill(WHITE)
    SCREEN.blit(MARIO[int(round(marioImageID, 0))],
                [(SCREEN.get_width() / 2 - MARIO[int(round(marioImageID, 0))].get_width() // 2) + marioCoords[0],
                 (SCREEN.get_height() / 2 - MARIO[int(round(marioImageID, 0))].get_height() // 2) + marioCoords[1]])
    pygame.display.flip()

    if marioImageID < len(MARIO) - 1:
        marioImageID += 0.1
    else:
        marioImageID = 0

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
            elif event.key == 27:   # Esc
                SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
                FULLSCREEN = False
            elif event.key == 119:  # w
                print "w"
                marioCoords[1] += 1
            elif event.key == 97:   # a
                print "a"
                marioCoords[0] -= 1
            elif event.key == 115:  # s
                print "s"
                marioCoords[1] -= 1
            elif event.key == 100:  # d
                print "d"
                marioCoords[0] += 1

            print marioCoords

    CLOCK.tick(60)

pygame.quit()