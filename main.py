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
    FPS = 30
    clock = pygame.time.Clock()
    Dots = []
    InfectedDots = []
    Bars = []
    main_font = pygame.font.SysFont("comicsans", 50)
    graphx = 0
    R0 = 0.0
    Disease = "Healthy"
    ss = 5

    def move():
        for d in Dots:
            if d.x > 10 and d.x < 740 and d.y > 10 and d.y < 490 and (d.i != 0 or d.j != 0):
                #print("moving")
                d.x += d.i
                d.y += d.j
            elif d.x <= 10:
                d.i = randint(0, d.speed)
                d.j = randint(-d.speed, d.speed)
                d.x += d.i
                d.y += d.j
                #print("cl")
            elif d.y <= 10:
                d.i = randint(-d.speed, d.speed)
                d.j = randint(0, d.speed)
                d.x += d.i
                d.y += d.j
                #print("ct")
            elif d.x >= 740:
                d.i = randint(-d.speed, 0)
                d.j = randint(-d.speed, d.speed)
                d.x += d.i
                d.y += d.j
                #print("cr")
            elif d.y >= 490:
                d.i = randint(-d.speed, d.speed)
                d.j = randint(-d.speed, 0)
                d.x += d.i
                d.y += d.j
                #print("cb")
            elif d.i == 0 and d.j == 0:
                #print("ij 0\n")
                d.i = randint(-d.speed, d.speed)
                d.j = randint(-d.speed, d.speed)
                d.x += d.i
                d.y += d.j

    def redraw_window():
        WIN.blit(BLACK_BACKGROUND, (0,0))
        infected_label = main_font.render("Infected: " + str(len(InfectedDots)), 1, (255,255,255))
        total_label = main_font.render("Total: " + str(len(Dots)), 1, (255,255,255))
        r0_label = main_font.render("R0: " + str(R0), 1, (255, 255, 255))
        disease_label = main_font.render(Disease, 1, (255, 255, 255))
        WIN.blit(infected_label, (10, 510))
        WIN.blit(total_label, (250,510))
        WIN.blit(r0_label, (450, 510))
        WIN.blit(disease_label, (10, 0))

    def draw_dots():
        for d in Dots:
            pygame.draw.circle(WIN, (d.r, d.g, d.b), (d.x, d.y), 10, 9)

    def spread():
        if len(InfectedDots) == 0:
            return
        else:
            newInfected = []
            newRecovered = []
            for id in InfectedDots:
                id.sick -= 1
                if id.sick == 0:
                    id.sick = -1
                    id.infected = 2
                    id.setRGB(0,0,255)
                    id.speed = 5
                    id.i = randint(-id.speed, id.speed)
                    id.j = randint(-id.speed, id.speed)
                    newRecovered.append(id)
                for d in Dots:
                    if d.infected == 1 or d.infected == 2:
                        continue
                    dist = math.sqrt(((id.x-d.x)**2) + ((id.y-d.y)**2))
                    if dist < 30 and d.infected == 0 and id.r0-1 >= 0:
                        id.r0 -= 1
                        d.setRGB(255,0,0)
                        d.infected = 1
                        d.sick = 300
                        d.speed = ss
                        d.i = randint(-d.speed, d.speed)
                        d.j = randint(-d.speed, d.speed)
                        newInfected.append(d)
            for ni in newInfected:
                InfectedDots.append(ni)
            for nr in newRecovered:
                InfectedDots.remove(nr)

    def draw_graph():
        pygame.draw.line(WIN, (255,255,255), (20, 720), (700, 720), 5)
        pygame.draw.line(WIN, (255,255,255), (20,720), (20, 550), 5)
        if graphx == 0:
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
                        temp = Dot(randint(0, 740), randint(0,500),255,255,255, randint(-5,5), randint(-5,5), random.uniform(R0-1,R0+1), 5, 1)
                        Dots.append(temp)
                if event.key == pygame.K_RSHIFT:
                    for d in Dots:
                        if d.infected == 0:
                            d.setRGB(255,0,0)
                            d.infected = 1
                            d.sick = randint(1000,3000)
                            InfectedDots.append(d)
                            break
                if event.key == pygame.K_c:
                    Dots = []
                    InfectedDots = []
                    Bars = []
                    graphx = 0
                    Disease = "Healthy"
                    R0 = 0
                if event.key == pygame.K_1:
                    Dots = []
                    InfectedDots = []
                    Bars = []
                    graphx = 0
                    Disease = "Seasonal Flu"
                    R0 = 1.1

                if event.key == pygame.K_2:
                    Dots = []
                    InfectedDots = []
                    Bars = []
                    graphx = 0
                    Disease = "Influenza"
                    R0 = 1.8
                    ss = 1
                if event.key == pygame.K_3:
                    Dots = []
                    InfectedDots = []
                    Bars = []
                    graphx = 0
                    Disease = "Ebola Virus"
                    R0 = 1.9
                    ss = 1
                if event.key == pygame.K_4:
                    Dots = []
                    InfectedDots = []
                    Bars = []
                    graphx = 0
                    Disease = "Corona Virus"
                    R0 = 2.1
                    ss = 5
                if event.key == pygame.K_5:
                    Dots = []
                    InfectedDots = []
                    Bars = []
                    graphx = 0
                    Disease = "Smallpox"
                    R0 = 5.9
                    ss = 1
                if event.key == pygame.K_6:
                    Dots = []
                    InfectedDots = []
                    Bars = []
                    graphx = 0
                    Disease = "Measles"
                    R0 = 11.5
                    ss = 1
        move()
        redraw_window()
        spread()
        draw_dots()
        draw_graph()

        pygame.display.update()
main()
