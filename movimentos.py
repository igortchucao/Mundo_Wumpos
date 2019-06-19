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

def adjacentes(posicao, percepcoes):
	# retorna uma lista com os vértices adjacentes daquela posição
	lista_adj = []
	x = posicao % 4
	y = posicao // 4

	if(x+1 <= 3):
		nova_pos = 4*y + (x+1)
		lista_adj.append(nova_pos)
	if(x-1 >= 0):
		nova_pos = 4*y + (x-1)
		lista_adj.append(nova_pos)
	if(y+1 <= 3):
		nova_pos = 4*(y+1) + x
		lista_adj.append(nova_pos)
	if(y-1 >= 0):
		nova_pos = 4*(y-1) + x
		lista_adj.append(nova_pos)
	
	return lista_adj

def posicao_segura(percepcoes, posicao):
	val1 = percepcoes[posicao]['Wumpus']
	val2 = percepcoes[posicao]['Poço']

	if (val1 == None or val1 == False) and (val2 == None or val2 == False):
		return True
	return False

'''FUNÇÃO QUE VAI ESCOLHER OS PROXIMOS PASSOS DADOS PELO PERSONAGEM'''
def escolhe_movimento(percepcoes, posicao, caminho):
	movimentos = [1, 4, -1, -4] # direita, baixo, esquerda, cima
	mov = 0

	x = posicao % 4
	y = posicao // 4

	mov_possiveis = []
	probabilidade = []

	# verificando as posições adjacentes
	# caso alguma delas apresente caminho livre (false ou none para poço/wumpus) 
	# adicionar o movimento à lista de movimentos possíveis.
	# se a posição não tiver sido percorrida anteriormente, adicionar peso 50 à ela
	# senão, removê-la da lista.

	if(x+1 <= 3):
		nova_pos = 4*y + (x+1)		
		if((percepcoes[nova_pos]['Poço'] == False or None) and (percepcoes[nova_pos]['Wumpus'] == False or None)):
			if caminho.count(nova_pos) == 0:
				mov_possiveis.append(1)
				probabilidade.append(50)
	
	if(x-1 >= 0):
		nova_pos = 4*y + (x-1)
		if((percepcoes[nova_pos]['Poço'] == False or None) and (percepcoes[nova_pos]['Wumpus'] == False or None)):
			if caminho.count(nova_pos) == 0:
				mov_possiveis.append(-1)
				probabilidade.append(25)
		
	if(y+1 <= 3):
		nova_pos = 4*(y+1) + x
		if((percepcoes[nova_pos]['Poço'] == False or None) and (percepcoes[nova_pos]['Wumpus'] == False or None)):
			if caminho.count(nova_pos) == 0:
				mov_possiveis.append(4)
				probabilidade.append(50)

	if(y-1 >= 0):
		nova_pos = 4*(y-1) + x
		if((percepcoes[nova_pos]['Poço'] == False 	or None) and (percepcoes[nova_pos]['Wumpus'] == False or None)):
			if caminho.count(nova_pos) == 0:
				mov_possiveis.append(-4)
				probabilidade.append(25)
		
	# se as posições adjacentes não são certezas (i.e Poço/Wumpus = True ou Talvez)
	# a escolha do movimento terá que ser aleatória

	# Se os movimentos possíveis forem 0, voltar um movimento e buscar
	# a posição não visitada mais próxima
	if(len(mov_possiveis) == 0):
		print('Procurar posição não descoberta mais próxima')
		'''
		escolha uma raiz s de G
		marque s
		insira s em F
		enquanto F não está vazia faça
			seja v o primeiro vértice de F
			para cada w ∈ listaDeAdjacência de v faça
				se w não está marcado então
					visite aresta entre v e w
					marque w
					insira w em F
				senao se w ∈ F entao
					visite aresta entre v e w
				fim se
			fim para
			retira v de F
		fim enquanto
		'''
		marcados = []
		F = []
		s = posicao
		marcados.append(s)
		F.append(s)
		while len(F) != 0:
			v = F[0]
			for w in adjacentes(v, percepcoes):
				# se não estiver marcado
				if marcados.count(w) == 0:
					marcados.append(w)
					F.append(w)
				elif F.count(w):
					pass
			F.pop(0)
		print('posição atual', posicao)
		print('posições percorridas', caminho)
		print('marcados', marcados)
		definido = False
		for m in marcados:
			if(caminho.count(m) == 0 and definido == False):
				definido = True
				prox_pos = m
		print('Posição mais próxima não descoberta', prox_pos)
		mov = 0
		
	# Senão, selecionar um dentre os possíveis
	else:
		mov = random.choices(mov_possiveis, probabilidade).pop()

	return mov

'''
0  1  2  3
4  5  6  7
8  9  10 11
12 13 14 15
'''