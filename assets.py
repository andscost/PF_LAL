# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import os
import sys
from config import FPS, WIDTH, HEIGHT, BLACK, Points, INIT, GAME, QUIT, ball_WIDTH, ball_HEIGHT, player_WIDTH, player_HEIGHT

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DU NARDS")

background = pygame.image.load('img/starfield.png').convert()
background = pygame.transform.scale(background, (WIDTH,HEIGHT))
ball_img = pygame.image.load('img/fire_ball.png').convert_alpha()
ball_img = pygame.transform.scale(ball_img, (ball_WIDTH, ball_HEIGHT))
player1_img = pygame.image.load('img/player1.png').convert_alpha()
player1_img = pygame.transform.scale(player1_img, (player_WIDTH, player_HEIGHT))
player2_img = pygame.image.load('img/player2.png').convert_alpha()
player2_img = pygame.transform.scale(player2_img, (player_WIDTH, player_HEIGHT))

# ----- Carrega os sons do jogo
pygame.mixer.music.load('snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound('snd/expl3.wav')
destroy_sound = pygame.mixer.Sound('snd/expl6.wav')
pew_sound = pygame.mixer.Sound('snd/pew.wav')
