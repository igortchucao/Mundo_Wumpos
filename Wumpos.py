from random import *

def gerar_ambiente():
    # Cada quadrado do ambiente tem 0,2 prob de ter um poço, menos o quadrado 0
    # Os quadrados adjacentes ao '0', no caso '1' e '4', também não são inclusos

    probabilidade = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    quadrado = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    c = 0
    pocos = []  # coord dos poços
    _pocos = []  # posições dos poços
    while c < 3:
        number = choices(quadrado, weights=probabilidade, cum_weights=None, k=1)
        if (_pocos.count(number[0]) == 0):
            _pocos.append(number.pop())
            c += 1

    for i in range(0, len(_pocos)):
        x = _pocos[i] % 4
        y = _pocos[i] // 4
        tupla = (x, y)
        pocos.append(tupla)

    # gerando a posição das brisas
    brisa = []  # coordenadas da brisa
    _brisa = []  # posições da brisa
    for _po in pocos:
        if (_po[0] + 1 < 4):
            tupla = (_po[0] + 1, _po[1])
            brisa.append(tupla)
            _brisa.append(tupla[1] * 4 + tupla[0])

        if (_po[0] - 1 > -1):
            tupla = (_po[0] - 1, _po[1])
            brisa.append(tupla)
            _brisa.append(tupla[1] * 4 + tupla[0])

        if (_po[1] + 1 < 4):
            tupla = (_po[0], _po[1] + 1)
            brisa.append(tupla)
            _brisa.append(tupla[1] * 4 + tupla[0])

        if (_po[1] - 1 > -1):
            tupla = (_po[0], _po[1] - 1)
            brisa.append(tupla)
            _brisa.append(tupla[1] * 4 + tupla[0])

    # gerando a posição do wumpus
    while True:
        _wumpus = choices(quadrado, None, k=1)
        if (_pocos.count(_wumpus[0]) == 0):
            wumpus = _wumpus.pop()
            break

    # gerando a posição dos fedores
    x = wumpus % 4
    y = wumpus // 4
    fedor = []  # coord dos fedores
    _fedor = []  # posições dos fedores

    if (x + 1 < 4):
        tupla = (x + 1, y)
        fedor.append(tupla)
        _fedor.append(tupla[1] * 4 + tupla[0])

    if (x - 1 > -1):
        tupla = (x - 1, y)
        fedor.append(tupla)
        _fedor.append(tupla[1] * 4 + tupla[0])

    if (y + 1 < 4):
        tupla = (x, y + 1)
        fedor.append(tupla)
        _fedor.append(tupla[1] * 4 + tupla[0])

    if (y - 1 > -1):
        tupla = (x, y - 1)
        fedor.append(tupla)
        _fedor.append(tupla[1] * 4 + tupla[0])

    # gerando a posição ouro
    while True:
        _ouro = choices(quadrado, None, k=1)
        if (_pocos.count(_ouro[0]) == 0 and wumpus != _ouro[0]):
            ouro = _ouro.pop()
            break

    ambiente = {
        'Poço': _pocos,
        'Brisa': _brisa,
        'Wumpus': wumpus,
        'Fedor': _fedor,
        'Ouro': ouro
    }

    return ambiente


def infere_aux(percepcoes, posicao):
    coord_pos = get_coord(posicao)

    if (coord_pos[0] - 1 > -1):
        nova_pos = coord_pos[1] * 4 + (coord_pos[0] - 1)
        if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Brisa'] == False):
            percepcoes[posicao]['Poço'] = False
            print('Não tem um poço em', posicao)
        if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Fedor'] == False):
            percepcoes[posicao]['Poço'] = False
            print('Não Wumpus em', posicao)
    if (coord_pos[0] + 1 < 5):
        nova_pos = coord_pos[1] * 4 + (coord_pos[0] + 1)
        if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Brisa'] == False):
            percepcoes[posicao]['Poço'] = False
            print('Não tem um poço em', posicao)
        if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Fedor'] == False):
            percepcoes[posicao]['Poço'] = False
            print('Não Wumpus em', posicao)
    if (coord_pos[1] - 1 > -1):
        nova_pos = (coord_pos[1] - 1) * 4 + coord_pos[0]
        if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Brisa'] == False):
            percepcoes[posicao]['Poço'] = False
            print('Não tem um poço em', posicao)
        if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Fedor'] == False):
            percepcoes[posicao]['Poço'] = False
            print('Não Wumpus em', posicao)
    if (coord_pos[1] + 1 < 5):
        nova_pos = (coord_pos[1] + 1) * 4 + coord_pos[0]
        if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Brisa'] == False):
            percepcoes[posicao]['Poço'] = False
            print('Não tem um poço em', posicao)
        if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Fedor'] == False):
            percepcoes[posicao]['Poço'] = False
            print('Não Wumpus em', posicao)
    return percepcoes


