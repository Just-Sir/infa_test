import random
import pygame
from pygame.draw import *

class MyPicture:
    def __init__(self, n_stripes: int):
        self.n = n_stripes
        self.width_stripe = HEIGTH / self.n
                
    def draw_bg(self):
        for i in range(self.n-1):
            # Drawning upper stripes
            if i is not self.n-2:
                rect(
                screen, (self._colorize()),
                (0, self.width_stripe*i, WIDTH, self.width_stripe)
                )
            # Drawning the lower thick stripe
            else:
                rect(
                screen, (self._colorize()),
                (0, self.width_stripe*i, WIDTH, self.width_stripe*2)
                )
    
    def draw_mountians(self):
        pass
        
    def draw_sun(self, r: int):
        circle(
        screen, (255, 255, 0), (WIDTH/2-r, self.width_stripe), r
        )
          
    def _colorize(self):
        color = ()
        for i in range(3):
            color += (random.randint(0, 255),)
        return color    
  

pygame.init()

WIDTH, HEIGTH = 1280, 500
FPS = 30
picture = MyPicture(5)
screen = pygame.display.set_mode((WIDTH, HEIGTH))

picture.draw_bg()
picture.draw_sun(70)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()