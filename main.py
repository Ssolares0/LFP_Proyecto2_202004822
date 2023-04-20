from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import BOLD
import tkinter as tk
from prettytable import PrettyTable
import webbrowser
from AnalizadorLexico import *
from AnalizadorSintactico import *
from bases import *
global ruta



window = Tk()

window.title("Proyecto 2 LFP")
window.geometry('1200x700')
window.configure(background = "SteelBlue1")

Label(window,text="Proyecto 2 LFP",bg="SteelBlue1",fg="black",font=("times new roman",15,BOLD)).pack()



    
    
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

def new_File():
    
    
    
        global ruta
        
        try:
                obtenerRuta= open(ruta,"r")
                print(obtenerRuta)
                msg_box = tk.messagebox.askquestion('Exit Application', '   Desea guardar la informacion del archivo actual?   ',
                                                icon='warning')
                if msg_box == 'yes':
                    try:
                        #SELECCIONAMOS EL ARCHIVO
                        ruta = filedialog.asksaveasfile( filetypes=[("Text file",".txt"),("HTML file", ".html"),("All files", ".*"),])

                        #ESCRIBIMOS EN EL ARCHIVO SELECCIONADO
                        archivoText = str(labelFrame.get(1.0,END))
                        ruta.write(archivoText)
                        ruta.close()
                        labelFrame.delete(1.0,END)
                        
                        
                    except:
                        pass 
                else:
                    labelFrame.delete(1.0,END)
                    
        except:
            labelFrame.delete(1.0,END)
              

        
       
                

        
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
    global lsttk2
    global lsttkErrores
    global lsttkErroresSintacticos
    try:
        cadena = open(ruta,"r+",encoding="utf-8")
        cadenaleido = cadena.read()

        mandar = AnalizadorLex()
        

        
        #mandamos el contenido del archivo a analizar
        mandar.analizar(cadenaleido)

        #imprimimos los tokens y errores
        

        #mandamos la lista de tokens a analizar
        lsttk = mandar.listaTokens

        lsttk2=mandar.listaTokensOriginal

        lsttkErrores = mandar.listaErrores
        

        
        #mandamos la lista de tokens a analizar
        sintactico = AnalizadorSintactico(lsttk)
        sintactico.analizar()
        lsttkErroresSintacticos = sintactico.errores

        
        

        #imprimimos los errores sintacticos
        sintactico.imprimirErrores()
        
        mostrarSalida()
        
    except:
        messagebox.showinfo(message=" Primero cargue el archivo", title=":)")
   
    

def mostrarTokens():
    try:
        count=1
        def mostrarDatos(tabla):
            count = 1
            for token in lsttk2:
                
                tabla.insert('',0,text=count,values=(token.lexema,token.linea,token.columna,token.tipo))
                
                count = count + 1
                #tabla.insert('','0',text='2',values=token.linea)
            #tabla.insert('','0',text='1',values='hola')
        
        
        
        x = PrettyTable()
        x.field_names = ["No","Lexema","linea","columna","tipo"]
        for token in lsttk2:
            x.add_row([count,token.lexema, token.linea, token.columna,token.tipo])
            count = count + 1
        print(x)
        ventana=Tk()
        
        tabla=ttk.Treeview(ventana,columns=('#0','#1','#2','#3','#4'))
        tabla.grid(row=1,column=0,columnspan=2)
        tabla.heading("#0",text="No")
        tabla.heading("#1",text="Lexema")
        tabla.heading("#2",text="linea")
        tabla.heading("#3",text="columna")
        tabla.heading("#4",text="tipo")
        mostrarDatos(tabla)
        ventana.mainloop()
    except:
        messagebox.showinfo(message="Analice Primero el archivo", title=":)")
        
def mostrarErrores():  
    try:  
        count=1
        def mostrarDatos(tabla):
            count = 1
            for error in lsttkErrores:
                
                tabla.insert('','0',text=count,values=(error.descripcion,error.linea,error.columna))
                
                count = count + 1
                #tabla.insert('','0',text='2',values=token.linea)
            #tabla.insert('','0',text='1',values='hola')
        
        
        
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion","linea","columna"]
        for error_ in lsttkErrores:
                x.add_row([error_.descripcion, error_.linea, error_.columna])
        print(x)             
        ventana=Tk()
        
        tabla=ttk.Treeview(ventana,columns=('#0','#1','#2','#3'))
        tabla.grid(row=1,column=0,columnspan=2)
        tabla.heading("#0",text="No")
        tabla.heading("#1",text="Descripcion")
        tabla.heading("#2",text="linea")
        tabla.heading("#3",text="columna")
        
        mostrarDatos(tabla)
        ventana.mainloop()
    except:
        messagebox.showinfo(message="Analice Primero el archivo", title=":)")    
def mostrarErroresSintacticos():
    try:
        
            
        
        count=1
        def mostrarDatos(tabla):
            count = 1
            for error in lsttkErroresSintacticos:
                
                tabla.insert('','0',text=count,values=([error]))
                
                count = count + 1
                #tabla.insert('','0',text='2',values=token.linea)
            #tabla.insert('','0',text='1',values='hola')
        
        
        
        
        
        ventana=Tk()
        
        tabla=ttk.Treeview(ventana,columns=('#0','#1'))
        tabla.grid(row=1,column=0,columnspan=2)
        tabla.heading("#0",text="No")
        tabla.heading("#1",text="Descripcion")
        
        
        mostrarDatos(tabla)
        ventana.mainloop()
    except:
        messagebox.showinfo(message="Analice Primero el archivo", title=":)")   
def mostrarSalida():
        lstSalidas = salidas
        print(lstSalidas)
        labelFrame2.delete(1.0,END)
        for x in lstSalidas:
            labelFrame2.insert(END,f"{x}\n")
        lstSalidas.clear()
            
        
        
    
        
def exit():
    window.destroy()

barra_menu = Menu(window)

#Creamos los menus
mnuArchivo = Menu(barra_menu)
mnuAnalisis = Menu(barra_menu)
mnuTokens = Menu(barra_menu)
mnuErrores = Menu(barra_menu)

#Creamos los comandos deL apartado archivo
mnuArchivo.add_command(label="Nuevo", command=new_File)
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
mnuErrores.add_command(label="Mostrar errores sintacticos", command=mostrarErroresSintacticos)



# Frame del texto general
labelFrame = tk.Text(window)
labelFrame.place(x=25,y=50,width= 520, height=565)
labelFrame.bind("<Button-1>", display_coordinates)

#Capturar coordenadas x,y del mouse
labelCoords = Label(window)
labelCoords.place(x=25,y=630,width= 100, height=28)


#frame dek segundo texto
labelFrame2 = tk.Text(window)
labelFrame2.place(x=630,y=50,width= 520, height=565)




barra_menu.add_cascade(label="Archivo", menu=mnuArchivo)
barra_menu.add_cascade(label="Analisis", menu=mnuAnalisis)
barra_menu.add_cascade(label="Tokens", menu=mnuTokens)
barra_menu.add_cascade(label="Errores", menu=mnuErrores)

#indicamos que la barra de menus esta en la ventana
window.config(menu=barra_menu)

window.mainloop()