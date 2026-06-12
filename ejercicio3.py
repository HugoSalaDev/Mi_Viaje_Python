personas_en_equipo = int(input("¿Cuántas personas hay en tu equipo? "))
nombres = []
for i in range(personas_en_equipo):
    
    nombres.append(input(f"Nombre de la persona {i + 1}: "))

print("Tu equipo:")
for j in range(personas_en_equipo):
    print(f"{j + 1}. {nombres[j]}")

