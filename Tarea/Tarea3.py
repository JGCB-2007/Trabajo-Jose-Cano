while True:
    articulo = input("Ingrese el nombre del artículo: ")
    precio_por_docena = float(input("Ingrese el precio por docena del artículo: "))
    cantidad_docenas = int(input("Ingrese la cantidad de docenas a comprar: "))
    
    subtotal = precio_por_docena * cantidad_docenas
    
    if cantidad_docenas > 3:
        descuento = subtotal * 0.15
        unidades_obsequio = cantidad_docenas - 3
    else:
        descuento = subtotal * 0.10
        unidades_obsequio = 0
    
    total_a_pagar = subtotal - descuento
    
    print("\n--- FACTURA ---")
    print(f"Artículo: {articulo}")
    print(f"Cantidad de docenas: {cantidad_docenas}")
    print(f"Precio por docena: C${precio_por_docena:.2f}")
    print(f"Subtotal: C${subtotal:.2f}")
    print(f"Descuento aplicado: C${descuento:.2f}")
    print(f"Total a pagar: C${total_a_pagar:.2f}")
    print(f"Unidades de obsequio: {unidades_obsequio}")
    
    repetir = input("¿Quieres repetir el programa? (si/no): ").strip().lower()
    if repetir == "no":
        print("Se acabó.")
        break
