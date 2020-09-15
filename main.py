from graphic import Dot
from random import randint
import pygame
import os
import time
import random

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

BLACK_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "blackground.png")), (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 120
    clock = pygame.time.Clock()
    Dots = []
    def move():
        for d in Dots:
            if d.x > 10 and d.x < 740 and d.y > 10 and d.y < 740 and (d.i != 0 or d.j != 0):
                print("moving")
                d.x += d.i
                d.y += d.j
            elif d.x <= 10:
                d.i = randint(0, 2)
                d.j = randint(-2, 2)
                d.x += d.i
                d.y += d.j
                #print("cl")
            elif d.y <= 10:
                d.i = randint(-2, 2)
                d.j = randint(0, 2)
                d.x += d.i
                d.y += d.j
                #print("ct")
            elif d.x >= 740:
                d.i = randint(-2, 0)
                d.j = randint(-2, 2)
                d.x += d.i
                d.y += d.j
                #print("cr")
            elif d.y >= 740:
                d.i = randint(-2, 2)
                d.j = randint(-2, 0)
                d.x += d.i
                d.y += d.j
                #print("cb")
            elif d.i == 0 and d.j == 0:
                print("ij 0\n")
                d.i = randint(-2,2)
                d.j = randint(-2,2)
                d.x += d.i
                d.y += d.j

    def redraw_window():
        WIN.blit(BLACK_BACKGROUND, (0,0))
        #pygame.display.update()

    def draw_dots():
        for d in Dots:
            pygame.draw.circle(WIN, (d.r, d.g, d.b), (d.x, d.y), 10, 9)
    while run:
        clock.tick(FPS)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    temp = Dot(randint(0, 1000), randint(0,1000),255,255,255, randint(-2,2), randint(-2,2))
                    Dots.append(temp)
                    print('Appended: ' + str(temp.i) + ', ' + str(temp.j))
        move()
        redraw_window()
        draw_dots()
        pygame.display.update()
main()
