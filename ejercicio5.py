def registrar_gastos(cantidad):
    nombres_gastos = []
    cantidades = []
    for i in range(cantidad):
        nombres_gastos.append(input(f"Gasto {i + 1} - Nombre: "))
        cantidades.append(int(input(f"Gasto {i + 1} - Cantidad: ")))
    
    return nombres_gastos, cantidades

def mostrar_gastos(nombres, cantidades):
    print("Tus gastos:")
    for i in range(len(cantidades)):
        print(f"{i + 1}. {nombres[i]}: {cantidades[i]}€")

def mostrar_estadisticas(cantidades):
    print(f"Total gastado: {sum(cantidades)}")
    print(f"Gasto más alto: {max(cantidades)}")
    print(f"Gasto más bajo: {min(cantidades)}")
    print(f"Gasto promedio: {sum(cantidades) / len(cantidades)}")

cantidad = int(input("¿Cuántos gastos quieres registrar? "))
nombres, cantidades = registrar_gastos(cantidad)
mostrar_gastos(nombres, cantidades)
mostrar_estadisticas(cantidades)