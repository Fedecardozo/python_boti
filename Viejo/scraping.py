import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pickle

# Iniciar con URL
url = 'https://www.facebook.com'

# Ruta al controlador de Chrome
path_driver = "C:\\Users\\Fedec\\SanJorge\\0003_AUTOMATIZACION\\DRIVER\\chromedriver.exe"

# Configuración del servicio
service = Service(path_driver)

# Cargar las cookies desde el archivo
with open('cookies.pkl', 'rb') as cookies_file:
    cookies = pickle.load(cookies_file)

# Configurar el navegador con las cookies cargadas
driver = webdriver.Chrome(service=service)
driver.get(url)

for cookie in cookies:
    driver.add_cookie(cookie)

# Cerrar el navegador
driver.quit()


#OTRO SCRIPT DEBERIA SER#

# Entrar a market place
# Esperar hasta que el elemento esté presente en la página
# market = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div/div[1]/div[1]/ul/li[3]/span/div/a'))
# )
# market.click()

# # Crear publicacion
# # Esperar hasta que el elemento esté presente en la página
# publicacion = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/a/div/div[2]'))
# )
# publicacion.click()

# time.sleep(8)
# driver.get('https://www.facebook.com/marketplace/create/item')

# #inputs market place
# titulo = driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[5]/div/div/label/div/div/input')

# titulo.send_keys("Termontanques electricos y multicas OFERTA!!")


# Bucle infinito para mantener el script en ejecución
while True:
    pass

# Espera de 10 segundos (puedes ajustar este valor según tus necesidades)
# time.sleep(100000)

# Cierra el navegador al finalizar
# driver.quit()