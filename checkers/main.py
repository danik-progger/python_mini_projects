import pygame
from checkers_game.constants import WIDTH, HEIGHT
from checkers_game.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

board = Board()

def gameLoop():
    run = True
    clock = pygame.time.Clock()
    board.draw(WIN)
    pygame.display.update()

    while run:
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()

gameLoop()