def infere_conhecimento(ambiente, percepcoes, posicao, probalidade=[]):
    coord_pos = get_coord(posicao)

    if (ambiente['Brisa'].count(posicao) or ambiente['Fedor'].count(posicao)):
        if (coord_pos[0] - 1 > -1):
            nova_pos = coord_pos[1] * 4 + (coord_pos[0] - 1)
            if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Poço'] == None):
                percepcoes[nova_pos]['Poço'] = 'Talvez'
                print('Talvez poço em', nova_pos)
                probalidade[0] /= 4
                percepcoes = infere_aux(percepcoes, nova_pos)

            if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Wumpus'] == None):
                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                probalidade[0] /= 4
                print('Talvez Wumpus em', nova_pos)
                percepcoes = infere_aux(percepcoes, nova_pos)
        if (coord_pos[0] + 1 < 5):
            nova_pos = coord_pos[1] * 4 + (coord_pos[0] + 1)
            if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Poço'] == None):
                percepcoes[nova_pos]['Poço'] = 'Talvez'
                print('Talvez poço em', nova_pos)
                probalidade[1] /= 4
                percepcoes = infere_aux(percepcoes, nova_pos)

            if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Wumpus'] == None):
                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                probalidade[1] /= 4
                print('Talvez Wumpus em', nova_pos)
                percepcoes = infere_aux(percepcoes, nova_pos)
        if (coord_pos[1] - 1 > -1):
            nova_pos = (coord_pos[1] - 1) * 4 + coord_pos[0]
            if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Poço'] == None):
                percepcoes[nova_pos]['Poço'] = 'Talvez'
                print('Talvez tenha poço em', nova_pos)
                probalidade[2] /= 4
                percepcoes = infere_aux(percepcoes, nova_pos)

            if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Wumpus'] == None):
                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                probalidade[2] /= 4
                print('Talvez Wumpus em', nova_pos)
                percepcoes = infere_aux(percepcoes, nova_pos)
        if (coord_pos[1] + 1 < 5):
            nova_pos = (coord_pos[1] + 1) * 4 + coord_pos[0]
            if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Poço'] == None):
                percepcoes[nova_pos]['Poço'] = 'Talvez'
                print('Talvez tenha poço em', nova_pos)
                probalidade[3] /= 4
                percepcoes = infere_aux(percepcoes, nova_pos)

            if (nova_pos < 16 and nova_pos > -1 and percepcoes[nova_pos]['Wumpus'] == None):
                percepcoes[nova_pos]['Wumpus'] = 'Talvez'
                probalidade[3] /= 4
                print('Talvez Wumpus em', nova_pos)
                percepcoes = infere_aux(percepcoes, nova_pos)

    return percepcoes, probalidade


def percepcao_ambiente(ambiente, percepcoes, posicao):
    # Se em uma determinada posição houver Fedor, não existe Wumpus nela.
    # A mesma coisa para Brisa/Poço
    cima = direita = 100
    baixo = esquerda = 50
    prob = [esquerda, direita, cima, baixo]
    ouro = False
    buraco = False
    wumpus = False
    if (ambiente['Fedor'].count(posicao) != 0):
        print('Contém fedor na posição ', posicao)
        percepcoes[posicao]['Wumpus'] = False
        percepcoes, prob = infere_conhecimento(ambiente, percepcoes, posicao, prob)
    else:
        percepcoes[posicao]['Fedor'] = False
        percepcoes[posicao]['Wumpus'] = False

    if (ambiente['Brisa'].count(posicao) != 0):
        print('Contém Brisa na posição ', posicao)
        percepcoes[posicao]['Poço'] = False
        percepcoes, prob = infere_conhecimento(ambiente, percepcoes, posicao, prob)
    else:
        percepcoes[posicao]['Poço'] = False
        percepcoes[posicao]['Brisa'] = False

    if (ambiente['Ouro'] == posicao):
        print('O personagem achou o Ouro')
        percepcoes[posicao]['Ouro'] = True
        ouro = True
    else:
        percepcoes[posicao]['Ouro'] = False

    if (ambiente['Poço'].count(posicao) != 0):
        print('O personagem caiu num poço')
        buraco = True

    if (ambiente['Wumpus'] == posicao):
        print('O personagem foi devorado pelo Wumpus')
        wumpus = True

    return percepcoes, ouro, buraco, wumpus, prob


