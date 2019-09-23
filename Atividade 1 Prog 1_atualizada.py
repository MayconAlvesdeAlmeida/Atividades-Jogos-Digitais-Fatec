# MAYCON ALVES DE ALMEIDA

import pygame
from math import trunc

tom = y_linha = 0

print()
print('DEFINA AS DIMENSÕES DA TELA GRÁFICA')
print()

opcoes = ['QUADRADO', 'RETÂNGULO', 'ELIPSE', 'CÍRCULO']

largura = input('Digite o valor da dimensão horizontal da tela: ').strip()
while largura.isalpha() or largura == '':
    largura = input('Dados inválidos! Insira somente números: ').strip()
largura = float(largura)
largura = int(largura)
while largura <= 0:
    largura = input('Insira somente valores positivos e maiores que 0: ').strip()
    while largura.isalpha() or largura == '':
        largura = input('Dados inválidos! Insira somente números: ').strip()
    largura = float(largura)
    largura = int(largura)

altura = input('Digite o valor da dimensão vertical da tela: ').strip()
while altura.isalpha() or altura == '':
    altura = input('Dados inválidos! Insira somente números: ').strip()
altura = float(altura)
altura = int(altura)
while altura <= 0 or altura < int(largura * .35):
    print()
    print(f'''A DIMENSÃO VERTICAL PRECISA SER MAIOR QUE {int(largura*.35)}...
OU SEJA,NO MÍNIMO SUPERIOR A 35% DA DIMENSÃO HORIZONTAL''')
    print()
    altura = input('Digite o valor da dimensão vertical da tela: ').strip()
    while altura.isalpha() or altura == '':
        altura = input('Dados inválidos! Insira somente números: ').strip()
    altura = float(altura)
    altura = int(altura)

