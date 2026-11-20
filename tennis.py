import random

import pygame
from sys import exit

def check_collision(dsk,c):
    if c.x >= dsk.x and c.x <= dsk.x + dsk.width and c.y >= 880:
        c.y_to = -c.y_to
        c.y = c.y -5

class Kubik:
    def __init__(self,x,y,kr):
        self.x = x
        self.y = y
        self.kr = kr

    def stuk(self,shar):
        if self.kr > 0:
            if shar.x > self.x and shar.x < self.x + 100 and shar.y > self.y and shar.y < self.y + 5 :
                self.kr = self.kr - 1
                shar.tolkanie_y()
            if shar.x > self.x and shar.x < self.x + 100 and shar.y > self.y +35 and shar.y < self.y + 40 :
                self.kr = self.kr - 1
                shar.tolkanie_y()
            if shar.x > self.x and shar.x < self.x + 5 and shar.y > self.y and shar.y < self.y +40 :
                self.kr = self.kr - 1
                shar.tolkanie_x()
            if shar.x > self.x + 95 and shar.x < self.x + 100 and shar.y > self.y  and shar.y < self.y +40 :
                self.kr = self.kr - 1
                shar.tolkanie_x()

    def draw(self):
        if self.kr == 1:
            pygame.draw.rect(screen, pygame.Color(0,255,0), pygame.Rect(self.x + 1, self.y + 1, 100 - 2, 40 - 2))
        if self.kr == 2:
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(self.x + 1, self.y + 1, 100 - 2, 40 - 2))
class Doska:
    def __init__(self,x,y,width):
        self.x = x
        self.y = y
        self.width = width

    def go(self,x):
        self.x = x

    def draw(self):
        pygame.draw.rect(screen, pygame.Color(255,0,0), (self.x, self.y,self.width,20))

class Shar:
    def __init__(self,x,y,x_to,y_to):
        self.x = x
        self.y = y
        self.x_to = x_to
        self.y_to = y_to

    def go(self):
        self.x = self.x + self.x_to
        self.y = self.y + self.y_to

        if self.y< 1+20:
            self.y_to = -self.y_to

        if self.x > 1799 -20 or self.x< 1+20:
            self.x_to = -self.x_to

    def tolkanie_x(self):
        self.x_to =- self.x_to

    def tolkanie_y(self):
        self.y_to =- self.y_to

    def draw(self):
        pygame.draw.circle(screen, pygame.Color(255,255,255), (self.x, self.y), 20)


pygame.init()
screen = pygame.display.set_mode((1800,900))
pygame.display.set_caption('wdsaferdwfse')
clock = pygame.time.Clock()

c = []
for i in range(10):
    x = random.randint(50,1750)
    y = random.randint(50,850)
    x_to = random.randint(0,1)*2 - 1
    y_to =  random.randint(0,1)*2 - 1
    c.append(Shar(x,y,x_to,y_to))


uroven = []
uroven.append([[0,0,2,1,1,1,1,1,1,2,0,0],[0,2,1,1,1,1,1,1,1,1,2,0],[2,1,1,1,1,1,1,1,1,1,1,2]])
kubiki = []

for i in range(len(uroven[0])):
    for j in range(len(uroven[0][i])):
        if uroven[0][i][j] != 0:
            kubiki.append(Kubik(j * 100,i * 40,uroven[0][i][j]))
        #print(f'i: {i}, j:{j}')


dsk = Doska(900,880,100)

while True:

    pygame.draw.rect(screen, pygame.Color(0,0,0),(0,0,1800,900))

    for i in range(len(c)):
        for j in range(len(kubiki)):
            kubiki[j].stuk(c[i])
            #print(f'kubik: {j}, sharik: {i}')

    for i in range(len(kubiki)):
        kubiki[i].draw()


    for i in range(10):
        c[i].go()
        check_collision(dsk, c[i])
        c[i].draw()

    x, y = pygame.mouse.get_pos()

    dsk.go(x)


    dsk.draw()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(160)