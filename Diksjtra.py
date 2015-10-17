from Leitor import Leitor
import random
import sys
import time

class Diksjtra:

	def completarSolucao(self, s, d, qt_vertice, pai, distancia):
		while not (len(s) == qt_vertice):
			
			nao_alocados = []
			for vt in range(qt_vertice):
				if not vt in s:
					nao_alocados.append(vt)

			menor_alelo = -1
			menor_custo = sys.maxint 
			for n in nao_alocados:
				if not (pai[n] in nao_alocados):
					pos_pai = s.index(pai[n])
					if(pos_pai == len(s)-1):
						s.append(n)
					else:
						s.insert(pos_pai+1, n)


	def Diksjtra(self, arquivo= "eil101.tsp", ini = 0):
		custo_solucao = 0
		s = []
		l = Leitor (arquivo)
		d = l.lerMatriz()
		qt_vertice = len(d)
		alelos = range(qt_vertice)

		pai = []
		distancia = []

		for i in range(qt_vertice):
			pai.append(-1)
			distancia.append(sys.maxint)

		#u = int(alelos[random.randint(0, qt_vertice)])
		u = ini
		expandido = []

		inicio = u
		ultimo = -1
		
		pai[inicio] = 0
		distancia[u] = 0
		alelos.remove(u)# tira o inicio da solucao para nao dar ciclos antes de percorret todos 
		

		while not u == -1:
			menor_alelo = -1
			menor_custo = sys.maxint
			
			for al in alelos:

				if(distancia[al] > distancia[u] + d[u][al]):
					distancia[al] = distancia[u] + d[u][al]
					pai[al] = u

			expandido.append(u)
			#atualizou todas as distancias

			#agora vai procurar a menor distancia para expandir
			menor_alelo = -1
			menor_custo = sys.maxint
			for possivel in alelos:
				if possivel in expandido:
					continue
				if(menor_alelo == -1):
					menor_alelo = al
					menor_custo = distancia[u] + d[u][al]
					continue
				elif  (distancia[u] + d[u][al]) < menor_custo:
					menor_alelo = al
					menor_custo = (distancia[u] + d[u][al])

			#ao fim desse for tem um novo vertice a ser visitado
			u = menor_alelo
			if not (u == -1):
				ultimo = menor_alelo
				alelos.remove(menor_alelo)
		

		print pai
		print distancia
		
		custo_solucao = distancia[ultimo] + d[ultimo][inicio]
		while ultimo != inicio:
			s.insert(0, ultimo)
			ultimo = pai[ultimo]
		s.insert(0, ultimo)

		self.completarSolucao(s, d, qt_vertice, pai, distancia)
		custo_solucao = 0
		for i in range(len(s)-1):
			custo_solucao = custo_solucao + d[s[i]][s[i+1]]

		custo_solucao = custo_solucao + d[s[0]][s[-1]]

		print ""
		print s
		print custo_solucao
		
		return custo_solucao

dis = Diksjtra()
#for i in range(10):
dis.Diksjtra()

ini = time.time()
dis = Diksjtra()
#for i in range(10):
dis.Diksjtra()

fim = time.time()
total = fim - ini
print total


