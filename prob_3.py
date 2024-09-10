








es_primo = True 

for i in range(2,n):
    resto = n % i 
    if resto == 0:
        es_primo = False
        break
if es_primo:
    print(f"el {n} es primo")
else:
    print(f"el {n} no es primo")