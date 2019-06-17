import pygame, os

pygame.init()

wumpusSound = pygame.mixer.Sound(os.path.join('Musicas',"Wumpus.wav"))
brisaSound = pygame.mixer.Sound(os.path.join('Musicas',"Brisateste.wav"))
pocoSound = pygame.mixer.Sound(os.path.join('Musicas',"Wilhelm-Scream.wav"))
tiroSound = pygame.mixer.Sound(os.path.join('Musicas',"Som-de-Tiro.wav"))

def somWumpus():
    pygame.mixer.Sound.play(wumpusSound)

def somBrisa():
    pygame.mixer.Sound.play(brisaSound)

def somPoco():
    pygame.mixer.Sound.play(pocoSound)

def somTiro():
    pygame.mixer.Sound.play(tiroSound)