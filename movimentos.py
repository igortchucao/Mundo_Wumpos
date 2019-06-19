import random, time, os

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
	x = movimento % 4
	y = movimento // 4
	return tuple((x, y))

def coord_to_pos(tu_posicao_atual, tu_movimento):
	x = tu_posicao_atual[0]+tu_movimento[0]
	y = tu_posicao_atual[1]+tu_movimento[1]
	return (4*y + x)

'''CERTIFICA SE O MOVIMENTO ESCOLHIDO É VALIDO'''
def mov_valido(coord_direcao, posicao, percepcoes):
	# pegando as coordenadas da posição
	coord_pos = get_coord(posicao)
	
	# O movimento é a soma das coordenadas 'coord_direcao' e 'coord_pos'
	coord_nova_pos = tuple((coord_pos[0]+coord_direcao[0], coord_pos[1]+coord_direcao[1]))

	# nova_pos é a coord_mov em forma de posições (0, 15)
	nova_pos =  coord_nova_pos[1]*4 + coord_nova_pos[0]

	# Se a nova posição estiver no intervalo do campo então é válido
	if((0 <= coord_nova_pos[0] < 4) and (0 <= coord_nova_pos[1] < 4)):
		return True
	return False

'''FUNÇÃO QUE VAI ESCOLHER OS PROXIMOS PASSOS DADOS PELO PERSONAGEM'''
def escolhe_movimento(percepcoes, posicao, caminho):
	movimentos = [] # direita, baixo, esquerda, cima
	contPos = 0
	mov = posicao

	mov_possiveis = []
	probabilidade = []

	# verificando as posições adjacentes
	# caso alguma delas apresente caminho livre (false ou none para poço/wumpus) 
	# adicionar o movimento à lista de movimentos possíveis.
	# se a posição não tiver sido percorrida anteriormente, adicionar peso 50 à ela
	# senão, removê-la da lista.
	
	if(0 <= (posicao % 4) + 1 < 4):
		movimentos.append(1)
		if((percepcoes[posicao + 1]['Poço'] == False) and (percepcoes[posicao + 1]['Wumpus'] == False)):
			if caminho.count(posicao + 1) == 0:
				mov_possiveis.append(1)
				probabilidade.append(25)
		if((percepcoes[posicao + 1]['Brisa'] == True) or (percepcoes[posicao + 1]['Fedor'] == True)):
			contPos += 1
	
	if(0 <= (posicao % 4) - 1 < 4):
		movimentos.append(-1)
		if((percepcoes[posicao - 1]['Poço'] == False) and (percepcoes[posicao - 1]['Wumpus'] == False)):
			if caminho.count(posicao - 1) == 0:
				mov_possiveis.append(-1)
				probabilidade.append(25)
		if((percepcoes[posicao - 1]['Brisa'] == True) or (percepcoes[posicao - 1]['Fedor'] == True)):
			contPos += 1

	if(0 <= posicao + 4 <= 15):
		movimentos.append(4)
		if((percepcoes[posicao + 4]['Poço'] == False) and (percepcoes[posicao + 4]['Wumpus'] == False)):
			if caminho.count(posicao + 4) == 0:
				mov_possiveis.append(4)
				probabilidade.append(25)
		if((percepcoes[posicao + 4]['Brisa'] == True) or (percepcoes[posicao + 4]['Fedor'] == True)):
			contPos += 1

	if(0 <= posicao - 4 <= 15):
		movimentos.append(-4)
		if((percepcoes[posicao - 4]['Poço'] == False) and (percepcoes[posicao - 4]['Wumpus'] == False)):
			if caminho.count(posicao - 4) == 0:
				mov_possiveis.append(-4)
				probabilidade.append(25)
		if((percepcoes[posicao - 4]['Brisa'] == True) or (percepcoes[posicao - 4]['Fedor'] == True)):
			contPos += 1
	
	if(percepcoes[mov]['Cor'] == 'Cinza'):
		mov = posicao + random.choice(movimentos)
	# se as posições adjacentes não são certezas (i.e Poço/Wumpus = True ou Talvez) a escolha do movimento terá que ser aleatória
	else:	
		if(len(mov_possiveis) == 0):
			if(percepcoes[mov]['Cor'] == 'Cinza'):
				percepcoes[mov]['Cor'] = 'Preto'

			elif(percepcoes[mov]['Cor'] == None):
				percepcoes[mov]['Cor'] = 'Cinza'
			del caminho[-1]
			mov = caminho[-1]
		else:
			mov = posicao + random.choices(mov_possiveis, probabilidade).pop()

	return mov
