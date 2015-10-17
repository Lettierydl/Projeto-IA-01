# -*- coding: utf-8 -*-
from math import sqrt
from Leitor import Leitor
import random
import sys

class BuscaCega: 

	def calculaValorSolucao (self, lista):
		total = 0
		for i in range(0, len(lista)-1):
			total = total + self.mapaCidades[lista[i]][lista[i+1]]
		return total



	def DSF(self, grafo, inicio = "1", visitados = None):
		if visitados == None:
			visitados= []
		visitados.append(inicio)
		if (len (visitados ) == len (grafo.keys())):
			visitados.append(visitados[0])
			print (visitados)
		proximos = set (grafo.keys()) - set (visitados)
		print ("meu id: " + str(inicio) + "  proximos : "+ str (proximos))
		for i in proximos:
			self.DSF(grafo, i, visitados)

	def algoritmoBuscaProfundidadeRecursivo(self, grafo, inicio, visitado=None, solucao = []):
		if visitado is None:
			visitado = set()
		visitado.add(inicio)
		solucao.append (inicio)
		if len ( set(grafo[inicio].keys()) -visitado )  == 0:
				print visitado
		for next in set(grafo[inicio].keys()) -visitado:
			self.algoritmoBuscaProfundidadeRecursivo(grafo, next, visitado, solucao)
		return visitado


	def buscaCega(self , arquivo = "eil101.tsp"):
		l = Leitor(arquivo)
		grafo = l.lerMatriz()
		iniciorandom.randint(0, len(grafo))

		solucao = []
		visitados, pilha = set(), [inicio]
		while pilha:
			vertice = pilha.pop()
			if vertice not in visitados:
				#solucao.append(vertice)
				visitados.add(vertice)
				pilha.extend(set(grafo[vertice].keys()) - visitados)
				#print "visitados= " + str (visitados) + "\n\n grafo: "+ str (pilha)  
				print "solucao " + str (solucao) +" valor " +  str (self.calculaValorSolucao(solucao))
				print "\n-------------------------------\n"

		return visitados

bc = BuscaCega()
print bc.buscaCega()


