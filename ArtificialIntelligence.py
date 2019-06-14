import random

#arq = open('Arquivos/Menu.txt', 'w')

def gera_ambiente():
	# Cada quadrado do ambiente tem 0,2 prob de ter um poço, menos o quadrado 0
	# Os quadrados adjacentes ao '0', no caso '1' e '4', também não são inclusos
        
        probabilidade = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
        quadrado = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        
        # Ambiente inicializado com 'none' para tudo em todas as posições
        ambiente = {
                0: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                1: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                2: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                3: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                4: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                5: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                6: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                7: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                8: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                9: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                10: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                11: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                12: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                13: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                14: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
                15: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None}
        }

        # Gerando as posições dos poços
        c = 0
        coord_pocos = []	# coord dos poços
        pos_pocos = []		# posições dos poços
        
        while c < 3:
                posicao = random.choices(quadrado, probabilidade).pop(0)
                if(ambiente[posicao]['Poço'] == None):
                        ambiente[posicao]['Poço'] = True
                        pos_pocos.append(posicao)
                        c += 1
                        
        for i in range(0, len(pos_pocos)):
                x = pos_pocos[i]%4
                y = pos_pocos[i]//4
                tupla = (x, y)
                coord_pocos.append(tupla)
                
        # gerando a posição das brisas
        for elem in coord_pocos:
                if(elem[0]+1 < 4):
                        tupla = (elem[0]+1, elem[1])
                        posicao = tupla[1]*4+tupla[0]
                        ambiente[posicao]['Brisa'] = True
                        
                if(elem[0]-1 > -1):
                        tupla = (elem[0]-1, elem[1])
                        posicao = tupla[1]*4+tupla[0]
                        ambiente[posicao]['Brisa'] = True
                        
                if(elem[1]+1 < 4):
                        tupla = (elem[0], elem[1]+1)
                        posicao = tupla[1]*4+tupla[0]
                        ambiente[posicao]['Brisa'] = True
                
                if(elem[1]-1 > -1):
                        tupla = (elem[0], elem[1]-1)
                        posicao = tupla[1]*4+tupla[0]
                        ambiente[posicao]['Brisa'] = True
        
        #gerando a posição do wumpus
        while True:
                posicao = random.choices(quadrado, None).pop(0)
                if(ambiente[posicao]['Poço'] == None or False):
                        ambiente[posicao]['Wumpus'] = True
                        wumpus = posicao
                        break
                        
        # gerando as posições dos fedores
        x = wumpus%4
        y = wumpus//4
        
        if(x+1 < 4):
                tupla = (x+1, y)
                posicao = tupla[1]*4+tupla[0]
                ambiente[posicao]['Fedor'] = True
                
        if(x-1 > -1):
                tupla = (x-1, y)
                posicao = tupla[1]*4+tupla[0]
                ambiente[posicao]['Fedor'] = True
                
        if(y+1 < 4):
                tupla = (x, y+1)
                posicao = tupla[1]*4+tupla[0]
                ambiente[posicao]['Fedor'] = True

        if(y-1 > -1):
                tupla = (x, y-1)
                posicao = tupla[1]*4+tupla[0]
                ambiente[posicao]['Fedor'] = True

        # Gerando a posição do ouro
        while True:
                posicao = random.choice(quadrado)
                if(ambiente[posicao]['Poço'] == None):
                #Caso Wumpus e Ouro não puderem ocupar mesmo espaço 'and ambiente[posicao[0]]['Wumpus'] == False'
                        ambiente[posicao]['Ouro'] = True
                        break
        
        return ambiente

def canto(posicao):
        if(posicao == 0 or 3 or 12 or 15):
                return True
        return False

