# MAYCON ALVES DE ALMEIDA

import pygame
from random import randint
pygame.init()

largura,altura=800,500

clock=pygame.time.Clock()
tela= pygame.display.set_mode((largura,altura))
pygame.display.set_caption('PROG 1 EXTRA 1')

vel_x1=vel_y1=vel_x2=vel_y2=0
x1=-10
y1=-10
x2=largura +10
y2=-10
preto=(0,0,0)
vermelho=(255,0,0)
azul=(0,0,255)
branco=(255,255,255)
neg_x1=neg_y1=pos_x1=pos_y1=False
neg_x2=neg_y2=pos_x2=pos_y2=False
cores_total=[(255,255,0),(0,255,0),(255,255,255),
             (128,255,255),(128,0,128),(255,128,0),
             (0,0,0),(255,0,128)]
cor=preto


sair= True
while sair:
    tela.fill(cor)
    clock.tick(30)
    for e in pygame.event.get():
        if e.type== pygame.QUIT:
            sair = False
    bola_1 = pygame.draw.ellipse(tela, vermelho, (x1, y1, 40, 40))
    bola_2 = pygame.draw.ellipse(tela, azul, (x2, y2, 40, 40))

    x1+=vel_x1
    y1+=vel_y1
    x2 += vel_x2
    y2 += vel_y2

    if x1 > largura - 40 :
        neg_x1=True
        pos_x1=False
    elif x1 < 0 :
        pos_x1=True
        neg_x1=False
    if y1 > altura - 40 :
        neg_y1 = True
        pos_y1=False
    elif y1 < 0 :
        pos_y1 = True
        neg_y1=False

    if neg_x1:
        vel_x1= -5
    elif pos_x1:
        vel_x1 = 5
    if neg_y1:
        vel_y1=-5
    elif pos_y1:
        vel_y1=5

    if x2 > largura - 40 :
        neg_x2=True
        pos_x2=False
    elif x2 < 0 :
        pos_x2=True
        neg_x2=False
    if y2 > altura - 40 :
        neg_y2 = True
        pos_y2=False
    elif y2 < 0 :
        pos_y2 = True
        neg_y2=False

    if neg_x2:
        vel_x2= -5
    elif pos_x2:
        vel_x2 = 5
    if neg_y2:
        vel_y2=-5
    elif pos_y2:
        vel_y2=5

    if bola_1.colliderect(bola_2) and neg_x2 and pos_x1:
        pos_x1,neg_x1=neg_x1,pos_x1
        pos_x2, neg_x2 = neg_x2, pos_x2
        cor=cores_total[randint(0,7)]

        



    pygame.display.update()

pygame.quit()




