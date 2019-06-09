import random

def gerar_ambiente():
    '''BRISA, FEDOR, OURO, BURACO, WUMPOS'''

    tabuleiro = {
        0: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        1: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        2: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        3: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        4: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        5: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        6: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        7: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        8: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        9: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        10: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        11: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        12: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        13: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        14: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
        15: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False},
    }

    '''FUNÇÃO QUE ADICIONA OS POÇOS AO TABULEIRO'''
    for i in range(0, 3):
        loop = True
        while loop:
            x = random.randrange(0, 3)
            y = random.randrange(0, 3)
            pos = (4 * y) + x

            if pos > 0 and tabuleiro[pos]['Poço'] == False:
                tabuleiro[pos]['Poço'] = True

                if pos + 1 < 16:
                    tabuleiro[pos + 1]['Brisa'] = True
                if pos + 4 < 16:
                    tabuleiro[pos + 4]['Brisa'] = True
                if pos - 1 >= 0:
                    tabuleiro[pos - 1]['Brisa'] = True
                if pos - 4 >= 0:
                    tabuleiro[pos - 4]['Brisa'] = True
                loop = False

    '''FUNÇÃO QUE ADICIONA O WUMPUS AO TABULEIRO'''
    loop = True
    while loop:
        x = random.randrange(0, 4)
        y = random.randrange(0, 4)
        pos = (4 * y) + x

        if tabuleiro[x]['Poço'] == False and pos > 0:
            tabuleiro[pos]['Wumpos'] = True
            if (pos + 1) < 16:
                tabuleiro[pos + 1]['Fedor'] = True
            if (pos - 1) >= 0:
                tabuleiro[pos - 1]['Fedor'] = True
            if (pos + 4) < 16:
                tabuleiro[pos + 4]['Fedor'] = True
            if (pos - 4) >= 0:
                tabuleiro[pos - 4]['Fedor'] = True
            loop = False

    '''FUNÇÃO QUE ADICIONA O OURO AO TABULEIRO'''
    loop = True
    while loop:
        x = random.randrange(0, 15, 1)
        if tabuleiro[x]['Wumpos'] == False and (tabuleiro[x]['Poço'] == False and x != 0):
            tabuleiro[x]['Ouro'] = True
            loop = False

    return tabuleiro
