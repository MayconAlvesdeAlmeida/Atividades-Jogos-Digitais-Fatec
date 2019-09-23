# INTEGRANTES
# ANDRÉ HIROKI SATO
# FÁBIO GICQUEL SILVEIRA
# LEANDRO DOS SANTOS RODRIGUES
# MAYCON ALVES DE ALMEIDA

import pygame
pygame.init()
largura=680
altura=680
tela= pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Atividade 2 Prog I')
clock = pygame.time.Clock()
cores=[(255,255,255),(0,0,0),(0,255,0),(255,255,0),(255,0,0),
       (0, 128, 255), (128, 0, 128), (255, 0, 128), (0, 255, 255), (128, 128, 128)]
incremento_x=incremento_y=x=y= contador=0
sair = True
while sair:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            sair = False
    pygame.draw.rect(tela,cores[0],(20,20,640,640))
    for c in range(2):
        pygame.draw.rect(tela,cores[2+c], (40+incremento_x, 40+incremento_y, 240, 240))
        pygame.draw.rect(tela, cores[1], (40 + incremento_x, 40 + incremento_y, 240, 240),1)
        pygame.draw.rect(tela, cores[0], (80 + incremento_x, 80 + incremento_y, 160, 160))
        for i in range(2):
            pygame.draw.rect(tela, cores[2 + c], (100 + incremento_x+x, 100 + incremento_y+y, 50, 50))
            pygame.draw.ellipse(tela,cores[1],(105+incremento_x+x,105+incremento_y+y,40,40),2)
            x+=70
        x=0
        y=70
        for i in range(2):
            pygame.draw.rect(tela, cores[2 + c], (100 + incremento_x+x, 100 + incremento_y+y, 50, 50))
            pygame.draw.ellipse(tela, cores[1], (105 + incremento_x + x, 105 + incremento_y + y, 40, 40), 2)
            x+=70
        x=0
        y=0
        incremento_x+=360
    incremento_x =0
    incremento_y = 360
    for c in range(2):
        pygame.draw.rect(tela,cores[4+c], (40+incremento_x, 40+incremento_y, 240, 240))
        pygame.draw.rect(tela, cores[1], (40 + incremento_x, 40 + incremento_y, 240, 240), 1)
        pygame.draw.rect(tela, cores[0], (80 + incremento_x, 80 + incremento_y, 160, 160))
        for i in range(2):
            pygame.draw.rect(tela, cores[4 + c], (100 + incremento_x+x, 100 + incremento_y+y, 50, 50))
            pygame.draw.ellipse(tela, cores[1], (105 + incremento_x + x, 105 + incremento_y + y, 40, 40), 2)
            x+=70
        x=0
        y=70
        for i in range(2):
            pygame.draw.rect(tela, cores[4 + c], (100 + incremento_x+x, 100 + incremento_y+y, 50, 50))
            pygame.draw.ellipse(tela, cores[1], (105 + incremento_x + x, 105 + incremento_y + y, 40, 40), 2)
            x+=70
        x=0
        y=0
        incremento_x+=360
    incremento_x = 0
    incremento_y = 0
    pygame.draw.rect(tela, cores[1], (40,40, 600, 600), 2)
    pygame.draw.rect(tela, cores[2], (80,280, 40, 80))
    pygame.draw.rect(tela, cores[2], (120,320, 160, 40))
    pygame.draw.rect(tela, cores[4], (280, 560, 80, 40))
    pygame.draw.rect(tela, cores[4], (320, 400, 40, 160))
    pygame.draw.rect(tela, cores[5], (560, 320, 40, 80))
    pygame.draw.rect(tela, cores[5], (400, 320,160,40))
    pygame.draw.rect(tela, cores[3], (320, 80, 80, 40))
    pygame.draw.rect(tela, cores[3], (320, 120,40, 160))
    for c in range(3):
        for i in range(15):
            pygame.draw.rect(tela, cores[1], (40 + incremento_x, 280 + incremento_y, 40, 40),1)
            incremento_x+=40
        incremento_x=0
        incremento_y+=40
    incremento_y=0
    for c in range(3):
        for i in range(15):
            pygame.draw.rect(tela, cores[1], (280 + incremento_x, 40 + incremento_y, 40, 40),1)
            incremento_y+=40
        incremento_y=0
        incremento_x+=40
    incremento_x=0
    pygame.draw.rect(tela, cores[0], (280, 280, 120, 120))
    pygame.draw.polygon(tela,cores[2],[(280,280),(340,340),(280,400)])
    pygame.draw.polygon(tela, cores[3], [(280, 280), (400, 280), (340, 340)])
    pygame.draw.polygon(tela, cores[4], [(280, 400), (340, 340), (400, 400)])
    pygame.draw.polygon(tela, cores[5], [(400, 400), (340, 340), (400, 280)])
    pygame.draw.polygon(tela, cores[0], [(280, 280), (340, 340), (280, 400)],4)
    pygame.draw.polygon(tela, cores[0], [(280, 280), (400, 280), (340, 340)],4)
    pygame.draw.polygon(tela, cores[0], [(280, 400), (340, 340), (400, 400)],4)
    pygame.draw.polygon(tela, cores[0], [(400, 400), (340, 340), (400, 280)],4)
    pygame.draw.rect(tela, cores[0], (281, 281, 118, 118),5)
    pygame.draw.rect(tela, cores[1], (280, 280, 120, 120), 1)
    pygame.draw.rect(tela, cores[3], (321, 241, 38, 38))
    pygame.draw.rect(tela, cores[4], (321, 401, 38, 38))
    pygame.draw.rect(tela, cores[2], (241, 321, 38, 38))
    pygame.draw.rect(tela, cores[5], (401, 321, 38, 38))
    for c in range(2):
        for i in range(3):
            pygame.draw.rect(tela, cores[1], (280 + incremento_x, 240 + incremento_y, 40, 40), 1)
            incremento_x += 40
        incremento_x = 0
        incremento_y += 160
    incremento_y = 0
    for c in range(2):
        for i in range(3):
            pygame.draw.rect(tela, cores[1], (240 + incremento_x, 280 + incremento_y, 40, 40), 1)
            incremento_y += 40
        incremento_y = 0
        incremento_x += 160
    incremento_x = 0
    pygame.draw.rect(tela, cores[1], (40,40,240,240),1)
    pygame.draw.rect(tela, cores[1], (400, 40, 240, 240), 1)
    pygame.draw.rect(tela, cores[1], (40, 400, 240, 240), 1)
    pygame.draw.rect(tela, cores[1], (400, 400, 240, 240), 1)
    pygame.draw.line(tela,cores[1],(339,630),(339,610),2)
    pygame.draw.line(tela, cores[1], (339, 50), (339, 70), 2)
    pygame.draw.line(tela, cores[1], (50, 339), (70, 339), 2)
    pygame.draw.line(tela, cores[1], (630, 339), (610, 339), 2)
    pygame.draw.line(tela,cores[1],(330,620),(339,610),2)
    pygame.draw.line(tela, cores[1], (339, 610), (349, 620), 2)
    pygame.draw.line(tela, cores[1], (330, 60), (339, 70), 2)
    pygame.draw.line(tela, cores[1], (339, 70), (349, 60), 2)
    pygame.draw.line(tela, cores[1], (60, 330), (70, 339), 2)
    pygame.draw.line(tela, cores[1], (70, 339), (60, 349), 2)
    pygame.draw.line(tela, cores[1], (620, 330), (610, 339), 2)
    pygame.draw.line(tela, cores[1], (610, 339), (620, 349), 2)
    pygame.draw.rect(tela, cores[0],(290, 586,20,4))
    pygame.draw.rect(tela, cores[0], (306, 570, 4,16))
    pygame.draw.rect(tela, cores[0], (90,290,4,20))
    pygame.draw.rect(tela, cores[0], (94,306,16,4))
    pygame.draw.rect(tela, cores[0], (370, 90, 20, 4))
    pygame.draw.rect(tela, cores[0], (370, 94, 4, 16))
    pygame.draw.rect(tela, cores[0], (570, 370, 20, 4))
    pygame.draw.rect(tela, cores[0], (586, 374, 4, 16))
    if contador ==20:
        cores = [(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0,128,255),(255,255,0)]
    elif contador==40:
        cores = [(255, 255, 255), (0, 0, 0),(0, 128, 255),(255,0,0),(255, 255, 0), (0, 255, 0)]
    elif contador==60:
        cores = [(255, 255, 255), (0, 0, 0),(255,255,0),(0,128, 255), (0, 255, 0), (255,0, 0)]
    elif contador==80:
        contador=0
        cores = [(255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 255, 0), (255, 0, 0), (0, 128, 255)]
    contador+=1
    pygame.display.update()
pygame.quit()
