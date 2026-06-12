import requests
from bs4 import BeautifulSoup
import csv

libros_data = []

precio_maximo = float(input("Introduce el precio máximo de los libros: "))

for i in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, "html.parser")
    libros = soup.find_all("article", class_="product_pod")
    for libro in libros:
        producto={}
        producto['titulo'] = libro.find("h3").text
        producto['precio'] = libro.find("p", class_="price_color").text
        libros_data.append(producto)

for libro in libros_data:
    print(f"{libro['titulo']} - {libro['precio']}")
    
print(f"Total de libros encontrados: {len(libros_data)}")

libros_filtrados = []

for libro in libros_data:
    precio_limpio = float(libro['precio'].strip().replace("£", "").replace("Â", ""))
    if precio_limpio < precio_maximo:
        libros_filtrados.append(libro)

with open("libros.csv", "w", newline="", encoding="utf-8") as archivo:
    writer = csv.DictWriter(archivo, fieldnames=["titulo", "precio"])
    writer.writeheader()
    writer.writerows(libros_filtrados)

print(f"Libros filtrados: {len(libros_filtrados)}")

print("Archivo libros.csv creado")