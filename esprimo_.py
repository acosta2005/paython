def es_primo(n):
     for i in range(2, n):
        if n % i == 0:
           return False 
        return True
     
for i in range(1,100): 
     if es_primo(i):
         print(i, end=" ")
""" es_primo = es_primo(8)
if es_primo:
    print("el numero es primo")
else:
    print("el numero no es primo") """

