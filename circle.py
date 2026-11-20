import random
import math
import pygame
from sys import exit

class Nitca:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
        a = self.x - c.x
        b = self.y - c.y
        v = math.floor(math.sqrt(a*a + b*b))
        #print(v)
        v =  v // 3
        if v > 255:
            v = v //3
            #v = 255




        pygame.draw.line(screen,pygame.Color(255-v,255-v,255-v),(c.x,c.y),(self.x,self.y))
class Kvas:


    def __init__(self):
        self.x = random.randint(50,1750)
        self.y = random.randint(50,850)
        self.dx = random.randint(0,1) * 10 - 5 # Получится или -5 или 5
        self.dy = random.randint(0,1) * 10 - 5 # Получится или -5 или 5

        self.r = random.randint(1,250)
        self.g = random.randint(1,250)
        self.b = random.randint(1,250)

        self.dr = random.randint(0,1) * 2 - 1 # Получится или -1 или 1
        self.dg = random.randint(0,1) * 2 - 1 # Получится или -1 или 1
        self.db = random.randint(0,1) * 2 - 1 # Получится или -1 или 1

        self.speed = 2

    def change_pos(self):

        if self.x > 1800 - 30:
            self.dx = -self.dx
            n.append(Nitca(self.x,self.y))

        if self.y > 900 - 30:
            self.dy = -self.dy
            n.append(Nitca(self.x, self.y))

        if self.x < 0:
            self.dx = -self.dx
            n.append(Nitca(self.x, self.y))

        if self.y < 0:
            self.dy = -self.dy
            n.append(Nitca(self.x, self.y))

        self.x = self.x + self.dx
        self.y = self.y + self.dy
        #return x,y,dx,dy

    def change_speed(self):
        self.speed = self.speed + 1
        #return speed

    def change_color(self):

        if self.r == 255 or self.r == 0:
            self.dr = -self.dr
        if self.g == 255 or self.g == 0:
            self.dg = -self.dg
        if self.b == 255 or self.b == 0:
            self.db = -self.db

        self.r = self.r + self.dr
        self.g = self.g + self.dg
        self.b = self.b + self.db
        #print(r, g, b, dr, dg, db)
        #return r, g, b, dr, dg, db

    def draw(self):
        color = pygame.Color(self.r, self.g, self.b, a=255)
        pygame.draw.circle(screen, color, (self.x, self.y), 50, 20)

c = Kvas()
n = []

pygame.init()
screen = pygame.display.set_mode((1800,900))
pygame.display.set_caption('New')
clock = pygame.time.Clock()

while True:

    pygame.draw.rect(screen,pygame.Color(0,0,0),(0,0,1800,900))

    for i in range(len(n)):
        n[i].draw()
    c.draw()
    c.change_pos()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(160)