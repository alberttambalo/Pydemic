from graphic import Dot
from graphic import Line
from random import randint
import pygame
pygame.font.init()
import os
import time
import random
import math

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

BLACK_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "blackground.png")), (WIDTH, HEIGHT))

def main():
    run = True
    FPS = 20
    clock = pygame.time.Clock()
    Dots = []
    InfectedDots = []
    Bars = []
    main_font = pygame.font.SysFont("comicsans", 50)
    graphx = 0
    def move():
        for d in Dots:
            if d.x > 10 and d.x < 740 and d.y > 10 and d.y < 490 and (d.i != 0 or d.j != 0):
                #print("moving")
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
            elif d.y >= 490:
                d.i = randint(-2, 2)
                d.j = randint(-2, 0)
                d.x += d.i
                d.y += d.j
                #print("cb")
            elif d.i == 0 and d.j == 0:
                #print("ij 0\n")
                d.i = randint(-2,2)
                d.j = randint(-2,2)
                d.x += d.i
                d.y += d.j

    def redraw_window():
        WIN.blit(BLACK_BACKGROUND, (0,0))
        infected_label = main_font.render("Infected: " + str(len(InfectedDots)), 1, (255,255,255))
        total_label = main_font.render("Total: " + str(len(Dots)), 1, (255,255,255))
        #gr = main_font.render("Total: " + str(len(Dots)), 1, (255, 255, 255))
        WIN.blit(infected_label, (10, 510))
        WIN.blit(total_label, (250,510))

    def draw_dots():
        for d in Dots:
            pygame.draw.circle(WIN, (d.r, d.g, d.b), (d.x, d.y), 10, 9)

    def spread():
        if len(InfectedDots) == 0:
            return
        else:
            newInfected = []
            for id in InfectedDots:
                #print("72")
                for d in Dots:
                    #print("74")
                    dist = math.sqrt(((id.x-d.x)**2) + ((id.y-d.y)**2))
                    if(dist < 10 and d.infected == False):
                        d.setRGB(255,0,0)
                        d.infected = True
                        newInfected.append(d)
            for ni in newInfected:
                InfectedDots.append(ni)

    def draw_graph():

        pygame.draw.line(WIN, (255,255,255), (20, 720), (700, 720), 5)
        pygame.draw.line(WIN, (255,255,255), (20,720), (20, 550), 5)
        if len(InfectedDots) == 0:
            return
        newLine = Line(20 + graphx, 720, 20 + graphx, (720-170*(len(InfectedDots) / len(Dots))), 255, 255, 255, 2)
        if(graphx < 680):
            Bars.append(newLine)
        for b in Bars:
            pygame.draw.line(WIN, (b.r, b.g, b.b), (b.x1,b.y1), (b.x2,b.y2), b.t)

    while run:

        clock.tick(FPS)
        if len(InfectedDots) != 0:
            graphx += 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    for i in range(0,100):
                        temp = Dot(randint(0, 740), randint(0,500),255,255,255, randint(-2,2), randint(-2,2))
                        Dots.append(temp)
                if event.key == pygame.K_RSHIFT:
                    for d in Dots:
                        if d.infected == False:
                            d.setRGB(255,0,0)
                            d.infected = True
                            InfectedDots.append(d)
                            break
                if event.key == pygame.K_c:
                    Dots = []
                    InfectedDots = []
                    Bars = []
                    graphx = 0
        move()
        redraw_window()
        spread()
        draw_dots()
        draw_graph()

        pygame.display.update()
main()
