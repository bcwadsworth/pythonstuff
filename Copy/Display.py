import pygame
pygame.init()

class pywindow:
    def __init__ (self, width = 500, length = 500, string = 'None', icon = 'None', backColor = (0,0,0)):
        self.width = width
        self.length = length
        self.resolution = (self.width, self.length)
        self.windowString = string
        self.windowIcon = icon
        self.fullscreen = False
        self.resizable = False
        self.frame = True
        self.backColor = backColor
        self.updateSysstat()
        self.updateScreen()
    
    def updateRes(self):
        self.resolution = (width, length)
        
    def updateScreen(self):
        if not self.fullscreen and not self.resizable and not self.frame:
            self.screen = pygame.display.set_mode(resolution, pygame.NOFRAME)
        if not self.fullscreen and not self.resizable and self.frame:
            self.screen = pygame.display.set_mode(resolution)
        if not self.fullscreen and self.resizable and not self.frame:
            self.screen = pygame.display.set_mode(resolution, pygame.NOFRAME|pygame.RESIZABLE)
        if not self.fullscreen and self.resizable and self.frame:
            self.screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
        if self.fullscreen and not self.resizable and not self.frame:
            self.screen = pygame.display.set_mode(resolution, pygame.NOFRAME|pygame.FULLSCREEN)
        if self.fullscreen and not self.resizable and self.frame:
            self.screen = pygame.display.set_mode(resolution|pygame.FULLSCREEN)
        if self.fullscreen and self.resizable and not self.frame:
            self.screen = pygame.display.set_mode(resolution, pygame.NOFRAME|pygame.RESIZABLE|pygame.FULLSCREEN)
        if self.fullscreen and self.resizable and self.frame:
            self.screen = pygame.display.set_mode(resolution, pygame.RESIZABLE|pygame.FULLSCREEN)

    def updateSysstat(self):
        if self.windowString != 'None':
            self.screen.set_caption(windowString)
        if self.windowIcon != 'None':
            self.screen.set_icon(windowIcon)

    def update(self, blank):
        self.screen.fill(self.backColor)
        for n in range(gameObject.gameObjects - 1):
            if gameObject.gameObjectArray[n][0]:
                self.screen.blit(gameObject.gameObjectArray[n][1], gameObject.gameObjectArray[n][2])
                # Array Entry = True, file, position
            else:
                if gameObject.gameObjectArray[n][1]:
                    pygame.draw.Rect(self.screen, gameObject.gameObjectArray[n][3],gameObject.gameObjectArray[n][2])
                    # Array Entry = False, True, Rect, Color
                else:
                    pygame.draw.circle(self.screen, gameObject.gameObjectArray[n][4], gameObject.gameObjectArray[n][2], gameObject.gameObjectArray[n][3])
                    # Array Entry = False, False, Coordinates, Radius, Color


class gameObject:
     gameObjects = 0
     gameObjectArray = []
     def __init__(self, blit, shape, x, y, lengthradius, width, filename, color):
         if blit:
              self.active = True
              self.blit = True
              self.filename = filename
              self.x = x
              self.y = y
              self.array = -1
              
         elif shape:
              self.active = True
              self.blit = True
              self.shape = True
              self.x = x
              self.y = y
              self.length = lengthradius
              self.width = width
              self.color = color
              self.array = -1
              
         else:
              self.active = True
              self.blit = True
              self.shape = False
              self.x = x
              self.y = y
              self.radius = lengthradius
              self.color = color
              self.array = -1
          
         self.update()
          
     def update(self):
          global gameObjectArray
          global gameObjects
          if self.active and self.blit:
               if self.array == -1:
                    self.position = (self.x,self.y)
                    gameObjectArray.append([True, self.filename, self.position])
                    self.array = len(gameObjectArray) - 1
                    gameObjects += 1
               else:
                    self.position = (self.x,self.y)
                    gameObjectArray[self.array] = [True, str(self.filename), self.position]
          elif self.active and self.shape:
               if self.array == -1:
                    self.rect = pygame.Rect(self.x, self.y, self.length, self.width)
                    gameObjectArray.append([False, True, self.rect, self.color])
                    self.array = len(gameObjectArray) - 1
                    gameObjects += 1
               else:
                    self.rect = pygame.Rect(self.x, self.y, self.length, self.width)
                    gameObjectArray.append([False, True, self.rect, self.color])
          elif self.active and not self.shape:
               if self.array == -1:
                    self.position = (self.x,self.y)
                    gameObjectArray.append([False, False, self.position, self.radius, self.color])
                    self.array = len(gameObjectArray) - 1
                    gameObjects += 1
               else:
                    gameObjectArray.append([False, False, self.position, self.radius, self.color])
          else:
               if self.array == -1:
                    pass
               else:
                    gameObjectArray.remove(self.array)
                    self.array = -1
                    gameObjects += -1
                    
               

