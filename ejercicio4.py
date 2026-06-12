gastos_registrar = int(input("Introduce cuantos gastos quieres registrar"))

nombres_gastos = []
cantidades = []

for i in range(gastos_registrar):
    nombres_gastos.append(input(f"Gasto {i + 1} - Nombre: "))
    cantidades.append(int(input(f"Gasto {i + 1} - Cantidad: ")))

print("Tus gastos:")
for i in range(gastos_registrar):
    print(f"{i + 1}. {nombres_gastos[i]}: {cantidades[i]}€")

print(f"Total gastado: {sum(cantidades)}")
print(f"Gasto más alto: {max(cantidades)}")
print(f"Gasto más bajo: {min(cantidades)}")
print(f"Gasto promedio: {sum(cantidades) / len(cantidades)}")