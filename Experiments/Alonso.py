# Austin Jenchi
# 1/29/2015
# 8th Period
# Alonso

import pygame
from pygame import QUIT
from pygame import KEYDOWN
from Tkinter import Tk as getScreen

pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# IMAGES
ALONSO = pygame.image.load("alonso.gif")

# FONTS
SYSFONT = pygame.font.Font(None, 48)
COMICSANS = pygame.font.SysFont("Comic Sans MS", 25, True, False)

# MUSIC
pygame.mixer.music.load("Who Likes to Party.mp3")

# WINDOW
DONE = False
FULLSCREEN = False
CLOCK = pygame.time.Clock()
SIZE = (700, 500)
SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
pygame.display.set_caption("BYOB")
pygame.display.set_icon(ALONSO)


monitor = getScreen()

angle = 0
flip = False

# pygame.mixer.music.play(-1)

while not DONE:
    SCREEN.fill(WHITE)
    SCREEN.blit(pygame.transform.rotate(ALONSO, angle),
                [SCREEN.get_width() / 2 - ALONSO.get_width() // 2, SCREEN.get_height() / 2 - ALONSO.get_height() // 2])
    # text = SYSFONT.render("BYOB. Bring Your Own Bad Memories.", True, BLACK)
    text = COMICSANS.render("I survived BYOB and all I got was this lousy program.", True, RED)
    SCREEN.blit(text,
                [SCREEN.get_width() / 2 - text.get_width() // 2, (SCREEN.get_height() / 2 - text.get_height() // 2) + 100])
    pygame.display.flip()

    if angle > 720 or angle < 0:
        flip = not flip

    if not flip:
        angle += 1
    else:
        angle -= 1

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
            elif event.key == 27:
                SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
                FULLSCREEN = False

    CLOCK.tick(60)

pygame.quit()
