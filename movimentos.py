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

def escolhe_movimento(percepcoes, posicao):
	movimentos = [1, 4, -1, -4] # direita, baixo, esquerda, cima
	mov_escolhido = False
	mov = 0
	validade = 0
	prox_pos = posicao

	caminho = open(os.path.join('Arquivos', 'caminho.txt'), 'a')
	leituraCaminho = open(os.path.join('Arquivos', 'caminho.txt'), 'r')
	listaCaminho = leituraCaminho.readlines()
	print(listaCaminho)
	mov_possiveis = []

	#verificando as posições adjacentes
	if(0 <= posicao + 1 <= 15):
		if((percepcoes[posicao+1]['Poço'] == False or None) and (percepcoes[posicao+1]['Wumpus'] == False or None) 
		and (not (posicao + 1) in listaCaminho)):
			mov_possiveis.append(1)
	
	if(0 <= posicao - 1 <= 15):
		if((percepcoes[posicao-1]['Poço'] == False or None) and (percepcoes[posicao-1]['Wumpus'] == False or None) 
		and (not (posicao - 1) in listaCaminho)):
			mov_possiveis.append(-1)

	if(0 <= posicao + 4 <= 15):
		if((percepcoes[posicao+4]['Poço'] == False or None) and (percepcoes[posicao+4]['Wumpus'] == False or None) 
		and (not (posicao + 4) in listaCaminho)):
			mov_possiveis.append(4)

	if(0 <= posicao - 4 <= 15):
		if((percepcoes[posicao-4]['Poço'] == False or None) and (percepcoes[posicao-4]['Wumpus'] == False or None) 
		and (not (posicao - 4) in listaCaminho)):
			mov_possiveis.append(-4)
		
	'''if(len(mov_possiveis) == 0):
		mov = random.choice(movimentos)
		caminho.write(str(posicao + mov) +'\n')
	else:'''
		
	mov = random.choice(mov_possiveis)
	teste = posicao + mov
	if not(str(teste) + '\n' in listaCaminho):
		caminho.write(str(posicao + mov) + '\n')
		caminho.write(str(0) + '\n')
		print('ha!')
		caminho.close()
		return mov
	
	caminho.write(str(posicao) + '\n')
	caminho.write(str(0) + '\n')
	caminho.close()
	return posicao
	
	
	