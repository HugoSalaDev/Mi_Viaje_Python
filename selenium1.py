from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://quotes.toscrape.com/js/")

frases = driver.find_elements(By.CLASS_NAME, "text")

for frase in frases:
    print(frase.text)

driver.quit()