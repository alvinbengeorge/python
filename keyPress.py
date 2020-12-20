import pygame
import time
wi=640
he=480
#wi=int(input("Enter width of screen:"))
#he=int(input("Enter height of the screen:"))
pygame.init()

win = pygame.display.set_mode((wi,he))

j=True
jcount=10
pygame.display.set_caption("HI")
x=50
y=50
width=50
height=60
neg=1
vel=15
run=True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    k=pygame.key.get_pressed()
    if k[pygame.K_LEFT] and x>vel:
        x=x-vel
    if k[pygame.K_RIGHT] and x<wi-width-vel:
        x=x+vel
    if not(j):
        if k[pygame.K_UP] and y>vel:
            y=y-vel
        if k[pygame.K_DOWN]and he-height-vel:
            y=y+vel
        if k[pygame.K_SPACE]:
            j=True
    else:
        if jcount>=-10:
            if jcount<0:
                neg=-1
            y-=(jcount*4)*neg
            jcount=jcount-1
        else:
            j=False
            jcount=10
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(int(x),int(y),width,height))
    pygame.display.update()
pygame.quit()
