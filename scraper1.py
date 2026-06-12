import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com"
respuesta = requests.get(url)
soup = BeautifulSoup(respuesta.text, "html.parser")

libros = soup.find_all("article", class_="product_pod")

libros_data = []

for libro in libros:
    producto={}
    producto['titulo'] = libro.find("h3").text
    producto['precio'] = libro.find("p", class_="price_color").text
    libros_data.append(producto)

for libro in libros_data:
    print(f"{libro['titulo']} - {libro['precio']}")
    
print(f"Total de libros encontrados: {len(libros_data)}")