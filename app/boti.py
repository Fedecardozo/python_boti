import pyautogui
import time
import Elementos
import Funciones
import Textos
import Descripcion
import Zonas


def marketplace(carpeta, fotos_path, zona, min, max, facebook):
    # Esperar 5 segundos para volver a publicar
    time.sleep(3)
    Funciones.ClickUrl("https://www.facebook.com/marketplace/create/item")
    time.sleep(7)

    # Cargar archivos
    Funciones.CargarArchivos(fotos_path, carpeta)

    # Ocultar amigos
    time.sleep(1)
    pyautogui.moveTo(350, 800)
    time.sleep(1)

    #Clari 700. demas 750
    if(facebook == 1): #clari
        pyautogui.scroll(-700)   
    elif(facebook == 2):
        pyautogui.scroll(-750)

    pyautogui.click()

    # Detalles abrir
    time.sleep(0.5)
    # pyautogui.click("detalles.png")
    Funciones.Click(Elementos.Detalles)

    # Descripcion
    time.sleep(0.7)
    Funciones.CopiarPegar(Elementos.Descripcion,Descripcion.Termotanques)
    time.sleep(2)

    # Ubicacion
    Funciones.CargarUbicacion(zona)

    # Detalles cerrar
    time.sleep(0.5)

    if(facebook == 1):
        # pyautogui.scroll(840) #Aires clari
        pyautogui.scroll(800) #Termotanques/Tanques clari
        # pyautogui.scroll(930) #Cocinas
    elif(facebook == 2):
        # pyautogui.scroll(910) #Cocinas
        pyautogui.scroll(780) #Termotanques/Tanques

    time.sleep(0.2)
    pyautogui.click()

    # Volver arriba
    time.sleep(0.5)
    pyautogui.scroll(100)

    # Titulo
    Funciones.CopiarPegar(Elementos.Titulo,Textos.ObtenerTitulo(Textos.titulos_termotanques))
    time.sleep(1.2)

    # Precio
    Funciones.CargarTexto(Elementos.Precio,Funciones.GenerarPrecio(min,max))

    # Categoria
    Funciones.CargarCategoria()

    # Estado
    Funciones.CargarEstado()

    # Cerrar Detalles
    time.sleep(0.2)
    pyautogui.click()

    # Siguiente
    Funciones.Click(Elementos.Siguiente)

    # Publicar
    time.sleep(0.5)
    # Funcion
    Funciones.Click(Elementos.Publicar)

print("Facebook en el que se va a publicar")
print("1- Clari")
print("2- Agus, Fede, Lea y Colo")
facebook = int(input("Ingrese Opcion: "))

# print("Facebook en el que se va a publicar")
# print("1- Termotanques")
# print("2- Cocinas")
# print("3- Aires")
# print("4- Tanques")
# producto = int(input("Ingrese Opcion: "))

min = int(input("Ingrese precio minimo: "))
max = int(input("Ingrese precio maximo: "))
num = 0
carpeta = input("Ingrese numero de carpeta: ")
zona = Zonas.ObtenerZona(int(input("Ingrese numero de zona: ")))
# carpeta = "26"
time.sleep(2)
Funciones.AbriNavegador()
time.sleep(5)

for i in range(len(zona)):    
    fotos_path = Funciones.NumerosSecuenciales(num,num+3)
    num = num + 3
    strCarpeta = '00'

    time.sleep(2)
    pathCarpeta = strCarpeta + carpeta
    marketplace(pathCarpeta,fotos_path,zona[i],min,max,facebook)
    time.sleep(12)