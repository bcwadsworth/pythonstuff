import pygame
import sys
import random
pygame.init()
smallFont = pygame.font.SysFont('Ariel', 64, False, False)
largeFont = pygame.font.SysFont('Ariel', 128, False, False)
color = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ballreturn = 0    
strEvent = 'To Start, Press Space'
Win = False
paddleaY = 250
paddleadir = 0
paddlebY = 250
paddlebdir = 0
balldir = 2
ballXdir = 0
ballX = 700
ballYdir = 0
ballY = 350
scoreA = 0
scoreB = 0
resolution = width, height = 1400, 700
screen = pygame.display.set_mode(resolution)
collision = False

def checkIntersect(bally, flippery):
    for value in range(flippery, flippery + 201):
        for ballValue in range(bally-20, bally+21):
            if value == ballValue:
                return True
    return False

def wait(delay):
    pygame.time.delay(delay)

def draw(gameElements, ball):
    global color
    global screen
    for n in range(0,15):
        color[n] += random.randrange(0, 21)
        if color[n] > 255:
            color[n] += -255
    colorA = (color[0], color[1], color[2])
    colorB = (color[3], color[4], color[5])
    colorC = (color[6], color[7], color[8])
    colorD = (color[9], color[10], color[11])
    colorE = (color[12], color[13], color[14])
    p1render = smallFont.render('P1: ' + str(scoreA), True, colorA)
    p2render = smallFont.render('P2: ' + str(scoreB), True, colorA)
    eventrender = largeFont.render(str(strEvent), True, colorA)
    screen.fill(colorB)
    screen.blit(p1render, (50,50))
    screen.blit(p2render, (1250,50))
    screen.blit(eventrender, (300,300))
    if gameElements:
        paddle = pygame.Rect(100, paddleaY, 50, 200)
        pygame.draw.rect(screen, colorC, paddle)
        paddle = pygame.Rect(1250, paddlebY, 50, 200)
        pygame.draw.rect(screen, colorD, paddle)
    if ball:
        pygame.draw.circle(screen, colorE, (ballX, ballY), 20)
    pygame.display.flip()
    wait(10)


while strEvent != ' ':
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                strEvent = ' '
    draw(False, False)
    
while True:
    #Input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddleadir = -2
            elif event.key == pygame.K_s:
                paddleadir = 2
            if event.key == pygame.K_UP:
                paddlebdir = -2
            elif event.key == pygame.K_DOWN:
                paddlebdir = 2
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and paddleadir == -2:
                paddleadir = 0
            if event.key == pygame.K_s and paddleadir == 2:
                paddleadir = 0
            if event.key == pygame.K_UP and paddlebdir == -2:
                paddlebdir = 0
            if event.key == pygame.K_DOWN and paddlebdir == 2:
                paddlebdir = 0
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
                
    #Check for and Register Game Events  
    if scoreA == 10 or scoreB == 10:
        if scoreA == 1:
            strEvent = 'P1 Wins!!!'
        else:
            strEvent = 'P2 Wins!!!'
        b = 0
        while b != 1000:
            b += 1
            draw(False, False)
        wait (10000)
        pygame.quit()
        sys.exit()
            
        
    if ballXdir == 0 and not Win:
        b = 0
        while b != 200:
            b += 1
            draw(False, False)
        strEvent = 'Get Ready!'
        b = 0
        while b != 200:
            b += 1
            draw(True, False)
        strEvent = 'GO!'
        b = 0
        while b != 100:
            b += 1
            draw(True, True)
        strEvent = ' '
        ballXdir = balldir
        ballYdir = 2
        balldir = -1*balldir
    
    if ballX >= 100 and ballX <= 150 and ballreturn != 1:
        collision = checkIntersect(ballY, paddleaY)
        if collision:
            ballreturn = 1
        
    if ballX <= 1300 and ballX >= 1250 and ballreturn != 2:
        collision = checkIntersect(ballY, paddlebY)
        if collision:
            ballreturn = 2

    if ballX <= 50:
        scoreB += 1
        strEvent = 'P2 scores!!!'
        ballX = 700
        ballY = 350
        ballXdir = 0
        ballYdir = 0
        ballreturn = 0
        paddleaY = 250
        paddlebY = 250
        
    if ballX >= 1350:
        scoreA += 1
        strEvent = 'P1 scores!!!'
        ballX = 700
        ballY = 350
        ballXdir = 0
        ballYdir = 0
        ballreturn = 0
        paddleaY = 250
        paddlebY = 250
        
    if ballY <= 50:
        ballYdir = ballYdir*-1

    if ballY >= 650:
        ballYdir = ballYdir*-1

    
    if collision:
        ballXdir = ballXdir*-1.1
        ballYdir = ballYdir*1.1
        collision = False
    
    #Move
    paddleaY += paddleadir
    paddlebY += paddlebdir
    ballX += int(ballXdir)
    ballY += int(ballYdir)
    draw(True, True)
