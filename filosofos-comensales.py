# -*- coding: utf_8 -*-
import os


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

