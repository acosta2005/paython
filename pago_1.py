# solicitar ingreso al usuario 
precio = int(input("ingrese el precio: "))
monto_pago = int(input("ingrese el pago: "))
# realisar calculos 
vuelto = monto_pago - precio 
# calcular cuanto billetes de a $ 1.000 se requieren 
billetes_1000 = int( vuelto / 1000)
vuelto = vuelto - (billetes_1000 + 1000) #vuelto % 1000
# calcular moneda de a $ 500 se requieren
moneda_500 = int( vuelto / 500)
vuelto = vuelto % 500
# calcular moneda de a $ 100 se requieren
moneda_100 = int( vuelto / 500)
# mostrar el resultado
print(f"- {billetes_1000} billetes de $1.000")
print(f" {moneda_500} moneda de $500")
print(f" {moneda_100} moneda de $100")
