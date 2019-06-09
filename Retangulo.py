import pygame

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Mundo do Wumpos')
width = 1200
height = 800
font = pygame.font.SysFont(None, 49)

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

class Rect():
    def __init__(self, tm):
        self.tm = tm
    
    def draw(self, ref, ambiente, show_amb):
        x = ((ref % 4) * self.tm)
        y = ((ref // 4) * self.tm)
        pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, self.tm, self.tm), 5)

        pygame.draw.rect(screen, WHITE, pygame.Rect(x + 8, y + 8, self.tm - 15, self.tm - 15), 5)

    '''FUNÇÃO QUE MOSTRA UM DETERMINADO QUADRADO'''
    def view_rect(self, ref, ambiente):
        '''99 É A REFERENCIA PARA PRINTAR TODO TABULEIRO'''
        if(ref == 99):
            for i in range(0, 16, +1):
                if ambiente[i]['Wumpos']:
                    wumpos_text = font.render('Wumpos', True, WHITE)
                    x_wumpos = ((i % 4) * self.tm) + 40
                    y_wumpos = ((i // 4) * self.tm) + 100
                    screen.blit(wumpos_text, [x_wumpos, y_wumpos])

                if ambiente[i]['Poço']:
                    poco_text = font.render('Poço', True, ROSA)
                    x_poco = ((i % 4) * self.tm) + 40
                    y_poco = ((i // 4) * self.tm) + 100
                    screen.blit(poco_text, [x_poco, y_poco])

                if ambiente[i]['Ouro']:
                    ouro_text = font.render('Ouro', True, YELLOW)
                    x_ouro = ((i % 4) * self.tm) + 40
                    y_ouro = ((i // 4) * self.tm) + 100
                    screen.blit(ouro_text, [x_ouro, y_ouro])

                if ambiente[i]['Brisa']:
                    brisa_text = font.render('Brisa', True, ROSA_c)
                    x_brisa = ((i % 4) * self.tm) + 40
                    y_brisa = ((i // 4) * self.tm) + 60
                    screen.blit(brisa_text, [x_brisa, y_brisa])

                if ambiente[i]['Fedor']:
                    Fedor_text = font.render('Fedor', True, MARROM_c)
                    x_Fedor = ((i % 4) * self.tm) + 40
                    y_Fedor = ((i // 4) * self.tm) + 20
                    screen.blit(Fedor_text, [x_Fedor, y_Fedor])

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

            '''INICIA OS TEXTOS DO MENU LATERAL'''
            text1 = text2 = text3 = text4 = text5 = font.render('Nada', True, BLACK)

            '''CRIA OS TEXTOS A PARTIR DA VARIAVEL'''
            if ambiente[ref]['Brisa']:
                text1 = font.render('Brisa', True, BLACK)
            if ambiente[ref]['Fedor']:
                text2 = font.render('Fedor', True, BLACK)
            if ambiente[ref]['Poço']:
                text3 = font.render('Poço', True, BLACK)
            if ambiente[ref]['Ouro']:
                text4 = font.render('Ouro', True, BLACK)
            if ambiente[ref]['Wumpos']:
                text5 = font.render('Wumpos', True, BLACK)

            '''CORREÇÃO DE ALTURA DO MENU'''
            lat = 950

            screen.blit(text1, [lat, 100])
            screen.blit(text2, [lat, 150])
            screen.blit(text3, [lat, 200])
            screen.blit(text4, [lat, 250])
            screen.blit(text5, [lat, 350])