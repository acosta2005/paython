n = int(input("ingresa un numero entero: "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} no es numero primo")
        break
    else:
        print(f"{n} es numero primo")
        break
    

    