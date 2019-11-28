import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

#set up the window
screen = pygame.display.set_mode((1024, 720), 0, 32)         #screen size(401, 300)
pygame.display.set_caption('animation')

#set up the colors
background_color = (102, 179, 255)
black = (0, 0, 0)
#background image
background_img = pygame.image.load('background_Image.jpg')
imgx = 0
imgy = 0

#the main game loop
loop = True
while loop:
    #screen.fill(background_color)
    screen.blit(pygame.transform.scale(background_img,(1024, 720)), (imgx, imgy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            loop = False






    pygame.display.update()
    fpsClock.tick(FPS)

while True:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)