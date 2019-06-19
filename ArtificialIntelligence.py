import random, time
import movimentos as Mov

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

def TELL_aux(percepcoes, posicao):
	# Inferindo conhecimento na BC sobre as informações das posições adjacentes
	wumpus_cont = poco_cont = 0
	xy_pos = Mov.get_coord(posicao)
	#print('Posição =', posicao, 'coordenadas = ', xy_pos)
	x = posicao%4
	y = posicao//4

	# Direita da posição
	if(x+1 <= 3):
		nova_pos = 4*y + (x+1)
		if(nova_pos >= 0 and nova_pos <= 15):
			#print('AUX::> Direita da pos',posicao,'=', nova_pos, ' coordenadas:',  Mov.get_coord(nova_pos))
			if(percepcoes[posicao]['Poço'] == True and percepcoes[nova_pos]['Brisa'] == False):
				percepcoes[posicao]['Poço'] = False
			elif(percepcoes[posicao]['Poço'] == True and percepcoes[nova_pos]['Brisa'] == True):
				poco_cont += 1
			if(percepcoes[posicao]['Wumpus'] == True and percepcoes[nova_pos]['Fedor'] == False):
				percepcoes[posicao]['Wumpus'] = False
			elif(percepcoes[posicao]['Wumpus'] == True and percepcoes[nova_pos]['Fedor'] == True):
				wumpus_cont += 1
	# Esquerda da posição
	if(x-1 >= 0):
		nova_pos = 4*y + (x-1)
		if(nova_pos >= 0 and nova_pos <= 15):
			#print('AUX::> Esquerda da pos',posicao,'=', nova_pos, ' coordenadas:',  Mov.get_coord(nova_pos))
			if(percepcoes[posicao]['Poço'] == True and percepcoes[nova_pos]['Brisa'] == False):
				percepcoes[posicao]['Poço'] = False
			elif(percepcoes[posicao]['Poço'] == True and percepcoes[nova_pos]['Brisa'] == True):
				poco_cont += 1
			if(percepcoes[posicao]['Wumpus'] == True and percepcoes[nova_pos]['Fedor'] == False):
				percepcoes[posicao]['Wumpus'] = False
			elif(percepcoes[posicao]['Wumpus'] == True and percepcoes[nova_pos]['Fedor'] == True):
				wumpus_cont += 1
	# Abaixo da posição
	if(y+1 <= 3):
		nova_pos = 4*(y+1) + x
		if(nova_pos >= 0 and nova_pos <= 15):
			#print('AUX::> Abaixo da pos',posicao,'=', nova_pos, ' coordenadas:',  Mov.get_coord(nova_pos))
			if(percepcoes[posicao]['Poço'] == True and percepcoes[nova_pos]['Brisa'] == False):
				percepcoes[posicao]['Poço'] = False
			elif(percepcoes[posicao]['Poço'] == True and percepcoes[nova_pos]['Brisa'] == True):
				poco_cont += 1
			if(percepcoes[posicao]['Wumpus'] == True and percepcoes[nova_pos]['Fedor'] == False):
				percepcoes[posicao]['Wumpus'] = False
			elif(percepcoes[posicao]['Wumpus'] == True and percepcoes[nova_pos]['Fedor'] == True):
				wumpus_cont += 1
	# Acima da posição
	if(y-1 >= 0):
		nova_pos = 4*(y-1) + x
		if(nova_pos >= 0 and nova_pos <= 15):
			#print('AUX::> Acima da pos',posicao,'=', nova_pos, ' coordenadas:',  Mov.get_coord(nova_pos))
			if(percepcoes[posicao]['Poço'] == True and percepcoes[nova_pos]['Brisa'] == False):
				percepcoes[posicao]['Poço'] = False
			elif(percepcoes[posicao]['Poço'] == True and percepcoes[nova_pos]['Brisa'] == True):
				poco_cont += 1
			if(percepcoes[posicao]['Wumpus'] == True and percepcoes[nova_pos]['Fedor'] == False):
				percepcoes[posicao]['Wumpus'] = False
			elif(percepcoes[posicao]['Wumpus'] == True and percepcoes[nova_pos]['Fedor'] == True):
				wumpus_cont += 1
        
	return percepcoes, wumpus_cont, poco_cont

