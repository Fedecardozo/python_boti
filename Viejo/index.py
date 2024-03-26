# Librerias
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

# Configuración de opciones de Chrome para desactivar notificaciones
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Objeto driver
driver = webdriver.Chrome(service=service,options=chrome_options)

# Configuracion driver
driver.maximize_window()

# Obtener un URL con el driver
driver.get(url)

# Inputs
email = driver.find_element('xpath', '//*[@id="email"]') 
password = driver.find_element('xpath', '//*[@id="pass"]') 
btnSesion = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button') 

# Acciones
email.send_keys("fedecardozocab")
password.send_keys("fede40812362")

# Hacer clic en el botón
btnSesion.click()

time.sleep(3)
driver.get('https://www.facebook.com/marketplace/create/item')

#inputs market place
time.sleep(5)
titulo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[6]/div/div/div[3]/div[2]/div[1]/div/div[4]/div[1]/div[2]/div/div/div[5]/div/div/label/div/div/input')

titulo.send_keys("Holaaa!")

# Bucle infinito para mantener el script en ejecución
while True:
    pass