import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))
screen.fill((220,220,220))

circle(screen, (255, 255, 0), (250, 250), 200)
circle(screen, (0, 0, 0), (250, 250), 200, 2)

circle(screen, (255, 0, 0), (250*0.7, 250*0.8), 35)
circle(screen, (0, 0, 0), (250*0.7, 250*0.8), 35, 2)
circle(screen, (0, 0, 0), (250*0.7, 250*0.8), 15)

circle(screen, (255, 0, 0), (250*1.3, 250*0.8), 25)
circle(screen, (0, 0, 0), (250*1.3, 250*0.8), 25, 2)
circle(screen, (0, 0, 0), (250*1.3, 250*0.8), 10)

rect(screen, (0, 0, 0), (250*0.7, 250*1.3, 160, 30))


line(screen, (0, 0, 0), (250*0.7+35, 250*0.8-20), (85, 85), 17)
line(screen, (0, 0, 0), (250*1.3-28, 250*0.8-20), (425, 95), 17)

# some new string
v = 95
# and another string
v2 = 3 * 5

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
