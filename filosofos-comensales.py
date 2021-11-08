# -*- coding: utf_8 -*-
import os
import time

#Retardo en Segundos para las pasusas:
RETARDO = 3 
ESPERANDO = "Esperando..."
COMIENDO = "Comiendo"

def limpiarPantalla():	
	if(os.name == "posix"):
		os.system("clear")
	elif(os.name == "ct" or os.name == "nt" or os.name == "dos"):
		os.system("cls")

class FilosofoComensal:
	"""docstring for FilosofoComensal"""
	def __init__(self):
		self.status = ESPERANDO
		self.numComidas = 0
		return

	def comer(self):
		self.status = COMIENDO
		self.numComidas += 1
		return
	def esperar(self):
		self.status = ESPERANDO
		return
	
# RDevuleve si los filósofos ya comieron al menos el número de veces especificado
def todosComieron(veces, *filosofos):
	todosComieron = True
	for filosofo in filosofos:
		if filosofo.numComidas < veces:
			todosComieron = False
			break
	return todosComieron
def imprimirTablaNumComidas():
	print("_________________________________________")
	print("| F1\t| F2\t| F3\t| F4\t| F5\t|")
	print("-----------------------------------------")
	print("|", F1.numComidas,"\t|",F2.numComidas,"\t|",F3.numComidas,"\t|",F4.numComidas,"\t|",F5.numComidas,"\t|")
	print("-----------------------------------------")
	return



#---------------------------------------------------------------------------
limpiarPantalla()
print("\n")
print("Actividad 12 - Filósofos Comensales")
print("\n")
print("Seminario de Sistemas Operativos - 2021 B")
print("Oscar Alejandro Quintero Iñiguez")
print("\n")
time.sleep(0)

F1 = FilosofoComensal()
F2 = FilosofoComensal()
F3 = FilosofoComensal()
F4 = FilosofoComensal()
F5 = FilosofoComensal()


for x in range(6):
	F1.comer()
for x in range(6):
	F2.comer()
for x in range(6):
	F3.comer()
for x in range(6):
	F4.comer()
for x in range(6):
	F5.comer()

print(todosComieron(6, F1, F2, F3, F4, F5))

F5.comer()
F5.esperar()
F3.comer()

print("Veces que ha comido cada filósofo:")
imprimirTablaNumComidas()
print("\n")

print("\tPalillo 5: Ocupado por...\n")
print("\u0332".join("Filósofo 1: "), F1.status, "\n")
print("\tPalillo 1: Ocupado por...\n")
print("\u0332".join("Filósofo 2: "), F2.status, "\n")
print("\tPalillo 2: Ocupado por...\n")
print("\u0332".join("Filósofo 3: "), F3.status, "\n")
print("\tPalillo 3: Ocupado por...\n")
print("\u0332".join("Filósofo 4: "), F4.status, "\n")
print("\tPalillo 4: Ocupado por...\n")
print("\u0332".join("Filósofo 5: "), F5.status, "\n")
print("\tPalillo 5: Ocupado por...\n")






