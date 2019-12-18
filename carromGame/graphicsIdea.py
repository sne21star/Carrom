from carromGame.graphics import *
import tkinter as tk
from PIL import ImageTk, Image
from pygame.locals import *
import pygame,sys
from carromGame.carromPiece import *
#Constants
LEFT = 1
WIDTH = 900
HEIGHT = 900
RUNNING = True
QUEEN = 0
BLACK = 1
WHITE = 2
CENTERL = 452
CENTERR = 423
LEFTTOP = 50
numPIECE = 9
sizePiece = 150
def main():
    #Initialize
    pygame.init()
    screen = pygame.display.set_mode((WIDTH + 100, HEIGHT + 100))
    pygame.display.set_caption('Carrom')
    screen.fill([0, 0, 0])

    #re-shape Board Image
    imageFile = "Board.png"
    im1 = Image.open(imageFile)
    im2 = im1.resize((WIDTH, HEIGHT))
    im2.save("Board.png")

    #re-shape Queen Image
    imageFile = "Queen_Piece_original.png"
    im1 = Image.open(imageFile)
    im2 = im1.resize((sizePiece, sizePiece))
    im2.save("Queen_Piece.png")

    # re-shape Black piece Image
    imageFile = "Black_Piece_original.png"
    im1 = Image.open(imageFile)
    im2 = im1.resize((sizePiece, sizePiece))
    im2.save("Black_Piece.png")

    # re-shape White Image
    imageFile = "White_Piece_original.png"
    im1 = Image.open(imageFile)
    im2 = im1.resize((sizePiece, sizePiece))
    im2.save("White_Piece.png")

    #Display Board
    background_image = pygame.image.load("Board.png").convert_alpha()
    screen.blit(background_image, [LEFTTOP, LEFTTOP])

    #Create Queen Piece
    pieces = pygame.sprite.RenderUpdates()
    pieces.add(CarromPiece(CENTERR,CENTERL,0,QUEEN))
    piece_selected = pygame.sprite.GroupSingle()

    #Create White PieceS
    i = 0
    k = 0
    while i < numPIECE:
        pieces = pygame.sprite.RenderUpdates()
        pieces.add(CarromPiece(CENTERR+45+k, CENTERL, 0, WHITE))
        piece_selected = pygame.sprite.GroupSingle()
        i += 1
        k += 20

    # Create Black PieceS
    i = 0
    k = 500
    while i < numPIECE:
        pieces = pygame.sprite.RenderUpdates()
        pieces.add(CarromPiece(k, k, 0, BLACK))
        piece_selected = pygame.sprite.GroupSingle()
        i += 1
        k += 20

    pygame.display.flip()

    #Game Loop
    while RUNNING:
        pieces.clear(screen, background_image)
        #pygame.display.update()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print ("You pressed the left mouse button at (%d, %d)" % event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            print ("You released the left mouse button at (%d, %d)" % event.pos)

    pygame.quit()

if __name__ == '__main__': main()