def TELL(ambiente, percepcoes, posicao, arrow):
	# Inferindo conhecimento na BC sobre as informações de cada posição
	wumpus_cont = poco_cont = 0
	x = posicao%4
	y = posicao//4
	
	# Direita da posição
	if(x+1 <= 3):
		nova_pos = 4*y + (x+1)
		if(0 <= nova_pos % 4 <= 3):
			if(percepcoes[posicao]['Brisa'] == False):
					percepcoes[nova_pos]['Poço'] = False
			
			elif(percepcoes[posicao]['Brisa'] == True):
					percepcoes[nova_pos]['Poço'] = True

			if(percepcoes[posicao]['Fedor'] == False):
					percepcoes[nova_pos]['Wumpus'] = False
					
			elif(percepcoes[posicao]['Fedor'] == True):
					if(percepcoes[nova_pos]['Wumpus']):
						for i in range(16, 0):
							percepcoes[i]['Wumpus'] = False
							percepcoes[i]['Fedor'] = False
					percepcoes[nova_pos]['Wumpus'] = True

			percepcoes, wumpus_cont, poco_cont = TELL_aux(percepcoes, nova_pos)

	# Esquerda da posição
	if(x-1 >= 0):
		nova_pos = 4*y + (x-1)
		if(0 <= nova_pos % 4 <= 3):
			if(percepcoes[posicao]['Brisa'] == False):
					percepcoes[nova_pos]['Poço'] = False
			
			elif(percepcoes[posicao]['Brisa'] == True):
					percepcoes[nova_pos]['Poço'] = True

			if(percepcoes[posicao]['Fedor'] == False):
					percepcoes[nova_pos]['Wumpus'] = False
					
			elif(percepcoes[posicao]['Fedor'] == True):
					percepcoes[nova_pos]['Wumpus'] = True
			percepcoes, wumpus_cont, poco_cont = TELL_aux(percepcoes, nova_pos)

	# Abaixo da posição
	if(y+1 <= 3):
		nova_pos = 4*(y+1) + x
		if(nova_pos >= 0 and nova_pos <= 15):
			if(percepcoes[posicao]['Brisa'] == False):
					percepcoes[nova_pos]['Poço'] = False
			
			elif(percepcoes[posicao]['Brisa'] == True):
					percepcoes[nova_pos]['Poço'] = True

			if(percepcoes[posicao]['Fedor'] == False):
					percepcoes[nova_pos]['Wumpus'] = False
					
			elif(percepcoes[posicao]['Fedor'] == True):
					percepcoes[nova_pos]['Wumpus'] = True
			percepcoes, wumpus_cont, poco_cont = TELL_aux(percepcoes, nova_pos)

	# Acima da posição
	if(y-1 >= 0):
		nova_pos = 4*(y-1) + x
		if(nova_pos >= 0 and nova_pos <= 15):
			if(percepcoes[posicao]['Brisa'] == False):
					percepcoes[nova_pos]['Poço'] = False
			
			elif(percepcoes[posicao]['Brisa'] == True):
					percepcoes[nova_pos]['Poço'] = True

			if(percepcoes[posicao]['Fedor'] == False):
					percepcoes[nova_pos]['Wumpus'] = False
					
			elif(percepcoes[posicao]['Fedor'] == True):
					percepcoes[nova_pos]['Wumpus'] = True
			percepcoes, wumpus_cont, poco_cont = TELL_aux(percepcoes, nova_pos)
	
	return percepcoes

def TELL_aux2(percepcoes, posicao):
	pos = posicao - 1
	if(pos >= 0 and pos <= 15):
		if(percepcoes[posicao]['Brisa'] == False):
			percepcoes[pos]['Poço'] = False
		if(percepcoes[posicao]['Fedor'] == False):
			percepcoes[pos]['Wumpus'] = False
	pos = posicao - 4
	if(pos >= 0 and pos <= 15):
		if(percepcoes[posicao]['Brisa'] == False):
			percepcoes[pos]['Poço'] = False
		if(percepcoes[posicao]['Fedor'] == False):
			percepcoes[pos]['Wumpus'] = False
	pos = posicao + 1
	if(pos >= 0 and pos <= 15):
		if(percepcoes[posicao]['Brisa'] == False):
			percepcoes[pos]['Poço'] = False
		if(percepcoes[posicao]['Fedor'] == False):
			percepcoes[pos]['Wumpus'] = False
	pos = posicao + 4
	if(pos >= 0 and pos <= 15):
		if(percepcoes[posicao]['Brisa'] == False):
			percepcoes[pos]['Poço'] = False
		if(percepcoes[posicao]['Fedor'] == False):
			percepcoes[pos]['Wumpus'] = False

	return percepcoes

