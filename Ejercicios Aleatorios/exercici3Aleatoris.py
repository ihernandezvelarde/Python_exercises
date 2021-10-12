'''
Crea un programa que escull dos números enters aleatoris A i B però no els mostri per
pantalla. Si els dos números fossin iguals, tornarà a repetir-se la elecció fins que siguin
diferents. El programa preguntarà per quin dels dos números apostem, A o B (guanya el
número més alt).
Una vegada l’usuari hagi introduït la seva aposta, el programa mostrarà el valor de A i B, dirà si
hem guanyat l’aposta (encertat el número més alt) o perdut i ens dirà quantes partides hem
guanyat i perdut fins al moment. Després d’una jugada, ens preguntarà si volem tornar a jugar
altre cop.

'''
import random
ganadas=0
perdidas=0
A= random.randrange(1,10)
B= random.randrange(1,10)
if A==B:
    A = random.randrange(1, 10)
    B = random.randrange(1, 10)
respuesta=str(input("A que numeros apostamos? A o B (Gana el numero mas grande): "))
if A>B and respuesta == "A":
    print("A saca un ", str(A), "y B saca un ", str(B), "Has ganado!")
    ganadas+=1
    print("Llevas", str(ganadas), " ganadas y ", str(perdidas), "perdidas")
elif A<B and respuesta == "A":
    print("A saca un ", str(A), "y B saca un ", str(B), "Has perdido!")
    perdidas += 1
    print("Llevas", str(ganadas), " ganadas y ", str(perdidas), "perdidas")
elif A>B and respuesta == "B":
    print("A saca un ", str(A), "y B saca un ", str(B), "Has perdido!")
    perdidas+=1
    print("Llevas", str(ganadas), " ganadas y ", str(perdidas), "perdidas")
elif A<B and respuesta == "B":
    print("A saca un ", str(A), "y B saca un ", str(B), "Has ganado!")
    ganadas += 1
    print("Llevas", str(ganadas), " ganadas y ", str(perdidas), "perdidas")

answer=str(input("Quieres volver a jugar? S/N "))
while answer == "S":
    if A == B:
        A = random.randrange(1, 10)
        B = random.randrange(1, 10)
    respuesta = str(input("A que numeros apostamos? A o B (Gana el numero mas grande): "))
    if A > B and respuesta == "A":
        print("A saca un ", str(A), "y B saca un ", str(B), "Has ganado!")
        ganadas += 1
        print("Llevas", str(ganadas), " ganadas y ", str(perdidas), "perdidas")
    elif A < B and respuesta == "A":
        print("A saca un ", str(A), "y B saca un ", str(B), "Has perdido!")
        perdidas += 1
        print("Llevas", str(ganadas), " ganadas y ", str(perdidas), "perdidas")
    elif A > B and respuesta == "B":
        print("A saca un ", str(A), "y B saca un ", str(B), "Has perdido!")
        perdidas += 1
        print("Llevas", str(ganadas), " ganadas y ", str(perdidas), "perdidas")
    elif A < B and respuesta == "B":
        print("A saca un ", str(A), "y B saca un ", str(B), "Has ganado!")
        ganadas += 1
        print("Llevas", str(ganadas), " ganadas y ", str(perdidas), "perdidas")
    if anwer == "N":
        print("Adios!")