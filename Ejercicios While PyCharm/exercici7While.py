numero = 0
contador = 0
suma = 0
print("Introduzca un numero y el programa calculara la suma de los n primeros naturales impares.")
numero = int(input())
while numero >= contador:
    if contador % 2 != 0:
        suma += contador
    contador += 1
print(str(suma))
