'''1. Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x 
was skipped'.
• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the 
loop was broken when x was ' + x.'''
x = 0
print(f'The value of the loop is {x}')
while True:
    x += 1
    if x!=4 and x!=6 and x!=10 and x!=15:
        print(f'The value of the loop is {x}')
    if x==4 or x==6 or x==10:
        print(f'The value {x} of the x was skipped')
        continue
    if x==15:
        print(f'The execution of the loop was broken when x was {x}')
        continue
    if x>=30:
        break
'''1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en 
mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.'''
print('Ingrese sus lineas (si desea finalizar la entrada de lineas digite " "): ')
cadena = []
cantidad_lineas = 0
while True:
    linea = input()
    linea = linea.upper()
    cantidad_lineas += 1
    if linea !=' ':
        cadena.append(linea)
    if linea==' ':
        for i in range(0,cantidad_lineas-1):
            n = cadena[i]
            print (n)
        print ( )
        break
'''2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350'''
print('Bienvenido a su cuenta bancaria')
print('Digite')
plata_en_cuenta = 0
while True:
    print('"D" si desea depositar o "R" si desea retirar o " " para salir')
    opcion = input()
    opcion = opcion.upper()
    if opcion=='D':
        deposito = int(input('D '))
        plata_en_cuenta = plata_en_cuenta + deposito
    if opcion=='R':
        retiro = int(input('R '))
        plata_en_cuenta = plata_en_cuenta - retiro
    if opcion==' ':
        print(f'Dinero disponible en cuenta {plata_en_cuenta}')
        print('Muchas gracias')
        break
'''3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores 
que 1, finalizando cuando se reciba un cero.
Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: 
él mismo y el 1.'''
cantidad_numeros_primos = 0
while True:
    numero = int(input('Ingrese un número: '))
    if numero>1:
        numero = int(input('Ingrese un número: ')) 
        if numero
