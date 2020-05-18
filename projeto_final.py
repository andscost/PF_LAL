import sys
import pygame

pygame.init()  # inicia rotinas do pygame

surf = pygame.display.set_mode([400, 400]) # crio superficie para o jogo

surf.fill( [0, 0, 0] ) # preenche a tela com a cor preta

pygame.draw.circle(surf, [0, 255, 255], [200, 200], 50) # desenha círculo

pygame.display.update() # faz a atualização da tela

# Game Loop
while True:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit() # terminado a aplicação pygame
            sys.exit()    # sai pela rotina do sistema