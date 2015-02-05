import pygame
from pygame import QUIT
from pygame import KEYDOWN
from Tkinter import Tk as getScreen

pygame.init()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FONTS
SYSFONT = pygame.font.Font(None, 48)

# WINDOW
DONE = False
FULLSCREEN = False
CLOCK = pygame.time.Clock()
SIZE = (700, 500)
SCREEN = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
pygame.display.set_caption("PyGame Demo")

monitor = getScreen()

while not DONE:
    SCREEN.fill(WHITE)
    text = SYSFONT.render("Hello World!", True, BLACK)
    SCREEN.blit(text, [SCREEN.get_width() / 2 - text.get_width() // 2, SCREEN.get_height() / 2 - text.get_height() // 2])
    pygame.display.flip()

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