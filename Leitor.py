# -*- coding: utf-8 -*-
from math import sqrt
class Leitor: 
	
	def __init__(self, endereco):
		arquivo = open (endereco, "r")
		self.lista = arquivo.readlines()
		self.mapaCidades = None
		self.solucoes=[]
		for i in range(0,len (self.lista)):
			self.lista[i] = self.lista[i].replace("\n", "")
		arquivo.close()

	def lerMatriz(self):
		mapaCidades= {}
		#calculando distancias entre cidades
		for i in range(0,len (self.lista)):
			nome, x, y = self.lista[i].split(" ")
			x, y = int (x), int (y)
			mapaDistancias = {}
			for j in range(0,len (self.lista)):
				nome2, xalvo, yalvo = self.lista[j].split(" ")
				xalvo, yalvo = int (xalvo), int (yalvo)
				distancia = sqrt((x-xalvo)**2) + ((y-yalvo)**2)
				mapaDistancias[int(nome2)-1]= distancia
			mapaCidades[int(nome)-1]= mapaDistancias
		self.mapaCidades = mapaCidades
		return self.mapaCidades
