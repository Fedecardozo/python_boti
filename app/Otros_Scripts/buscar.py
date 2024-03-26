def Imprimir(elements):
    i=0
    for el in elements:
        print("indice: ",i)
        print("element: ",el.text)
        i = i + 1

def ObtenerElement(elemens, name):
    for el in elemens:
        if(el.text == name):
            return el
        
def CortarElements(elements, text):
    i=0
    for el in elements:
        if(el.text == text):
            return i
        i=i+1