import pygame
from .piece import Piece
from .constants import BROWN, BEIGE, WHITE, BLACK, ROWS, COLS, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.createBoard()

    def drawSquares(self, win):
        win.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BEIGE, (row * SQUARE_SIZE,
                                 col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def createBoard(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == (row + 1) % 2:
                    piece = 0
                    if row < 3:
                        piece = Piece(row, col, WHITE)
                    elif row > 4:
                        piece = Piece(row, col, BLACK)
                    self.board[row].append(piece)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.drawSquares(win)

        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
