from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import csv

options = Options()
options.add_argument(r"--user-data-dir=C:\Users\hugop\selenium_profile")



def obtener_productos(keyword):
    # Abre Wallapop, busca keyword, extrae títulos y precios
    # Devuelve lista de diccionarios
    todos_anuncios = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"https://es.wallapop.com/search?keywords={keyword}&order_by=most_relevance")
    time.sleep(4)
    titulos = driver.find_elements(By.CLASS_NAME, 'item-card_ItemCard__title__5TocV')
    precios = driver.find_elements(By.CLASS_NAME, 'item-card_ItemCard__price__pVpdc')

    for titulo, precio in zip(titulos,precios):
        producto = {}
        producto['titulo'] = titulo.text
        producto['precio'] = precio.text
        todos_anuncios.append(producto)

    return todos_anuncios
    


def guardar_csv(datos, nombre_archivo):
    # Ya sabes hacerlo
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["titulo", "precio"])
        writer.writeheader()
        writer.writerows(datos)

def mostrar_resumen(datos):
    contador = 0
    for anuncio in datos:
        contador+=1
        print(f"{contador}. {anuncio['titulo']} - {anuncio['precio']}")

# Programa principal
keyword = input("¿Qué producto quieres buscar? ")
productos = obtener_productos(keyword)
guardar_csv(productos, "wallapop.csv")
mostrar_resumen(productos)