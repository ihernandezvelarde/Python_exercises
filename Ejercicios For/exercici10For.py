print("Introduce un numero")
num = int(input())

k = num - 1

# bucle exterior para manejar el número de filas

for i in range(0, num):

    # bucle interno para manejar espacios numéricos
    # valores cambiantes  (el requisito)
    for j in range(0, k):
        print(end=" ")

    # decrementar despues de cada ciclo
    k = k - 1

    # bucle interno para manejar el número de columnas
    # valores cambiantes (el bucle exterior)
    for j in range(0, i + 1):
        # printar estrellas
        print("* ", end="")

    # espacio despues de cada *
    print("")