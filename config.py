import pygame
import os
import sys

# Dados gerais do jogo.
WIDTH = 600 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define tamanhos
ball_WIDTH = 50
ball_HEIGHT = 50
player_WIDTH = 20
player_HEIGHT = 100

# Define algumas variáveis com as cores básicas

BLACK = (0, 0, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2

Points = [0,0]
