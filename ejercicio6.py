productos = []
contador = 0
productos_registrar = int(input("Cuantos productos quiere registrar? "))

for i in range(productos_registrar):
    producto = {}
    producto['nombre'] = input("Introduce el nombre del producto ")
    producto['precio'] = int(input("Introduce el precio del producto "))
    producto['categoria'] = input("Introduce la categoría del producto ")
    productos.append(producto)

print("Tus productos:")
for producto in productos:
    contador += 1
    print(f"{contador}. {producto['nombre']} - {producto['precio']} - Categoría: {producto['categoria']}")

print("Productos baratos (menos de 100€):")
for producto in productos:
    if producto['precio'] < 100:
        print(f"{producto['categoria']}: {producto['precio']}")

print(f"Producto más caro: {max(productos, key=lambda p: p['precio'])}")
print(f"Producto más barato: {min(productos, key=lambda p: p['precio'])}")