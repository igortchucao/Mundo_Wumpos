import pygame, os

pygame.init()

wumpusSound = pygame.mixer.Sound(os.path.join('Musicas',"Wumpus.wav"))
brisaSound = pygame.mixer.Sound(os.path.join('Musicas',"Brisateste.wav"))
pocoSound = pygame.mixer.Sound(os.path.join('Musicas',"Wilhelm-Scream.wav"))

def somWumpus():
    pygame.mixer.Sound.play(wumpusSound)

def somBrisa():
    pygame.mixer.Sound.play(brisaSound)

def somPoco():
    pygame.mixer.Sound.play(pocoSound)