#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 13:10:08 2023

@author: ckettmayer
"""


def son_iguales_a_menos_de_tres_comparaciones(cadena1, cadena2):
    # Asegúrate de que las cadenas tengan la misma longitud
    if len(cadena1) != len(cadena2):
        return False

    # Inicializa el contador de diferencias
    diferencias = 0

    # Compara caracter por caracter
    for char1, char2 in zip(cadena1, cadena2):
        if char1.lower() != char2.lower():
            diferencias += 1

        # Si el número de diferencias es mayor o igual a 3, podemos salir del bucle
        if diferencias >= 3:
            break

    # Devuelve True si hay menos de 3 diferencias, de lo contrario, False
    return diferencias < 3

# Ejemplo de uso
cadena_1 = "Ejemplo"
cadena_2 = "ejmplo"
if son_iguales_a_menos_de_tres_comparaciones(cadena_1, cadena_2):
    print("Las cadenas son iguales a menos de 3 comparaciones.")
else:
    print("Las cadenas no son iguales a menos de 3 comparaciones.")
