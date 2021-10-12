import random

contadorPuntosAnna = 9
contadorPuntosBernat = 9
numero = random.randrange(1, 7)
while contadorPuntosBernat or contadorPuntosAnna != 0:
    if numero % 2 == 0:
        print("Bernat has ganado! Se te suman ", numero, " puntos al marcador. Anna tu has perdido ", numero," puntos.")
        contadorPuntosAnna -= numero
        contadorPuntosBernat += numero
        print("Bernat tu contador ahora tiene: ", contadorPuntosBernat, " puntos.")
        print("Anna tu contador ahora tiene: ", contadorPuntosAnna, " puntos.")
    else:
        print("Anna has ganado! Se te suman ", numero, " puntos al marcador. Bernat tu has perdido ", numero," puntos.")
        contadorPuntosAnna += numero
        contadorPuntosBernat -= numero
        print("Bernat tu contador ahora tiene: ", contadorPuntosBernat, " puntos.")
        print("Anna tu contador ahora tiene: ", contadorPuntosAnna, " puntos.")


    if contadorPuntosBernat <= 0 or contadorPuntosAnna <= 0:
        print("Juego finalizado.")
        answer = input("Quieres volver a jugar? S/N ")
        break

while answer == "S":
    contadorPuntosAnna = 9
    contadorPuntosBernat = 9
    numero = random.randrange(1, 7)
    while contadorPuntosBernat or contadorPuntosAnna != 0:
        if numero % 2 == 0:
            print("Bernat has ganado! Se te suman ", numero, " puntos al marcador. Anna tu has perdido ", numero,
                  " puntos.")
            contadorPuntosAnna -= numero
            contadorPuntosBernat += numero
            print("Bernat tu contador ahora tiene: ", contadorPuntosBernat, " puntos.")
            print("Anna tu contador ahora tiene: ", contadorPuntosAnna, " puntos.")
        else:
            print("Anna has ganado! Se te suman ", numero, " puntos al marcador. Bernat tu has perdido ", numero,
                  " puntos.")
            contadorPuntosAnna += numero
            contadorPuntosBernat -= numero
            print("Bernat tu contador ahora tiene: ", contadorPuntosBernat, " puntos.")
            print("Anna tu contador ahora tiene: ", contadorPuntosAnna, " puntos.")

        if contadorPuntosBernat <= 0 or contadorPuntosAnna <= 0:
            answer = input("Quieres volver a jugar? S/N ")
            print("Juego finalizado.")
            break
else:
    print("Adios Gracias por jugar!")




