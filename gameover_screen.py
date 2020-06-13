import pygame
import os

from config import FPS, BLACK, Points, PLAYING, DONE

def gameover_screen (window): 
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
                state = DONE
                game = False

            if event.type == pygame.KEYUP:
                state = PLAYING
                Points[0] = 0
                Points[1] = 0
                game = False

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets['gameover'], assets['gameover_rect'])

        pygame.display.flip()  # Mostra o novo frame para o jogador
    return state