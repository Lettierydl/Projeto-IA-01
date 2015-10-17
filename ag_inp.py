from Leitor import Leitor
import random
import sys
import copy

class Solucao:
	cidades = []
	custo = 0
	alelos = []
	d = {}
	qt_cidades = 0

	def __init__(self, qt_cidades, d):
		self.qt_cidades = qt_cidades
		self.alelos = range(0, qt_cidades)
		self.d = d

	def existe(self, cidade):
		existe = False
		for ci in self.cidades:
			if ci == cidade :
				existe = True			
				break
		return existe

	def addNextCidade(self, cidade):
		if( not self.existe(cidade) ):
			self.cidades.append(cidade)
			self.alelos.remove(cidade)
		if(len(self.alelos) == 0):
			self.recalcularCusto()
	
	def recalcularCusto(self):
		self.custo = 0
		for index in range(len(self.cidades)-1):
			self.custo = self.custo + self.d[self.cidades[index]][self.cidades[index+1]]
		self.custo = self.custo + self.d[self.cidades[0]][self.cidades[-1]]

	def cruzar(self, other, pos_corte = qt_cidades/2 ) :
		p1_ci = self.cidades[0 : pos_corte]
		p2_ci = self.cidades[pos_corte : self.qt_cidades]

		p1_ci2 = other.cidades[0:pos_corte]
		p2_ci2 = other.cidades[pos_corte:other.qt_cidades]

		filho1 = Solucao(self.qt_cidades, self.d)
		filho2 = Solucao(self.qt_cidades, self.d)
		filho3 = Solucao(self.qt_cidades, self.d)
		filho4 = Solucao(self.qt_cidades, self.d)

		filho1.cidades = p1_ci + p1_ci2
		filho2.cidades = p2_ci + p2_ci2
		filho3.cidades = p1_ci + p2_ci2
		filho4.cidades = p2_ci + p1_ci2
		
		filho1.recalcularCusto()
		filho2.recalcularCusto()
		filho3.recalcularCusto()
		filho4.recalcularCusto()

		return [filho1, filho2, filho3, filho4]




	def factivel():
		if not len(cidades) == qt_cidades:
			return False

		qt_iqual = 0
		for c1 in cidades:
			for c2 in cidades:
				if c2 == c1:
					qt_iqual = qt_iqual + 1

		if qt_iqual > 2:
			return False



	def __gt__(self, other):
		return (self.custo > other.custo)

	def __cmp__( self, other ) :
		if self.custo < other.custo :
			rst = -1
		elif self.custo > other.custo :
			rst = 1
		else :
			rst = 0
		return rst

	def multar(self):
		ci1 = random.randint(0, qt_vertice)
		ci2 = random.randint(0, qt_vertice)
		ind1 = self.cidade.index(ci1)
		ind2 = self.cidade.index(ci2)
		self.cidade[ind1] = ci2
		self.cidade[ind2] = ci1
		self.recalcularCusto()

class Algoritmo:
	d = {}

	def algoritmo(self, populacaoInicial = 50, geracoes = 100, arquivo = "eil101.tsp"):
		l = Leitor(arquivo)
		self.d = l.lerMatriz()

		populacao = self.gerarPopulacao(populacaoInicial, len(self.d))
		populacao_anterior = copy.copy(populacao)
		for g in range(geracoes):
			populacao.sort()
			selecionados = selecionar_cruzamento(populacao)
			self.cruzamento(selecionados, populacao)
			selecionados = selecionar_mutacao(populacao)
			for sel in selecionados:
				sel.multar()

			populacao.sort()
			populacao_anterior = copy.copy(populacao)
			populacao = []
			for i in range(populacaoInicial):
				populacao.append(populacao_anterior[i])
		
		print populacao[0].cidades
		print populacao[0].custo



	def cruzamento(self, selecionados, populacao):
		for sel in range(len(selecionados)-1):
			filhos = selecionados[sel].cruzar(selecionados[sel+1])
			for fi in filhos:
				if(fi.factivel()):
					populacao.append(fi)




	def gerarPopulacao(self, qt_individuos, qt_cidades):
		populacao = []
		for i in range(qt_individuos):
			populacao.append(self.gerarSolucaoAleatoriamente(qt_cidades, self.d))


	def gerarSolucaoAleatoriamente(self, qt_cidades, d ):
		s = Solucao(qt_cidades, d)
		for i in range(qt_cidades):
			cid = int(s.alelos[random.randint(0, len(s.alelos)-1 )])
			s.addNextCidade(cid)
		print s.cidades

a = Algoritmo()
a.algoritmo()


	