import pygame, os

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Mundo do Wumpus')
width = 1200
height = 800
font = pygame.font.SysFont(None, 49)

'''Imagens'''
Imagem_buraco = pygame.image.load(os.path.join('Imagens', 'buraco1.png'))
Imagem_wumpus = pygame.image.load(os.path.join('Imagens', 'Wumpus1.png'))
Imagem_Ouro = pygame.image.load(os.path.join('Imagens', 'Ouro.png'))

'''Cores'''
BLACK = 0, 0, 0
WHITE = 255, 255, 255
YELLOW = 255, 255, 0
ROSA = 255, 0, 255
ROSA_c = 238, 130, 238
MARROM_c = 184, 134, 11

'''Tamanho da janela'''
size = width, height

'''Cria a tela do pygamegame'''
screen = pygame.display.set_mode(size)

class Menu():
    def __init__(self, tm):
        self.tm = tm
        self.menu = open('Arquivos/Menu.txt', 'r')
    
    '''FUNÇÃO QUE DESENHA O TABULEIRO'''
    def draw(self, ref, ambiente, show_amb):
        x = ((ref % 4) * self.tm)
        y = ((ref // 4) * self.tm)
        pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, self.tm, self.tm), 5)

        pygame.draw.rect(screen, WHITE, pygame.Rect(x + 8, y + 8, self.tm - 15, self.tm - 15), 5)

    '''FUNÇÃO QUE MOSTRA UM DETERMINADO QUADRADO'''
    def view_rect(self, ref, ambiente):
        '''99 É A REFERENCIA PARA PRINTAR TODO TABULEIRO'''
        if(ref == 99) or ambiente[ref]['Wumpus']:
            for i in range(0, 16, +1):
                if ambiente[i]['Wumpus']:
                    x_wumpos = ((i % 4) * self.tm) + 100
                    y_wumpos = ((i // 4) * self.tm) + 100
                    screen.blit(Imagem_wumpus, (x_wumpos - 74, y_wumpos - 74))
                else:

                    if ambiente[i]['Poço']:
                        x_poco = ((i % 4) * self.tm) + 100
                        y_poco = ((i // 4) * self.tm) + 100
                        screen.blit(Imagem_buraco, (x_poco - 74, y_poco - 74))
                    else:

                        if ambiente[i]['Ouro']:
                            x_ouro = ((i % 4) * self.tm) + 100
                            y_ouro = ((i // 4) * self.tm) + 100
                            screen.blit(Imagem_Ouro, (x_ouro - 74, y_ouro - 74))
                        else:

                            if ambiente[i]['Fedor']:
                                fedor_text = font.render('Fedor', True, MARROM_c)
                                x_Fedor = ((i % 4) * self.tm) + 40
                                y_Fedor = ((i // 4) * self.tm) + 20
                                screen.blit(fedor_text, [x_Fedor, y_Fedor])

                            if ambiente[i]['Brisa']:
                                brisa_text = font.render('Brisa', True, ROSA_c)
                                x_brisa = ((i % 4) * self.tm) + 40
                                y_brisa = ((i // 4) * self.tm) + 60
                                screen.blit(brisa_text, [x_brisa, y_brisa])

                screen.blit(pygame.font.SysFont(None, 150).render('G', True, BLACK), [970, 100])
                screen.blit(pygame.font.SysFont(None, 150).render('A', True, BLACK), [970, 180])
                screen.blit(pygame.font.SysFont(None, 150).render('M', True, BLACK), [970, 260])
                screen.blit(pygame.font.SysFont(None, 150).render('E', True, BLACK), [970, 340])
                screen.blit(pygame.font.SysFont(None, 150).render('O', True, BLACK), [970, 450])
                screen.blit(pygame.font.SysFont(None, 150).render('V', True, BLACK), [970, 530])
                screen.blit(pygame.font.SysFont(None, 150).render('E', True, BLACK), [970, 610])
                screen.blit(pygame.font.SysFont(None, 150).render('R', True, BLACK), [970, 690])

        else:
            x = ((ref % 4) * self.tm) + 100
            y = ((ref // 4) * self.tm) + 100
            pygame.draw.circle(screen, YELLOW, (x, y), 90)
            pygame.draw.circle(screen, BLACK, (x, y), 88, 1)
            pygame.draw.circle(screen, BLACK, (x, y), 85, 2)

            '''CRIA OS TEXTOS A PARTIR DA VARIAVEL'''
            if ambiente[ref]['Wumpus']:
                screen.blit(Imagem_wumpus, (x - 74, y - 74))
            elif ambiente[ref]['Ouro']:
                screen.blit(Imagem_Ouro, (x - 74, y - 74))
            elif ambiente[ref]['Poço']:
                screen.blit(Imagem_buraco, (x - 74, y - 74))
            else:
                if ambiente[ref]['Brisa']:
                    screen.blit(font.render('Brisa', True, BLACK), [x - 42, y])
                if ambiente[ref]['Fedor']:
                    screen.blit(font.render('Fedor', True, MARROM_c), [x - 42, y - 40])

    def menu_lateral(self):
        texto = self.menu.readlines()
        for linha in texto :
            screen.blit(font.render(linha, True, BLACK), [950, 200])

def menu():
    pygame.draw.rect(screen, WHITE, pygame.Rect(805, 0, 395, 800), 5)
    pygame.draw.rect(screen, WHITE, pygame.Rect(815, 10, 375, 780))
    text = font.render('MUNDO DO WUMPUS ', True, BLACK)
    screen.blit(text, [832, 40])
