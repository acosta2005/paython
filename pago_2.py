# solicitar ingreso del lado del cuadrado al usuario
lado = float(input(" ingrese el lado del cuadrado: "))
# calcular el area del cuadrado
area = lado ** 2
# calcular el area del triangulo equilatero
area_triangulo = ((3 ** (0,5))/4) * (lado ** 2)
# calcular el area de un pentagono regular
are_pent = (lado ** 2 * (25 + 10 * 5 ** (0,5)) ** (0,5))/4
# mostrar resultado
print(f"el area del cuadrado es: {area:.2f}")
print(f"el area del triangulo es: {area_triangulo:.2f}")
print(f"el area del pentagono es: {area_pent:.2f}")