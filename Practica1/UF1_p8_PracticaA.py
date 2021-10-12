num = int(input("Introduce un numero que dictaminara el ancho y largo de la figura: "))

contador = num


for i in range(num): #columnas
    print("*", end="")
    for j in range(num): #lineas
        if(i == 0 or i == num or i <= 2 * j - 1):
            print("*", end="")
        else:
            print("#", end="")

    print()
