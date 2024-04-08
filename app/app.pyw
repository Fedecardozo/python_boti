import boti
from tkinter import * 
from tkinter import ttk
import tkinter.messagebox as msjBox

# ----------------------------- INICIO FUNCIONES --------------------------

def centrar_ventana(ventana, app_ancho, app_largo):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho/2) - (app_ancho/2))
    y = int((pantalla_largo/2) - (app_largo/2))
    return ventana.geometry(f"{app_ancho}x{app_largo}+{x}+{y}")

def validarZona():
    zone = entryZona.get()
    retorno = True
    if(zone == ""):
        msjBox.showerror("Error!","El campo zona no puede estar vacio!")
        retorno = False
    else:
        zone = int(zone)
        if(zone < 1):
            retorno = False
            msjBox.showerror("Error!","La zona no puede ser menor a 1!")
        elif(zone > 24):
            retorno = False
            msjBox.showerror("Error!","La zona no puede ser mayor a 24!")
    
    return retorno

def validarPrecios():
    min = entry.get()
    max = entryMax.get()
    retorno = True

    if(min == "" or max == ""):
        msj = "El campo precio minimo no puede estar vacio!"
        retorno = False

        if(min == "" and max == ""):
            msj = "Los campos precios minimo y maximo no pueden estar vacios!"
        elif(max == ""):
            msj = "El campo precio maximo no puede estar vacio!"

        msjBox.showerror("Error!",msj)
    else:
        min = int(min)
        max = int(max)
        if(min == 0 and max == 0):
            retorno = False
            msjBox.showerror("Error!","Los precios minimo y maximo. No pueden ser menor a 1!")
        elif(min < 1):
            retorno = False
            msjBox.showerror("Error!","El precio minimo no puede ser menor a 1!")
        elif(max < 1):
            retorno = False
            msjBox.showerror("Error!","El precio maximo no puede ser menor a 1!")
        elif(min >= max):
            retorno = False
            msjBox.showerror("Error!","El precio minimo no puede ser mayor o igual al precio maximo!")

    return retorno

def confirmar():
    res = msjBox.askyesno("Confirmación!", "¿Estas seguro de publicar?")
    if(res):
        rta = msjBox.showinfo("Advertencia!","UNA VEZ QUE TOQUE 'Aceptar' NO TOQUE EL MOUSE Y NIGUNA TECLA HASTA QUE TERMINE!")
        return rta == "ok"

def clickPublicar():
    if(validarPrecios() and validarZona() and confirmar()):
        #llamar a boti
        boti.publicarBoti(int(entry.get()),int(entryMax.get()),int(entryZona.get()),var.get(),select_options.get())

def validate_input(new_text):
    # Verificar si el nuevo texto contiene solo números
    return new_text.isdigit() or new_text == ""

# ----------------------------- FIN FUNCIONES --------------------------


# INCIO PROGRAMA
raiz = Tk()
raiz.resizable(width="false",height="false")

# Registrar la función de validación
validate_numeric_input = raiz.register(validate_input)

#Frame izquierdo
frameIzq = Frame(raiz,bg="#262c40")
fondo = PhotoImage(file="C:\\Users\\Fedec\\SanJorge\\0003_AUTOMATIZACION\\app\\img\\fondoJorge.png")
lblImage = Label(frameIzq,image=fondo,bg="#262c40")
lblImage.pack(side="left")
frameIzq.pack()

#Frame Derecho
frameDer = Frame(frameIzq,padx=10)
frameDer.config(bg="#8AB4F8")
frameDer.pack(side="right",fill="y")

# TITULO
raiz.title("Bot publicador Facebook")
raiz.iconbitmap("C:\\Users\\Fedec\\SanJorge\\0003_AUTOMATIZACION\\app\\img\\icon.ico")



# ------------------------- INICIO RADIO BUTTONS -----------------------------------

frame1 = Frame(frameDer,bg="#8AB4F8")
frame1.pack(fill="x", pady=10)

# Variable de control para los botones de radio
var = IntVar(value=1)

