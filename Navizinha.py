# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import math
import sys

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# ----- Inicia assets
ball_WIDTH = 50
ball_HEIGHT = 50
player_WIDTH = 20
player_HEIGHT = 100
Points = [0,0]
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('img/starfield.png').convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
inicio = pygame.image.load('img/inicio.png').convert()
inicio_rect = background.get_rect()
ball_img = pygame.image.load('img/fire_ball.png').convert_alpha()
ball_img = pygame.transform.scale(ball_img, (ball_WIDTH, ball_HEIGHT))
player1_img = pygame.image.load('img/player1.png').convert_alpha()
player1_img = pygame.transform.scale(player1_img, (player_WIDTH, player_HEIGHT))
player2_img = pygame.image.load('img/player2.png').convert_alpha()
player2_img = pygame.transform.scale(player2_img, (player_WIDTH, player_HEIGHT))

# ----- Carrega os sons do jogo
pygame.mixer.music.load('snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.2)
boom_sound = pygame.mixer.Sound('snd/expl3.wav')
destroy_sound = pygame.mixer.Sound('snd/expl6.wav')
pew_sound = pygame.mixer.Sound('snd/pew.wav')

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class player(pygame.sprite.Sprite):
    def __init__(self, img, player):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        espaço_da_tela = 10
        if player == 1:
            self.rect.left = espaço_da_tela
        if player == 2:
            self.rect.right = WIDTH - espaço_da_tela
        self.rect.centery = HEIGHT/2
        self.speedy = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.y += self.speedy
        # Mantem dentro da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class ball(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2
        #definir a direção e a velocidade inicial da bola
        self.ball_speed = 15
        self.speedx = 15
        self.speedy = 0

    def update(self):
        # Atualizando a posição da bola  testar spritecollide
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se a bola toca no teto ou no fundo, ela inverte a velocidade
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.speedy *= -1
        # colisao da bola com os players, que randomiza os valores da direção
        contato = 15 #define a largura da regiao de colisao que fica na frente do retangulo
        #player1
        if self.rect.left < player1.rect.right+contato and self.rect.left > player1.rect.right and self.rect.top < player1.rect.bottom and self.rect.bottom > player1.rect.top:
            pew_sound.play()
            rng = random.randint(12,20)
            angulo = (rng*math.pi)/16
            self.speedx = -(self.ball_speed*math.cos(angulo))
            self.speedy = self.ball_speed*math.sin(angulo)
        #player2
        if self.rect.right > player2.rect.left-contato and self.rect.right < player2.rect.left and self.rect.top < player2.rect.bottom and self.rect.bottom > player2.rect.top:
            pew_sound.play()
            rng = random.randint(12,20)
            angulo = (rng*math.pi)/16
            self.speedx = self.ball_speed*math.cos(angulo)
            self.speedy = self.ball_speed*math.sin(angulo)
        #renicia a posição da bolinha e sua velocidade caso alg pontue 
        if self.rect.left > WIDTH: #player 1 ganha ponto
            destroy_sound.play()
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
            self.speedx = 15
            self.speedy = 0
            Points[0] += 1 
            
        if self.rect.right < 0: #player 2 ganha ponto
            destroy_sound.play()
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
            self.speedx = -15
            self.speedy = 0 
            Points[1] += 1  
game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

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
GAMEOVER = 2
state = PLAYING

# ===== Loop principal =====
game = True
while game:
    clock.tick(FPS)
    # ----- Trata eventos
        
    for event in pygame.event.get():
        #tela de inicio
        window.fill((0,0,0))  # Preenche com a cor preta
        window.blit(inicio, inicio_rect) 
        pygame.display.update()  # Mostra o novo frame para o jogador

        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYUP:
            pygame.mixer.music.play(loops=-1)
            while state == PLAYING: 
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
                window.fill((0, 0, 0))  # Preenche com a cor branca
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
                        state = DONE

                pygame.display.update()  # Mostra o novo frame para o jogador
            state = GAMEOVER
            while state == GAMEOVER:
                clock.tick(FPS)
                # ----- Trata eventos
                for event in pygame.event.get():
                    # ----- Verifica consequências
                    if event.type == pygame.QUIT:
                        state = DONE
                    if event.type == pygame.KEYUP: #recomeçar o jogo
                        state = PLAYING
                        Points[0] = 0
                        Points[1] = 0
                window.fill((255,255,255))  # Preenche com a cor preta
                pygame.display.update()  # Mostra o novo frame para o jogador
# ===== Finalização =====

pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

