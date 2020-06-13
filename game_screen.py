import pygame
import sys
from config import FPS, WIDTH, HEIGHT, BLACK, Points, START, DONE, PLAYING, GAMEOVER
from assets import load_assets
from sprites import player, ball 


def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    # Criando os jogadores
    player1 = player(assets['player1_img'],1)
    player2 = player(assets['player2_img'],2)
    all_sprites.add(player1)
    all_sprites.add(player2)

    # Criando o array das bolas
    all_balls = pygame.sprite.Group()

    pygame.font.init()
    pygame.mixer.init()
    
    font = pygame.font.Font(None, 48)

    state = PLAYING
    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state == PLAYING:
        clock.tick(FPS)
        timer += 1
        if timer > FPS*10:
            timer = 0
            bola = ball(assets['ball_img'],all_balls)
            all_sprites.add(bola)
            all_balls.add(bola)
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
                        player1.speedy = -10
                    if event.key == pygame.K_s:
                        player1.speedy = 10
                    if event.key == pygame.K_a:
                        player1.speedx = -10
                    if event.key == pygame.K_d:
                        player1.speedx = 10
                    #player2
                    if event.key == pygame.K_UP:
                        player2.speedy = -10
                    if event.key == pygame.K_DOWN:
                        player2.speedy = 10
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    #player1
                    if event.key == pygame.K_w:
                        player1.speedy = 0
                    if event.key == pygame.K_s:
                        player1.speedy = 0
                    #player2
                    if event.key == pygame.K_UP:
                        player2.speedy = 0
                    if event.key == pygame.K_DOWN:
                        player2.speedy = 0


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

        #verifica se a quantidade de pontos para dar game over
        for pontos in Points:
            if pontos >= 3:
                state = GAMEOVER
                #reenicia todas as codições dos jogadores
                player1.speedy = 0
                player2.speedy = 0
                player1.rect.centery = HEIGHT/2
                player2.rect.centery = HEIGHT/2
        pygame.display.update()  # Mostra o novo frame para o jogador
    pygame.mixer.music.stop()  #para a musica
    return state
