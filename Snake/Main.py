import Display
import pygame
pygame.init()
screen = Display.pywindow(500, 500, 'Snake', 'None', backColor = (0,0,255))
screen.updateSysstat()
screen.updateScreen()
thing = Display.gameObject(True, False, 10, 10, 0, 0, 'minecraft_icon.bmp',(0,0,0))
while True:
     screen.update()