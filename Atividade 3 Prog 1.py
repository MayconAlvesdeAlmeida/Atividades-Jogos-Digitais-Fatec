# MAYCON ALVES DE ALMEIDA
import pygame
pygame.init()
cores={'branco':(255,255,255),'vermelho':(255,0,0),'verde':(0,255,0),'roxo':(128,0,128),'preto':(0,0,0),
'amarelo':(255,255,0)}
largura,altura=1200,700
tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('ATIVIDADE 03')
clock=pygame.time.Clock()
vx=vy=50
x,y,a,b,contador,contador_img=150,500,0,0,0,0
seta1=[(80,275),(90,255),(90,265),(110,265),(110,255),(120,275),(110,295),(110,285),(90,285),(90,295)]
seta2=[(1080,275),(1090,255),(1090,265),(1110,265),(1110,255),(1120,275),(1110,295),(1110,285),(1090,285),(1090,295)]
seta3=[(375,80),(395,90),(385,90),(385,110),(395,110),(375,120),(355,110),(365,110),(365,90),(355,90)]
seta4=[(375,580),(395,590),(385,590),(385,610),(395,610),(375,620),(355,610),(365,610),(365,590),(355,590)]
seta5=[(1080,515),(1130,515),(1130,505),(1140,525),(1130,545),(1130,535),(1080,535)]

colisoes=[[100,100],[150,100],[200,100],[250,100],[300,100],[400,100],[450,100],[500,100],[550,100],[600,100],[650,100],
[700,100],[750,100],[800,100],[850,100],[900,100],[950,100],[1000,100],[1050,100],[100,550],[150,550],[200,550],
[250,550],[300,550],[400,550],[450,550],[500,550],[550,550],[600,550],[650,550],[700,550],[750,550],[800,550],[850,550],
[900,550],[950,550],[1000,550],[1050,550],[100,150],[100,200],[100,300],[100,350],[100,400],[100,450],[100,500],
[1050,150],[1050,200],[1050,300],[1050,350],[1050,400],[1050,450],[400,150],[400,200],[400,250],[400,300],[400,350],
[350,350],[300,350],[250,350],[250,400],[250,450],[850,500],[850,450],[850,400],[800,400],[750,400],[700,400],[700,350],
[700,300],[700,250],[650,250],[600,250],[550,250],[550,300],[550,350],[550,400],[1100,550],[1100,450]]

sair = True

def texto(msg,cor,tam,italico,x,y,rotate):
    texto=pygame.font.SysFont(None,tam,False,italico)
    texto1=texto.render(msg,True,cor)
    rot=pygame.transform.rotate(texto1,90)
    if rotate == 1:
        tela.blit(rot, (x, y))
    else:
        tela.blit(texto1,(x,y))



