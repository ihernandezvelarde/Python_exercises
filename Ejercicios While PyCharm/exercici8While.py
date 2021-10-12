'''Escriu un programa que vaja llegint números fins que s’introdueixi un -1, haurà
de sumar i comptar aquells números compresos entre 0 i 10, imprimir aquells
que no suma i finalment imprimir la mitjana dels números sumats
'''
contador = 0
suma = 0
number = 1
total = 0
print("Introduce numeros enteros, los que estén ente 0 y 10 se sumaran y finalmente se hara la media aritmetica de estos. Los que no, se imprimiran una vez introducidos. El programa terminara una vez introduzcas un numero negativo (0 no cuenta como negativo)")
while number > 0:
    print("Introduce un numero entero: ")
    number = int(input())
    if number >= 0 and number <= 10:
        suma += number
        contador += 1
    else:
       print("Este numero no se suma ya que no esta entre 0 y 10: " + str(number))
total = suma / contador
roundtotal = round(total)
print("La media de los numeros introducidos entre 0 y 10 es: " + str(roundtotal))



