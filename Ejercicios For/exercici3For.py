print("Introduce un numero entero")
numero1=int(input())
print("Introduce un segundo numero entero mayor que el primero")
numero2=int(input())
i=0
while numero1>= numero2:
    print("ERROR. El numero 1 debe ser menor que el numero 2")
    print("Introduce un numero entero")
    numero1 = int(input())
    print("Introduce un segundo numero entero mayor que el primero")
    numero2 = int(input())
for i in range(numero1,numero2+1):
    if i % 2 == 0:
        print(str(i))
