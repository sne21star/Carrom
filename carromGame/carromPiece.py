from carromGame.graphics import *
import tkinter as tk
from PIL import ImageTk, Image
from pygame.locals import *
import pygame,sys

#constant
QUEEN = 0
BLACK = 1
WHITE = 2
blackColor = [0,0,0]
class CarromPiece(pygame.sprite.Sprite):
        def __init__(self, x_coord, y_coord, speed, pieceType):
            pygame.sprite.Sprite.__init__(self)
            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.x_coord = x_coord
            self.y_coord = y_coord
            if(pieceType == QUEEN):
                self.image = pygame.image.load("Queen_Piece.png").convert()
                self.rect = self.image.get_rect()
                self.image.set_colorkey(blackColor)
            if (pieceType == BLACK):
                self.image = pygame.image.load('Black_Piece.png').convert()
                self.rect = self.image.get_rect()
                self.image.set_colorkey(blackColor)
            if (pieceType == WHITE):
                self.image = pygame.image.load('White_Piece.png').convert()
                self.rect = self.image.get_rect()
                self.image.set_colorkey(blackColor)
            self.speed = speed
            self.pieceType = pieceType
            self.type = "piece"
            screen.blit(self.image, [self.x_coord, self.y_coord])


