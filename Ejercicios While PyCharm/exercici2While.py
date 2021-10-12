masgrande=0
numero=1

while numero>0:
    print("Introduce un numero, el programa finalizara y dira el nombre mas grande introducido si pones un numero negativo. (0 no es un numero negativo)")
    numero = int(input())
    if numero>masgrande:
        numero=numero+masgrande
    else:
        print("El programa ha finalizado, el numero mas grande introducido es: "+str(masgrande))