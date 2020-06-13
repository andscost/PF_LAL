import pygame
import os

from config import FPS, WIDTH, HEIGHT, BLACK, DONE, PLAYING
from assets import load_assets

def init_screen (window): 
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    assets = load_assets()
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
                state = PLAYING
                game = False

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets['inicio'], assets['inicio_rect'])
        pygame.display.flip()  # Mostra o novo frame para o jogador
    return state