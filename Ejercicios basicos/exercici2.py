print("Introduce el numero de payasos por pedido por favor: ")
payasos=int(input())
print("Introduce el numero de muñecas por pedido por favor: ")
muñecas=int(input())
peso = (payasos*112)+(muñecas*75)

if payasos>200 and payasos<500:
    precio= peso+500
elif payasos>500 and payasos<700:
    precio= peso+600
elif payasos>700:
    precio= peso+1000
else:
    precio=peso

print("El peso total del paquete (ya que cada payaso pesa 112g y las muñecas 75g) es: " + str(peso))