import pygame
import sys
import os # new code below
blackColor = [0,0,0]
class Player(pygame.sprite.Sprite):

    def __init__(self, namePic):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        self.images = []
        img = pygame.image.load(namePic).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.image.set_colorkey(blackColor)