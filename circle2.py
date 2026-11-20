import random
import math
import pygame
from sys import exit

cnt = 0

class Krest:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.age = 0

    def add_age(self):
        self.age = self.age + 1
        if self.age > 250:
            return True

    def draw(self):
        color = pygame.Color(255 - self.age , 255 - self.age , 255 - self.age )
        pygame.draw.line(screen, color, [self.x -24,self.y -24 ] , [self.x + 50-24, self.y + 50-24 ]  )
        pygame.draw.line(screen, color, [self.x + 50-24,self.y -24 ] , [self.x-24 , self.y + 50 -24]  )


class Sharik:
    def __init__(self):
        self.x = random.randint(25,1775)
        self.y = random.randint(25, 875)
        self.r = 25
        r = random.randint(50,255)
        g = random.randint(50,255)
        b = random.randint(50,255)
        self.color = pygame.Color(r,g,b)

    def up(self):
        self.r = self.r + 0.5

    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),math.floor(self.r))

    def click(self,x,y):
        a = self.x - x
        b = self.y - y
        c = math.sqrt(a*a + b*b)
        if c <= self.r:
            return True

pygame.init()
screen = pygame.display.set_mode((1800,900))
pygame.display.set_caption('New')
clock = pygame.time.Clock()

k = []
c = []
c.append(Sharik())
c.append(Sharik())
c.append(Sharik())

while True:

    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0, 0, 1800, 900))

    cnt = cnt + 1
    if cnt >= 200:
        c.append(Sharik())
        cnt = 0

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()

            k.append(Krest(x,y))


            for i, e in enumerate(c):
                if c[i].click(x,y):
                    c.pop(i)

    #print(len(k))
    for i, e in enumerate(k):
        k[i].draw()
        if k[i].add_age():
            k.pop(i)

    for i,e in enumerate(c):
        c[i].up()
        c[i].draw()

    pygame.display.update()
    clock.tick(160)