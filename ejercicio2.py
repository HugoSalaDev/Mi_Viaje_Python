nombre = input("Cual es su nombre?")
dinero = int(input("Cuanto dinero tiene?"))

if dinero >= 500:
    print(f"{nombre}, puedes montar un negocio online, tienes {dinero}$")
elif dinero >= 200:
    print(f"{nombre}, puedes comprar un curso profesional, tienes {dinero}$")
elif dinero >= 50:
    print(f"{nombre}, puedes comprar libros y aprender gratis el resto, tienes {dinero}$")
else:
    print(f"{nombre}, empieza ahora, el conocimiento es gratis, tienes {dinero}$")