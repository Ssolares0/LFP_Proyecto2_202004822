import os
import webbrowser
global salidas
salidas = []


class bases():
    
    def CrearBD(name):
        #print(f'use(\'{name}\');')
        salidas.append(f'use(\'{name}\');')

    def EliminarBD(name):
        #print(f'db.dropDatabase();')
        salidas.append(f'db.dropDatabase();')
    def CrearColeccion(name):
        #print(f'db.createCollection(\'{name}\');')  
        salidas.append(f'db.createCollection(\'{name}\');')
    def EliminarColeccion(name):
        #print(f'db.{name}.drop();')
        salidas.append(f'db.{name}.drop();')


