'''
Crear un programa que permeti jugar al joc pedra, paper i tisora. L’ordinador generarà un
número aleatori de l’1 al 3 (1:pedra, 2: paper i 3:tisora) i l’usuari introdueix un número de l’1 al
tres per tal de guanya la partida. L’objectiu és guanyar a l’ordinador seleccionant l’arma que
guanya segons aquestes regles:
'''
import random
numero= random.randrange(1,4)
respuesta=int(input("Introduce un numero del 1 al 3, el 1:Piedra, 2:papel y 3:tijeras: "))
if numero == 1:
    numero="Piedra"
elif numero == 2:
    numero="Papel"
else:
    numero="Tijeras"

print("El ordenador ha sacado "+ str(numero))

if respuesta == 1 and numero == "Papel":
    print("Has perdido! El papel envuelve a la piedra.")
elif respuesta== 1 and numero == "Tijeras":
    print("Has ganado! La piedra aplasta a las tijeras.")
elif respuesta == 2 and numero == "Piedra":
    print("Has ganado! El papel envuelve a la piedra.")
elif respuesta == 2 and numero== "Tijeras":
    print("Has perdido! Las tijeras cortan el papel.")
elif respuesta == 3 and numero == "Piedra":
    print("Has perdido! La piedra aplasta a las tijeras.")
elif respuesta == 3 and numero == "Papel":
     print("Has ganado! Las tijeras cortan el papel.")

while respuesta==numero:
    print("Habeis empatado, vuelve a jugar.")
    numero = random.randrange(1, 4)
    respuesta = int(input("Introduce un numero del 1 al 3, el 1:Piedra, 2:papel y 3:tijeras: "))
    print("El ordenador ha sacado " + str(numero))
