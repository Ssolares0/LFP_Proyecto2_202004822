from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import BOLD
import tkinter as tk
import webbrowser
from AnalizadorLexico import *
from AnalizadorSintactico import *
window = Tk()

window.title("Proyecto 2 LFP")
window.geometry('1000x700')
window.configure(background = "pale green")

Label(window,text="Proyecto 1 LFP",bg="pale green",fg="black",font=("times new roman",15,BOLD)).pack()
print("hola")
print("hoadasdas")
def new_File():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file is None:
        return
    text2save = str(labelFrame.get(1.0, END))
    file.write(text2save)
    file.close()
#Funcion para abrir el archivo
def windowOpenFile():
    global objeto
    global ruta
    try:
        ruta = filedialog.askopenfilename(filetypes = (("JSON file","json"),("TXT file","txt"),("all files","*.*")))
        leerRuta = open(ruta,"r")
        labelFrame.insert(END,leerRuta.read())
    except:
        messagebox.showerror("ERROR","No se ha cargado correctamente la ruta")   

#Funcion para guardar el archivo
def windowSaveFile():
    try:    
        modRuta= open(ruta,"w",encoding="utf-8")

        modRuta.write(str(labelFrame.get(1.0,END)))
        messagebox.showinfo(message="Guardado Correctamente", title=":)")
    except:
        messagebox.showinfo(message="Cargue el archivo primero", title=":)")
        windowOpenFile()

#Funcion para guardar el archivo como
def windowSaveAsFile():
    try:
        #SELECCIONAMOS EL ARCHIVO
        ruta = filedialog.asksaveasfile( filetypes=[("Text file",".txt"),("HTML file", ".html"),("All files", ".*"),])

        #ESCRIBIMOS EN EL ARCHIVO SELECCIONADO
        archivoText = str(labelFrame.get(1.0,END))
        ruta.write(archivoText)
        ruta.close()
    except:
        pass 
def display_coordinates(event):
    x = event.x
    y = event.y
    
    labelCoords['text'] = f'(x={x}, y={y})'


def generarMongoDB():
    cadena = open(ruta,"r+",encoding="utf-8")
    cadenaleido = cadena.read()

    mandar = AnalizadorLex()
    

    
    #mandamos el contenido del archivo a analizar
    mandar.analizar(cadenaleido)

    #imprimimos los tokens y errores
    mandar.imprimirTokens()
    mandar.imprimirErrores()

    #mandamos la lista de tokens a analizar
    lsttk = mandar.listaTokens

    #mandamos la lista de tokens a analizar
    sintactico = AnalizadorSintactico(lsttk)
    sintactico.analizar()

    #imprimimos los errores sintacticos
    sintactico.imprimirErrores()

   
    

def mostrarTokens():
    pass

def mostrarErrores():    
    pass

def exit():
    window.destroy()

barra_menu = Menu(window)

#Creamos los menus
mnuArchivo = Menu(barra_menu)
mnuAnalisis = Menu(barra_menu)
mnuTokens = Menu(barra_menu)
mnuErrores = Menu(barra_menu)

#Creamos los comandos deL apartado archivo
mnuArchivo.add_command(label="Nuevo")
mnuArchivo.add_command(label="Abrir", command=windowOpenFile)
mnuArchivo.add_command(label="Guardar", command=windowSaveFile)
mnuArchivo.add_command(label="Guardar como", command=windowSaveAsFile)
mnuArchivo.add_command(label="Salir", command=exit)
mnuArchivo.add_separator()

#Creamos los comandos del apartado analisis
mnuAnalisis.add_command(label="Generar sentencias MongoDB", command=generarMongoDB)

#Creamos los comandos del apartado tokens
mnuTokens.add_command(label="Mostrar tokens", command=mostrarTokens)

#Creamos los comandos del apartado errores
mnuErrores.add_command(label="Mostrar errores", command=mostrarErrores)



# Frame del texto general
labelFrame = tk.Text(window)
labelFrame.place(x=25,y=50,width= 920, height=565)
labelFrame.bind("<Button-1>", display_coordinates)

#Capturar coordenadas x,y del mouse
labelCoords = Label(window)
labelCoords.place(x=25,y=630,width= 100, height=28)




barra_menu.add_cascade(label="Archivo", menu=mnuArchivo)
barra_menu.add_cascade(label="Analisis", menu=mnuAnalisis)
barra_menu.add_cascade(label="Tokens", menu=mnuTokens)
barra_menu.add_cascade(label="Errores", menu=mnuErrores)

#indicamos que la barra de menus esta en la ventana
window.config(menu=barra_menu)

window.mainloop()