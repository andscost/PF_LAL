# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# ----- Inicia assets
ball_WIDTH = 50
ball_HEIGHT = 50
rect_WIDTH = 20
rect_HEIGHT = 100
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('img/starfield.png').convert()
ball_img = pygame.image.load('img/fire_ball.png').convert_alpha()
ball_img = pygame.transform.scale(ball_img, (ball_WIDTH, ball_HEIGHT))
rect_img = pygame.image.load('img/playerShip1_orange.png').convert_alpha()
rect_img = pygame.transform.scale(rect_img, (rect_WIDTH, rect_HEIGHT))

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class rect(pygame.sprite.Sprite):
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
        self.speedx = ball_speedx
        self.speedy = ball_speedy

    def update(self):
        # Atualizando a posição da bola
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se a bola toca alguma parede, ela inverte a velocidade
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.speedy = ball_speedy*(-1)
        if self.rect.right > WIDTH or self.rect.left < 0 :
            self.speedx = ball_speedx*(-1)
                #self.rect.x = random.randint(0, WIDTH-ball_WIDTH) apenas para reniciar o jogo
                #self.rect.y = random.randint(-100, -ball_HEIGHT)
    

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

#definir a direção inicial da bola
ball_speed = 12
ball_speedx = ball_speed - random.randint(6,10)
ball_speedy = ball_speed - ball_speedx


all_sprites = pygame.sprite.Group()

# Criando os jogadores
player1 = rect(rect_img,1)
player2 = rect(rect_img,2)
all_sprites.add(player1)
all_sprites.add(player2)
# Criando a bola
ball = ball(ball_img)
all_sprites.add(ball)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            #player1
            if event.key == pygame.K_UP:
                player1.speedy -= 8
            if event.key == pygame.K_DOWN:
                player1.speedy += 8
            #player2
            if event.key == pygame.K_w:
                player2.speedy -= 8
            if event.key == pygame.K_s:
                player2.speedy += 8
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            #player1
            if event.key == pygame.K_UP:
                player1.speedy += 8
            if event.key == pygame.K_DOWN:
                player1.speedy -= 8
            #player2
            if event.key == pygame.K_w:
                player2.speedy += 8
            if event.key == pygame.K_s:
                player2.speedy -= 8


    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

