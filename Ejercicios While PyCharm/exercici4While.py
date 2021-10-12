numero = 1
total=0
contador=0
while numero>0:
    print("Introduce un numero, el programa finalizara cuando introduzcas un numero negativo (0 no es un numero negativo) y se sumaran los positivos")
    numero = int(input())
    total=total+numero
    contador=contador+1
print("La suma de los numeros positivos es: "+str(total-numero)+" Y la cantidad de numeros introducidos es: " + str(contador-1))