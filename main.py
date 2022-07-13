# pygame
# pip freeze
from json import load
import pygame,sys,time

fps = 60
gameclock = pygame.time.Clock()

canvasWidth = 720
canvasHeight = 670

window = pygame.display.set_mode((canvasWidth,canvasHeight))

def loadImage(name,sx = -1,sy = -1):
    a = pygame.image.load(name).convert_alpha() # transparent
    a = pygame.transform.scale(a,(sx,sy))
    return a
    
    
bg = loadImage('bg.jpg',720,720)
gameOverImg = loadImage('gameOverImg.jpg',760,canvasHeight)
# ping = loadImage('pingpong.png',200,100)
# Surfaces

paddle1x = 260
paddle1y = 0

paddle2x = 260
paddle2y = 620

direction = 0
direction2 = 0

ballMoveX = canvasWidth/2-100
ballMoveY = canvasHeight/2-45

directionX = 6
directionY = 3

life = 3
pygame.init()
font = pygame.font.SysFont('Roboto', 16)

def gameOver2():
    window.blit(gameOverImg,(0,0))

while True:
    window.fill(pygame.Color(255,120,46))
    window.blit(bg, (0,0))
    
    p1 = pygame.draw.rect(window,pygame.Color(0,255,0),pygame.Rect(paddle1x,paddle1y,200,50)) # (l,t,w,h)
    p2 = pygame.draw.rect(window,pygame.Color(0,255,0),pygame.Rect(paddle2x,paddle2y,200,50)) # (l,t,w,h)
    ball = pygame.draw.circle(window, pygame.Color(0,0,234),(ballMoveX,ballMoveY),40) # (l,t,w,

    if ballMoveX >= 675 or ballMoveX <= 18:
        directionX = directionX * -1
        # directionY = directionY * -1

    if p2.collidepoint(ballMoveX,ballMoveY+40):
        directionY = directionY * -1

    if p1.collidepoint(ballMoveX,ballMoveY-38):
        directionY = directionY * -1
        print("working")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # paddle1x -= 10
                direction = -10
                
            if event.key == pygame.K_d:
                # paddle1x += 10
                direction = 10
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # paddle1x -= 10
                direction2 = -10
                
            if event.key == pygame.K_RIGHT:
                # paddle1x += 10
                direction2 = 10


        
    paddle1x += direction
    if paddle1x <= 0:
        paddle1x = 0
        
    if paddle1x >= 520:
        paddle1x = 520

    paddle2x += direction2
    if paddle2x <= 0:
        paddle2x = 0
        
    if paddle2x >= 520:
        paddle2x = 520
    
    ballMoveX = ballMoveX+directionX
    ballMoveY = ballMoveY+directionY

    if ballMoveY > 620 or ballMoveY < 0:
        life -= 1
        ballMoveX = canvasWidth/2-100
        ballMoveY = canvasHeight/2-45
        time.sleep(1)
    
    if life == 0:
        gameOver = True
        gameOver2()
    
    gameclock.tick(fps)
    pygame.display.update()
    