contador = 0
multiplicacion = 0
total = 1
print("Introduzca un numero entero por favor y el programa calculara el producto de los 'x' primeros numeros enteros una vez introduzca un numero negativo (0 no es negativo).")
numero = int(input())
while numero != contador:
    contador = contador + 1
    total = total * contador
print("El producto de los primeros " + str(numero) + " numeros es: " + str(total))