def coord_do_movimento(movimento):
    tupla = (0, 0)
    if (movimento == 'direita'):
        # direita  = 1
        tupla = tuple((1, 0))
    elif (movimento == 'esquerda'):
        # esquerda = -1
        tupla = tuple((-1, 0))
    elif (movimento == 'cima'):
        # cima     = 4
        tupla = tuple((0, 1))
    elif (movimento == 'baixo'):
        # baixo    = -4
        tupla = tuple((0, -1))
    return tupla


def get_coord(movimento):
    x = movimento % 4
    y = movimento // 4
    return tuple((x, y))


def prox_posicao(tu_posicao_atual, tu_movimento):
    x = tu_posicao_atual[0] + tu_movimento[0]
    y = tu_posicao_atual[1] + tu_movimento[1]
    return (4 * y + x)


def mov_valido(direcao, posicao, percep):
    # pegando as coordenadas da posição
    coord_pos = get_coord(posicao)

    # movimento 'm' é a soma das coordenadas da 'direcao' mais as coordenadas da posição 'coord_pos'
    m = tuple((coord_pos[0] + direcao[0], coord_pos[1] + direcao[1]))
    pos_m = m[1] * 4 + m[0]
    print('Próxima posição', pos_m)

    # se o movimento 'm' estiver no intervalo do campo e não possuir Poço ou Wumpus naquela posição é válido
    if ((m[0] < 4 and m[0] > -1) and
            (m[1] < 4 and m[1] > -1) and
            (percep[pos_m]['Poço'] == False or percep[pos_m]['Poço'] == None) and
            (percep[pos_m]['Wumpus'] != True)):
        return True
    return False


def string_direcao(movimento):
    string = ''
    if (movimento == 'esquerda'):
        string = 'esquerda'
    elif (movimento == 'direita'):
        string = 'direita'
    elif (movimento == 'cima'):
        string = 'cima'
    elif (movimento == 'baixo'):
        string = 'baixo'

    return string


def jogo(ambiente):
    # O personagem começa na posição '0'
    posicao_atual = 0
    ouro = False
    buraco = False
    wumpus = False
    probabilidade = []

    # movimentos possíveis
    movimentos = ['esquerda', 'direita', 'cima', 'baixo']

    # Persepção inicial do personagem. Começa tudo como desconhecido (None)
    perc_do_ambiente = {
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
        15: {'Poço': None, 'Brisa': None, 'Wumpus': None, 'Fedor': None, 'Ouro': None},
    }

    # O loop para quando achar um ouro, cair num poço ou encontrar com o Wumpus
    while (ouro != True and wumpus != True and buraco != True):
        print('Posição atual:', posicao_atual)

        # Verificando posição atual se existe algum problema
        perc_do_ambiente, ouro, buraco, wumpus, probabilidade = percepcao_ambiente(ambiente, perc_do_ambiente,
                                                                                   posicao_atual)
        print(probabilidade)
        # Escolhe aleatoriamente um movimento todos com probabilidades iguais
        mov = choices(movimentos, weights=probabilidade, cum_weights=None, k=1)
        print(mov)
        prox_movimento = mov.pop()

        # tupla com as coordenadas do movimento escolhido
        tu_prox_mov = coord_do_movimento(prox_movimento)

        # Verifica se o movimento é possível
        if (mov_valido(tu_prox_mov, posicao_atual, perc_do_ambiente) == True):
            print('Indo para', prox_movimento, 'da posição', posicao_atual, '\n')
            posicao_atual = prox_posicao(get_coord(posicao_atual), tu_prox_mov)
        else:
            print('Não é possível ir para', prox_movimento, 'a partir da posição', posicao_atual, end='\n\n')

    # imprimindo informações do ambiente
    print('\nINFORMAÇÕES DO AMBIENTE:')
    for i, j in ambiente.items():
        print(i, j)
    print('\nINFORMAÇÕES DA PERCEPÇÃO DO AGENTE:')
    # imprimindo perCepções
    for i, j in perc_do_ambiente.items():
        print('Posição {:>2}'.format(i))
        for k, l in j.items():
            print('{}: {} '.format(k.upper(), l), end=' ')
        print()

