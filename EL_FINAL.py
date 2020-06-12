# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import os
import sys

pygame.init()
pygame.mixer.init()

from config import FPS, WIDTH, HEIGHT, BLACK, Points, INIT, GAME, QUIT, ball_WIDTH, ball_HEIGHT, player_WIDTH, player_HEIGHT
from assets import background, ball_img, player1_img, player2_img,boom_sound, destroy_sound, pew_sound
from sprites import Player, Ball 
from init_screen import init_screen
from game_screen import game_screen

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('EL FINAL')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

