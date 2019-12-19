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
POINTSB = 10
POINTSW = 20
POINTSQ = 50
def blackPiecePos():
    i = 0
    k = 500
    while i < numPIECE:
        xCoord = 0
        yCoord = 0
        pieces = pygame.sprite.RenderUpdates()
        pieces.add(CarromPiece(xCoord, yCoord, 0, BLACK, POINTSB))
        i += 1
        k += 20
    return 0
def whitePiecePos():
    i = 0
    k = 0
    l = 0
    j = 27
    m = 0
    z = 0
    while i < numPIECE:
        xCoord = CENTERR
        yCoord = CENTERL
        if 0 <= i < 2:
            xCoord = CENTERR + 32 + k
            yCoord = CENTERL + 27 + k
            k += 25
        if 2 <= i < 4:
            xCoord = CENTERR - l - 32
            yCoord = CENTERL + l + 27
            l += 25
        if 4 <= i < 6:
            xCoord = CENTERR
            yCoord = CENTERL - 36 - j
            j -= 27
        # CENTERL = 452
        # CENTERR = 423
        if 6 <= i < 9:
            q = 1
            zeroX = 1
            zeroY = 1
            if (i % 7 == 0):
                q = -1
            if (i % 8 == 0):
                zeroX = 0
                zeroY = 100
            xCoord = CENTERR + (+70) * q * zeroX
            yCoord = CENTERL + (-20) + zeroY
        pieces = pygame.sprite.RenderUpdates()
        pieces.add(CarromPiece(xCoord, yCoord, 0, WHITE, POINTSW))
        i += 1
    return 0
#function will give menu
def start():
    screen = pygame.display.set_mode((WIDTH + 100, HEIGHT + 100))
    pygame.display.set_caption('Carrom by Sneha')
    screen.fill([0, 0, 0])
    return screen

#function will give instructions and ask for either type game 1 or type game 2
def instructions():
    return 0

def main():
    #Initialize
    pygame.init()
    screen = start()
    pygame.display.flip()
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
    pieces.add(CarromPiece(CENTERR,CENTERL,0,QUEEN, POINTSQ))

    #Create White PieceS
    whitePiecePos()

    # Create Black PieceS
    blackPiecePos()

    pygame.display.flip()
    #event Loop
    piece_selected = pygame.sprite.GroupSingle()

    #Game Loop
    while RUNNING:
        pieces.clear(screen, background_image)
        #pygame.display.update()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            break
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print ("You pressed the left mouse button at (%d, %d)" % event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            print ("You released the left mouse button at (%d, %d)" % event.pos)
    pygame.quit()
    exit()

if __name__ == '__main__': main()