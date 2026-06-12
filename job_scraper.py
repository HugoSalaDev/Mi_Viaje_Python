import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def obtener_ofertas(url):
    # Extrae ofertas de una página
    # Devuelve lista de diccionarios
    todas_ofertas = []
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, "html.parser")
    ofertas = soup.find_all('div', class_='alert')
    for oferta in ofertas:
        datos={}
        datos['titulo'] = oferta.find('strong').text.replace(":", "").strip()
        datos['descripcion'] = oferta.get_text().replace(oferta.find("strong").text, "").strip()
        datos['enlace'] = "https://realpython.com" + oferta.find("a", class_="btn")["href"]

        todas_ofertas.append(datos)

    return todas_ofertas

def guardar_csv(datos, nombre_archivo):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["titulo", "descripcion", "enlace"])
        writer.writeheader()
        writer.writerows(datos)

def mostrar_resumen(datos):
    contador = 0
    for oferta in datos:
        contador+=1
        print(f"{contador}. {oferta['titulo']} - {oferta['enlace']}")
    

# Programa principal

todas_las_ofertas = []

url = f"https://realpython.com/jobs/"
ofertas = obtener_ofertas(url)
todas_las_ofertas.extend(ofertas)

guardar_csv(todas_las_ofertas, "ofertas.csv")
print(f"Total ofertas extraídas: {len(todas_las_ofertas)}")
mostrar_resumen(todas_las_ofertas)