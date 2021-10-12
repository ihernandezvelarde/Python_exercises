contra = "hola"
print("Bienvenido/a a tu cuenta de Discord, cual es la contraseña? ")
contra2= str(input())
if contra2.lower()==contra.lower():
    print("Tu contraseña es correcta! La contraseña que pusiste al cerar la cuenta era: "+str(contra))
else:
    print("Tu contraseña es incorrecta! La contraseña que pusiste al crear la cuenta era: "+str(contra))
