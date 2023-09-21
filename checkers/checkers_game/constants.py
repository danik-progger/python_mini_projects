import pygame

WIDTH = HEIGHT = 800
ROWS = COLS = 8

SQUARE_SIZE = WIDTH // COLS
PADDING = 10

BROWN = (127, 72, 41)
BEIGE = (187, 169, 178)
WHITE = (220, 220, 220)
BLACK = (51, 51, 51)
GREEN = (41, 171, 135)

CROWN = pygame.image.load('assets/crown.png')
CROWN = pygame.transform.scale(CROWN, (44, 44))
