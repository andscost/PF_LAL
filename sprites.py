import pygame
import random
from config import WIDTH, HEIGHT, Points, timer, espaço_da_tela, ball_speed, contato
from assets import load_assets

assets = load_assets()

class player(pygame.sprite.Sprite):
    def __init__(self, img, player):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
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
        if len(all_balls)%2 == 0:
            self.speedx = ball_speed
        else: 
            self.speedx = -ball_speed
        self.speedy = 0

    def update(self):
        global timer
        # Atualizando a posição da bola  testar spritecollide
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se a bola toca no teto ou no fundo, ela inverte a velocidade
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.speedy *= -1
        # colisao da bola com os players, que randomiza os valores da direção
        #player1
        if self.rect.left < player1.rect.right+contato and self.rect.left > player1.rect.right and self.rect.top < player1.rect.bottom and self.rect.bottom > player1.rect.top:
            assets['pew_sound'].play()
            rng = random.randint(12,20)
            angulo = (rng*math.pi)/16
            self.speedx = -(ball_speed*math.cos(angulo))
            self.speedy = ball_speed*math.sin(angulo)
        #player2
        if self.rect.right > player2.rect.left-contato and self.rect.right < player2.rect.left and self.rect.top < player2.rect.bottom and self.rect.bottom > player2.rect.top:
            assets['pew_sound'].play()
            rng = random.randint(12,20)
            angulo = (rng*math.pi)/16
            self.speedx = ball_speed*math.cos(angulo)
            self.speedy = ball_speed*math.sin(angulo)
        #renicia a posição da bolinha e sua velocidade caso alg pontue 
        if self.rect.left > WIDTH: #player 1 ganha ponto
            assets['destroy_sound'].play()
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
            self.speedx = ball_speed
            self.speedy = 0
            Points[0] += 1
            timer = 8*FPS
            for bolinha in all_balls:
                bolinha.kill() 
            
        if self.rect.right < 0: #player 2 ganha ponto
            assets['destroy_sound'].play()
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
            self.speedx = -ball_speed
            self.speedy = 0 
            Points[1] += 1
            timer = 8*FPS
            for bolinha in all_balls:
                bolinha.kill()