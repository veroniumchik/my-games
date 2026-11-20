import random
from turtledemo.nim import randomrow
import pygame

def change_lvl(lvl):
    p = 0
    for i in range(len(s)):
        p = p + len(s[i].el)
    p = p - 5
    if lvl == 1 and p >= 5:
        lvl = 2
    if lvl == 2 and p >= 15:
        lvl = 3
        #for i in range(len(s.el) - 5):
        #    s.el.pop(0)
    return lvl


pygame.font.init()

my_font = pygame.font.SysFont('котики милые', 30)

x = 0
y = 0
k = 0
level = 1
screen = pygame.display.set_mode((1800, 900))

class Apple:
    def __init__(self,x=None,y=None):
        if x is None:
            self.x = random.randint(1,35) * 50
        else:
            self.x = x
        if y is None:
            self.y = random.randint(1,15) * 50
        else:
            self.y = y
        a = random.randint(0,5)
        self.t = 1
        if a == 0:
            self.t = 2
        if a == 3:
            self.t = 3
    def food_draw(self):
        if self.t == 1:
            pygame.draw.circle(screen, (255, 97, 97), (self.x, self.y), 15)
        if self.t == 2:
            pygame.draw.circle(screen, (249, 255, 129), (self.x, self.y), 30)
        if self.t == 3:
            pygame.draw.circle(screen, (0, 27, 183), (self.x, self.y), 15)

apple = []
for i in range(5):
    apple.append(Apple())

clock = pygame.time.Clock()

class El_snake:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, (31,255, 57), (self.x - 20, self.y - 20, 40, 40), 50,2)
        #print(self.x, self.y)
    def morda(self):
        pygame.draw.rect(screen, (8,134, 24), (self.x - 20, self.y - 20, 40, 40), 50,2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + 35 - 20, self.y + 30 - 20),(self.x + 5 - 20, self.y + 30 - 20), 3)
        pygame.draw.circle(screen, (0, 0, 0,), (self.x + 15 - 20, self.y + 15 - 20),3)
        pygame.draw.circle(screen, (0, 0, 0,), (self.x + 15 - 20, self.y + 35 - 20),3)

