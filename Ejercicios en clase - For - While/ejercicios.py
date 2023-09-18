'''1- Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6
integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que
deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un
método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del
mensaje - considerando la posición de cada una en el alfabeto - una determinada cantidad de lugares.
Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se
correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el
mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a
comenzar desde la letra “a”.
Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto
español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una
vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.'''
primer_mensaje = input('Primer mensaje: ')
segundo_mensaje = input('Segundo mensaje: ')
tercer_mensaje = input('Tercer mensaje: ')
cuarto_mensaje = input('Cuarto mensaje: ')
quinto_mensaje = input('Quinto mensaje: ')
corrimiento = int(input('Corrimiento: '))
primer_mensaje = primer_mensaje.lower()
segundo_mensaje = segundo_mensaje.lower()
tercer_mensaje = tercer_mensaje.lower()
cuarto_mensaje = cuarto_mensaje.lower()
quinto_mensaje = quinto_mensaje.lower()
primer_mensaje_encriptado = []
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in primer_mensaje:
    if (i)=='a':
        if (-1+corrimiento)>26:
            (i) = letras [(corrimiento - 26)%26]
            primer_mensaje_encriptado.append(i)
        if (-1+corrimiento)<=26:
            (i) = letras [corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='b':
        if (0+corrimiento)>26:
            (i) = letras [(1+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (0+corrimiento)<=26:
            (i) = letras [1+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='c':
        if (1+corrimiento)>26:
            (i) = letras [(2+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (1+corrimiento)<=26:
            (i) = letras [2+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='c':
        if (2+corrimiento)>26:
            (i) = letras [(3+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (2+corrimiento)<=26:
            (i) = letras [3+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='d':
        if (3+corrimiento)>26:
            (i) = letras [(4+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (3+corrimiento)<=26:
            (i) = letras [4+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='e':
        if (4+corrimiento)>26:
            (i) = letras [(5+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (4+corrimiento)<=26:
            (i) = letras [5+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='f':
        if (5+corrimiento)>26:
            (i) = letras [(6+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (5+corrimiento)<=26:
            (i) = letras [6+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='g':
        if (6+corrimiento)>26:
            (i) = letras [(7+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (6+corrimiento)<=26:
            (i) = letras [7+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='h':
        if (7+corrimiento)>26:
            (i) = letras [(8+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (7+corrimiento)<=26:
            (i) = letras [8+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='i':
        if (8+corrimiento)>26:
            (i) = letras [(9+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (8+corrimiento)<=26:
            (i) = letras [9+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='j':
        if (9+corrimiento)>26:
            (i) = letras [(10+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (9+corrimiento)<=26:
            (i) = letras [10+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='k':
        if (10+corrimiento)>26:
            (i) = letras [(11+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (10+corrimiento)<=26:
            (i) = letras [11+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='l':
        if (11+corrimiento)>26:
            (i) = letras [(12+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (11+corrimiento)<=26:
            (i) = letras [12+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='m':
        if (12+corrimiento)>26:
            (i) = letras [(13+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (12+corrimiento)<=26:
            (i) = letras [13+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='n':
        if (13+corrimiento)>26:
            (i) = letras [(14+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (13+corrimiento)<=26:
            (i) = letras [14+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='ñ':
        if (14+corrimiento)>26:
            (i) = letras [(15+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (14+corrimiento)<=26:
            (i) = letras [15+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='o':
        if (15+corrimiento)>26:
            (i) = letras [(16+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (15+corrimiento)<=26:
            (i) = letras [16+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='p':
        if (16+corrimiento)>26:
            (i) = letras [(17+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (16+corrimiento)<=26:
            (i) = letras [17+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='q':
        if (17+corrimiento)>26:
            (i) = letras [(18+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (17+corrimiento)<=26:
            (i) = letras [18+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='r':
        if (18+corrimiento)>26:
            (i) = letras [(19+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (18+corrimiento)<=26:
            (i) = letras [19+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='s':
        if (19+corrimiento)>26:
            (i) = letras [(20+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (19+corrimiento)<=26:
            (i) = letras [(20+corrimiento)]
            primer_mensaje_encriptado.append(i)
    elif (i)=='t':
        if (20+corrimiento)>26:
            (i) = letras [(21+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (20+corrimiento)<=26:
            (i) = letras [(21+corrimiento) - 26]
            primer_mensaje_encriptado.append(i)
    elif (i)=='u':
        if (21+corrimiento)>26:
            (i) = letras [(22+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (21+corrimiento)<=26:
            (i) = letras [22+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='v':
        if (22+corrimiento)>26:
            (i) = letras [(23+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (22+corrimiento)<=26:
            (i) = letras [23+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='w':
        if (23+corrimiento)>26:
            (i) = letras [(24+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (23+corrimiento)<=26:
            (i) = letras [24+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='x':
        if (24+corrimiento)>26:
            (i) = letras [(24+corrimiento)%26]
            primer_mensaje_encriptado.append(i)
        if (24+corrimiento)<=26:
            (i) = letras [24+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='y':
        if (25+corrimiento)>26:
            (i) = letras [(25+corrimiento)-27]
            primer_mensaje_encriptado.append(i)
        if (25+corrimiento)<=26:
            (i) = letras [25+corrimiento]
            primer_mensaje_encriptado.append(i)
    elif (i)=='z':
        if (26+corrimiento)>26:
            (i) = letras [(26+corrimiento)-27]
            primer_mensaje_encriptado.append(i)
        if (26+corrimiento)<=26:
            (i) = letras [26+corrimiento]
            primer_mensaje_encriptado.append(i)
    else:
        print('Mensaje invalido')                                                                                                                                                                                                       
for i in primer_mensaje_encriptado:
    print(i)



