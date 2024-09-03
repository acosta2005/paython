def calcular_precio_total(libros_comprados, precios):
    total_precio = 0
    for libro, cantidad in libros_comprados.items():
        total_precio += precios[libro] * cantidad
    return total_precio

def aplicar_descuento(total_precio, cantidad_libros, tipo_descuento):
    descuentos = {
        '4_diferentes': 0.20,  # 20% descuento por 4 libros diferentes
        '2_diferentes': 0.15,   # 15% descuento por 2 libros diferentes
        '4_mismo': 0.10,        # 10% descuento por 4 libros del mismo tipo
        '2_mismo': 0.05         # 5% descuento por 2 libros del mismo tipo
    }
    
    if tipo_descuento in descuentos:
        return total_precio * (1 - descuentos[tipo_descuento])
    return total_precio

def main():
    precios = {
        'Cocina': 5500,
        'Arte': 4500,
        'Religioso': 6500,
        'Novelas': 5000
    }
    
    clientes = []
    cantidad_clientes = int(input("Ingrese el número de clientes: "))
    
    for i in range(cantidad_clientes):
        print(f"\nDatos del cliente {i + 1}:")
        libros_comprados = {libro: 0 for libro in precios.keys()}
        
        for libro in precios.keys():
            cantidad = int(input(f"Cantidad de libros de '{libro}': "))
            libros_comprados[libro] = cantidad
        
        total_libros = sum(libros_comprados.values())
        total_precio = calcular_precio_total(libros_comprados, precios)
        tipo_descuento = None
        
        # Determinar el tipo de descuento aplicable
        if all(cantidad > 0 for cantidad in libros_comprados.values()):
            if total_libros >= 4:
                tipo_descuento = '4_diferentes'
            elif total_libros >= 2:
                tipo_descuento = '2_diferentes'
        
        for cantidad in libros_comprados.values():
            if cantidad >= 4:
                tipo_descuento = '4_mismo'
            elif cantidad >= 2:
                tipo_descuento = '2_mismo'
        
        if tipo_descuento:
            total_precio = aplicar_descuento(total_precio, total_libros, tipo_descuento)
        
        clientes.append({
            'id': i + 1,
            'libros_comprados': libros_comprados,
            'total_precio': total_precio,
            'descuento_total': tipo_descuento
        })
    
    # Mostrar la cantidad total de libros comprados por cliente
    for cliente in clientes:
        print(f"\nCliente {cliente['id']}:")
        for libro, cantidad in cliente['libros_comprados'].items():
            print(f"{libro}: {cantidad} libro(s)")
        print(f"Total a pagar: ${cliente['total_precio']:.2f}")
    
    # Encontrar el cliente que compró más libros
    cliente_mas_libros = max(clientes, key=lambda x: sum(x['libros_comprados'].values()))
    print(f"\nCliente que compró más libros: Cliente {cliente_mas_libros['id']} con {sum(cliente_mas_libros['libros_comprados'].values())} libros.")
    
    # Encontrar el cliente(s) que tuvo más descuento
    # En este caso, buscamos el tipo de descuento más alto.
    max_descuento = max(clientes, key=lambda x: {
        '4_diferentes': 20,
        '2_diferentes': 15,
        '4_mismo': 10,
        '2_mismo': 5
    }.get(x['descuento_total'], 0))
    
    print(f"\nCliente(s) con más descuento aplicado:")
    for cliente in clientes:
        if cliente['descuento_total'] == max_descuento['descuento_total']:
            descuento_value = {
                '4_diferentes': 20,
                '2_diferentes': 15,
                '4_mismo': 10,
                '2_mismo': 5
            }.get(cliente['descuento_total'], 0)
            print(f"Cliente {cliente['id']} con {descuento_value}% de descuento.")

if __name__ == "__main__":
    main()
