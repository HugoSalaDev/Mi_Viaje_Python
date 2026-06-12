nombre = input("Cual es tu nombre?")
edad = int(input("Cuantos años tienes?"))
horas_al_dia = int(input("Cuantas horas puedes dedicarle al dia?"))

if horas_al_dia >= 4:
    print(f"{nombre}, en 3 meses puedes tener tu primer cliente, tienes {edad} años")
elif horas_al_dia >= 2:
    print(f"{nombre}, en 6 meses puedes tener tu primer cliente, tienes {edad} años")
elif horas_al_dia == 1:
    print(f"{nombre}, en 1 año puedes tener tu primer cliente, tienes {edad} años")
else:
    print(f"{nombre}, necesitas comprometerte más, tienes {edad} años")