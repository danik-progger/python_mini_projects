from .constants import BLACK, SQUARE_SIZE, PADDING, CROWN
import pygame

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = True
        self.direction = 1 if color == BLACK else -1

        self.x = 0
        self.y = 0
        self.calculatePosition()

    def calculatePosition(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def setKing(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2,
                             self.y - CROWN.get_height() // 2))

    def __repr__(self):
        return str(self.color)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculatePosition()