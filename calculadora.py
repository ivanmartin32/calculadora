#!/usr/bin/env python

'''
Calculadora [Python]
---------------------------
Autor: Iván Martín
Version: 1.0

Descripcion:
Calculadora que devuelve los valores en consola

'''

__author__ = "Iván Martín"
__email__ = "ivanmartin_32@hotmail.com"
__version__ = "1.0"

def calculadora():

    print('Calculadora')
    print('Ingrese primer numero')
    numero1 = float(input())
    print('Ingrese Operador')
    operador = str(input())
    print('Ingrese segundo numero')
    numero2 = float(input())
    if operador == '+':
        resultado = numero1 + numero2
        print('El resultado es', resultado)
    if operador == '-':
        resultado = numero1 - numero2
        print('El resultado es', resultado)
    if operador == '*':
        resultado = numero1 * numero2
        print('El resultado es', resultado)
    if operador == '/':
        resultado = numero1 / numero2
        print('El resultado es', resultado)
    # variable muestra para pausar resultado en la consola de windows
    muestra = int(input())
if __name__ == '__main__':
    calculadora()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