class Snake:
    def __init__(self,x,y,el=None):
        self.x = x
        self.y = y
        self.d = 0 # 0 = низ/ 1 = верх/ 2 = лево/ 3 = право
        self.z = 0
        if el is not None:
            self.el = el
        else:
            self.el = []
            for i in range(5):
                self.el.append(El_snake(self.x, i * 50 + 200))

    def kill(self):
        global apple
        for j in range(len(self.el)):
            apple.append(Apple(self.el[j].x, self.el[j].y))
        for j in range(len(s)):
            if self == s[j]:
                s.pop(j)
                return 1

    def draw(self):
        for i in range(len(self.el)):
            self.el[i].morda()
        for i1 in range(len(self.el) - 1):
            self.el[i1].draw()

    def move(self):
        if len(self.el) > 1:
            for i in range(len(s)):
                for j in range(len(s[i].el) - 1):
                    if s[i].el[j].x == self.el[-1].x and s[i].el[j].y == self.el[-1].y and s[i].el[j] != self.el[-1]: # Змея врезалась в змею
                        if self.el[0].x != self.el[-1].x and self.el[0].y != self.el[-1].y: # Костыль чтобы змея длиной 1 не умирала когда кушает
                            self.kill()
                            return 1

            for j in range(len(self.el) - 1):
                if (abs(self.el[j + 1].x - self.el[j].x) + abs(self.el[j + 1].y - self.el[j].y) <= 50
                        or abs(self.el[j + 1].x - self.el[j].x) + abs(self.el[j + 1].y - self.el[j].y) >= 500): # Дырки нет
                    print('1')
                    self.el[j].x = self.el[j + 1].x
                    self.el[j].y = self.el[j + 1].y
                else: # Дырка есть
                    if j != 0:
                        s.append(Snake(self.el[j].x,self.el[j].y,self.el[0:j]))
                        self.el[0:j] = []
                        return 0
            if self.d == 0:
                self.el[-1].y = self.el[-1].y + 50
            if self.d == 1:
                self.el[-1].y = self.el[-1].y - 50
            if self.d == 2:
                self.el[-1].x = self.el[-1].x - 50
            if self.d == 3:
                self.el[-1].x = self.el[-1].x + 50

        elif len(self.el) == 1:
            if self.d == 0:
                self.el[0].y = self.el[0].y + 50
            if self.d == 1:
                self.el[0].y = self.el[0].y - 50
            if self.d == 2:
                self.el[0].x = self.el[0].x - 50
            if self.d == 3:
                self.el[0].x = self.el[0].x + 50

        else:
            for i in range(len(s)):
                if s[i] == self:
                    s.pop(i)
                    return 1

        if self.el[-1].x >= 1800:
            self.el[-1].x = 0
        if self.el[-1].y >= 900:
            self.el[-1].y = 0
        if self.el[-1].x < 0:
            self.el[-1].x = 1750
        if self.el[-1].y < 0:
            self.el[-1].y = 850

        for i in range(len(b[level-1])): # Кирпичи
            if len(self.el) > 1:
                if self.el[-1].x == b[level-1][i].x and self.el[-1].y == b[level-1][i].y:
                    self.kill()
            else:
                if self.el[0].x == b[level-1][i].x and self.el[0].y == b[level-1][i].y:
                    self.kill()



        for i1 in range(len(apple)):
            if (self.el[-1].x // 50 == apple[i1].x  // 50)  and (self.el[-1].y  // 50 == apple[i1].y  // 50):
                if apple[i1].t == 1:
                    self.el.insert(0,(El_snake(self.el[0].x, self.el[0].y)))
                if apple[i1].t == 2:
                    for i in range(10):
                        self.el.insert(0,(El_snake(self.el[0].x, self.el[0].y)))

                if apple[i1].t == 3:
                    self.z = 25
                apple.pop(i1)
                break
                print('ура борщ')



class Brick:
    def __init__(self,x,y):
        self.x = x + 50
        self.y = y + 50

    def draw(self):
        #(self.x, self.y)
        pygame.draw.rect(screen, (255, 136, 85), (self.x - 25, self.y - 25, 50,  50))
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 25, self.y - 25, 50, 50),1)

        pygame.draw.line(screen, (0,0,0), (self.x - 25, self.y - 25 + 13), ( self.x + 50 - 25,self.y + 13 - 25))
        pygame.draw.line(screen, (0,0,0), (self.x - 25, self.y + 26  - 25), ( self.x + 50 - 25,self.y + 26 - 25))
        pygame.draw.line(screen, (0, 0, 0), (self.x - 25, self.y - 25 + 39), (self.x + 50 - 25, self.y + 39 - 25))

        pygame.draw.line(screen, (0, 0, 0), (self.x + 13 - 25, self.y - 25), (self.x + 13 - 25, self.y + 13 - 25))
        pygame.draw.line(screen, (0, 0, 0), (self.x + 26 - 25, self.y + 13 - 25), (self.x + 26 - 25, self.y + 26 - 25))
        pygame.draw.line(screen, (0, 0, 0), (self.x + 39 - 25, self.y + 26 - 25), (self.x + 39 - 25, self.y + 39 - 25))
        pygame.draw.line(screen, (0, 0, 0), (self.x + 13 - 25, self.y + 39 - 25), (self.x + 13 - 25, self.y + 49 - 25))





s = []
s.append(Snake(200,200))
b = [[],[],[]]
for i in range(36):
    b[1].append(Brick(i * 50, 0))
for i in range(36):
    b[1].append(Brick(0, i * 50))
for i in range(36):
    b[1].append(Brick(i * 50, 800))
for i in range(36):
    b[1].append(Brick(1700, i * 50))

for i in range(5):
    b[2].append(Brick(i * 50, 0))
for i in range(5):
    b[2].append(Brick(0, i * 50))
for i in range(5):
    b[2].append(Brick(i * 50, 800))
for i in range(5):
    b[2].append(Brick(0, i * 50 + 550))