while sair:
    contador+=1
    contador_img+=1
    tela.fill(cores['branco'])
    clock.tick(10)
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            print('Passe os níveis para sair')

    pygame.draw.rect(tela, cores['amarelo'], (100, 100, 1000, 500))
    for xy in colisoes[:-2]:
        pygame.draw.rect(tela,cores['roxo'],(xy[0],xy[1],50,50))
    for c in range(10):
        for i in range(20):
            pygame.draw.rect(tela, cores['preto'], (100+a, 100+b, 50, 50), 1)
            a+=50
        a=0
        b+=50
    b=0

    texto('Passagem', cores['preto'],40,True,307,40,0)
    texto('Passagem', cores['preto'], 40, True,40,203, 1)
    texto('Passagem', cores['preto'], 40, True, 1130, 203, 1)
    texto('Passagem', cores['preto'], 40, True, 307, 630,0)
    texto('Saída', cores['preto'], 40,True, 1110, 562,0)

    pygame.draw.rect(tela, cores['preto'], (100, 100, 1000, 500), 2)



    if contador <=5:
        texto('LEVEL 01', cores['preto'], 80, False, 940, 10, 0)
    if contador>10:
        contador=0
    pygame.draw.rect(tela, cores['verde'], (x, y, 50, 50))
    if contador_img<=5:
        pygame.draw.rect(tela, cores['preto'], (x + 15, y + 25, 20, 5))
        pygame.draw.ellipse(tela, cores['branco'], (x + 10, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['branco'], (x + 30, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['preto'], (x + 12, y + 10, 6, 6))
        pygame.draw.ellipse(tela, cores['preto'], (x + 32, y + 10, 6, 6))
    else:
        pygame.draw.ellipse(tela, cores['preto'], (x+15, y+20, 20, 25))
        pygame.draw.ellipse(tela, cores['branco'], (x + 10, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['branco'], (x + 30, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['preto'], (x + 12, y + 10, 6, 6))
        pygame.draw.ellipse(tela, cores['preto'], (x + 32, y + 10, 6, 6))
    if contador_img>10:
        contador_img=0


    pygame.draw.rect(tela, cores['preto'], (x, y, 50, 50),1)
    if x!=100 or y!=250:
        pygame.draw.polygon(tela, cores['vermelho'], seta1)
    if x!=1050 or y!=250:
        pygame.draw.polygon(tela, cores['vermelho'], seta2)
    if y!=100 or x!=350:
        pygame.draw.polygon(tela, cores['vermelho'], seta3)
    if y!=550 or x!=350:
        pygame.draw.polygon(tela, cores['vermelho'], seta4)
    if (x!=1050 or y!=500) and (x!=1100 or y!=500):
        pygame.draw.polygon(tela, cores['vermelho'], seta5)

    teclas=pygame.key.get_pressed()

    xant,yant=x,y

    if teclas[pygame.K_LEFT]:
        x-=vx
    elif teclas[pygame.K_RIGHT]:
        x+=vx
    elif teclas[pygame.K_UP]:
        y-=vy
    elif teclas[pygame.K_DOWN]:
        y+=vy

    for xy in colisoes:
        if x==xy[0] and y==xy[1]:
            x,y=xant,yant
    if x<100 and y==250:
        x=1050
    elif x > 1050 and y == 250:
        x = 100
    elif x > 1100 and y == 500:
        sair=False
    if y < 100 and x == 350:
        y = 550
    elif y > 550 and x == 350:
        y = 100

    pygame.display.update()
colisoes=[[100,100],[150,100],[200,100],[250,100],[300,100],[350,100],[400,100],[450,100],[500,100],[550,100],[600,100],
[650,100],[700,100],[750,100],[800,100],[850,100],[900,100],[950,100],[1050,100],[100,550],[200,550],[250,550],[300,550],
[350,550],[400,550],[450,550],[500,550],[550,550],[600,550],[650,550],[700,550],[750,550],[800,550],[850,550],[900,550],
[950,550],[1000,550],[1050,550],[100,150],[100,200],[100,300],[100,350],[100,400],[100,450],[100,500],[1050,150],[1050,200],
[1050,300],[1050,350],[1050,400],[1050,450],[500,500],[500,450],[500,400],[500,350],[500,300],[500,250],[500,200],[500,150],
[650,500],[650,450],[650,400],[700,400],[750,400],[800,400],[850,400],[900,400],[950,400],[1000,300],[950,300],
[900,300],[850,300],[850,250],[850,200],[200,200],[250,200],[300,200],[300,250],[300,300],[300,350],[250,350],[200,350],
[200,400],[200,450],[1100,550],[1100,450]]

seta1=[(80,275),(90,255),(90,265),(110,265),(110,255),(120,275),(110,295),(110,285),(90,285),(90,295)]
seta2=[(1080,275),(1090,255),(1090,265),(1110,265),(1110,255),(1120,275),(1110,295),(1110,285),(1090,285),(1090,295)]
seta3=[(1025,80),(1045,90),(1035,90),(1035,110),(1045,110),(1025,120),(1005,110),(1015,110),(1015,90),(1005,90)]
seta4=[(175,580),(195,590),(185,590),(185,610),(195,610),(175,620),(155,610),(165,610),(165,590),(155,590)]
seta5=[(1080,515),(1130,515),(1130,505),(1140,525),(1130,545),(1130,535),(1080,535)]

sair=True
vx=vy=50
x,y,a,b,contador,contador_img=250,400,0,0,0,0
while sair:
    contador += 1
    contador_img += 1
    tela.fill(cores['branco'])
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            print('Passe os níveis para sair')
    pygame.draw.rect(tela, cores['amarelo'], (100, 100, 1000, 500))
    for xy in colisoes[:-2]:
        pygame.draw.rect(tela,cores['roxo'],(xy[0],xy[1],50,50))
    for c in range(10):
        for i in range(20):
            pygame.draw.rect(tela, cores['preto'], (100+a, 100+b, 50, 50), 1)
            a+=50
        a=0
        b+=50
    b=0
    texto('Passagem', cores['preto'], 40, True, 40, 203, 1)
    texto('Passagem', cores['preto'], 40, True, 1130, 203, 1)
    texto('Passagem', cores['preto'], 40, True, 107, 630, 0)
    texto('Saída', cores['preto'], 40, True, 1110, 562, 0)
    pygame.draw.rect(tela, cores['preto'], (100, 100, 1000, 500), 2)

    if contador <=5:
        texto('LEVEL 02', cores['preto'], 80, False, 930, 10, 0)
    if contador>10:
        contador=0
    pygame.draw.rect(tela, cores['verde'], (x, y, 50, 50))
    if contador_img<=5:
        pygame.draw.rect(tela, cores['preto'], (x + 15, y + 25, 20, 5))
        pygame.draw.ellipse(tela, cores['branco'], (x + 10, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['branco'], (x + 30, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['preto'], (x + 12, y + 10, 6, 6))
        pygame.draw.ellipse(tela, cores['preto'], (x + 32, y + 10, 6, 6))
    else:
        pygame.draw.ellipse(tela, cores['preto'], (x+15, y+20, 20, 25))
        pygame.draw.ellipse(tela, cores['branco'], (x + 10, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['branco'], (x + 30, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['preto'], (x + 12, y + 10, 6, 6))
        pygame.draw.ellipse(tela, cores['preto'], (x + 32, y + 10, 6, 6))
    if contador_img>10:
        contador_img=0
    pygame.draw.rect(tela, cores['preto'], (x, y, 50, 50), 1)

    if x!=100 or y!=250:
        pygame.draw.polygon(tela, cores['vermelho'], seta1)
    if x!=1050 or y!=250:
        pygame.draw.polygon(tela, cores['vermelho'], seta2)
    if y!=100 or x!=1000:
        pygame.draw.polygon(tela, cores['vermelho'], seta3)
    if y!=550 or x!=150:
        pygame.draw.polygon(tela, cores['vermelho'], seta4)
    if (x!=1050 or y!=500) and (x!=1100 or y!=500):
        pygame.draw.polygon(tela, cores['vermelho'], seta5)

    teclas = pygame.key.get_pressed()

    xant, yant = x, y

    if teclas[pygame.K_LEFT]:
        x -= vx
    elif teclas[pygame.K_RIGHT]:
        x += vx
    elif teclas[pygame.K_UP]:
        y -= vy
    elif teclas[pygame.K_DOWN]:
        y += vy

    for xy in colisoes:
        if x == xy[0] and y == xy[1]:
            x, y = xant, yant

    if x<100 and y==250:
        x=1050
    elif x > 1050 and y == 250:
        x = 100
    elif x > 1100 and y == 500:
        sair=False
    if y < 100 and x == 1000:
        x,y = 150,550
    elif y > 550 and x == 150:
        x,y = 1000,100
    pygame.display.update()

colisoes=[[100,100],[150,100],[200,100],[250,100],[300,100],[350,100],[400,100],[450,100],[500,100],[550,100],[600,100],
[650,100],[750,100],[800,100],[850,100],[900,100],[950,100],[1000,100],[1050,100],[100,550],[150,550],[200,550],
[250,550],[300,550],[350,550],[400,550],[450,550],[550,550],[600,550],[650,550],[700,550],[750,550],[800,550],[850,550],
[900,550],[950,550],[1000,550],[1050,550],[100,200],[100,250],[100,300],[100,350],[100,400],[100,450],[100,500],
[1050,150],[1050,200],[1050,250],[1050,300],[1050,350],[1050,400],[1050,450],[200,450],[200,400],[200,350],[200,300],
[200,250],[200,200],[250,200],[300,200],[300,250],[300,300],[250,300],[400,500],[400,450],[400,400],[400,350],[400,300],
[400,250],[450,250],[500,250],[500,300],[500,350],[450,350],[450,400],[500,450],[550,500],[650,150],[650,200],[600,200],
[600,250],[600,300],[600,350],[650,350],[650,400],[700,350],[700,300],[700,250],[700,200],[950,200],[900,200],[850,200],
[800,200],[800,250],[800,300],[800,350],[800,400],[800,450],[850,450],[900,450],[950,450],[950,400],[950,350],[900,350]]

seta1=[(80,175),(90,155),(90,165),(110,165),(110,155),(120,175),(110,195),(110,185),(90,185),(90,195)]
seta2=[(1080,525),(1090,545),(1090,535),(1110,535),(1110,545),(1120,525),(1110,505),(1110,515),(1090,515),(1090,505)]
seta3=[(725,80),(745,90),(735,90),(735,110),(745,110),(725,120),(705,110),(715,110),(715,90),(705,90)]
seta4=[(525,580),(545,590),(535,590),(535,610),(545,610),(525,620),(505,610),(515,610),(515,590),(505,590)]

sair=True
vx=vy=50
x,y,a,b,contador,contador_img=150,500,0,0,0,0

while sair:
    contador += 1
    contador_img += 1
    tela.fill(cores['branco'])
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            print('Passe os níveis para sair')
    pygame.draw.rect(tela, cores['amarelo'], (100, 100, 1000, 500))
    for xy in colisoes:
        pygame.draw.rect(tela,cores['roxo'],(xy[0],xy[1],50,50))
    for c in range(10):
        for i in range(20):
            pygame.draw.rect(tela, cores['preto'], (100+a, 100+b, 50, 50), 1)
            a+=50
        a=0
        b+=50
    b=0

    texto('Passagem', cores['preto'], 40, True, 657, 40, 0)
    texto('Passagem', cores['preto'], 40, True, 40, 103, 1)
    texto('Passagem', cores['preto'], 40, True, 1130, 453, 1)
    texto('Passagem', cores['preto'], 40, True, 457, 630, 0)

    pygame.draw.rect(tela, cores['preto'], (100, 100, 1000, 500), 2)

    if contador <= 5:
        texto('LEVEL 03', cores['preto'], 80, False, 930, 10, 0)
    if contador > 10:
        contador = 0
    pygame.draw.rect(tela, cores['verde'], (x, y, 50, 50))
    if contador_img <= 5:
        pygame.draw.ellipse(tela, cores['branco'], (460, 455, 30, 40))
        pygame.draw.ellipse(tela, cores['preto'], (460, 455, 30, 40),1)
        pygame.draw.ellipse(tela, cores['amarelo'], (465, 460, 20, 30))
        pygame.draw.ellipse(tela, cores['preto'], (465, 460, 20, 30),1)

        pygame.draw.rect(tela, cores['preto'], (x + 15, y + 25, 20, 5))
        pygame.draw.ellipse(tela, cores['branco'], (x + 10, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['branco'], (x + 30, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['preto'], (x + 12, y + 10, 6, 6))
        pygame.draw.ellipse(tela, cores['preto'], (x + 32, y + 10, 6, 6))
    else:
        pygame.draw.rect(tela, cores['branco'], (473, 455, 5, 40))
        pygame.draw.rect(tela, cores['preto'], (473, 455, 5, 40),1)

        pygame.draw.ellipse(tela, cores['preto'], (x + 15, y + 20, 20, 25))
        pygame.draw.ellipse(tela, cores['branco'], (x + 10, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['branco'], (x + 30, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['preto'], (x + 12, y + 10, 6, 6))
        pygame.draw.ellipse(tela, cores['preto'], (x + 32, y + 10, 6, 6))
    if contador_img > 10:
        contador_img = 0
    pygame.draw.rect(tela, cores['preto'], (x, y, 50, 50), 1)

    if x!=100 or y!=150:
        pygame.draw.polygon(tela, cores['vermelho'], seta1)
    if x!=1050 or y!=500:
        pygame.draw.polygon(tela, cores['vermelho'], seta2)
    if y!=100 or x!=700:
        pygame.draw.polygon(tela, cores['vermelho'], seta3)
    if y!=550 or x!=500:
        pygame.draw.polygon(tela, cores['vermelho'], seta4)


    teclas = pygame.key.get_pressed()

    xant, yant = x, y

    if teclas[pygame.K_LEFT]:
        x -= vx
    elif teclas[pygame.K_RIGHT]:
        x += vx
    elif teclas[pygame.K_UP]:
        y -= vy
    elif teclas[pygame.K_DOWN]:
        y += vy

    for xy in colisoes:
        if x == xy[0] and y == xy[1]:
            x, y = xant, yant

    if x<100 and y==150:
        x,y=1050,500
    elif x > 1050 and y == 500:
        x,y = 100,150
    if x==450 and y==450:
        sair=False
    if y < 100 and x == 700:
        x,y = 500,550
    elif y > 550 and x == 500:
        x,y = 700,100
    pygame.display.update()
sair=True
x,y,contador_img,contador=550,350,0,0
while sair:
    contador_img+=1
    tela.fill(cores['branco'])
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sair = False

    texto('Thanks for Playing', cores['preto'], 140, True, 150, 200, 0)

    pygame.draw.rect(tela, cores['verde'], (x, y, 50, 50))
    if contador_img <= 5:
        pygame.draw.rect(tela, cores['preto'], (x + 15, y + 25, 20, 5))
        pygame.draw.ellipse(tela, cores['branco'], (x + 10, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['branco'], (x + 30, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['preto'], (x + 12, y + 10, 6, 6))
        pygame.draw.ellipse(tela, cores['preto'], (x + 32, y + 10, 6, 6))
    else:
        pygame.draw.rect(tela, cores['preto'], (x + 15, y + 25, 20, 5))
        pygame.draw.ellipse(tela, cores['branco'], (x + 10, y + 5, 10, 15))
        pygame.draw.ellipse(tela, cores['preto'], (x + 30, y + 5, 10, 15),1)
        pygame.draw.ellipse(tela, cores['preto'], (x + 12, y + 10, 6, 6))

    if contador_img > 10:
        contador_img = 0
    pygame.display.update()

pygame.quit()
