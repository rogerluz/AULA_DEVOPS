q1 = int(input("quantos numeros deseja calcular, min 2 max 4?"))
if q1 == 2:
    n1 = float(input("digite o primeiro número?"))
    n2 = float(input("digite o segundo número?"))
    op = str(input("qual operação: Soma(+), Subtração(-), Multiplicação(*), ou Divisão(/) ? "))
    if op == '+':
       r = n1 + n2
       print(r)
    elif op == '-':
       r = n1 - n2
       print(r)
    elif op == '*':
       r = n1 * n2
       print(r)
    elif op == '/':
       r = n1 / n2
       print(r)
elif q1 == 3:
     n1 = float(input("digite o primeiro número?"))
     n2 = float(input("digite o segundo número?"))
     n3 = float(input("digite o segundo número?"))
     op = str(input("qual operação: Soma(+), Subtração(-), Multiplicação(X), ou Divisão(/) ? "))
     if op == '+':
       r = n1 + n2 + n3
       print(r)
     elif op == '-':
       r = n1 - n2 - n3
       print(r)
     elif op == 'X':
       r = n1 * n2 * n3
       print(r)
     elif op == '/':
       r = n1 / n2 / n3
       print(r)
elif q1 == 4:
     n1 = float(input("digite o primeiro número?"))
     n2 = float(input("digite o segundo número?"))
     n3 = float(input("digite o terceiro número?"))
     n4 = float(input("digite o quarto número?"))
     op = str(input("qual operação: Soma(+), Subtração(-), Multiplicação(X), ou Divisão(/) ? "))
     if op == '+':
       r = n1 + n2 + n3 - n4
       print(r)
     elif op == '-':
       r = n1 - n2 - n3 - n4
       print(r)
     elif op == 'X':
       r = n1 * n2 * n3 * n4
       print(r)
     elif op == '/':
       r = n1 / n2 / n3 / n4
       print(r)
