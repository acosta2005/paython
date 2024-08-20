respuesta_sentido_universo = input("¿cual es el misterio del universo? ")
respuesta_sentido_universo = respuesta_sentido_universo.lower().strip().split()
respuesta_sentido_universo = ' '.join(respuesta_sentido_universo)

print(respuesta_sentido_universo)

if respuesta_sentido_universo == "42" or respuesta_sentido_universo == "cuarenta y dos":
   print("si")
else:
   print("no")
