import random
import pygame
from pygame.draw import *

class Background:
    def __init__(self, n_stripes):
        self.n = n_stripes
        self.width_stripe = HEIGTH / self.n
                
    def draw(self):
        for i in range(self.n):
            rect(
            screen, (self.colorize()),
            (0, self.width_stripe*i, WIDTH, self.width_stripe)
            )
             
    def colorize(self):
        color = ()
        for i in range(3):
            color += (random.randint(0, 255),)
        return color    
  

pygame.init()

WIDTH, HEIGTH = 1280, 500
FPS = 30
bg = Background(5)
screen = pygame.display.set_mode((WIDTH, HEIGTH))

bg.draw()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()