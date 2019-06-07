import random

def gerar_ambiente():
    '''BRISA, FEDOR, OURO, BURACO, WUMPOS'''

    tabuleiro = {
        0: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': 'Nada'},
        1: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        2: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        3: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        4: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        5: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        6: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        7: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        8: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        9: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        10: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        11: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        12: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        13: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        14: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
        15: {'Poço': False, 'Brisa': False, 'Wumpos': False, 'Fedor': False, 'Ouro': False, 'Estado': "Nada"},
    }

    for i in range(0, 3, +1):
        pos = 0
        while pos == 0:
            x = random.randrange(0, 4, 1)
            y = random.randrange(0, 4, 1)
            pos = 4 * y + x
            tabuleiro[pos]['Poço'] = True

        if x + 1 < 4:
            tabuleiro[pos + 1]['Brisa'] = True
        if pos + 4 < 16:
            tabuleiro[pos + 4]['Brisa'] = True
        if x - 1 >= 0:
            tabuleiro[pos - 1]['Brisa'] = True
        if (pos - 4) >= 0:
            tabuleiro[pos - 4]['Brisa'] = True

    loop = True
    while loop:
        x = random.randrange(0, 4, 1)
        y = random.randrange(0, 4, 1)
        pos = 4 * y + x

        if tabuleiro[x]['Poço'] == False and tabuleiro[x]['Ouro'] == False and pos != 0:
            tabuleiro[x]['Wumpos'] = True
            if (x + 1) < 16:
                tabuleiro[x + 1]['Fedor'] = True
            if (x - 1) >= 0:
                tabuleiro[x - 1]['Fedor'] = True
            if (x + 4) < 16:
                tabuleiro[x + 4]['Fedor'] = True
            if (x - 4) >= 0:
                tabuleiro[x - 4]['Fedor'] = True
            loop = False

    loop = True
    while loop:
        x = random.randrange(0, 15, 1)
        if (tabuleiro[x]['Wumpos'] == False) and (tabuleiro[x]['Poço'] == False and x != 0):
            tabuleiro[x]['Ouro'] = True
            loop = False

    return tabuleiro
