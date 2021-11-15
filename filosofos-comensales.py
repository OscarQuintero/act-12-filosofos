# -*- coding: utf_8 -*-
import os
import time
import random
import threading

# Retardo en Segundos para las pausas:
RETARDO = 1 
# Estados de los filósofos
ESPERANDO = "Esperando..."
COMIENDO = "Comiendo"
# Estados de los cubiertos
DISPONIBLE = "Disponible"
OCUPADO = "Ocupado"
#Forma de ver las operaciones
DIAGRAMA = 1
LISTA = 0

Visualización = DIAGRAMA

def limpiarPantalla():	
	if(os.name == "posix"):
		os.system("clear")
	elif(os.name == "ct" or os.name == "nt" or os.name == "dos"):
		os.system("cls")

class FilosofoComensal:
	"""docstring for FilosofoComensal"""
	def __init__(self,name, indiceCubiertoIzq, indiceCubiertoDer, ListaCubiertos):
		self.status = ESPERANDO
		self.numComidas = 0
		self.name = name
		self.indiceCubiertoIzq = indiceCubiertoIzq
		self.indiceCubiertoDer = indiceCubiertoDer
		self.ListaCubiertos = ListaCubiertos
		return
			
	def esPosibleComer(self):
		result = False
		cubiertoIzqLibre = self.ListaCubiertos[self.indiceCubiertoIzq].status == DISPONIBLE
		cubiertoDerLibre = self.ListaCubiertos[self.indiceCubiertoDer].status == DISPONIBLE
		result = cubiertoIzqLibre and cubiertoDerLibre		
		return result

	def comer(self):
		self.status = COMIENDO
		self.numComidas += 1
		self.ListaCubiertos[self.indiceCubiertoIzq].usar()
		self.ListaCubiertos[self.indiceCubiertoDer].usar()
		time.sleep(1)
		self.ListaCubiertos[self.indiceCubiertoIzq].desocupar()
		self.ListaCubiertos[self.indiceCubiertoDer].desocupar()
		self.status = ESPERANDO
		time.sleep(0.5)
		return

	def esperar(self):
		self.status = ESPERANDO
		return

	def intentarComer(self):
		if(Visualización==LISTA):
			print(self.name, "intentando comer....")			
		if self.esPosibleComer():
			if(Visualización==LISTA):
				print(self.name, "Comiendo...")
			comiendo = threading.Thread(target=self.comer)
			comiendo.start()
		else:
			if(Visualización==LISTA):
				print(self.name, "No es posible comer")
		return


class Cubierto:
	def __init__(self):
		self.status = DISPONIBLE
		pass
	def usar(self):
		self.status = OCUPADO
		return
	def desocupar(self):
		self.status = DISPONIBLE
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

ListaCubiertos = []

C5 = Cubierto()
ListaCubiertos.append(C5)
C1 = Cubierto()
ListaCubiertos.append(C1)
C2 = Cubierto()
ListaCubiertos.append(C2)
C3 = Cubierto()
ListaCubiertos.append(C3)
C4 = Cubierto()
ListaCubiertos.append(C4)



F1 = FilosofoComensal('F1',0,1,ListaCubiertos)
F2 = FilosofoComensal('F2',1,2,ListaCubiertos)
F3 = FilosofoComensal('F3',2,3,ListaCubiertos)
F4 = FilosofoComensal('F4',3,4,ListaCubiertos)
F5 = FilosofoComensal('F5',4,0,ListaCubiertos)

ListaFilosofos = [F5, F1, F2, F3, F4]
monitor = 1


Lugar1 = None
Lugar2 = None
Lugar3 = None
while not todosComieron(6, F1, F2, F3, F4, F5):
	limpiarPantalla()

	# Monitor de uno
	if monitor:
		turno = random.randint(0,4)
		Lugar1 = ListaFilosofos[turno]
		turno = random.randint(0,4)
		Lugar2 = ListaFilosofos[turno]
		turno = random.randint(0,4)
		Lugar3 = ListaFilosofos[turno]

		Lugar1.intentarComer()
		Lugar2.intentarComer()
		Lugar3.intentarComer()

		monitor = 0

	if (Lugar1.status == ESPERANDO and Lugar2.status == ESPERANDO and Lugar3.status == ESPERANDO): 
		monitor = 1

	
	print("Veces que ha comido cada filósofo:")
	imprimirTablaNumComidas()
	print("\n")



	print("\tCubierto 5:", C5.status, "\n")
	print("\u0332".join("Filósofo 1: "), F1.status, "\n")
	print("\tCubierto 1:", C1.status, "\n")
	print("\u0332".join("Filósofo 2: "), F2.status, "\n")
	print("\tCubierto 2:", C2.status, "\n")
	print("\u0332".join("Filósofo 3: "), F3.status, "\n")
	print("\tCubierto 3:", C3.status, "\n")
	print("\u0332".join("Filósofo 4: "), F4.status, "\n")
	print("\tCubierto 4:", C4.status, "\n")
	print("\u0332".join("Filósofo 5: "), F5.status, "\n")
	print("\tCubierto 5:", C5.status, "\n")
	time.sleep(RETARDO)


	


