# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load("exercicios_python/exemplo.mp3")
pygame.mixer.music.play()
time.sleep(10)  
input("Pressione Enter para encerrar o programa...")
pygame.mixer.music.stop()
pygame.mixer.quit()