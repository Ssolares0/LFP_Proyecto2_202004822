from Error import *
from Token import *
from tkinter import *
from tkinter import ttk
from prettytable import PrettyTable

class AnalizadorLex:
    def __init__(self) -> None:
        self.listaTokens  = []
        self.listaTokensOriginal = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 0
        self.i = 0

    def agregar_token(self,caracter,linea,columna,token):
        self.listaTokens.append(Token(caracter,linea,columna,token))
        self.listaTokensOriginal.append(Token(caracter,linea,columna,token))
        self.buffer = ''


    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido en el lenguaje.', linea, columna))

    def s0(self,caracter : str):
        '''Estado S0'''
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1

        elif caracter == '=':
            self.estado = 2
            self.buffer += caracter
            self.columna += 1    
        elif caracter == '(':
            self.estado = 3
            self.buffer += caracter
            self.columna += 1

        elif caracter == '"':
            self.estado = 4
            self.buffer += caracter
            self.columna += 1

        elif caracter ==',':
            self.estado = 5
            self.buffer += caracter
            self.columna += 1    


        elif caracter == ')':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1                                          
        elif caracter == ';':
            self.estado = 7
            self.buffer += caracter
            self.columna += 1    
        elif caracter == '{':
            self.estado = 8
            self.buffer += caracter
            self.columna += 1    
        elif caracter == '}':
            self.estado = 9
            self.buffer += caracter
            self.columna += 1
        elif caracter == ':':
            self.estado = 10
            self.buffer += caracter
            self.columna += 1               
        elif caracter== '\n':
            self.linea += 1
            self.columna = 0
        elif caracter in ['\t',' ']:
            self.columna += 1
        elif caracter == '^':
            print('Se terminó el análisis')
        else:
            self.agregar_error(caracter,self.linea,self.columna)               

    def s1(self,caracter : str):

        '''Estado S1'''
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1
        elif caracter.isdigit():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1          
        else: 
            if self.buffer in ['CrearBD','nueva','EliminarBD','$set','CrearColeccion','EliminarColeccion','InsertarUnico','ActualizarUnico','EliminarUnico','BuscarTodo','BuscarUnico']:
                self.agregar_token(self.buffer,self.linea,self.columna,'reservada_'+self.buffer)    
                self.estado = 0
                self.i -= 1

            else:
                self.agregar_token(self.buffer,self.linea,self.columna,'identificador')
                self.estado = 0
                self.i -= 1
    def s2(self,caracter : str):
        '''Estado S6'''
        self.agregar_token(self.buffer,self.linea,self.columna,'signoIgual')
        self.estado = 0
        self.i -= 1

    def s3(self,caracter : str):
        '''Estado S3'''
        self.agregar_token(self.buffer,self.linea,self.columna,'parentesisIzquierdo')
        self.estado = 0
        self.i -= 1
    def s4(self,caracter : str):
        '''Estado S3'''
        self.agregar_token(self.buffer,self.linea,self.columna,'comillasDobles')
        self.estado = 0
        self.i -= 1
    def s5(self,caracter : str):
        '''Estado S3'''
        self.agregar_token(self.buffer,self.linea,self.columna,'coma')
        self.estado = 0
        self.i -= 1    
    def s6(self,caracter : str):
        '''Estado S4'''
        self.agregar_token(self.buffer,self.linea,self.columna,'parentesisDerecho')
        self.estado = 0
        self.i -= 1


    def s7(self,caracter : str):
        '''Estado S5'''                
        self.agregar_token(self.buffer,self.linea,self.columna,'puntoYComa')
        self.estado = 0
        self.i -= 1

    def s8(self,caracter : str):
        '''Estado S5'''                
        self.agregar_token(self.buffer,self.linea,self.columna,'llaveIzquierda')
        self.estado = 0
        self.i -= 1

    def s9(self,caracter : str):
        '''Estado S5'''                
        self.agregar_token(self.buffer,self.linea,self.columna,'llaveDerecha')
        self.estado = 0
        self.i -= 1   

    def s10(self,caracter : str):
        '''Estado S5'''                
        self.agregar_token(self.buffer,self.linea,self.columna,'dosPuntos')
        self.estado = 0
        self.i -= 1   
                  


    

    def analizar(self, cadena):
        cadena = cadena + '^'
        
        self.listaErrores = []
        self.listaTokens = []
        self.i = 0
        while self.i < len(cadena):
            if self.estado == 0:
                self.s0(cadena[self.i])
            elif self.estado == 1:
                self.s1(cadena[self.i])
            elif self.estado == 2:
                self.s2(cadena[self.i])
            elif self.estado == 3:
                self.s3(cadena[self.i])  
            elif self.estado == 4:
                self.s4(cadena[self.i])
            elif self.estado == 5:
                self.s5(cadena[self.i])   
            elif self.estado == 6:
                self.s6(cadena[self.i])  
            elif self.estado == 7:
                self.s7(cadena[self.i])
            elif self.estado == 8:
                self.s8(cadena[self.i])   
            elif self.estado == 9:
                self.s9(cadena[self.i])  
            elif self.estado == 10:
                self.s10(cadena[self.i])   
                                              

            self.i += 1    

    '''def mostrarDatos(tabla):
        tabla.insert('','0',text='1',values='hola')
'''
    def imprimirTokens(self):
        count = 1
        #Imprime una tabla con los tokens
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna","tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna,token.tipo])
            count += 1
        print(x)

       
        

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["DEscripcion","linea","columna"]
        for error_ in self.listaErrores:
            x.add_row([error_.descripcion, error_.linea, error_.columna])
        print(x)                
