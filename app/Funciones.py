import pyautogui
import time
import random
import Elementos
import clipboard
import Producto

def NumerosSecuenciales(min,max):
    # Generar una lista de strings con formato "0001.jpg", "0002.jpg", etc.
    imagenes = ['"{:04d}.jpg"'.format(i+1) for i in range(min,max)]

    # Unir las cadenas en un solo string
    resultado = ' '.join(imagenes)

    return resultado

def CargarArchivos(fotos_path,carpeta,producto):
    time.sleep(1)
    # pyautogui.click("fotos.png")
    Click(Elementos.Fotos)

    time.sleep(1)
    pyautogui.write(fotos_path)

    # archivo_ruta = 'C:\\Users\\Fedec\\SanJorge\\COMBO_TANQUES\\' + carpeta
    archivo_ruta = 'C:\\Users\\Fedec\\SanJorge\\'+Producto.ObtenerNameCarpeta(producto)+'\\' + carpeta
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

# def GenerarPrecio(min, max):
#     num = random.randint(min,max)
#     strNum = str(num)
#     indice = random.randint(0,1)
#     vec = ["000","999"]
#     return strNum + vec[indice]

# def GenerarPrecio(min, max):
#     num = random.randint(min,max)
#     strNum = str(num)
#     azar = random.randint(100,999)
#     return strNum + str(azar)

def GenerarPrecio(min, max):
    num = random.randint(min,max)
    strNum = str(num)
    # 45.999 - 58.999 - 36-999 - 52.372 - 90.000 - 85.000 - 32.999 - gratis - 95.999
    azar = [45999, 58999, 36999, 52372, 90000, 85000, 32999, 0, 95999]
    indice = random.randint(0,len(azar)-1)
    return str(azar[indice])

def AbriNavegador():
    pyautogui.hotkey("win","r")
    time.sleep(1)
    pyautogui.write("chrome.exe --start-maximized", 0.03)
    time.sleep(2)
    pyautogui.press("enter")

def getCarpeta(zone):
    if(zone < 10):
        return "0"+str(zone)
    else:
        return str(zone)
    
def scrollFacebook(opc=1, producto="termotanques"):
    scroll = Producto.ObtenerScroll(producto)
    divScroll = scroll-500
    pyautogui.scroll(500) 
    pyautogui.sleep(0.5)

    if(opc == 1):
        # 840 Aires clari
        # 930 Cocinas clari
        # 800 termos/tanques clari
        pyautogui.scroll(divScroll+20) 
        
    elif(opc == 2):
        # 820 Aires
        # 910 Cocinas
        # 780 Termo/Tanques 
        pyautogui.scroll(divScroll) 

def scrollNegativoFacebook(opc=1):
    if(opc == 1):
        pyautogui.scroll(-700) 
    elif(opc == 2):
        pyautogui.scroll(-750) 