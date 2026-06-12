import requests
from bs4 import BeautifulSoup
import csv

def obtener_frases(url):
    todas_frases=[]
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, "html.parser")
    frases = soup.find_all("div", class_="quote")
    for frase in frases:
        pagina={}
        pagina['frase'] = frase.find('span', class_="text").text
        pagina['autor'] = frase.find('small', class_="author").text
        todas_frases.append(pagina)
    return todas_frases

def guardar_csv(datos, nombre_archivo):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["frase", "autor"])
        writer.writeheader()
        writer.writerows(datos)

todas_las_frases = []

for i in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{i}/"
    frases = obtener_frases(url)
    todas_las_frases.extend(frases)

guardar_csv(todas_las_frases, "frases.csv")
print(f"Total frases extraídas: {len(todas_las_frases)}")