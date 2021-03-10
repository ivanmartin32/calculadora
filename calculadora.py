if __name__ == '__main__':
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