def TELL_aux(percepcoes, posicao):
        # Inferindo conhecimento na BC sobre as informações das posições adjacentes
        wumpus_cont = 0
        xy_pos = get_coord(posicao)
        #print('Posição =', posicao, 'coordenadas = ', xy_pos)
        x = posicao%4
        y = posicao//4

        # Direita da posição
        if(x+1 <= 3):
                nova_pos = 4*y + (x+1)
                if(nova_pos >= 0 and nova_pos <= 15):
                        #print('AUX::> Direita da pos',posicao,'=', nova_pos, ' coordenadas:',  get_coord(nova_pos))
                        if(percepcoes[posicao]['Poço'] == 'Talvez' and percepcoes[nova_pos]['Brisa'] == False):
                                percepcoes[posicao]['Poço'] = False
                        if(percepcoes[posicao]['Wumpus'] == 'Talvez' and percepcoes[nova_pos]['Fedor'] == False):
                                percepcoes[posicao]['Wumpus'] = False
                        elif(percepcoes[posicao]['Wumpus'] == 'Talvez' and percepcoes[nova_pos]['Fedor'] == True):
                                wumpus_cont += 1
        # Esquerda da posição
        if(x-1 >= 0):
                nova_pos = 4*y + (x-1)
                if(nova_pos >= 0 and nova_pos <= 15):
                        #print('AUX::> Esquerda da pos',posicao,'=', nova_pos, ' coordenadas:',  get_coord(nova_pos))
                        if(percepcoes[posicao]['Poço'] == 'Talvez' and percepcoes[nova_pos]['Brisa'] == False):
                                percepcoes[posicao]['Poço'] = False
                        if(percepcoes[posicao]['Wumpus'] == 'Talvez' and percepcoes[nova_pos]['Fedor'] == False):
                                percepcoes[posicao]['Wumpus'] = False
                        elif(percepcoes[posicao]['Wumpus'] == 'Talvez' and percepcoes[nova_pos]['Fedor'] == True):
                                wumpus_cont += 1
        # Abaixo da posição
        if(y+1 <= 3):
                nova_pos = 4*(y+1) + x
                if(nova_pos >= 0 and nova_pos <= 15):
                        #print('AUX::> Abaixo da pos',posicao,'=', nova_pos, ' coordenadas:',  get_coord(nova_pos))
                        if(percepcoes[posicao]['Poço'] == 'Talvez' and percepcoes[nova_pos]['Brisa'] == False):
                                percepcoes[posicao]['Poço'] = False
                        if(percepcoes[posicao]['Wumpus'] == 'Talvez' and percepcoes[nova_pos]['Fedor'] == False):
                                percepcoes[posicao]['Wumpus'] = False
                        elif(percepcoes[posicao]['Wumpus'] == 'Talvez' and percepcoes[nova_pos]['Fedor'] == True):
                                wumpus_cont += 1
        # Acima da posição
        if(y-1 >= 0):
                nova_pos = 4*(y-1) + x
                if(nova_pos >= 0 and nova_pos <= 15):
                        #print('AUX::> Acima da pos',posicao,'=', nova_pos, ' coordenadas:',  get_coord(nova_pos))
                        if(percepcoes[posicao]['Poço'] == 'Talvez' and percepcoes[nova_pos]['Brisa'] == False):
                                percepcoes[posicao]['Poço'] = False
                        if(percepcoes[posicao]['Wumpus'] == 'Talvez' and percepcoes[nova_pos]['Fedor'] == False):
                                percepcoes[posicao]['Wumpus'] = False
                        elif(percepcoes[posicao]['Wumpus'] == 'Talvez' and percepcoes[nova_pos]['Fedor'] == True):
                                wumpus_cont += 1
        
        return percepcoes, wumpus_cont

