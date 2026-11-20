import pygame
import random

w = 0.8
w2 = 0.6
w3 = 0.4
a = 0

screen = pygame.display.set_mode((1800, 900))

class Cloud:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.drop = []
    def draw(self):
        for i in range(len(self.drop)):
            self.drop[i].draw()

        pygame.draw.circle(screen, pygame.Color(140, self.y // 4, 255), (self.x,self.y), 70)
        pygame.draw.circle(screen, pygame.Color(140, self.y // 4, 255), (self.x - 50,self.y + 50), 70)
        pygame.draw.circle(screen, pygame.Color(140, self.y // 4, 255), (self.x + 50, self.y + 50), 70)

    def piss(self):
        self.drop.append(Drop(self.x + random.randint(0,200) - 100, self.y))
    def move(self):
        shift = self.x + w / (self.y / 150 ) + w / 4

        for i in range(len(cloud)):
            if (cloud[i].x - self.x < 250)and(cloud[i].x - self.x > 0)and(w > 0)and(cloud[i] != self)and(cloud[i].y == self.y):
                shift = self.x
                #print(self.x,cloud[i].x,i, cloud[i].x - self.x)
            if (self.x - cloud[i].x < 250)and(self.x - cloud[i].x > 0)and(w < 0)and(cloud[i] != self)and(cloud[i].y == self.y):
                shift = self.x
                #print(self.x, cloud[i].x, i, cloud[i].x - self.x)

        if (self.x >= 1800 - 125)and(w > 0):
            shift = 1800 - 125
        if (self.x <= 0 + 125)and(w < 0):
            shift = 0 + 125
            #print(self.x, cloud[i].x, i, cloud[i].x - self.x)

        self.x = shift

class Drop:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = y // 4
    def draw(self):
        if self.y < 900:
            self.y = self.y + 1
            self.x = self.x + w
            pygame.draw.line(screen,(8,107,self.color), (self.x, self.y), (self.x, self.y + 10))
        if self.y == 899:
            i = int((self.x) // 18)
            if i > 99:
                i = 99
            if i < 0:
                i = 0
            grass[i].h += 1

cloud = []
for i in range(5):
    cloud.append(Cloud(i * 350 + 100,100))
for i2 in range(5):
    cloud.append(Cloud(i2 * 350 + 100,400))
for i3 in range(5):
    cloud.append(Cloud(i3 * 350 + 100,700))

clock = pygame.time.Clock()

class Grass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.h = 5
    def draw(self):
        pygame.draw.line(screen, (21, 173,18), (self.x, self.y),(self.x, self.y - self.h))
        self.h = self.h - 0.1
        if self.h < 1:
            self.h = 1

grass = []


for i in range(100):
    grass.append(Grass(i * 18, 890))
    print('жопа', i)



while True:

    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0, 0, 1800, 900))


    for i in range(15):
        cloud[i].move()
        cloud[i].piss()
        cloud[i].draw()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            pass

    for i in range(100):
        grass[i].draw()
    a = a + 1
    if a == 800:
        a = 0
        w = (random.randint(0, 2) - 1) / 1
    pygame.display.update()
    clock.tick(160)