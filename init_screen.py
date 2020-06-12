# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import sys
import os

from config import FPS, WIDTH, HEIGHT, BLACK, Points, INIT, GAME, QUIT, ball_WIDTH, ball_HEIGHT, player_WIDTH, player_HEIGHT

def init_screen (window): 

    background = pygame.image.load('img/inicio.png').convert()
    background = pygame.transform.scale(background, (WIDTH,HEIGHT))
    background_rect = background.get_rect()

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # ===== Loop principal =====
    game = True
    while game:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = QUIT
                game = False

            if event.type == pygame.KEYUP:
                state = GAME
                game = False

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(background, background_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

    return state