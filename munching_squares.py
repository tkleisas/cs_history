# This Python file uses the following encoding: utf-8
# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height),pygame.FULLSCREEN)
srf =pygame.Surface((width, height), SRCALPHA)
ovr = pygame.Surface((width, 128), SRCALPHA)
# 3 - Load images
# player = pygame.image.load("resources/images/dude.png")
y=0
t=0
z=2
fadestep = 16
fadein = 0
fadeinstep = 32
font = pygame.font.Font(None, 60)

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again

    screen.fill(0)
    px = pygame.PixelArray(srf)
    # 6 - draw the screen elements
    # screen.blit(player, (100,100))
    # 7 - update the screen

    for x in range (width):
        for y in range (height):
            if (((x ^ y) + t) % 2**z) > (2**(z-1)):
                # srf.set_at((x,y),(t%255,t%127+128,t%255))
                px[x,y] = (0,255,0)
                #srf.set_at((x,y),)
            else:
                # color = srf.get_at((x,y))
                color = Color((px[x,y] >> 16) & 0xff,(px[x,y] >> 8) & 0xff ,(px[x,y] & 0xff),  (px[x,y] >> 24 & 0xff))
                if (color.g >= fadestep):
                    color.g = color.g - fadestep;

                #srf.set_at((x,y), (0,color.g,0))
                px[x,y] = (0,color.g,0)
            #srf.set_at((x,y),  (0, ((x+t)^(y+t))%256, 0))
    del px
    t=t+1
    if( t % z**3 == 0):
        z=z+1
        if(z>9):
            z=1
    if(fadein<255-fadeinstep):
        fadein = fadein+fadeinstep
    txt = font.render("Munching Squares (1964)", True, (fadein,fadein,fadein,0))
    txt2 = font.render(u"Μια πρώϊμη επίδειξη γραφικών", True, (fadein,fadein,fadein,0))
    txt3 = font.render(u"στον PDP-1", True, (fadein,fadein,fadein,0))
    pygame.draw.rect(ovr, (0,0,0,txt.get_height()+txt2.get_height()+txt3.get_height()),(0,0,width,128),0)
    screen.blit(srf,(0,0))
    ovr.blit(txt,(0,0))
    ovr.blit(txt2,(0,txt2.get_height()+1));
    ovr.blit(txt3,(0,txt2.get_height()+txt3.get_height()+1))
    screen.blit(ovr,(0,0))
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
