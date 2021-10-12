print("Cuanto dinero quieres depositar en la cuenta de ahorro? En este banco damos el 4% de intereses al año.")

dinero= float(input())
intereses=(dinero*0.04)
roundintereses= round(intereses)
totalcuenta= (dinero+intereses)
roundtotalcuenta= round(totalcuenta)

print("El banco genera un 4% de intereses en un año, por "+str(dinero)+" euros generará " +str(roundintereses) +" euros. Por lo tanto en tu cuenta tendras " +str(roundtotalcuenta) + " euros después de un año.")
totalintereses2= (totalcuenta*0.04)
roundtotalintereses2= round(totalintereses2)
totalcuenta2=(totalcuenta+totalintereses2)
roundtotalcuenta2= round(totalcuenta2)

totalintereses3= (totalcuenta2*0.04)
roundtotalintereses3= round(totalintereses3)
totalcuenta3=(totalcuenta2+totalintereses3)
roundtotalcuenta3= round(totalcuenta3)

print("En el segundo año el banco vuelve a generara unos intereses del 4% esto sumado al anterior hace un 8%, por " + str(roundtotalcuenta) + " euros, generará " +str(roundtotalintereses2)+ " euros. Por lo que tendrás " +str(roundtotalcuenta2) + " euros después de dos años.")
print("Y en el tercer año el banco generara unos intereses del 12% por acumulacion de los otros dos años. En tu cuenta habrá "+str(roundtotalcuenta2)+ " euros que generará " +str(roundtotalintereses3)+ " euros. Por lo que tendrás " +str(roundtotalcuenta3) + " euros después de tres años.")