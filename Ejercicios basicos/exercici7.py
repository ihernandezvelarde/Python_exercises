print("Introduce tu edad para saber si tienes que tributar este año: ")
edad= int(input())
print("Introduce tus ingresos mensuales: ")
ingresos= int(input())
if edad>16 and ingresos>=1000:
    print("Este año si que tienes que tributar!")
else:
    print("Aun no tienes que tributar!")
