import pyautogui
import time
import Elementos
import Funciones
import Textos
import Descripcion
import Zonas
import random


def marketplace(carpeta, fotos_path, zona, min, max, facebook, producto, ocultarAmigo=True):
    # Esperar 5 segundos para volver a publicar
    time.sleep(3)
    Funciones.ClickUrl("https://www.facebook.com/marketplace/create/item")
    time.sleep(7)

    # Cargar archivos
    Funciones.CargarArchivos(fotos_path, carpeta, producto)

    # Ocultar amigos
    time.sleep(1)
    pyautogui.moveTo(350, 800)
    time.sleep(1)

    # Scroll
    Funciones.scrollNegativoFacebook(facebook)
    if(ocultarAmigo):
        pyautogui.click()

    # Detalles abrir
    time.sleep(0.5)
    # pyautogui.click("detalles.png")
    Funciones.Click(Elementos.Detalles)

    # Descripcion
    time.sleep(0.7)
    descrip = Descripcion.ObtenerDescripcion(producto)
    Funciones.CopiarPegar(Elementos.Descripcion,descrip)
    time.sleep(2)

    # Ubicacion
    Funciones.CargarUbicacion(zona)

    # Detalles cerrar
    time.sleep(0.5)

    # Scroll
    Funciones.scrollFacebook(facebook, producto)

    time.sleep(0.2)
    pyautogui.click()

    # Volver arriba
    time.sleep(0.5)
    pyautogui.scroll(100)

    # Titulo
    Funciones.CopiarPegar(Elementos.Titulo,Textos.ObtenerTitulo(Textos.GetTitulo(producto)))
    time.sleep(1.5)

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

# INICIO CODIGO NORMAL 
    
# print("Facebook en el que se va a publicar")
# print("1- Clari")
# print("2- Agus, Fede, Lea y Colo")

# facebook = int(input("Ingrese Opcion: "))
# min = int(input("Ingrese precio minimo: "))
# max = int(input("Ingrese precio maximo: "))
# carpeta = input("Ingrese numero de carpeta: ")

def publicarBoti(min, max, zone, facebook, producto, ocultarAmigos):
    num = 0
    zona = Zonas.ObtenerZona(zone)
    carpeta = Funciones.getCarpeta(zone)

    time.sleep(2)
    Funciones.AbriNavegador()
    time.sleep(6)

    for i in range(len(zona)):
        if(i>0):
            time.sleep(12)
        
        fotos_path = Funciones.NumerosSecuenciales(num,num+3)
        num = num + 3
        strCarpeta = '00'
        time.sleep(2)
        pathCarpeta = strCarpeta + carpeta
        marketplace(pathCarpeta,fotos_path,zona[i],min,max,facebook,producto,ocultarAmigos)

# publicarBoti(min,max,carpeta,zona,facebook)

# FIN CODIGO NORMAL


# PUBLICAR DE MANERA CONTINUA
# for j in range(10,18):
#     zona = Zonas.ObtenerZona(j)
#     num = 0
#     strCarpeta = '00'
#     pathCarpeta = strCarpeta + str(j)
#     min = random.randint(20,40)
#     max = random.randint(50,99)

#     for i in range(len(zona)):    
#         fotos_path = Funciones.NumerosSecuenciales(num,num+3)
#         num = num + 3
#         time.sleep(2)
#         marketplace(pathCarpeta,fotos_path,zona[i],min,max,1)
#         time.sleep(12)