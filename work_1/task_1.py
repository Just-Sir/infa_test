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
circle(screen, (0, 0, 0), (250*0.7, 250*0.8), 10)

circle(screen, (255, 0, 0), (250*1.3, 250*0.8), 35)
circle(screen, (0, 0, 0), (250*1.3, 250*0.8), 35, 2)
circle(screen, (0, 0, 0), (250*1.3, 250*0.8), 10)

rect(screen, (0, 0, 0), (250*0.7, 250*1.3, 160, 30))


line(screen, (125, 152, 10), (85, 85), (240, 240), 12)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
