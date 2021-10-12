'''

Programa que permet a l’usuari que endevini un número aleatori entre l’1 al 100.
L’usuari disposarà de 5 intents per endevinar el número.
A cada intent de l’usuari se l’indicarà si elnúmero generat aleatòriament és menor o major que el que ha dit l’usuari.
'''
import random
numero= random.randrange(101)
respuesta=int(input("Introduce un numero: "))
print(numero)
i=1
if respuesta != numero:
    while i <= 5:
        print("Error, intentalo de nuevo. ")
        if respuesta<numero:
            print("El numero es mas grande")
            respuesta = int(input("Introduce un numero: "))
        elif respuesta>numero:
            print("El numero es mas pequeño")
            respuesta = int(input("Introduce un numero: "))
        else:
            print("Has acertado!")
            break
        i += 1
    if i == 6 and respuesta != numero:
        print("Ya no te quedan intentos")
else:
    print("HAS ACERTADO!")