def ASK(ambiente, percepcoes, posicao):
	# Consultando a base de conhecimento sobre as informações
	#a cerca do ambiente
	arrow = False
	
	if(ambiente[posicao]['Fedor'] == True):
		percepcoes[posicao]['Fedor'] = True
		percepcoes[posicao]['Wumpus'] = False
	else:
		percepcoes[posicao]['Fedor'] = False
		percepcoes[posicao]['Wumpus'] = False

	if(ambiente[posicao]['Brisa'] == True):
		percepcoes[posicao]['Brisa'] = True
		percepcoes[posicao]['Poço'] = False
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

	percepcoes = TELL(ambiente, percepcoes, posicao, arrow)
	
	return percepcoes, arrow

def end_game(percepcoes, posicao):
	if(percepcoes[posicao]['Ouro'] == True):
		print('O personagem encontrou o Ouro!')
	elif(percepcoes[posicao]['Wumpus'] == True):
		print('O personagem foi devorado pelo Wumpus.')
	elif(percepcoes[posicao]['Poço'] == True):
		print('O personagem caiu no poço!')

def show_info(ambiente, percepcoes):
	print('\nINFORMAÇÕES DO AMBIENTE:')
	for i,j in ambiente.items():
		print(i, j)
	print('\nINFORMAÇÕES DA PERCEPÇÃO DO AGENTE:')
	# imprimindo perCepções
	for i, j in percepcoes.items():
		print('Posição {:>2}'.format(i))
		for k, l in j.items():
			print('{}: {} '.format(k.upper(), l), end=' ')
		print()

def print_ambiente(ambiente):
	print('----------------PERCEPÇÕES DO AMBIENTE------------------')
	print('Posição |  Poço   |  Brisa  | Wumpus  |  Fedor  |  Ouro')
	print('--------------------------------------------------------')
	for pos, pos_dict in ambiente.items():
		print('{:^8}'.format(pos), end='')
		for att, value in pos_dict.items():
			if(value == None):
				print('|  None  ',end=' ')
			elif(value == True):
				print('|  True  ',end=' ')
			elif(value == False):
				print('|  False ',end=' ')
			elif(value == 'Talvez'):
				print('| Talvez ',end=' ')
		print()

def atirar(ambiente, percepcoes):
	# Essa função só é chamada quando o Wumpus é supostamente encontrado
        pos = None
        hit = False
        for i in range(0, 16):
                if(percepcoes[i]['Wumpus'] == True):
                        pos = i
        if(ambiente[pos]['Wumpus'] == True):
                hit = True
                ambiente[pos]['Wumpus'] = False
                percepcoes[pos]['Wumpus'] = False
                for i in range(0, 16):
                        ambiente[i]['Fedor'] = False
                        percepcoes[i]['Fedor'] = False
        return pos, hit

def jogo(posicao_atual, ambiente, percepcoes, caminho):
	ouro = False
	buraco = False
	wumpus = False

	if caminho.count(posicao_atual) == 0:
		caminho.append(posicao_atual)
	print('\nposições percorridas', caminho)

	# Verificando posição atual se existe algum problema
	percepcoes, arrow = ASK(ambiente, percepcoes, posicao_atual)
	if(percepcoes[posicao_atual]['Wumpus'] == True):
		wumpus = True
	elif(percepcoes[posicao_atual]['Poço'] == True):
		buraco = True
	elif(percepcoes[posicao_atual]['Ouro'] == True):
		ouro = True
	else:
		# Escolhe aleatoriamente um movimento todos com probabilidades iguais
		posicao_atual = Mov.escolhe_movimento(percepcoes, posicao_atual, caminho)

		# tupla com as coordenadas do movimento escolhido
		

		# Verifica se o movimento é possível
		#validade = Mov.mov_valido(coord_porx_mov, posicao_atual, percepcoes)
		#posicao_atual += movimento

	return posicao_atual, ouro, buraco, wumpus, arrow, caminho

def jogoUser(posicao_atual, ambiente, percepcoes):
	ouro = False
	buraco = False
	wumpus = False

	# Verificando posição atual se existe algum problema
	percepcoes, arrow = ASK(ambiente, percepcoes, posicao_atual)

	if(percepcoes[posicao_atual]['Wumpus'] == True):
		wumpus = True
	if(percepcoes[posicao_atual]['Poço'] == True):
		buraco = True
	if(percepcoes[posicao_atual]['Ouro'] == True):
		ouro = True

	if(ouro == True or buraco == True or wumpus == True):
		validade = False
	return posicao_atual, ouro, buraco, wumpus, arrow