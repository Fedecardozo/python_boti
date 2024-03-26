from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
import buscar
import pyautogui

path_driver = 'C:\\Users\\Fedec\\SanJorge\\0003_AUTOMATIZACION\\DRIVER\\chromedriver.exe'

service = Service(path_driver)

# Configuración de opciones de Chrome para desactivar notificaciones
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Objeto driver con opciones personalizadas
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

url='https://www.facebook.com/'

driver.get(url)

#LOGIN INPUTS
email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
btnSesion = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

email.send_keys('Cla-alvarez98@hotmail.com')
password.send_keys('eriklamela')
btnSesion.click()

#ABRIR MARKETPLACE
time.sleep(3)
driver.execute_script("window.open('about:blank', '_blank');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.facebook.com/marketplace/create/item')

# Obtener elementos
time.sleep(2)
spans = driver.find_elements(By.TAG_NAME,'span')
detalles = buscar.ObtenerElement(spans,'Más detalles')
ocultarAmigos = buscar.ObtenerElement(spans, 'Ocultar a amigos')
fotosAdd = buscar.ObtenerElement(spans, 'Agregar fotos')

# Abrir mas detalles
# detalles.click()

# time.sleep(1)
# area = driver.find_elements(By.TAG_NAME,'textarea')
# # Descripcion
# area[0].send_keys("Esto es una descripcion")
# # Etiquetas
# # area[1]

# # Cerrar detalles
# time.sleep(1)
# detalles.click()

# # Ocultar amigos
# time.sleep(1)
# ocultarAmigos.click()

time.sleep(1)
# Encontrar todos los elementos de entrada (inputs)
inputs = driver.find_elements(By.TAG_NAME, 'input')

time.sleep(1)
# Titulo
inputs[5].send_keys("Hasta Agotar stock termotanques escorial señorial")
# Precio
inputs[6].send_keys("140000")

# # Obtener Labels
# labels = driver.find_elements(By.TAG_NAME,'label')

# # Categoria
# time.sleep(1)
# labels[5].click()
# time.sleep(1) # 177 a 220
# categorias = driver.find_elements(By.CSS_SELECTOR,'.x193iq5w')
# time.sleep(1)
# min = buscar.CortarElements(categorias,'Herramientas')
# max = min + 4
# numAleatorio = random.randint(min,max)
# time.sleep(1)
# categorias[numAleatorio].click()

# # Cerrar detalles
# time.sleep(1)
# detalles.click()

# # Estado Nuevo
# time.sleep(2)
# labels[6].click()
# time.sleep(2)
# nuevo = driver.find_element(By.CSS_SELECTOR,'.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.xudqn12.x3x7a5m.x6prxxf.xvq8zen.xk50ysn.xzsf02u.x1yc453h')
# nuevo.click()

# Abrir fotos
# fotosAdd.click()

# Esperar un breve momento para que la ventana de carga de archivos aparezca
# time.sleep(2)

# Ruta al archivo que deseas subir
# archivo_ruta = 'C:\\Users\\Fedec\\SanJorge\\TERMOTANQUES\\0001\\0001.jpg'

# Utilizar pyautogui para escribir la ruta del archivo y presionar Enter
# pyautogui.write(archivo_ruta)
# pyautogui.press('enter')


while True:
    if(input("Ingrese 'x' para cortar: ") == 'x'):
        driver.quit()
        break
    pass