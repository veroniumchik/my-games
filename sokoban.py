import random
import pygame
from sys import exit


level = 0

# 0 - пусто
# 1 - стена
# 2 - коробка
# 3 - точка, куда коробка должна попасть
# 9 - игрок

map = []
map.append([[0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 3, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 2, 0, 2, 3, 1],
            [1, 3, 0, 2, 9, 1, 1, 1],
            [1, 1, 1, 1, 2, 1, 0, 0],
            [0, 0, 0, 1, 3, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0]])

map.append([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
            [0, 1, 2, 0, 9, 0, 0, 2, 0, 1, 0],
            [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
            [1, 1, 0, 1, 3, 3, 3, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


class People:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self):
         pygame.draw.circle(screen, pygame.Color(70, 210, 249), (self.x * 50+25, self.y * 50+25), 25)
         pygame.draw.circle(screen, pygame.Color(255, 255, 255), (self.x * 50 + 15, self.y * 50 + 20), 5)
         pygame.draw.circle(screen, pygame.Color(255, 255, 255), (self.x * 50 + 35, self.y * 50 + 20), 5)
         pygame.draw.line(screen, pygame.Color(0, 0, 0), [self.x * 50 + 35, self.y * 50 + 30],
                             [self.x * 50 + 15, self.y * 50 + 30])

    def move(self,d):
        if d == 'left':
            dx = -1
            dy = 0

        if d == 'right':
            dx = 1
            dy = 0

        if d == 'up':
            dx = 0
            dy = -1

        if d == 'down':
            dx = 0
            dy = 1
        if map[level][self.y + dy][self.x + dx] == 1:
            return 0
        if (map[level][self.y + dy][self.x + dx] == 2) or ((map[level][self.y + dy][self.x + dx] == 5)):
            if (map[level][self.y + dy * 2][self.x + dx * 2] == 0) or (
                    map[level][self.y + dy * 2][self.x + dx * 2] == 3):
                map[level][self.y + dy * 2][self.x + dx * 2] = map[level][self.y + dy * 2][self.x + dx * 2] + 2
                map[level][self.y + dy][self.x + dx] = map[level][self.y + dy][self.x + dx] - 2
            else:
                return 0
        self.x = self.x + dx
        self.y = self.y + dy

        win()

def add_chel():
    global chel
    for y in range(len(map[level])):
        for x in range(len(map[level][y])):

            if map[level][y][x] == 9:
                chel = People(x, y)
                map[level][y][x] = 0
def win():
    global level
    w = True

    for y in range(len(map[level])):
        for x in range(len(map[level][y])):
            if map[level][y][x] == 2:
                w = False

    if w:
        level = level + 1
        add_chel()

def draw(d,x,y):
    if d == 'wall':
        pygame.draw.rect(screen, pygame.Color(164, 164, 164), (x * 50, y * 50, 50, 50))
        pygame.draw.line(screen, pygame.Color(87, 87, 87), [x * 50 + 20, y * 50], [x * 50 + 20, y * 50 + 50])
        pygame.draw.line(screen, pygame.Color(87, 87, 87), [x * 50 + 40, y * 50], [x * 50 + 40, y * 50 + 50])
        pygame.draw.line(screen, pygame.Color(87, 87, 87), [x * 50, y * 50 + 20], [x * 50 + 50, y * 50 + 20])
        pygame.draw.line(screen, pygame.Color(87, 87, 87), [x * 50, y * 50 + 40], [x * 50 + 50, y * 50 + 40])
    if d == 'point':
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), (x * 50 + 25, y * 50 + 25), 10)
    if d == 'block':
        pygame.draw.rect(screen, pygame.Color(255, 186, 247), (x * 50, y * 50, 50, 50))
        pygame.draw.line(screen, pygame.Color(255, 32, 229), [x * 50,y * 50 ] , [x * 50 + 50, y * 50 + 50 ]  )
        pygame.draw.line(screen, pygame.Color(255, 32, 229), [x * 50 + 50,y * 50 ] , [x * 50, y * 50 + 50 ]  )
    if d == 'block_on_point':
        pygame.draw.rect(screen, pygame.Color(255, 32, 229), (x * 50, y * 50, 50, 50))
        pygame.draw.line(screen, pygame.Color(244, 186, 247), [x * 50, y * 50], [x * 50 + 50, y * 50 + 50])
        pygame.draw.line(screen, pygame.Color(244, 186, 247), [x * 50 + 50, y * 50], [x * 50, y * 50 + 50])

add_chel()

pygame.init()
screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption('New')
clock = pygame.time.Clock()

while True:

    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (0, 0, 1800, 900))

    for y in range(len(map[level])):
        for x in range(len(map[level][y])):

            if map[level][y][x] == 1:
                draw('wall', x, y)

            if map[level][y][x] == 2:
                draw('block', x, y)

            if map[level][y][x] == 3:
                draw('point', x, y)

            if map[level][y][x] == 5:
                draw('block_on_point', x, y)

    chel.draw()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                chel.move('left')
            if event.key == pygame.K_RIGHT:
                chel.move('right')
            if event.key == pygame.K_UP:
                chel.move('up')
            if event.key == pygame.K_DOWN:
                chel.move('down')

    pygame.display.update()
    clock.tick(160)

