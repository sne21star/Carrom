from carromGame.graphics import *
import tkinter as tk
from PIL import ImageTk, Image

"""
 Simple snake example.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame

#import pygame, sys

LEFT = 1
WIDTH = 900
HEIGHT = 900

running = True
screen = pygame.display.set_mode((WIDTH + 100, HEIGHT + 100))
screen.fill([0, 0, 0])
imageFile = "Board.jpg"
im1 = Image.open(imageFile)
im2 = im1.resize((WIDTH, HEIGHT))
im2.save("Board.jpg")
background_image = pygame.image.load("Board.jpg").convert()
screen.blit(background_image, [50, 50])

while running:
 pygame.display.flip()
 event = pygame.event.poll()
 if event.type == pygame.QUIT:
     running = False
     pygame.quit()

 elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
     print ("You pressed the left mouse button at (%d, %d)" % event.pos)
 elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
     print ("You released the left mouse button at (%d, %d)" % event.pos)

pygame.quit()