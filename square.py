import random

import pygame
from sys import exit

class Kub:
    def __init__(self,x,y,dx,c):
        self.x = x
        self.y = y
        self.dx = dx
        self.c = c
    def move(self):
        self.x = self.x + self.dx

        if self.x <= wall_l:
            self.dx = -self.dx
            self.x = self.x + 1
        if self.x >= 1800 - wall_r - 50:
            self.x = self.x - 1
            self.dx = -self.dx

    def move_bug(self):
        self.x = self.x + self.dx

        if self.x <= wall_l:
            self.dx = -self.dx
        if self.x >= 1800 - wall_r:
            self.dx = -self.dx


    def draw (self):
        pygame.draw.rect(screen,self.c,(self.x,self.y,50,50))

def move_and_draw_walls():
    global wall_r
    global wall_l

    wall_l = wall_l + 0.1
    wall_r = wall_r + 0.1
    pygame.draw.rect(screen, (125, 125, 125), (0, 0, wall_l, 900))
    pygame.draw.rect(screen, (125, 125, 125), (1800 - wall_r, 0, 1800, 900))

wall_l = 0
wall_r = 0


pygame.init()
screen = pygame.display.set_mode((1800,900))
pygame.display.set_caption('New')
clock = pygame.time.Clock()

#c = pygame.Color(255,255,255)
#ku = Kub(50,50,1,c)

k = []
for i in range(10):
    r = 255
    g = 0
    b = 0
    if i < 3:
        g = (i+1) * 70
    if (i >= 3)and(i < 6):
        g = (i -3) * 70
        r = 255 - (i-3) * 70
    if (i >= 6):
        #g = (i -6) * 70
        r = 255 - (i-6) * 70
        b = (i-6) * 70

    c = pygame.Color(r,g,b)
    k.append(Kub(15,i * 60 ,1 + i / 10,c))

while True:

    pygame.draw.rect(screen,pygame.Color(0,0,0),(0,0,1800,900))

    move_and_draw_walls()

    for i in range(10):
        k[i].move()
        k[i].draw()


    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    pygame.display.update()
    clock.tick(160)
