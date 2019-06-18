import random, time

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

def escolhe_movimento(percepcoes, posicao):
	lista_movimentos = [1, 4, -1, -4] # direita, baixo, esquerda, cima
	mov_escolhido = False
	mov = 0
	validade = 0
	prox_pos = posicao
	while mov_escolhido == False:
		mov = random.choice(lista_movimentos)
		prox_pos = posicao + mov
		if(prox_pos <= 15 and prox_pos >= 0):
			if(percepcoes[prox_pos]['Poço'] != True):
				mov_escolhido = True
	return mov