from graphic import Dot
from random import randint
import pygame
import os
import time
import random

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    Dots = []
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    temp = Dot(randint(0, 1000), randint(0,1000),255,255,255)
                    Dots.append(temp)

        for d in Dots:

            pygame.draw.circle(WIN, (d.r, d.g, d.b), (d.x, d.y), 10, 9)
            pygame.display.update()
main()
