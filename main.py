import pygame, sys, os, Retangulo, Wumpos2

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Mundo do Wumpus')
width = 1200
height = 800
font = pygame.font.SysFont(None, 49)
font2 = pygame.font.SysFont(None, 30)

'''Imagens'''
Imagem_menu = pygame.image.load(os.path.join('Imagens', 'Wumpos.png'))

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
loop = True

def menu():
    pygame.draw.rect(screen, WHITE, pygame.Rect(805, 0, 395, 800), 5)
    pygame.draw.rect(screen, WHITE, pygame.Rect(815, 10, 375, 780))
    text = font.render('MUNDO DO WUMPOS ', True, BLACK)
    screen.blit(text, [832, 40])

pygame.mixer.music.play(-1)

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

retangulo = Retangulo.Rect(200)
view = False
ambiente = Wumpos2.gerar_ambiente()

sel = vert = hor = 0
while 1:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                Wumpos2.Resultado_bot(ambiente)
            if event.key == pygame.K_F2:
                view = True
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

    screen.fill(BLACK)
    menu()
    if (view):
        retangulo.view_rect(99, ambiente)
    else :
        retangulo.view_rect((4 * vert) + (hor), ambiente)

    for j in range(0, 16, +1):
        retangulo.draw(j, ambiente, False)
    pygame.display.update()

pygame.mixer.music.stop()