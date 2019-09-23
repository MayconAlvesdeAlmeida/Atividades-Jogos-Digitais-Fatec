# MAYCON ALVES DE ALMEIDA

import pygame
from math import sin,cos,radians
pygame.init()

largura,altura=800,600
tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('RADAR')
clock=pygame.time.Clock()

jogando=True
b=largura/2
c=altura/2
r=200
a=d=e=0
tom=0
r1=220
c_l=20

while jogando:
    clock.tick(30)
    tela.fill((0,0,0))
    pygame.draw.ellipse(tela,(0,255,0),(largura/2 -220,altura/2-220,440,440),5)
    pygame.draw.ellipse(tela, (0, 255, 0), (largura / 2 - 240, altura / 2 - 240, 480, 480), 5)
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            jogando=False

    if a<-360:
        a=0
    if d<-360:
        d=0

    for i in range(0+d,331+d,30):
        x1=b+sin(radians(i))*r1
        y1=c+cos(radians(i))*r1
        x2=sin(radians(i))*c_l
        y2=cos(radians(i))*c_l
        pygame.draw.line(tela,(0,255,0),(x1,y1),(x1+x2,y1+y2),5)
    d-=2



    for i in range(0+a,181+a):
        pygame.draw.line(tela,(0,255-tom,0),(b,c),(b+sin(radians(i))*r,c+cos(radians(i))*r),5)
        tom+=2
        if tom > 255:
            tom=255

    a-=1
    tom=0
    if a <-240 and a > -355:
        pygame.draw.circle(tela,(0,255,0),(500,240),5)
    if a <-170 and a > -270:
        pygame.draw.circle(tela,(0,255,0),(370,230),5)
    if a <-50 and a >- 170:
        pygame.draw.circle(tela,(0,255,0),(290,400),5)
    pygame.display.update()

pygame.quit()

