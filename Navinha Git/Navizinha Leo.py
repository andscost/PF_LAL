import pygame
import os
import sys

BRANCO = (255,255,255)
AZUL = (108, 194, 236)
VERDE = (152,231,114)
VERMELHO = (255,0,0)
AMARELO = (255,200,0)

def main():

    pygame.init()

    # configurações tela principal
    WIDTH = 600
    HEIGHT = 600
    tela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pega a nave")


    arquivo = os.path.join("background2.jpg") 
    try:
        imagem = pygame.image.load("background2.jpg")
        imagem = pygame.transform.scale(imagem, [600,600])
    except pygame.error:
        print ("Erro ao tentar ler imagem: background2.jpg")
        sys.exit() 

    arquivo2 = os.path.join("bola imagem.jpg") 
    try:
        imagem2 = pygame.image.load("bola imagem.jpg")
        imagem2 = pygame.transform.scale(imagem2, [20,20])
    except pygame.error:
        print ("Erro ao tentar ler imagem: bola imagem.jpg")
        sys.exit() 


    clock = pygame.time.Clock()                     # objeto para controle das atualizações de imagens
    pos_tela = [0, 0]
    pos_bola = [0, 0]
    pos_rect = [0, 0]
    pos_rect2 = [0, 0]
    velocidade = [0.3, 0.35]

    rect = pygame.Rect(10, 300, 5, 75)               # desenhos na tela 
    rect2 = pygame.Rect(585,300,5,75)

    loop = True
    while loop:
        delta_time = clock.tick(60) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):           # sair do jogo
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:      # movimentos pelo teclado
                if event.key == pygame.K_UP:
                    pos_rect[1] = -5
                if event.key == pygame.K_DOWN:
                    pos_rect[1] = 5
                if event.key == pygame.K_w:
                    pos_rect2[1] = -5
                if event.key == pygame.K_s:
                    pos_rect2[1] = 5

        tela.blit(imagem, pos_tela)                  # movimento tela background

        # movimento da bola no eixo x e y
        pos_bola[0] += velocidade[0] * delta_time
        pos_bola[1] += velocidade[1] * delta_time
        if pos_bola[0] > tela.get_width() - imagem2.get_width():
            velocidade[0] = -velocidade[0]
            pos_bola[0] = tela.get_width() - imagem2.get_width()
        elif pos_bola[0] < 0:
            velocidade[0] = -velocidade[0]
            pos_bola[0] = 0

        if pos_bola[1] > tela.get_height() - imagem2.get_height():
            velocidade[1] = -velocidade[1]
            pos_bola[1] = tela.get_height() - imagem2.get_height()
        elif pos_bola[1] < 0:
            velocidade[1] = -velocidade[1]
            pos_bola[1] = 0

        # movimento dos retangulos para cima e para baixo 
        tela.blit(imagem2, pos_bola)
        if rect[1] < 0:
            pos_rect[1] = 0
            rect[1] += 5
        elif rect[1] > 525:
            pos_rect[1] = 0
            rect[1] -= 5
        
        if rect2[1] < 0:
            pos_rect2[1] = 0
            rect2[1] += 5
        elif rect2[1] > 525:
            pos_rect2[1] = 0
            rect2[1] -= 5

        rect[1] += pos_rect[1]
        rect2[1] += pos_rect2[1]

        pygame.draw.rect(tela, VERMELHO, rect)
        pygame.draw.rect(tela, AMARELO, rect2)

        if pos_bola == rect[1]:
            pos_bola[0] += velocidade[0] * delta_time
            pos_bola[1] += velocidade[1] * delta_time

        pygame.display.update()                     # faz a atualização da tela

main()
