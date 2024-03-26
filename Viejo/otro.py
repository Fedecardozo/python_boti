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

# Obtener las cookies
cookies = driver.get_cookies()

# Guardar las cookies en un archivo
with open('cookies.pkl', 'wb') as cookies_file:
    pickle.dump(cookies, cookies_file)

# Cerrar el navegador
driver.quit()


