import pygame, os

pygame.init()

wumpusSound = pygame.mixer.Sound(os.path.join('Musicas',"Wumpus.wav"))
brisaSound = pygame.mixer.Sound(os.path.join('Musicas',"Brisateste.wav"))

def somWumpus():
    pygame.mixer.Sound.play(wumpusSound)

def somBrisa():
    pygame.mixer.Sound.play(brisaSound)