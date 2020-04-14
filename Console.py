#25 pts Calculadora por consola (Debe sumar, restar, multiplicar y dividir 2 números, Tener menú de opciones)

def suma():
    x = float(input('Primer Numero \n'))
    y = float(input('Segundo Numero \n'))
    return (round(x+y,5))
def resta():
    x = float(input('Primer Numero \n'))
    y = float(input('Segundo Numero \n'))
    return (round(x-y,5))
def mult():
    x = float(input('Primer Numero \n'))
    y = float(input('Segundo Numero \n'))
    return (round(x*y,5))
def div():
    x = float(input('Primer Numero \n'))
    y = float(input('Segundo Numero \n'))
    return (round(x/y,5))
def menu():
    print('-----------------')
    print('Menu')
    print('1)Suma')
    print('2)Resta')
    print('3)Multiplicacion')
    print('4)Division')
    print('0)Salir')
    print('-----------------')
while(True):
    menu()
    op=int(input())
    if(op==1):
        print(suma())
    elif(op==2):
        print(resta())
    elif(op==3):
        print(mult())
    elif(op==4):
        print(div())
    elif(op==0):
        print('Salir')
        break
    else:
        print('No existe ese numero')