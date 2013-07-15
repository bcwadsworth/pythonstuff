import pygame
import sys
pygame.init()
a = 0
b = 0
c = 0
color = (0, 0, 0)
resolution = width, height = 1920, 1920
screen = pygame.display.set_mode(resolution)

while True:
    #Input

    #Move
    a += 9
    b += 6
    c += 21
    if a > 255:
        a += -255
    if b > 255:
        b += -255
    if c > 255:
        c += -255
    color = (a, b, c)
        
    #Draw
    screen.fill(color)
    pygame.display.flip() 
    pygame.time.delay(10)

    #Check for quit
    if pygame.event.peek(pygame.KEYDOWN): 
        pygame.quit
        sys.exit

