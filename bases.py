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

    def InsertarUnico(nameCreacion,name1,name2,autor1,autor2):
        dicc ={
            "nombre": name1+" "+name2,
            "autor": autor1+" "+autor2
        }

        #values
        #print(f'db.{name}.insert({values});')
        salidas.append(f'db.{nameCreacion}.insertOne({dicc});')   

    def ActualizarUnico(nameCreacion,name1,name2,name3,name4,name5,name6): 
        dicc={
            name1: name2+" "+name3,
        },{
            '$set':{name4: name5+" "+name6}
        }
        salidas.append(f'db.{nameCreacion}.updateOne{dicc};')
         
    def EliminarUnico(nameCreacion,name1,name2,name3):
        dicc={
            name1: name2+" "+name3,
        }
        salidas.append(f'db.{nameCreacion}.deleteOne{dicc};')
        
        
    def BuscarTodo(name):
        #print(f'db.{name}.find();')
        salidas.append(f'db.{name}.find();')

    def BuscarUnico(name):
        #print(f'db.{name}.findOne();')
        salidas.append(f'db.{name}.findOne();')


    def mostrarSalida():
        lstSalidas = salidas
        with open('Salida/salida.txt','r+') as myfile:
            data = myfile.read()
            myfile.seek(0)
            for x in lstSalidas:
                myfile.write(x[0])
                myfile.truncate()
            
            


    

