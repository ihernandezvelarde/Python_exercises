base = int(input("Introduzca el numero entero que hara de base:  "))
exponente = int(input("Introduzca el numero entero que hara de exponente:  "))
potencia=1;

while(exponente>0): 
         potencia = potencia*base;
         exponente=exponente-1;

print ("El resultado es: " +str(potencia))