def TELL(ambiente, percepcoes, posicao):
        # Inferindo conhecimento na BC sobre as informações de cada posição
        xy_pos = get_coord(posicao)
        wumpus_cont = 0
        arrow = False
        x = posicao%4
        y = posicao//4
        
        # Direita da posição
        if(x+1 <= 3):
                nova_pos = 4*y + (x+1)
                if(nova_pos >= 0 and nova_pos <= 15):
                        #print('TELL::> Direita da pos',posicao,'=', nova_pos, ' coordenadas:',  get_coord(nova_pos))
                        if(percepcoes[posicao]['Brisa'] == True):
                                percepcoes[nova_pos]['Poço'] = 'Talvez'
                                #percepcoes = TELL_aux(percepcoes, nova_pos)
                        if(percepcoes[posicao]['Fedor'] == True):
                                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                                percepcoes, wumpus_cont = TELL_aux(percepcoes, nova_pos)  
                if wumpus_cont >= 3 and percepcoes[nova_pos]['Wumpus'] == 'Talvez':
                        percepcoes[nova_pos]['Wumpus'] = True
                        arrow = True
        # Esquerda da posição
        if(x-1 >= 0):
                nova_pos = 4*y + (x-1)
                if(nova_pos >= 0 and nova_pos <= 15):
                        #print('TELL::> Esquerda da pos',posicao,'=', nova_pos, ' coordenadas:',  get_coord(nova_pos))
                        if(percepcoes[posicao]['Brisa'] == True):
                                percepcoes[nova_pos]['Poço'] = 'Talvez'
                                #percepcoes = TELL_aux(percepcoes, nova_pos)
                        if(percepcoes[posicao]['Fedor'] == True):
                                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                                percepcoes, wumpus_cont = TELL_aux(percepcoes, nova_pos)
                if wumpus_cont >= 3 and percepcoes[nova_pos]['Wumpus'] == 'Talvez':
                        percepcoes[nova_pos]['Wumpus'] = True
                        arrow = True
        # Abaixo da posição
        if(y+1 <= 3):
                nova_pos = 4*(y+1) + x
                if(nova_pos >= 0 and nova_pos <= 15):
                        #print('TELL::> Abaixo da pos',posicao,'=', nova_pos, ' coordenadas:',  get_coord(nova_pos))
                        if(percepcoes[posicao]['Brisa'] == True):
                                percepcoes[nova_pos]['Poço'] = 'Talvez'
                                #percepcoes = TELL_aux(percepcoes, nova_pos)
                        if(percepcoes[posicao]['Fedor'] == True):
                                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                                percepcoes, wumpus_cont = TELL_aux(percepcoes, nova_pos)
                if wumpus_cont >= 3 and percepcoes[nova_pos]['Wumpus'] == 'Talvez':
                        percepcoes[nova_pos]['Wumpus'] = True
                        arrow = True
        # Acima da posição
        if(y-1 >= 0):
                nova_pos = 4*(y-1) + x
                if(nova_pos >= 0 and nova_pos <= 15):
                        #print('TELL::> Acima da pos',posicao,'=', nova_pos, ' coordenadas:',  get_coord(nova_pos))
                        if(percepcoes[posicao]['Brisa'] == True):
                                percepcoes[nova_pos]['Poço'] = 'Talvez'
                                #percepcoes = TELL_aux(percepcoes, nova_pos)
                        if(percepcoes[posicao]['Fedor'] == True):
                                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                                percepcoes, wumpus_cont = TELL_aux(percepcoes, nova_pos)
                if wumpus_cont >= 3 and percepcoes[nova_pos]['Wumpus'] == 'Talvez':
                        percepcoes[nova_pos]['Wumpus'] = True
                        arrow = True
        
        return percepcoes, arrow

def ASK(ambiente, percepcoes, posicao):
        # Consultando a base de conhecimento sobre as informações
        #a cerca do ambiente
        arrow = False
        
        if(ambiente[posicao]['Fedor'] == True):
                percepcoes[posicao]['Fedor'] = True
                percepcoes[posicao]['Wumpus'] = False
                percepcoes, arrow = TELL(ambiente, percepcoes, posicao)
        else:
                percepcoes[posicao]['Fedor'] = False
                percepcoes[posicao]['Wumpus'] = False

        if(ambiente[posicao]['Brisa'] == True):
                percepcoes[posicao]['Brisa'] = True
                percepcoes[posicao]['Poço'] = False
                percepcoes, arrow = TELL(ambiente, percepcoes, posicao)
        else:
                percepcoes[posicao]['Poço'] = False
                percepcoes[posicao]['Brisa'] = False

        if(ambiente[posicao]['Ouro'] == True):
                percepcoes[posicao]['Ouro'] = True
        else:
                percepcoes[posicao]['Ouro'] = False
        
        if(ambiente[posicao]['Poço'] == True):
                percepcoes[posicao]['Poço'] = True
        else:
                percepcoes[posicao]['Poço'] = False
        
        if(ambiente[posicao]['Wumpus'] == True):
                percepcoes[posicao]['Wumpus'] = True
        else:
                percepcoes[posicao]['Wumpus'] = False
        
        return percepcoes, arrow

