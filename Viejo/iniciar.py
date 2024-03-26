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

# Bucle infinito para mantener el script en ejecución
while True:
    pass