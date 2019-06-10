import pygame

def music(ref, ambiente):
    pygame.mixer.music.stop()
    if ref < 99:
        if ambiente[ref]["Wumpos"]:
            pygame.mixer.music.load("Musicas/Wumpus.mp3")
            pygame.mixer.music.play(-1)
        elif ambiente[ref]["Poço"]:
            print("oi")
        elif ambiente[ref]["Ouro"]:
            print("oi")
        else:
            if ambiente[ref]['Brisa'] == 3:
                pygame.mixer.music.load("Musicas/Brisa.mp3")
                pygame.mixer.music.play(-1, 2)
    elif ref == 99:
        pygame.mixer.music.load("Musicas/GameOver.mp3")
        print("game")
        pygame.mixer.music.play(-1)
    elif ref == 100:
        pygame.mixer.music.load("Musicas/DarkSouls3.mp3")
        pygame.mixer.music.play(-1, 3)