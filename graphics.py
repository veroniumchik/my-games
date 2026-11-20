import random
import pygame
from sys import exit
import math

class P:
    def __init__(self,size):
        self.size = size
        self.r = 255 - size * 1
        self.g = 0
        self.b = 255 - size * 1
        self.angle = 0
        self.x = 900
        self.y = 450

    def turn(self):
        self.angle = self.angle + 0.4 + self.size / 5

    def draw(self):
        x1 = math.floor(math.sin(math.radians(self.angle + 45)) * self.size * 2) + self.x
        y1 = math.floor(math.cos(math.radians(self.angle + 45)) * self.size * 2) + self.y

        x2 = math.floor(math.sin(math.radians(self.angle + 135)) * self.size * 2) + self.x
        y2 = math.floor(math.cos(math.radians(self.angle + 135)) * self.size * 2) + self.y

        x3 = math.floor(math.sin(math.radians(self.angle + 225)) * self.size * 2) + self.x
        y3 = math.floor(math.cos(math.radians(self.angle + 225)) * self.size * 2) + self.y

        x4 = math.floor(math.sin(math.radians(self.angle + 315)) * self.size * 2) + self.x
        y4 = math.floor(math.cos(math.radians(self.angle + 315)) * self.size * 2) + self.y

        pygame.draw.polygon(screen,(self.r,self.g,self.b),((x1,y1),(x2,y2),(x3,y3),(x4,y4)))





cp = []

for i in range(255):
    cp.append(P(255 - i))

pygame.init()
screen = pygame.display.set_mode((1800,900))
pygame.display.set_caption('New')
clock = pygame.time.Clock()

while True:

    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0, 0, 1800, 900))



    for i in  range(255):
        cp[i].turn()
        cp[i].draw()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(160)