precios = {
    "cafe": 1500,
    "te": 1000,
    "jugo natural": 2000,
    "pastel de chocolate": 2500,

}

pedidos = {
    "cafe": int(input("ingrese la cantidad de cafe: ")),
    "te":  int(input("ingrese la cantidad de cafe: ")),
    "jugo natural": int(input("ingrese la cantidad de jugo natural: ")),
    "pastel de chocolate": int(input("ingrese la cantidad de pastel de chocolate: ")),
    "tarta de frutas": int(input("ingrese la cantidad ded frutas: ")),
}
total = 0
for producto, cantidad in pedidos.items():
    total += cantidad * precios[producto]

print(total)