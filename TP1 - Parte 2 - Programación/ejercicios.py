'''1.Calcular el perimetro y area de un rectangulo dada su base y su altura'''
base = float(input('Ingrese la longitud de la base del rectángulo (en cm): '))
altura = float(input('Ingrese la altura del rectángulo (en cm): '))
perimetro = 2 * base + 2 * altura
area = base * altura
print(f'El perímetro del rectángulo es: {perimetro}cm y su área es: {area}cm²')
'''2.Dados los catetos de un triángulo rectángulo calcular su hipotenusa'''
cateto1 = float(input('Ingrese la longitud del primer cateto (en cm): '))
cateto2 = float(input('Ingrese la longitud del segundo cateto (en cm):'))
hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
print(f'La longitud de la hipotenusa es: {round(hipotenusa,2)}cm.')
'''3.Dado dos números mostrar la suma, resta, multiplicación y división de ambos.'''
numero1 = float(input('Ingrese el primer número: '))
numero2 = float(input('Ingrese el segundo número: '))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f'La suma entre ambos números es: {suma}, la resta entre ambos números es: {resta}, la división entre ambos números es: {division} y la multiplicación entre ambos números es: {multiplicacion}.')
'''4.Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: C= (F-32)*5/9'''
valor_fahrenheit = float(input('Ingrese la temperatura en grados Fahrenheit: '))
valor_celsius = (valor_fahrenheit - 32)*5/9
print(f'La temperatura ingresada en grados Fahrenheit es: {valor_fahrenheit} y dicha temperatura expresada en grados Celsius es: {valor_celsius}.')
'''5.¿Que problemas tienen las siguientes instrucciones?¿Como las solucionarías?'''
'''a) Primero que se definió a la variable con una letra mayuscula lo cuál no está recomendado, 
segundo si quisiera que el usuario ingrese su nombre y su cancion favorita deberia hacerlo de otra manera: 
nombre, cancion_favorita = str(input('Ingrese su nombre: ')),str(input('¿Cuál es su canción favorita? '))'''
'''b) El error es que cuando se le pidió al usuario ingresar el precio, no se utilizo el metodo float o int 
por lo que al intentar utilizar la variable en un procedimiento matemático nos salta error porque no se puede 
operar con variables tipo string'''
'''c) El error esta en el print. Solución: 
edad = int(input(Edad: ))
print(f'Tu edad es {edad})'''
'''d) Para corroborar si la edad ingresada por el usuario es igual a 18 deberia hacerse por medio de un 'if'. Solución:
edad = int(input('Edad: '))
if edad == 18:
    print('Usted tiene 18 años!')
else:
    print(f'Usted no tiene 18 años, usted tiene {edad} años')'''
'''6. Calcular la media de tres números pedidos por teclado.'''
primer_numero = float(input('Ingrese el primer número: '))
segundo_numero = float(input('Ingrese el segundo número: '))
tercer_numero = float(input('Ingrese el tercer número: '))
media = (primer_numero + segundo_numero + tercer_numero) / 3
print(f'La media de los tres números ingresados es: {media}')
'''7. Realizar un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas 
horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.'''
minutos = int(input('Ingrese la cantidad de minutos: '))
if minutos % 60 == 0:
    print(f'{minutos} minutos son {minutos // 60} horas.')
else:
    print(f'{minutos} minutos son {minutos // 60} horas y {(minutos % 60)} minutos.')
'''8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber
cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá 
en el mes tomando en cuenta su sueldo base y comisiones.'''
primer_venta = float(input('Ingrese el monto de su primer venta: '))
segunda_venta = float(input('Ingrese el monto de su segunda venta: '))
tercer_venta = float(input('Ingrese el monto de su tercer venta: '))
sueldo_base = float(input('Ingrese su sueldo base (sin comisiones): '))
comision_mensual = (primer_venta + segunda_venta + tercer_venta)*0.1
sueldo_total = sueldo_base + comision_mensual
print(f'Su comisión mensual es {round(comision_mensual,2)} y su sueldo total es {round(sueldo_total,2)}')
'''9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto 
deberá pagar finalmente por su compra'''
valor_inicial_compra = float(input('Ingrese el monto inicial de la compra: '))
print(f'El monto final a pagar es ${(valor_inicial_compra)*0.85}')
'''10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se 
compone de los siguientes porcentajes: -55% del promedio de sus tres calificaciones parciales. 
-30% de la calificación del examen final. -15% de la calificación de un trabajo final.'''
primer_parcial, segundo_parcial, tercer_parcial, examen_final, trabajo_final = int(input('Ingrese la nota del primer parcial: ')),int(input('Ingrese la nota del segundo parcial: ')),int(input('Ingrese la nota del tercer parcial: ')),int(input('Ingrese la nota del examen final: ')),int(input('Ingrese la nota del trabajo final: '))
if 0<=primer_parcial<=10 and 0<=segundo_parcial<=10 and 0<=tercer_parcial<=10 and 0<=examen_final<=10 and 0<=trabajo_final<=10:
    calificacion_final = 0.55 * ((primer_parcial + segundo_parcial + tercer_parcial)/3) + 0.30 * (examen_final) + 0.15 * (trabajo_final)
    print(f'Su calificación final es: {calificacion_final}')
else: 
    print(f'Ingresó una nota incorrectamente')
'''11. Pide al usuario dos números y muestra la 'distancia' entre ellos 
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo.)'''
