import random

def gera_ambiente():
	# Cada quadrado do ambiente tem 0,2 prob de ter um poço, menos o quadrado 0
	# Os quadrados adjacentes ao '0', no caso '1' e '4', também não são inclusos
        
        probabilidade = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
        quadrado = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        c = 0
        pocos = []		# coord dos poços
        _pocos = []		# posições dos poços
        while c < 3:
                number = random.choices(quadrado, weights=probabilidade, cum_weights=None, k=1)
                if(_pocos.count(number[0]) == 0):
                        _pocos.append(number.pop())
                        c += 1
                        
        for i in range(0, len(_pocos)):
                x = _pocos[i]%4
                y = _pocos[i]//4
                tupla = (x, y)
                pocos.append(tupla)
                
        # gerando a posição das brisas
        brisa = []		# coordenadas da brisa
        _brisa = []		# posições da brisa
        for _po in pocos:
                if(_po[0]+1 < 4):
                        tupla = (_po[0]+1, _po[1])
                        brisa.append(tupla)
                        _brisa.append(tupla[1]*4+tupla[0])
                        
                if(_po[0]-1 > -1):
                        tupla = (_po[0]-1, _po[1])
                        brisa.append(tupla)
                        _brisa.append(tupla[1]*4+tupla[0])
                        
                if(_po[1]+1 < 4):
                        tupla = (_po[0], _po[1]+1)
                        brisa.append(tupla)
                        _brisa.append(tupla[1]*4+tupla[0])
                
                if(_po[1]-1 > -1):
                        tupla = (_po[0], _po[1]-1)
                        brisa.append(tupla)
                        _brisa.append(tupla[1]*4+tupla[0])
        
        #gerando a posição do wumpus
        while True:
                _wumpus = random.choices(quadrado, None, k=1)
                if(_pocos.count(_wumpus[0]) == 0):
                        wumpus = _wumpus.pop()
                        break
                        
        # gerando a posição dos fedores
        x = wumpus%4
        y = wumpus//4
        fedor = []		# coord dos fedores
        _fedor = []		# posições dos fedores
        
        if(x+1 < 4):
                tupla = (x+1, y)
                fedor.append(tupla)
                _fedor.append(tupla[1]*4+tupla[0])
                
        if(x-1 > -1):
                tupla = (x-1, y)
                fedor.append(tupla)
                _fedor.append(tupla[1]*4+tupla[0])
                
        if(y+1 < 4):
                tupla = (x, y+1)
                fedor.append(tupla)
                _fedor.append(tupla[1]*4+tupla[0])

        if(y-1 > -1):
                tupla = (x, y-1)
                fedor.append(tupla)
                _fedor.append(tupla[1]*4+tupla[0])
        while True:
                _ouro = random.choices(quadrado, None, k=1)
                if(_pocos.count(_ouro[0]) == 0 and wumpus != _ouro[0]):
                        ouro = _ouro.pop()
                        break

        amb = {
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
        ambiente = {
		'Poço': _pocos,
		'Brisa': _brisa,
		'Wumpus': wumpus,
		'Fedor': _fedor,
		'Ouro': ouro
        }
        for elem in ambiente['Poço']:
                amb[elem]['Poço'] = True
        for elem in ambiente['Brisa']:
                amb[elem]['Brisa'] = True
        for elem in ambiente['Fedor']:
                amb[elem]['Fedor'] = True
        amb[ambiente['Wumpus']]['Wumpus'] = True
        amb[ambiente['Ouro']]['Ouro'] = True
        
        return amb

def infere_aux(percepcoes, posicao):
        coord_pos = get_coord(posicao)
        if(coord_pos[0]-1 > -1):
                nova_pos = coord_pos[1]*4 + (coord_pos[0]-1)
                if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Brisa'] == False):
                        percepcoes[posicao]['Poço'] = False
                        print('Não tem um poço em', posicao)
        
        if(coord_pos[0]+1 < 5):
                nova_pos = coord_pos[1]*4 + (coord_pos[0]+1)
                if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Brisa'] == False):
                        percepcoes[posicao]['Poço'] = False
                        print('Não tem um poço em', posicao)

        if(coord_pos[1]-1 > -1):
                nova_pos = (coord_pos[1]-1)*4 + coord_pos[0]
                if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Brisa'] == False):
                        percepcoes[posicao]['Poço'] = False
                        print('Não tem um poço em', posicao)

        if(coord_pos[1]+1 < 5):
                nova_pos = (coord_pos[1]+1)*4 + coord_pos[0]
                if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Brisa'] == False):
                        percepcoes[posicao]['Poço'] = False
                        print('Não tem um poço em', posicao)

        if(coord_pos[0]-1 > -1):
                nova_pos = coord_pos[1]*4 + (coord_pos[0]-1)
                if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Fedor'] == False):
                        percepcoes[posicao]['Poço'] = False
                        print('Não tem um wumpus em', posicao)
        
        if(coord_pos[0]+1 < 5):
                nova_pos = coord_pos[1]*4 + (coord_pos[0]+1)
                if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Fedor'] == False):
                        percepcoes[posicao]['Poço'] = False
                        print('Não tem um wumpus em', posicao)

        if(coord_pos[1]-1 > -1):
                nova_pos = (coord_pos[1]-1)*4 + coord_pos[0]
                if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Fedor'] == False):
                        percepcoes[posicao]['Poço'] = False
                        print('Não tem um wumpus em', posicao)

        if(coord_pos[1]+1 < 5):
                nova_pos = (coord_pos[1]+1)*4 + coord_pos[0]
                if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Fedor'] == False):
                        percepcoes[posicao]['Poço'] = False
                        print('Não tem um wumpus em', posicao)
        
        
        return percepcoes

def infere_conhecimento(ambiente, percepcoes, posicao):
        coord_pos = get_coord(posicao)
        
        if(ambiente[posicao]['Brisa'] == True):
                if(coord_pos[0]-1 > -1):
                        nova_pos = coord_pos[1]*4 + (coord_pos[0]-1)
                        if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Poço'] == None):
                                percepcoes[nova_pos]['Poço'] = 'Talvez'
                                percepcoes = infere_aux(percepcoes, nova_pos)
                
                if(coord_pos[0]+1 < 5):
                        nova_pos = coord_pos[1]*4 + (coord_pos[0]+1)
                        if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Poço'] == None):
                                percepcoes[nova_pos]['Poço'] = 'Talvez'
                                percepcoes = infere_aux(percepcoes, nova_pos)

                if(coord_pos[1]-1 > -1):
                        nova_pos = (coord_pos[1]-1)*4 + coord_pos[0]
                        if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Poço'] == None):
                                percepcoes[nova_pos]['Poço'] = 'Talvez'
                                percepcoes = infere_aux(percepcoes, nova_pos)

                if(coord_pos[1]+1 < 5):
                        nova_pos = (coord_pos[1]+1)*4 + coord_pos[0]
                        if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Poço'] == None):
                                percepcoes[nova_pos]['Poço'] = 'Talvez'
                                percepcoes = infere_aux(percepcoes, nova_pos)
                        
        if(ambiente[posicao]['Fedor'] == True):
                if(coord_pos[0]-1 > -1):
                        nova_pos = coord_pos[1]*4 + (coord_pos[0]-1)
                        if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Wumpus'] == None):
                                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                                percepcoes = infere_aux(percepcoes, nova_pos)
                                
                if(coord_pos[0]+1 < 5):
                        nova_pos = coord_pos[1]*4 + (coord_pos[0]+1)
                        if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Wumpus'] == None):
                                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                                percepcoes = infere_aux(percepcoes, nova_pos)

                if(coord_pos[1]-1 > -1):
                        nova_pos = (coord_pos[1]-1)*4 + coord_pos[0]
                        if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Wumpus'] == None):
                                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                                percepcoes = infere_aux(percepcoes, nova_pos)

                if(coord_pos[1]+1 < 5):
                        nova_pos = (coord_pos[1]+1)*4 + coord_pos[0]
                        if(nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Wumpus'] == None):
                                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                                percepcoes = infere_aux(percepcoes, nova_pos)
        
        return percepcoes

def percepcao_ambiente(ambiente, percepcoes, posicao):
        # Se em uma determinada posição houver Fedor, não existe Wumpus nela.
        # A mesma coisa para Brisa/Poço
        
        if(ambiente[posicao]['Fedor'] == True):
                print('Contém fedor na posição ', posicao)
                percepcoes[posicao]['Wumpus'] = False
                percepcoes = infere_conhecimento(ambiente, percepcoes, posicao)
        else:
                percepcoes[posicao]['Fedor'] = False
                percepcoes[posicao]['Wumpus'] = False

        if(ambiente[posicao]['Brisa'] == True):
                print('Contém Brisa na posição ', posicao)
                percepcoes[posicao]['Poço'] = False
                percepcoes = infere_conhecimento(ambiente, percepcoes, posicao)
        else:
                percepcoes[posicao]['Poço'] = False
                percepcoes[posicao]['Brisa'] = False

        if(ambiente[posicao]['Ouro'] == True):
                print('O personagem achou o Ouro')
                percepcoes[posicao]['Ouro'] = True
        else:
                percepcoes[posicao]['Ouro'] = False
        
        if(ambiente[posicao]['Poço'] == True):
                print('O personagem caiu num poço')
                percepcoes[posicao]['Ouro'] = True
        
        if(ambiente[posicao]['Wumpus'] == posicao):
                print('O personagem foi devorado pelo Wumpus')
                percepcoes[posicao]['Wumpus'] = True
        
        return percepcoes

def coord_do_movimento(movimento):
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

def prox_posicao(tu_posicao_atual, tu_movimento):
        x = tu_posicao_atual[0]+tu_movimento[0]
        y = tu_posicao_atual[1]+tu_movimento[1]
        return (4*y + x)

def mov_valido(direcao, posicao, percep):
        # pegando as coordenadas da posição
        coord_pos = get_coord(posicao)
        ouro = False
        buraco = False
        wumpus = False

        # movimento 'm' é a soma das coordenadas da 'direcao' mais as coordenadas da posição 'coord_pos'
        m = tuple((coord_pos[0]+direcao[0], coord_pos[1]+direcao[1]))
        pos_m =  m[1]*4 + m[0]

        # se o movimento 'm' estiver no intervalo do campo e não possuir Poço ou Wumpus naquela posição é válido
        if((m[0] < 4 and m[0] > -1) and (m[1] < 4 and m[1] > -1)):
                if(percep[pos_m]['Wumpus'] == True):
                        wumpus = True
                if(percep[pos_m]['Poço'] == True):
                        buraco = True
                if(percep[pos_m]['Ouro'] == True):
                        ouro = True
                return True, ouro, buraco, wumpus
        return False, ouro, buraco, wumpus

def string_direcao(movimento):
        if(movimento == -1):
                        string = 'esquerda'
        elif(movimento == 1):
                        string = 'direita'
        elif(movimento == 4):
                        string = 'cima'
        elif(movimento == -4):
                        string = 'baixo'

        return string

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

def jogo(posicao_atual, ambiente, perc_do_ambiente):
        # O personagem começa na posição '0'
        #posicao_atual = 0
        ouro = False
        buraco = False
        wumpus = False
        
        # movimentos possíveis 
        movimentos = [-1, 1, 4, -4] # esquerda, direita, cima, baixo
        
        #while (ouro != True and wumpus != True and buraco != True):
        
        # Verificando posição atual se existe algum problema
        perc_do_ambiente = percepcao_ambiente(ambiente, perc_do_ambiente, posicao_atual)
        
        # Escolhe aleatoriamente um movimento todos com probabilidades iguais
        prox_movimento = random.choice(movimentos)     
        
        # tupla com as coordenadas do movimento escolhido
        tu_prox_mov = coord_do_movimento(prox_movimento)
        #string_movimento = string_direcao(prox_movimento)

        # Verifica se o movimento é possível
        validade, ouro, buraco, wumpus = mov_valido(tu_prox_mov, posicao_atual, perc_do_ambiente)
        if(validade == True):
                #print('Indo para', string_movimento, 'da posição', posicao_atual,'\n')
                posicao_atual = prox_posicao(get_coord(posicao_atual), tu_prox_mov)
        return posicao_atual, ouro, wumpus, buraco
        
        #end_game(perc_do_ambiente, posicao_atual)
        # imprimindo informações do ambiente
        #show_info(ambiente, perc_do_ambiente)


#main()
"""
 12 13 14 15
 8  9  10 11
 4  5  6  7
 0  1  2  3
"""
