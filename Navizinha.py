import pygame
import os
import sys

# caracteristicas do ambiente 

pygame.init()

# config tela principal
WIDTH = 600
HEIGHT = 600
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pega a nave")

arquivo = os.path.join("background.png")         #caso esteja em uma pasta diferente 
try:
    imagem = pygame.image.load("background.png")
    imagem = pygame.transform.scale(imagem, [WIDTH,HEIGHT])
except pygame.error:
    print ("Erro ao tentar ler imagem: background.png")
    sys.exit() 

# cores
cor_branca = (255,255,255)
cor_azul = (108, 194, 236)
cor_verde = (152,231,114)

clock = pygame.time.Clock()     # objeto para controle das atualizações de imagens
pos = 0

rect = pygame.Rect(10, 10, 5, 75)
rect2 = pygame.Rect(585,520,5,75)

loop = True
while loop:
    delta_time = clock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-10,0)
            if event.key == pygame.K_RIGHT:
                rect.move_ip(10,0)
            if event.key == pygame.K_UP:
                rect.move_ip(0,-10)
            if event.key == pygame.K_DOWN:
                rect.move_ip(0,10)
            if event.key == pygame.K_SPACE:
                rect.move_ip(10,10)
            if event.key == pygame.K_BACKSPACE:
                rect.move_ip(-10,-10)

    tela.blit(imagem, [pos,0])
    pygame.draw.rect(tela, [255,0,0], rect)
    pygame.draw.rect(tela, [255,255,0], rect2)
    pygame.display.flip()         # faz a atualização da tela

