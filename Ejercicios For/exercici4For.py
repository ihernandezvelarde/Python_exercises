print("Introduce un numero entero")
numero1=int(input())
print("Introduce un segundo numero entero mayor que el primero")
numero2=int(input())
i=0
divisor=0
while numero1>= numero2:
    print("ERROR. El numero 1 debe ser menor que el numero 2")
    print("Introduce un numero entero")
    numero1 = int(input())
    print("Introduce un segundo numero entero mayor que el primero")
    numero2 = int(input())
for i in range(2,numero1):
    if numero1 % i == 0:
        divisor=i
if divisor==0:
    print("Es primo")
else:
    print("El divisor más grande es: ", divisor)

