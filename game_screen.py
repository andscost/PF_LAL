import pygame
import os
import sys
from config import FPS, WIDTH, HEIGHT, BLACK, Points, INIT, GAME, QUIT, ball_WIDTH, ball_HEIGHT, player_WIDTH, player_HEIGHT
from assets import background, ball_img, player1_img, player2_img,boom_sound, destroy_sound, pew_sound
from sprites import player, ball 

def game_screen(window):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    all_sprites = pygame.sprite.Group()

    # Criando os jogadores
    player1 = player(player1_img,1)
    player2 = player(player2_img,2)
    all_sprites.add(player1)
    all_sprites.add(player2)

    # Criando a bola
    ball = ball(ball_img)
    all_sprites.add(ball)
    

    DONE = 0
    PLAYING = 1
    PERDEVIDA = 2
    font = pygame.font.SysFont(None, 48)
    state = PLAYING

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    #player1
                    if event.key == pygame.K_w:
                        player1.speedy -= 8
                    if event.key == pygame.K_s:
                        player1.speedy += 8
                    #player2
                    if event.key == pygame.K_UP:
                        player2.speedy -= 8
                    if event.key == pygame.K_DOWN:
                        player2.speedy += 8
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    #player1
                    if event.key == pygame.K_w:
                        player1.speedy += 8
                    if event.key == pygame.K_s:
                        player1.speedy -= 8
                    #player2
                    if event.key == pygame.K_UP:
                        player2.speedy += 8
                    if event.key == pygame.K_DOWN:
                        player2.speedy -= 8


        # ----- Atualiza estado do jogo
        # Atualizando a posição dos meteoros
        all_sprites.update()

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(background, (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = font.render("{}   {}".format(Points[0],Points[1]), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador

