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
    
    def draw_mountians(self, start: tuple, n_dots: int):
        polygon(screen, self._colorize(), self._dots(start, n_dots))
               
    def draw_sun(self, r: int):
        circle(
        screen, (255, 255, 0), (WIDTH/2-r, self.width_stripe), r
        )
          
    def _colorize(self):
        color = ()
        for i in range(3):
            color += (random.randint(0, 255),)
        return color
    
    def _dots(self, start, n):
        d = [start]
        mount_h = HEIGTH/5
        len_segment = random.randrange(int(WIDTH/9), int(WIDTH/6))
        down = int(start[1])
        up = int(start[1] - mount_h)        
        
        for i in range(n):
            left = int(d[i][0])
            right = int(d[i][0] + len_segment)
            
            x = random.randrange(left, right)
            y = random.randrange(up, down)
            d.append((x, y))
        d.append((WIDTH, start[1]))        
        return d
        
        
pygame.init()

WIDTH, HEIGTH = 1280, 500
FPS = 30
picture = MyPicture(5)
screen = pygame.display.set_mode((WIDTH, HEIGTH))

picture.draw_bg()
picture.draw_sun(70)
picture.draw_mountians((5, HEIGTH/2), 19)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()