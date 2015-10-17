from Leitor import Leitor
import random
import sys
import time


class Guloso:

	def guloso(self, arquivo = "eil101.tsp", ini = 0):
		custo_solucao = 0
		s = []
		l = Leitor (arquivo)
		d = l.lerMatriz()
		qt_vertice = len(d)
		alelos = range(qt_vertice)

		#s.append( alelos[random.randint(0, qt_vertice)] )
		s.append(ini)
		alelos.remove(s[0])


		for i in range (1, qt_vertice):
			ant = s[i-1]
			menor_custo =  sys.maxint
			melhor_alelo = -1
			for al in alelos:
				custo_al = d[ant][al]
				if custo_al < menor_custo:
					menor_custo = custo_al
					melhor_alelo = al

			if 	melhor_alelo == -1:
				break
			else:
				alelos.remove(melhor_alelo)
				s.append(melhor_alelo)
				custo_solucao = menor_custo + custo_solucao
		
		custo_solucao = custo_solucao + d[ s[len(s)-1] ][ s[0] ] 
		
		print ""
		print s
		print custo_solucao

		return custo_solucao

ini = time.time()
g = Guloso()
g.guloso()
fim = time.time()
total = fim - ini
print total
