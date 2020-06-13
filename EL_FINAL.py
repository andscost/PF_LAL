import pygame
import random
from config import WIDTH, HEIGHT, START, PLAYING, DONE, GAMEOVER
from init_screen import init_screen
from game_screen import game_screen

pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CrazyPong')

state = START
while state != DONE:
    if state == START:
        state = init_screen(window)
    elif state == PLAYING:
        state = game_screen(window)
    elif state == GAMEOVER:
        state = gameover_screen(window)
    else:
        state = DONE

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

