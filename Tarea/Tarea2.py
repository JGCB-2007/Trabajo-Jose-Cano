while True:
    articulo = input("Ingrese el nombre del artículo: ")
    precio_unitario = float(input("Ingrese el precio unitario del artículo: "))
    cantidad = int(input("Ingrese la cantidad a comprar: "))
    
    subtotal = precio_unitario * cantidad
    iva = subtotal * 0.15
    descuento = 0
    
    if subtotal > 1000:
        descuento = subtotal * 0.12
    
    total = subtotal + iva - descuento
    
    print("\n--- FACTURA ---")
    print(f"Artículo: {articulo}")
    print(f"Cantidad: {cantidad}")
    print(f"Precio unitario:{precio_unitario:.2f} Cordoba")
    print(f"Subtotal: {subtotal:.2f} Cordoba")
    print(f"IVA (15%): {iva:.2f} Cordoba")
    print(f"Descuento (12% si aplica): {descuento:.2f} Cordoba")
    print(f"Total a pagar: {total:.2f}Cordoba")
    
    repetir = input("¿Quieres repetir el programa? (si/no): ").strip().lower()
    if repetir == "no":
        print("Se acabó.")
        break
