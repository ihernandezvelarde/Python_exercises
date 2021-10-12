numero = 1
total=0
while numero>0:
    print("Introduce un numero, el programa finalizara cuando introduzcas un numero negativo (0 no es negativo) y se sumaran los positivos")
    numero = int(input())
    total=total+numero

print(str(total-numero))