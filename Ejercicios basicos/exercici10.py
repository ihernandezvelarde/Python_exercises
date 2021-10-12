print("Hola! Introduce los puntos que has conseguido en el trabajo este año para saber tu sueldo. (Ej: 0.0 , 0.4 , 0.6 o más).")
answer= float(input())
dinero=2400
if answer == 0.0:
    total=dinero*0.0
    print("Es inaceptable! Tu sueldo es "+str(total)+ "€")
elif answer == 0.4:
    total=dinero*0.4
    print("Es aceptable! Tu sueldo es de "+str(total)+"€")
elif answer>= 0.6:
    total=dinero*answer
    print("Tienes mucho merito! Tu sueldo es de " +str(total)+"€")