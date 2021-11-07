# -*- coding: utf_8 -*-
import os
import time

#Retardo en Segundos para las pasusas:
RETARDO = 3 

def limpiarPantalla():	
	if(os.name == "posix"):
		os.system("clear")
	elif(os.name == "ct" or os.name == "nt" or os.name == "dos"):
		os.system("cls")



#---------------------------------------------------------------------------
limpiarPantalla()
print("\n")
print("Actividad 12 - Filósofos Comensales")
print("\n")
print("Seminario de Sistemas Operativos - 2021 B")
print("Oscar Alejandro Quintero Iñiguez")
print("\n")
time.sleep(0)

print("\tPalillo 5: Ocupado por...\n")
print("\u0332".join("Filósofo 1: "), "Esperando...\n")
print("\tPalillo 1: Ocupado por...\n")
print("\u0332".join("Filósofo 2: "), "Esperando...\n")
print("\tPalillo 2: Ocupado por...\n")
print("\u0332".join("Filósofo 3: "), "Esperando...\n")
print("\tPalillo 3: Ocupado por...\n")
print("\u0332".join("Filósofo 4: "), "Esperando...\n")
print("\tPalillo 4: Ocupado por...\n")
print("\u0332".join("Filósofo 5: "), "Esperando...\n")
print("\tPalillo 5: Ocupado por...\n")






