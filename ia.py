import ArtificialIntelligence as Ia

passos = [1, -1, 4, -4]

percepcoes = {
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

def atribuicaoVolta(percepcoes, pos, termo, estado):
    if(0 <= (pos % 4) + 1 < 4):
        percepcoes[pos + 1][termo] = estado
        print(percepcoes[pos + 1][termo])
    if(0 <= (pos % 4) - 1 < 4):
        percepcoes[pos - 1][termo] = estado 
        print('tiro2')
    if(0 <= (pos + 4) // 4 < 4):
        percepcoes[pos + 4][termo] = estado 
        print('tiro3')
    if(0 <= (pos - 4) // 4 < 4):
        percepcoes[pos - 4][termo] = estado 
        print('tiro4') 

def IA(ambiente, persepcoes):
    newPos = 0
    posPerson = 1
    while(newPos != posPerson):
        posPerson = newPos
        if(ambiente[posPerson]['Brisa'] == (False or None)):
            atribuicaoVolta(persepcoes, posPerson, 'Poço', False)
        else:
            atribuicaoVolta(percepcoes, posPerson, 'Poço', 'Talvez')

        if(ambiente[posPerson]['Fedor'] == (False or None)):
            atribuicaoVolta(persepcoes, posPerson, 'Wumpus', False)
        else: 
            atribuicaoVolta(persepcoes, posPerson, 'Wumpus', 'Talvez')
        
        newPos = escolhePasso(persepcoes, posPerson)
        print(newPos, posPerson)
        print(percepcoes)

def escolhePasso(persepcoes, pos):
    for i in passos:
        if(0 <= pos + i < 16):
            if(persepcoes[pos + i]['Wumpus'] == False and persepcoes[pos + i]['Poço'] == False):
                return pos + i
    return pos
        
def main():
    ambiente = Ia.gera_ambiente()
    IA(ambiente, percepcoes)
    print(ambiente)

if __name__ == "__main__":
    main()