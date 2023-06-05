# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()  #Para iniciar o pygame
pygame.mixer.music.load('ex021.mp3')    # Para carregar o arquivo
pygame.mixer.music.play()   # Para iniciar o evento
input()
pygame.event.wait()           # Para esperar o evento acabar para encerrar o programa