# Fieldset Facebook a publicar
fieldset = LabelFrame(frame1, text="Facebook en el que se va a publicar",padx=10,pady=10)
fieldset.config(bg="#8AB4F8")
fieldset.pack(fill="x")

# Crear botones de radio
radio1 = Radiobutton(fieldset, text="Opción 1", variable=var, value=1,bg="#8AB4F8",cursor="hand2")
radio2 = Radiobutton(fieldset, text="Opción 2", variable=var, value=2,bg="#8AB4F8",cursor="hand2")

radio1.pack(pady=5)
radio2.pack(pady=5)

# ------------------------- FIN RADIO BUTTONS -----------------------------------

# ------------------------- INICIO COMBO BOX ------------------------------------
frame2 = Frame(frameDer,bg="#8AB4F8")
frame2.pack(fill="x",  pady=10)

# Fieldset que vas a publicar, combo box
fieldset2 = LabelFrame(frame2, text="Que vas publicar",padx=10,pady=10)
fieldset2.config(bg="#8AB4F8")
fieldset2.pack(fill="x")

opciones = ["Termotanques", "Cocinas", "Tanques", "Aires"]

select_options = StringVar()
select_options.set(opciones[0])

combo_box = ttk.Combobox(fieldset2, values=opciones, textvariable=select_options, state="readonly",cursor="hand2")
combo_box.pack()
    
# ------------------------- FIN COMBO BOX ------------------------------------

# ------------------------- INICIO ENTRY PRECIO ------------------------------
frame3 = Frame(frameDer,bg="#8AB4F8")
frame3.pack(fill="x",  pady=10)

# Precio minimo y maximo
fieldset3 = LabelFrame(frame3, text="Precios a publicar",padx=10,pady=10)
fieldset3.config(bg="#8AB4F8")
fieldset3.pack(fill="x")

# Ingresar precios minimo
lblMinimo = Label(fieldset3, text="Precio minimo:",bg="#8AB4F8")
lblMinimo.grid(row=0, column=0, pady=5)

entry = Entry(fieldset3, justify="center",validate="key", validatecommand=(validate_numeric_input, '%P'))
entry.grid(row=0, column=1)

# Ingresar precios maximo
lblMaximo = Label(fieldset3, text="Precio maximo:",bg="#8AB4F8")
lblMaximo.grid(row=1, column=0, pady=5)

entryMax = Entry(fieldset3, justify="center",validate="key", validatecommand=(validate_numeric_input, '%P'))
entryMax.grid(row=1, column=1)

# ------------------------- FIN ENTRY PRECIO ------------------------------

# ----------------------- INICIO ZONA PUBLICAR ------------------------------
frame4 = Frame(frameDer,bg="#8AB4F8")
frame4.pack(fill="x", pady=10)

# Zona a publicar
fieldset4 = LabelFrame(frame4, text="Zona a publicar",padx=10,pady=10,bg="#8AB4F8")
fieldset4.pack(fill="x")

# Ingresar Zona
lblZona = Label(fieldset4, text="Ingrese zona(1 a 24):",bg="#8AB4F8")
lblZona.grid(row=0,column=0)

entryZona = Entry(fieldset4, justify="center",validate="key", validatecommand=(validate_numeric_input, '%P'))
entryZona.grid(row=0,column=1)

# ----------------------- FIN ZONA PUBLICAR ------------------------------

# ----------------------- INICIO BOTONES ------------------------------

# FRAME BOTONES
frameBtns = Frame(frameDer,bg="#8AB4F8",pady=10)
frameBtns.pack(fill="x", pady=15)

# Boton salir
btnSalir = Button(frameBtns,text="Salir",width=15,padx=5,pady=5,bg="red",cursor="hand2", command=exit)
btnSalir.grid(row=0,column=0,padx=5)

# Boton publicar
btnPublicar = Button(frameBtns, text="Publicar",width=20,padx=5,pady=5,bg="green",cursor="hand2",command=clickPublicar)
btnPublicar.grid(row=0,column=1,padx=5)

# ----------------------- FIN BOTONES ------------------------------

raiz.mainloop()

