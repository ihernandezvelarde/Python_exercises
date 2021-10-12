print("Hola! Podrías decirme cuantas barras de pan no son del dia por favor? ")

numerobarras= int(input())
preciobarra= 3.49
preciodescuento= (3.49*0.60)
roundpreciodescuento=round(preciodescuento)

descuento=(preciobarra-preciodescuento)
rounddescuento=round(descuento)
costetotal= (numerobarras*preciodescuento)
roundcostetotal=round(costetotal)

print("El precio de una barra normal es de: "+str(preciobarra)+" € El descuento será de: "+str(rounddescuento)+" € El precio total será de: "+str(roundcostetotal)+" €")