def mov_to_coord(movimento):
        tupla = (0, 0)
        if(movimento == 1):
                # direita  = 1
                tupla = tuple((1, 0))
        elif(movimento == -1):
                # esquerda = -1
                tupla = tuple((-1, 0))
        elif(movimento == 4):
                # cima     = 4
                tupla = tuple((0, 1))
        elif(movimento == -4):
                # baixo    = -4
                tupla = tuple((0, -1))
        return tupla

def get_coord(movimento):
        x = movimento%4
        y = movimento//4
        return tuple((x, y))

def coord_to_pos(tu_posicao_atual, tu_movimento):
        x = tu_posicao_atual[0]+tu_movimento[0]
        y = tu_posicao_atual[1]+tu_movimento[1]
        return (4*y + x)

def mov_valido(coord_direcao, posicao, percepcoes):
        # pegando as coordenadas da posição
        coord_pos = get_coord(posicao)
        
        # O movimento é a soma das coordenadas 'coord_direcao' e 'coord_pos'
        coord_nova_pos = tuple((coord_pos[0]+coord_direcao[0], coord_pos[1]+coord_direcao[1]))
        # nova_pos é a coord_mov em forma de posições (0, 15)
        nova_pos =  coord_nova_pos[1]*4 + coord_nova_pos[0]

        # Se a nova posição estiver no intervalo do campo então é válido
        if((coord_nova_pos[0] < 4 and coord_nova_pos[0] > -1)
        and (coord_nova_pos[1] < 4 and coord_nova_pos[1] > -1)):
                return True
        return False

def end_game(percepcoes, posicao):
        if(percepcoes[posicao]['Ouro'] == True):
                print('O personagem encontrou o Ouro!')
        elif(percepcoes[posicao]['Wumpus'] == True):
                print('O personagem foi devorado pelo Wumpus.')
        elif(percepcoes[posicao]['Poço'] == True):
                print('O personagem caiu no poço!')

def show_info(ambiente, perc_do_ambiente):
        print('\nINFORMAÇÕES DO AMBIENTE:')
        for i,j in ambiente.items():
                print(i, j)
        print('\nINFORMAÇÕES DA PERCEPÇÃO DO AGENTE:')
        # imprimindo perCepções
        for i, j in perc_do_ambiente.items():
                print('Posição {:>2}'.format(i))
                for k, l in j.items():
                        print('{}: {} '.format(k.upper(), l), end=' ')
                print()

def print_ambiente(ambiente):
    for pos, pos_dict in ambiente.items():
        print(pos,':\n{', end='')
        for att, value in pos_dict.items():
            print(att, value, ' ',end='')
        print('}')

def atirar(percepcoes):
        for i in range(0, 16):
                if(percepcoes[i]['Wumpus'] == True):
                        return i
        return None

def jogo(posicao_atual, ambiente, percepcoes):
        ouro = False
        buraco = False
        wumpus = False
        
        # movimentos possíveis 
        li_movimentos = [-1, 1, 4, -4] # esquerda, direita, cima, baixo
        
        # Verificando posição atual se existe algum problema
        percepcoes, arrow = ASK(ambiente, percepcoes, posicao_atual)
        if(percepcoes[posicao_atual]['Wumpus'] == True):
                wumpus = True
        if(percepcoes[posicao_atual]['Poço'] == True):
                buraco = True
        if(percepcoes[posicao_atual]['Ouro'] == True):
                ouro = True
        
        # Escolhe aleatoriamente um movimento todos com probabilidades iguais
        #movimento = random.choice(li_movimentos)     
        
        # tupla com as coordenadas do movimento escolhido
        #coord_porx_mov = mov_to_coord(movimento)

        # Verifica se o movimento é possível
        #validade = mov_valido(coord_porx_mov, posicao_atual, percepcoes)
        if(ouro == True or buraco == True or wumpus == True):
                validade = False
        #if(validade == True):
                #posicao_atual = coord_to_pos(get_coord(posicao_atual), coord_porx_mov)
        
        return posicao_atual, ouro, buraco, wumpus, arrow