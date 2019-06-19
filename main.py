import sys, os, View, time, Musicas
import ArtificialIntelligence as ai
import pygame 

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Mundo do Wumpus')
width = 1200

height = 800
font = pygame.font.SysFont(None, 49)
font2 = pygame.font.SysFont(None, 30)

# Percepções do ambiente
percepcoes = {
    0: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    1: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    2: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    3: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    4: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    5: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    6: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    7: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    8: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    9: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    10: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    11: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    12: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    13: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    14: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None},
    15: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None,'Cor': None}
}

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
    # Definições de variáveis importantes
    ouro = poco = wumpus = arrow = False
    arrowAmount = 1
    loop = hit = True
    caminho = []
    desempenho = 0
    
    '''TELA DE INICIO'''
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
    
    '''CRIA O OBJETO DO MENU'''
    MenuWump = View.Menu(200)
    TheEnd = False
    iaKey = False
    ambiente = ai.gera_ambiente()

    pos = vert = hor = 0
    while(1):
        clock.tick(10)
        if(arrow == True and arrowAmount == 1):
            pos_wumpus, hit = ai.atirar(ambiente, percepcoes)
            print('Wumpus em', pos_wumpus,'ATIRAR!')
            desempenho -= 10
            arrowAmount = 0
            
            MenuWump.personagem.tiro(ambiente, (pos_wumpus))
        
        if(ouro == True):
            iaKey = False
            print('Pegou o ouro!')
            MenuWump.view_rect(ambiente, 99)

        screen.fill(BLACK)
        MenuWump.draw()
        View.menu()

        # Keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                caminho = open(os.path.join('Arquivos', 'caminho.txt'), 'a')
                caminho.write(str(0))
                caminho.close()
                os.remove(os.path.join('Arquivos', 'caminho.txt'))
                pygame.mixer.music.stop()
                ai.print_ambiente(percepcoes)
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    if(iaKey == True):
                        iaKey = False
                    else:
                        iaKey = True
                if event.key == pygame.K_F2:
                    TheEnd = True
                if event.key == pygame.K_F3:
                    TheEnd = False
                # Comandos para usuário jogar
                if event.key == pygame.K_UP:
                    if 0 <= vert - 1:
                        MenuWump.personagem.updateUp(((hor * 197 + 24), (vert * 197 + 17)))
                        vert -= 1
                        desempenho -= 1
                        if(ambiente[vert*4+hor]['Poço']):
                            MenuWump.personagem.cairBuraco(vert*4+hor)
                            TheEnd = True
                elif event.key == pygame.K_DOWN:
                    if vert + 1 < 4:
                        MenuWump.personagem.updateDown(((hor * 197 + 50), (vert * 197 + 17)))
                        vert += 1
                        desempenho -= 1
                        if(ambiente[vert*4+hor]['Poço']):
                            MenuWump.personagem.cairBuraco(vert*4+hor)
                            TheEnd = True
                elif event.key == pygame.K_LEFT:
                    if 0 <= hor - 1:
                        MenuWump.personagem.updateEsquerda(((hor * 197 + 50), (vert * 197 + 17)))
                        hor -= 1
                        desempenho -= 1
                        if(ambiente[vert*4+hor]['Poço']):
                            MenuWump.personagem.cairBuraco(vert*4+hor)
                            TheEnd = True
                elif event.key == pygame.K_RIGHT:
                    if hor + 1 < 4:
                        MenuWump.personagem.updateDireita(((hor * 197 + 50), (vert * 197 + 17)))
                        hor += 1
                        desempenho -= 1
                        if(ambiente[vert*4+hor]['Poço']):
                            MenuWump.personagem.cairBuraco(vert*4+hor)
                            TheEnd = True 
                elif event.key == pygame.K_SPACE:

                    MenuWump.personagem.tiro(ambiente, (vert*4)+hor)
                    
                    desempenho -= 10
                    if(ambiente[(vert*4)+hor+1]['Wumpus']):
                        percepcoes[(vert*4)+hor+1]['Wumpus'] = False
                        if(0 <= ((vert*4)+hor+2) < 15):
                            percepcoes[(vert*4)+hor+2]['Fedor'] = False
                        if(0 <= ((vert*4)+hor) < 15):
                            percepcoes[(vert*4)+hor]['Fedor'] = False
                        if(0 <= ((vert*4)+hor+5) < 15):
                            percepcoes[(vert*4)+hor+5]['Fedor'] = False
                        if(0 <= ((vert*4)+hor-3) < 15):
                            percepcoes[(vert*4)+hor-3]['Fedor'] = False

                    if(ambiente[(vert*4)+hor-1]['Wumpus']):
                        percepcoes[(vert*4)+hor-1]['Wumpus'] = False
                        if(0 <= ((vert*4)+hor) < 15):
                            percepcoes[(vert*4)+hor]['Fedor'] = False
                        if(0 <= ((vert*4)+hor-2) < 15):
                            percepcoes[(vert*4)+hor-2]['Fedor'] = False
                        if(0 <= ((vert*4)+hor+3) < 15):
                            percepcoes[(vert*4)+hor+3]['Fedor'] = False
                        if(0 <= ((vert*4)+hor-5) < 15):
                            percepcoes[(vert*4)+hor-5]['Fedor'] = False
                    
                    if(ambiente[(vert*4)+hor+4]['Wumpus']):
                        percepcoes[(vert*4)+hor+4]['Wumpus'] = False
                        if(0 <= ((vert*4)+hor+5) < 15):
                            percepcoes[(vert*4)+hor+5]['Fedor'] = False
                        if(0 <= ((vert*4)+hor+3) < 15):
                            percepcoes[(vert*4)+hor+3]['Fedor'] = False
                        if(0 <= ((vert*4)+hor+8) < 15):
                            percepcoes[(vert*4)+hor+8]['Fedor'] = False
                        if(0 <= ((vert*4)+hor) < 15):
                            percepcoes[(vert*4)+hor]['Fedor'] = False
                    
                    if(ambiente[(vert*4)+hor-4]['Wumpus']):
                        percepcoes[(vert*4)+hor-4]['Wumpus'] = False
                        if(0 <= ((vert*4)+hor-3) < 15):
                            percepcoes[(vert*4)+hor-3]['Fedor'] = False
                        if(0 <= ((vert*4)+hor-5) < 15):
                            percepcoes[(vert*4)+hor-5]['Fedor'] = False
                        if(0 <= ((vert*4)+hor) < 15):
                            percepcoes[(vert*4)+hor]['Fedor'] = False
                        if(0 <= ((vert*4)+hor-8) < 15):
                            percepcoes[(vert*4)+hor-8]['Fedor'] = False

        if(ouro == True):
            iaKey = False
            print('Pegou o ouro!')
            MenuWump.view_rect(ambiente, 99)
        
        if(poco == True):
            iaKey = False
            MenuWump.personagem.cairBuraco(pos)

        # Se 'iaKey' == True, a posição depende do ai.jogo()
        if(iaKey):
            pos_ant = pos
            pos, ouro, poco, wumpus, arrow, caminho = ai.jogo(pos, ambiente, percepcoes, caminho)
            hor = pos % 4
            vert = pos // 4
            '''if (pos_ant - 1 == pos):
                MenuWump.personagem.updateEsquerda(((hor * 197 + 50), (vert * 197 + 17)))
            elif (pos_ant + 1 == pos):
                MenuWump.personagem.updateDireita(((hor * 197 + 50), (vert * 197 + 17)))
            elif (pos_ant + 4 == pos):
                MenuWump.personagem.updateDown(((hor * 197 + 50), (vert * 197 + 17)))
            elif (pos_ant - 4 == pos):
                MenuWump.personagem.updateUp(((hor * 197 + 24), (vert * 197 + 17)))'''

            time.sleep(1)
            desempenho -= 1
        else:
            pos = (4 * vert) + (hor)
            '''pos, ouro, poco, wumpus, arrow = ai.jogoUser(pos, ambiente, percepcoes)
            desempenho -= 1'''
        if (TheEnd):
            MenuWump.view_rect(99, ambiente)
        else :
            MenuWump.view_rect(pos, ambiente)
        
        # Atualização do valor de desempenho para ouro/wumpus/poço
        if ouro == True:
            desempenho += 1000
        if wumpus == True or poco == True:
            desempenho -= 1000
        
        screen.blit(pygame.font.SysFont(None, 50).render('DESEMPENHO:', True, BLACK), [width - 370, 750])
        screen.blit(pygame.font.SysFont(None, 50).render(str(desempenho), True, BLACK), [width - 75, 750])
        pygame.display.update()

    ai.end_game(percepcoes, pos)

if __name__ == '__main__':
    main()