print()
while True:
    print('DEFINA A FORMA GEOMÉTRICA QUE SERÁ APRESENTADA NA TELA')
    print()
    print('MENU')
    for c in range(len(opcoes)):
        print(f'[ {c} ] : {opcoes[c]}')
    print()
    escolha = input('Digite o número correspondente a opção desejada: ').strip()
    while escolha.isalpha() or escolha == '':
        escolha = input('Dados inválidos! Insira somente números: ').strip()
    escolha = float(escolha)
    escolha = int(escolha)
    while escolha < 0 or escolha > 3:
        escolha = input('0 para QUADRADO | 1 para RETÂNGULO | 2 para ELIPSE | 3 para CÍRCULO: ').strip()
        while escolha.isalpha() or escolha == '':
            escolha = input('Dados inválidos! Insira somente números: ').strip()
        escolha = float(escolha)
        escolha = int(escolha)

    cont = trunc(altura / 165) + 1
    if altura < 165:
        cont = 1

    if escolha == 0 or escolha == 3:
        x_tamanho = (largura - 80) / 15
        x_incremento = x_tamanho + 5
        inicio_x = inicio_y = 5

    elif escolha == 1 or escolha == 2:
        x_tamanho = (largura - 110) / 10
        x_incremento = x_tamanho + 10
        y_tamanho = .5 * x_tamanho
        y_incremento = y_tamanho + 10
        inicio_x = inicio_y = 10

    cores = [(255, 255, 0), (255, 0, 0), (0, 0, 0), (0, 255, 255)]

    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    clock = pygame.time.Clock()
    pygame.display.set_caption('EX01 - PROG I')

    sair = True
    while sair:
        clock.tick(30)
        for c in range(165):
            for i in range(cont):
                pygame.draw.line(tela, (255 - c, 90 + c, 255 - c), (0, y_linha), (largura, y_linha), 1)
                y_linha += 1
            if y_linha > altura:
                break
        y_linha = 0

        for a in pygame.event.get():
            if a.type == pygame.QUIT:
                sair = False
        if escolha == 0:
            for c in range(5):
                for i in range(15):
                    pygame.draw.rect(tela, (0 , 128 - tom, 255 - tom), (inicio_x, inicio_y, x_tamanho, x_tamanho))
                    inicio_x += x_incremento
                inicio_x = 5
                inicio_y += x_incremento
                tom += 30
            inicio_x = 5 * x_tamanho + 30
            inicio_y = 2 * x_tamanho + 15
            for c in range(2):
                pygame.draw.rect(tela, cores[c], (inicio_x, inicio_y, x_tamanho, x_tamanho))
                inicio_x += (4 * x_incremento)

            inicio_x = 6 * x_tamanho + 35
            inicio_y = x_tamanho + 10
            for c in range(2):
                pygame.draw.rect(tela, cores[c + 2], (inicio_x, inicio_y, x_tamanho, x_tamanho))
                inicio_x += 2 * x_incremento
                inicio_y += (2 * x_incremento)

            inicio_x = 5
            inicio_y = 5
            tom = 0
        elif escolha == 1:
            for c in range(5):
                for i in range(10):
                    pygame.draw.rect(tela,(0 , 128 - tom, 255 - tom), (inicio_x, inicio_y, x_tamanho, y_tamanho))
                    inicio_x += x_incremento
                inicio_x = 10
                inicio_y += y_incremento
                tom += 30

            inicio_x = 3 * x_tamanho + 40
            inicio_y = 2 * y_tamanho + 30
            for c in range(2):
                pygame.draw.rect(tela, cores[c], (inicio_x, inicio_y, x_tamanho, y_tamanho))
                inicio_x += (3 * x_incremento)

            inicio_x = 4 * x_tamanho + 50
            inicio_y = y_tamanho + 20
            for c in range(2):
                pygame.draw.rect(tela, cores[c + 2], (inicio_x, inicio_y, x_tamanho, y_tamanho))
                inicio_x += x_incremento
                inicio_y += (2 * y_incremento)

            inicio_x = 10
            inicio_y = 10
            tom = 0
        elif escolha == 2:
            for c in range(5):
                for i in range(10):
                    pygame.draw.ellipse(tela,(0 , 128 - tom, 255 - tom), (inicio_x, inicio_y, x_tamanho, y_tamanho))
                    inicio_x += x_incremento
                inicio_x = 10
                inicio_y += y_incremento
                tom += 30
            inicio_x = 3 * x_tamanho + 40
            inicio_y = 2 * y_tamanho + 30
            for c in range(2):
                pygame.draw.ellipse(tela, cores[c], (inicio_x, inicio_y, x_tamanho, y_tamanho))
                inicio_x += (3 * x_incremento)

            inicio_x = 4 * x_tamanho + 50
            inicio_y = y_tamanho + 20
            for c in range(2):
                pygame.draw.ellipse(tela, cores[c + 2], (inicio_x, inicio_y, x_tamanho, y_tamanho))
                inicio_x += x_incremento
                inicio_y += (2 * y_incremento)
            inicio_x = 10
            inicio_y = 10
            tom = 0
        else:
            for c in range(5):
                for i in range(15):
                    pygame.draw.ellipse(tela,(0 , 128 - tom, 255 - tom), (inicio_x, inicio_y, x_tamanho, x_tamanho))
                    inicio_x += x_incremento
                inicio_x = 5
                inicio_y += x_incremento
                tom += 30
            inicio_x = 5 * x_tamanho + 30
            inicio_y = 2 * x_tamanho + 15

            for c in range(2):
                pygame.draw.ellipse(tela, cores[c], (inicio_x, inicio_y, x_tamanho, x_tamanho))
                inicio_x += (4 * x_incremento)

            inicio_x = 6 * x_tamanho + 35
            inicio_y = x_tamanho + 10
            for c in range(2):
                pygame.draw.ellipse(tela, cores[c + 2], (inicio_x, inicio_y, x_tamanho, x_tamanho))
                inicio_x += 2 * x_incremento
                inicio_y += 2 * x_incremento

            inicio_x = 5
            inicio_y = 5
            tom = 0
        pygame.display.update()
    pygame.quit()
    print()
    continuar = input('Deseja voltar ao MENU ? [ S / N ]').upper().strip()
    while continuar not in 'SN' or continuar == '':
        continuar = input('Digite S para SIM ou N para NÃO :').upper().strip()
    print()
    if continuar == 'N':
        print()
        print('OBRIGADO POR PARTICIPAR')
        break


