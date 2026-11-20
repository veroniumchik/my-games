import random

import pygame
from sys import exit
import math
angle = -90
y = 0
x = 0
skycolor_b = 55

def sky():
    global skycolor_b
    if y > 550:
        skycolor_b = 55
    if y < 350:
        skycolor_b = 247
    if y >= 350 and y <= 550:
        i = y - 350 # i будет в диапазоне от 0 до 200
        skycolor_b = 255 - i

    pygame.draw.rect(screen,pygame.Color(0,0,skycolor_b),(0,0,1800,450))

def grass():
    pygame.draw.rect(screen,pygame.Color(0,50,0),(0,450,1800,900))
    for i in range(1500):
        pygame.draw.line(screen, (0, 155, 0), (x_grass[i], y_grass[i] - 5), (x_grass[i], y_grass[i] + 5),3)

class Gora:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        global x
        i = (x - self.x) // 5
        if y >= 450:
            c1 = 0
            c2 = 0

        if y < 450:
            if x < self.x:
                c1 = 150 + i
                c2 = 100 + i
            else:
                c1 = 100 + i
                c2 = 150 + i

        if c1 > 255:
            c1 = 255
        if c2 > 255:
            c2 = 255
        if c1 < 0:
            c1 = 0
        if c2 < 0:
            c2 = 0

        x1 = self.x
        y1 = self.y - 300

        x2 = self.x
        y2 = self.y + 300

        x3 = self.x - 300
        y3 = self.y + 300

        pygame.draw.polygon(screen,(c1,c1,c1),((x1,y1),(x2,y2),(x3,y3)))


        x1 = self.x
        y1 = self.y - 300

        x2 = self.x
        y2 = self.y + 300

        x3 = self.x + 300
        y3 = self.y + 300

        pygame.draw.polygon(screen, (c2, c2, c2), ((x1, y1), (x2, y2), (x3, y3)))



def sun():
    global angle
    global x
    global y
    angle = angle + -1
    x = math.floor(math.cos(math.radians(angle + 45)) * 500 ) + 900
    y = math.floor(math.sin(math.radians(angle + 45)) * 500 ) + 450
    pygame.draw.circle(screen,pygame.Color(255,255,0),(x,y),90)

def star():
    if y > 550:
        sc_r = 255
        sc_g = 255
        sc_b = 255

    if (y >= 450)and(y <=550):
        i = y - 450 # i имеет значения от 0 до 100
        sc_r = math.floor(0 + i * 2.5)
        sc_g = math.floor(0 + i * 2.5)
        sc_b = 255

    if y > 450:
        for i in range(100):
            pygame.draw.line(screen,(sc_r,sc_g,sc_b),(x_star[i]-1,y_star[i]),(x_star[i]+1,y_star[i]))
            pygame.draw.line(screen, (sc_r, sc_g, sc_b), (x_star[i] , y_star[i] - 1), (x_star[i] , y_star[i] + 1))

x_star = []
y_star = []

x_grass = []
y_grass = []

for i in range(100):
    x_star.append(random.randint(0,1800))
    y_star.append(random.randint(0, 450))

for i in range(1500):
    x_grass.append(random.randint(0,1800))
    y_grass.append(random.randint(450, 900))

pp = Gora(900,450)
yy = Gora(1050,600)


pygame.init()
screen = pygame.display.set_mode((1800,900))
pygame.display.set_caption('New')
clock = pygame.time.Clock()

while True:

    sky()
    sun()
    star()
    yy.draw()
    pp.draw()
    grass()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(160)