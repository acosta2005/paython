# verifcar si un numero es multiplo de otro 
a = int(input["ingresar el primer numero: "])
b = int(input["ingresar el segundo numero: "])

dtv = a / b 
resto = a % b 

if resto == 0:
    print(f"(a)es multiplo de (b)")
else:
    print(f"(a) no es multiplo de (b)")
    