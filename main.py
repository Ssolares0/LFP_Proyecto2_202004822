from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import BOLD
import tkinter as tk
import webbrowser

window = Tk()
window.title("Proyecto 2 LFP")
window.geometry('1000x700')
window.configure(background = "light blue")

Label(window,text="Proyecto 1 LFP",bg="light blue",fg="black",font=("times new roman",15,BOLD)).pack()

def new_File():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file is None:
        return
    text2save = str(labelFrame.get(1.0, END))
    file.write(text2save)
    file.close()

def windowOpenFile():
    global objeto
    global ruta
    try:
        ruta = filedialog.askopenfilename(filetypes = (("JSON file","json"),("TXT file","txt"),("all files","*.*")))
        leerRuta = open(ruta,"r")
        labelFrame.insert(END,leerRuta.read())
    except:
        messagebox.showerror("ERROR","No se ha cargado correctamente la ruta")   


barra_menu = Menu(window)

#Creamos los menus
mnuArchivo = Menu(barra_menu)
mnuEdicion = Menu(barra_menu)

#Creamos los comandos de los menus

mnuArchivo.add_command(label="Nuevo")
mnuArchivo.add_separator()


labelFrame = tk.Text(window)
labelFrame.place(x=25,y=50,width= 920, height=565)

barra_menu.add_cascade(label="Archivo", menu=mnuArchivo)

#indicamos que la barra de menus esta en la ventana
window.config(menu=barra_menu)

window.mainloop()