for i in range(5):
    b[2].append(Brick(1700, i * 50))
for i in range(5):
    b[2].append(Brick(i * 50 + 1500, 0))
for i in range(5):
    b[2].append(Brick(i * 50 + 1500, 800))
for i in range(5):
    b[2].append(Brick(1700, i * 50 + 550))

class Bomb:
    def __init__(self):
        self.x = random.randint(1,36) * 50
        self.y = random.randint(1,17) * 50
        self.t = 300
        self.color = 0
    def draw(self):
        pygame.draw.circle(screen,(self.color, 0 ,0), (self.x, self.y), 20)
    def tick(self,j):
        self.t = self.t - 1
        if self.t % 10 == 0:
            if self.color == 255:
               self.color = 0
            else:
                self.color = 255
        if self.t <= 0:
            for i in range(36):
                pygame.draw.line(screen, (self.color, 0, 0), (i * 50 - 25, self.y - 25), (i * 50 + 25, self.y + 25), 5)
                pygame.draw.line(screen, (self.color, 0, 0), ( self.x + 25, i * 50 + 25), ( self.x - 25, i * 50 - 25), 5)
                pygame.draw.line(screen, (self.color, 0, 0), (i * 50 + 25, self.y - 25), (i * 50 - 25, self.y + 25), 5)
                pygame.draw.line(screen, (self.color, 0, 0), ( self.x - 25, i * 50 + 25), ( self.x + 25, i * 50 - 25), 5)

            for i, el in enumerate(apple):
                if el.y == self.y:
                    apple.pop(i)
                if el.x == self.x:
                    apple.pop(i)

            for i, el in enumerate(b[level - 1]):
                if el.y == self.y:
                    b[level - 1].pop(i)
                elif el.x == self.x:
                    b[level - 1].pop(i)

            for j in range(len(s)):
                for i, el in enumerate(s[j].el):
                    if el.y == self.y:
                        s[j].el.pop(i)
                    elif el.x == self.x:
                        s[j].el.pop(i)

        if self.t <= -30:
            for i in range(len(bo)):
                if bo[i] == self:
                    bo.pop(i)
                    return True



bo = []









while True:
    pygame.draw.rect(screen, pygame.Color(133, 255, 147), (0, 0, 1800, 900))
    for i in range(len(apple)):
        apple[i].food_draw()
    level = change_lvl(level)

    p = 0

    for i in range(len(s)):
        p = p + len(s[i].el)
    text_surface = my_font.render(f'очки:{p - 5}, а нужно 50', False, (255, 30, 30))


    screen.blit(text_surface, (0, 0))

    for i in range(len(s)):
        if i < len(s):
            if s[i].z == 0:
                if k % 15 == 0:
                    print(i, s[i].z, len(s[i].el),len(s))
                    if s[i].move() == 1:
                        print('жопа')
                        break


    for i in range(len(s)):
        if s[i].z > 0:
            if k % 5 == 0:
                if s[i].move() == 1:
                    print('попа')
                    break
                s[i].z = s[i].z - 1
    if k % 100 == 0:
        apple.append(Apple())

    #for i in range(len(s)):
    #    print(i,s[i].z, len(s[i].el))
    if level >= 2:
        if random.randint(0, 300) == 0 or random.randint(0, 300) == 299:
            bo.append(Bomb())
        for i in range(len(bo)):
            if bo[i].tick(i):
                break
            bo[i].draw()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for i in range(len(s)):
                    if s[i].d != 3:
                        s[i].d = 2
            if event.key == pygame.K_RIGHT:
                for i in range(len(s)):
                    if s[i].d != 2:
                        s[i].d = 3
            if event.key == pygame.K_UP:
                for i in range(len(s)):
                    if s[i].d != 0:
                        s[i].d = 1
            if event.key == pygame.K_DOWN:
                for i in range(len(s)):
                    if s[i].d != 1:
                        s[i].d = 0

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            pass
    for i in range(len(b[level-1])):
        b[level-1][i].draw()

    for i in range(len(s)):
        s[i].draw()
    pygame.display.update()
    clock.tick(60)
    k = k + 1

