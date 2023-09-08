productos = {
    "producto1": 10,
    "producto2": 20,
    "producto3": 30
}

nombre_producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad: "))

if nombre_producto in productos:
    precio_unitario = productos[nombre_producto]
    total_pagar = precio_unitario * cantidad
    print("Total a pagar:", total_pagar)
else:
    print("El producto no se encuentra disponible.")