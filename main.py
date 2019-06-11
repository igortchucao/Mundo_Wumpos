import pygame, sys, os, View, Gerador, Musics

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Mundo do Wumpus')
width = 1200
height = 800
font = pygame.font.SysFont(None, 49)
font2 = pygame.font.SysFont(None, 30)

'''Imagens'''
Imagem_menu = pygame.image.load(os.path.join('Imagens', 'Wumpus.png'))

'''Sons'''
pygame.mixer.music.load("Musicas/DarkSouls3.mp3")

'''Cores'''
BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0

'''Tamanho da janela'''
size = width, height

'''Cria a tela do pygamegame'''
screen = pygame.display.set_mode(size)

'''ITENS'''
line = pygame.Surface((100, 100))
line.fill(WHITE)

'''CONTROLES'''
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def main():
    loop = True
    pygame.mixer.music.play(-1)
    '''TELA DE INICIO'''
    while loop:
        screen.fill(BLACK)
        screen.blit(Imagem_menu, (0,0))
        text = font2.render('ESPAÇO PARA COMECAR', True, WHITE)
        screen.blit(text, [650, 750])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop = False
        pygame.display.update()
    '''CRIA O OBJETO DO MENU'''
    MenuWump = View.Menu(200)
    TheEnd = False
    ambiente = Gerador.gerar_ambiente()

    pos = vert = hor = 0
    while 1:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    print("algo")
                    '''CODIGO AQUI'''
                if event.key == pygame.K_F2:
                    TheEnd = True
                    Musics.music(99, ambiente)
                if event.key == pygame.K_F3:
                    TheEnd = False
                    Musics.music(100, ambiente)
                if event.key == pygame.K_UP:
                    if 0 <= vert - 1:
                        vert -= 1
                elif event.key == pygame.K_DOWN:
                    if vert + 1 < 4:
                        vert += 1
                elif event.key == pygame.K_LEFT:
                    if 0 <= hor - 1:
                        hor -= 1
                elif event.key == pygame.K_RIGHT:
                    if hor + 1 < 4:
                        hor += 1

        pos = (4 * vert) + (hor)
        screen.fill(BLACK)
        View.menu()
        if (TheEnd):
            MenuWump.view_rect(99, ambiente)
        else :
            MenuWump.view_rect(pos, ambiente)

        for j in range(0, 16, +1):
            MenuWump.draw(j, ambiente, False)
        pygame.display.update()

    pygame.mixer.music.stop()

if __name__ == '__main__':
    main()