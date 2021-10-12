print("Hola! Introduce tu renta anual para saber el tipo impositivo que se te aplican.")
renta=float(input())
if renta<10000:
    totalrenta= renta*0.05
    print("Tu renta es "+str(renta)+" euros. Por lo tanto se te aplica el 5% que esto hara un total de "+str(totalrenta)+ " €")
if renta>=10000 and renta<20000:
    totalrenta2 =renta*0.15
    print("Tu renta es " + str(renta) + " euros. Por lo tanto se te aplica el 15%% que esto hara un total de " + str(totalrenta2)+" €")
if renta>=20000 and renta<35000:
    totalrenta3= renta*0.20
    print("Tu renta es " + str(renta) + " euros. Por lo tanto se te aplica el 20% que esto hara un total de " + str(totalrenta3)+" €")
if renta>=35000 and renta<60000:
    totalrenta4= renta*0.30
    print("Tu renta es " + str(renta) + " euros. Por lo tanto se te aplica el 30% que esto hara un total de " + str(totalrenta4)+" €")
if renta>=60000:
    totalrenta5= renta*0.45
    print("Tu renta es " + str(renta) + " euros. Por lo tanto se te aplica el 45% que esto hara un total de " + str(totalrenta5))
