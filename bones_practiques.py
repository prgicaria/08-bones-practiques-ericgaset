#!/usr/bin/env python

'''Bones pràctiques. Fes la divisió entera de dos nombres i indica el resultat.

Institut Icària
Programació - 1r Batxillerat - Curs 2023-24

Utilitzant el dividend i divisor, que son dos nombres que tu posaràs,
el programa et calcularà el quocient, el residu i els ensenya a la pantalla.
També ensenya el procés de la divisió a la pantalla.
'''
__author__ = "Eric Gaset Orus"
__email__= "egaset@instituticaria.cat"
__date__ = "2024/10/23"

dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))
quocient = dividend // divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")