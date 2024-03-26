import pyautogui
import time
import random
import Elementos
import clipboard

def NumerosSecuenciales(min,max):
    # Generar una lista de strings con formato "0001.jpg", "0002.jpg", etc.
    imagenes = ['"{:04d}.jpg"'.format(i+1) for i in range(min,max)]

    # Unir las cadenas en un solo string
    resultado = ' '.join(imagenes)

    return resultado

def CargarArchivos(fotos_path,carpeta):
    time.sleep(1)
    # pyautogui.click("fotos.png")
    Click(Elementos.Fotos)

    time.sleep(1)
    pyautogui.write(fotos_path)

    # archivo_ruta = 'C:\\Users\\Fedec\\SanJorge\\COMBO_TANQUES\\' + carpeta
    archivo_ruta = 'C:\\Users\\Fedec\\SanJorge\\TERMOTANQUES\\' + carpeta
    # archivo_ruta = 'C:\\Users\\Fedec\\SanJorge\\COCINAS\\' + carpeta
    # archivo_ruta = 'C:\\Users\\Fedec\\SanJorge\\AIRES\\' + carpeta
    ClickUrl(archivo_ruta)

    time.sleep(1)
    # pyautogui.press("enter")
    pyautogui.moveTo(1132,792)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)

def ClickUrl(ruta):
    time.sleep(0.5)
    pyautogui.moveTo(800,60)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write(ruta)
    time.sleep(0.5)
    pyautogui.press("enter")

def CargarTexto(coordenada,text):
    time.sleep(1)
    # pyautogui.click(img)
    Click(coordenada)
    time.sleep(1)
    pyautogui.write(text)

def CopiarPegar(coordenada,text):
    time.sleep(1)
    clipboard.copy(text)
    time.sleep(1)
    Click(coordenada)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')

def CargarCategoria():
    categorias = Elementos.Categorias
    max = len(categorias) -1
    indice = random.randint(0,max)

    time.sleep(0.5)
    # pyautogui.click("categoria.png")
    Click(Elementos.Categoria)

    time.sleep(1)
    Click(categorias[indice])

def CargarEstado():
    time.sleep(1)
    # pyautogui.click("estado.png")
    Click(Elementos.Estado)

    time.sleep(0.5)
    # pyautogui.click("nuevo.png")
    Click(Elementos.Nuevo)


def ImprimirCoordenadas(img, name):
    time.sleep(1)
    coordena = pyautogui.locateOnScreen(img)
    print(name)
    print(coordena)
    time.sleep(1)

def Click(coordena):
    pyautogui.click(*pyautogui.center(coordena))

def CargarUbicacion(ubi):
    time.sleep(1)
    pyautogui.scroll(-550)
    pyautogui.click()
    clipboard.copy(ubi)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    # pyautogui.write(ubi,0.01)
    time.sleep(1.5)
    # pyautogui.click("acassuso.png")
    Click(Elementos.Ubicacion)

def GenerarPrecio(min, max):
    num = random.randint(min,max)
    strNum = str(num)
    indice = random.randint(0,1)
    vec = ["000","999"]
    return strNum + vec[indice]

def AbriNavegador():
    pyautogui.hotkey("win","r")
    time.sleep(1)
    pyautogui.write("chrome.exe --start-maximized", 0.03)
    time.sleep(2)
    pyautogui.press("enter")