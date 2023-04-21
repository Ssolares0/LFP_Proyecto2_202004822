from prettytable import PrettyTable
from bases import *

class AnalizadorSintactico:

    def __init__(self,tokens : list) -> None:
        self.errores = []
        self.tokens = tokens

    def agregarError(self,esperado,obtenido):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {}'''.format(obtenido,esperado)
        )

    def sacarToken(self):
        ''' Saca el primer token y lo quita de la lista'''
        try:
            return self.tokens.pop(0)
        except:
            return None

    def observarToken(self):
        ''' Saca el primer token y lo mete de nuevo en de la lista'''
        try:
            return self.tokens[0]
        except:
            return None

    
    def analizar(self):
        self.S()

    def S(self):
        self.INICIO()

    def INICIO(self):
        temp = self.observarToken()
        if temp is None:
            self.agregarError('reservada_CrearBD | reservada_EliminarBD | reservada_CrearColeccion | reservada_EliminarColeccion | InsertarUnico | reservada_ActualizarUnico | reservada_EliminarUnico | reservada_BuscarTodo | reservada_BuscarUnico','EOF') 

        elif temp.tipo == 'reservada_CrearBD':

            self.CREARBD()
            self.analizar()
        elif temp.tipo == 'reservada_EliminarBD':
            
            self.ELIMINARBD()
            self.analizar()
        elif temp.tipo == 'reservada_CrearColeccion':
            self.CREARCOLECCION() 
            self.analizar()              
        elif temp.tipo == 'reservada_EliminarColeccion':
            self.ELIMINARCOLECCION()
            self.analizar()
            
        elif temp.tipo == 'reservada_InsertarUnico':
            self.INSERTARUNICO()
            self.analizar()
            
            
        elif temp.tipo == 'reservada_ActualizarUnico':
            self.ACTUALIZARUNICO()
            self.analizar()
        elif temp.tipo == 'reservada_EliminarUnico':
            #self.ELIMINARUNICO()
            pass
        elif temp.tipo == 'reservada_BuscarTodo':
            self.BUSCARTODO()
            self.analizar()
        elif temp.tipo == 'reservada_BuscarUnico':
            #self.BUSCARUNICO()
            pass
            
        else:
            self.agregarError('reservada_CrearBD | reservada_ElmiminarBD | reservada_CrearColeccion | reservada_EliminarColeccion | InsertarUnico | reservada_ActualizarUnico | reservada_EliminarUnico | reservada_BuscarTodo | reservada_BuscarUnico',temp.tipo) 
        
    def CREARBD(self):
        
        
        token = self.sacarToken()
        if token.tipo == 'reservada_CrearBD':
            token = self.sacarToken()
            nombre_creacion = token.lexema
            if token is None:
                self.agregarError('identificador','EOF')
                return
            elif token.tipo ==  'identificador':
                token = self.sacarToken()

                if token is None:
                    self.agregarError('signoIgual','EOF')
                    return
                elif token.tipo == 'signoIgual':
                    token = self.sacarToken()

                    if token is None:
                        self.agregarError('reservada_nueva','EOF')
                        return
                    elif token.tipo == 'reservada_nueva':
                        token = self.sacarToken()

                        if token is None:
                            self.agregarError('reservada_CrearBD','EOF')
                            return
                        elif token.tipo == 'reservada_CrearBD':
                            token = self.sacarToken()

                            if token is None:
                                self.agregarError('parentesisIzquierdo','EOF')
                            elif token.tipo == 'parentesisIzquierdo':
                                token = self.sacarToken()

                                if token is None:
                                    self.agregarError('parentesisDerecho','EOF')
                                    return    
                                elif token.tipo == 'parentesisDerecho':
                                    token = self.sacarToken()

                                    if token is None:
                                        self.agregarError('puntoYComa','EOF')
                                        return
                                    elif token.tipo == 'puntoYComa':
                                        
                                        bases.CrearBD(nombre_creacion)
                                        
                                        
                                    else:
                                        self.agregarError('puntoYComa',token.tipo)
                                        print('Error falta punto y coma')    

                                else:
                                    self.agregarError('parentesisDerecho',token.tipo)
                                    print('Error falta parentesis Derecho')
                            else:
                                self.agregarError('parentesisIzquierdo',token.tipo)
                                print('Error falta parentesis Izquierdo')
                        else:
                            self.agregarError('reservada_CrearBD',token.tipo)
                            print('Error falta reservada CrearBD')
                    else:
                        self.agregarError('reservada nueva',token.tipo)
                        print('Error falta reservada nueva')
                else:
                    self.agregarError('signoIgual',token.tipo)
                    print('Error falta signo igual')
            else:
                self.agregarError('identificador',token.tipo)
                print('Error falta identificador')
        else:
            self.agregarError('reservada_CrearBD','EOF')
            print('Error')
       
               

    def ELIMINARBD(self):
        
        token = self.sacarToken()
        if token.tipo == 'reservada_EliminarBD':
            token = self.sacarToken()
            nombre_creacion = token.lexema
            if token is None:
                self.agregarError('identificador','EOF')
                return
            elif token.tipo ==  'identificador':
                token = self.sacarToken()

                if token is None:
                    self.agregarError('signoIgual','EOF')
                    return
                elif token.tipo == 'signoIgual':
                    token = self.sacarToken()

                    if token is None:
                        self.agregarError('reservada_nueva','EOF')
                        return
                    elif token.tipo == 'reservada_nueva':
                        token = self.sacarToken()

                        if token is None:
                            self.agregarError('reservada_EliminarBD','EOF')
                            return
                        elif token.tipo == 'reservada_EliminarBD':
                            token = self.sacarToken()

                            if token is None:
                                self.agregarError('parentesisIzquierdo','EOF')
                            elif token.tipo == 'parentesisIzquierdo':
                                token = self.sacarToken()

                                if token is None:
                                    self.agregarError('parentesisDerecho','EOF')
                                    return    
                                elif token.tipo == 'parentesisDerecho':
                                    token = self.sacarToken()

                                    if token is None:
                                        self.agregarError('puntoYComa','EOF')
                                        return
                                    elif token.tipo == 'puntoYComa':
                                        
                                        print('si llego ')
                                        bases.EliminarBD(nombre_creacion)
                                        
                                        
                                    else:
                                        self.agregarError('puntoYComa',token.tipo)
                                        print('Error falta punto y coma')    

                                else:
                                    self.agregarError('parentesisDerecho',token.tipo)
                                    print('Error falta parentesis Derecho')
                            else:
                                self.agregarError('parentesisIzquierdo',token.tipo)
                                print('Error falta parentesis Izquierdo')
                        else:
                            self.agregarError('reservada_EliminarBD',token.tipo)
                            print('Error falta reservada EliminarBD')
                    else:
                        self.agregarError('reservada_nueva',token.tipo)
                        print('Error falta reservada_nueva')
                else:
                    self.agregarError('signoIgual',token.tipo)
                    print('Error falta signo igual')
            else:
                self.agregarError('identificador',token.tipo)
                print('Error falta identificador')
        else:
            self.agregarError('reservada_EliminarBD','EOF')
            print('Error')

    def CREARCOLECCION(self):

        
        token = self.sacarToken()
        if token.tipo == 'reservada_CrearColeccion':

            token = self.sacarToken()
            
            
            if token is None:
                self.agregarError('identificador','EOF')
                return
            elif token.tipo ==  'identificador':
                token = self.sacarToken()
                

                if token is None:
                    self.agregarError('signoIgual','EOF')
                    return
                elif token.tipo == 'signoIgual':
                    token = self.sacarToken()

                    if token is None:
                        self.agregarError('reservada_nueva','EOF')
                        return
                    elif token.tipo == 'reservada_nueva':
                        token = self.sacarToken()

                        if token is None:
                            self.agregarError('reservada_CrearColeccion','EOF')
                            return
                        elif token.tipo == 'reservada_CrearColeccion':
                            token = self.sacarToken()

                            if token is None:
                                self.agregarError('parentesisIzquierdo','EOF')
                            elif token.tipo == 'parentesisIzquierdo':
                                token = self.sacarToken()

                                if token is None:
                                    self.agregarError('comillasDobles','EOF')
                                    return    
                                elif token.tipo == 'comillasDobles':
                                    token = self.sacarToken()
                                    nombre_creacion = token.lexema

                                    if token is None:
                                        self.agregarError('identificador','EOF')
                                        return
                                    elif token.tipo == 'identificador':
                                        token = self.sacarToken()
                                        

                                        
                                        if token is None:
                                            self.agregarError('comillasDobles','EOF')
                                            return
                                        elif token.tipo == 'comillasDobles':
                                            token = self.sacarToken()

                                            if token is None:
                                                self.agregarError('parentesisDerecho','EOF')
                                                return    
                                            elif token.tipo == 'parentesisDerecho':
                                                token = self.sacarToken()


                                                if token is None:
                                                    self.agregarError('puntoYComa','EOF')
                                                    return
                                                elif token.tipo == 'puntoYComa':

                                                    
                                                    print('si llego al final de crear coleccion ')
                                                    bases.CrearColeccion(nombre_creacion)

                                                else:
                                                    self.agregarError('puntoYComa',token.tipo)
                                                    print('Error falta punto y coma')
                                                
                                            else:
                                                self.agregarError('parentesisDerecho',token.tipo)
                                                print('Error falta parentesisDerecho')

                                        else:
                                            self.agregarError('comillasDobles',token.tipo)
                                            print('Error falta comillasDobles')
                                        
                                    else:
                                        self.agregarError('identificador',token.tipo)
                                        print('Error falta identificador')    

                                else:
                                    self.agregarError('comillasDobles',token.tipo)
                                    print('Error falta comillasDobles')
                            else:
                                self.agregarError('parentesisIzquierdo',token.tipo)
                                print('Error falta parentesis Izquierdo')
                        else:
                            self.agregarError('reservada_CrearColeccion',token.tipo)
                            print('Error falta reservada_CrearColeccion')
                    else:
                        self.agregarError('reservada_nueva',token.tipo)
                        print('Error falta reservada_nueva')
                else:
                    self.agregarError('signoIgual',token.tipo)
                    print('Error falta signo igual')
            else:
                self.agregarError('identificador',token.tipo)
                print('Error falta identificador')
        else:
            self.agregarError('reservada_CrearColeccion','EOF')
            print('Error')

    def ELIMINARCOLECCION(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_EliminarColeccion':

            token = self.sacarToken()
            
            
            if token is None:
                self.agregarError('identificador','EOF')
                return
            elif token.tipo ==  'identificador':
                token = self.sacarToken()
                

                if token is None:
                    self.agregarError('signoIgual','EOF')
                    return
                elif token.tipo == 'signoIgual':
                    token = self.sacarToken()

                    if token is None:
                        self.agregarError('reservada_nueva','EOF')
                        return
                    elif token.tipo == 'reservada_nueva':
                        token = self.sacarToken()

                        if token is None:
                            self.agregarError('reservada_EliminarColeccion','EOF')
                            return
                        elif token.tipo == 'reservada_EliminarColeccion':
                            token = self.sacarToken()

                            if token is None:
                                self.agregarError('parentesisIzquierdo','EOF')
                            elif token.tipo == 'parentesisIzquierdo':
                                token = self.sacarToken()

                                if token is None:
                                    self.agregarError('comillasDobles','EOF')
                                    return    
                                elif token.tipo == 'comillasDobles':
                                    token = self.sacarToken()
                                    nombre_creacion = token.lexema

                                    if token is None:
                                        self.agregarError('identificador','EOF')
                                        return
                                    elif token.tipo == 'identificador':
                                        token = self.sacarToken()
                                        

                                        
                                        if token is None:
                                            self.agregarError('comillasDobles','EOF')
                                            return
                                        elif token.tipo == 'comillasDobles':
                                            token = self.sacarToken()

                                            if token is None:
                                                self.agregarError('parentesisDerecho','EOF')
                                                return    
                                            elif token.tipo == 'parentesisDerecho':
                                                token = self.sacarToken()


                                                if token is None:
                                                    self.agregarError('puntoYComa','EOF')
                                                    return
                                                elif token.tipo == 'puntoYComa':

                                                    
                                                    print('si llego al final de eliminar coleccion ')
                                                    bases.EliminarColeccion(nombre_creacion)

                                                else:
                                                    self.agregarError('puntoYComa',token.tipo)
                                                    print('Error falta punto y coma')
                                                
                                            else:
                                                self.agregarError('parentesisDerecho',token.tipo)
                                                print('Error falta parentesisDerecho')

                                        else:
                                            self.agregarError('comillasDobles',token.tipo)
                                            print('Error falta comillasDobles')
                                        
                                    else:
                                        self.agregarError('identificador',token.tipo)
                                        print('Error falta identificador')    

                                else:
                                    self.agregarError('comillasDobles',token.tipo)
                                    print('Error falta comillasDobles')
                            else:
                                self.agregarError('parentesisIzquierdo',token.tipo)
                                print('Error falta parentesis Izquierdo')
                        else:
                            self.agregarError('reservada_EliminarColeccion',token.tipo)
                            print('Error falta reservada_EliminarColeccion')
                    else:
                        self.agregarError('reservada_nueva',token.tipo)
                        print('Error falta reservada_nueva')
                else:
                    self.agregarError('signoIgual',token.tipo)
                    print('Error falta signo igual')
            else:
                self.agregarError('identificador',token.tipo)
                print('Error falta identificador')
        else:
            self.agregarError('reservada_EliminarColeccion','EOF')
            print('Error')
    
    def INSERTARUNICO(self):
        print('entro a insertar unico')
        token = self.sacarToken()
        if token.tipo == 'reservada_InsertarUnico':

            token = self.sacarToken()
            
            
            if token is None:
                self.agregarError('identificador','EOF')
                return
            elif token.tipo ==  'identificador':
                token = self.sacarToken()
                

                if token is None:
                    self.agregarError('signoIgual','EOF')
                    return
                elif token.tipo == 'signoIgual':
                    token = self.sacarToken()

                    if token is None:
                        self.agregarError('reservada_nueva','EOF')
                        return
                    elif token.tipo == 'reservada_nueva':
                        token = self.sacarToken()

                        if token is None:
                            self.agregarError('reservada_InsertarUnico','EOF')
                            return
                        elif token.tipo == 'reservada_InsertarUnico':
                            token = self.sacarToken()

                            if token is None:
                                self.agregarError('parentesisIzquierdo','EOF')
                            elif token.tipo == 'parentesisIzquierdo':
                                token = self.sacarToken()

                                if token is None:
                                    self.agregarError('comillasDobles','EOF')
                                    return    
                                elif token.tipo == 'comillasDobles':
                                    token = self.sacarToken()
                                    nombre_creacion = token.lexema

                                    if token is None:
                                        self.agregarError('identificador','EOF')
                                        return
                                    elif token.tipo == 'identificador':
                                        token = self.sacarToken()
                                        

                                        
                                        if token is None:
                                            self.agregarError('comillasDobles','EOF')
                                            return
                                        elif token.tipo == 'comillasDobles':
                                            token = self.sacarToken()

                                            if token is None:
                                                self.agregarError('coma','EOF')
                                                return
                                            elif token.tipo == 'coma':
                                                token = self.sacarToken()

                                                if token is None:
                                                    self.agregarError('comillasDobles','EOF')
                                                    return
                                                elif token.tipo == 'comillasDobles':
                                                    token = self.sacarToken()

                                                    if token is None:
                                                        self.agregarError('llaveIzquierda','EOF')
                                                        return
                                                    elif token.tipo == 'llaveIzquierda':
                                                        token = self.sacarToken()

                                                        if token is None:
                                                            self.agregarError('comillasDobles','EOF')
                                                            return
                                                        elif token.tipo == 'comillasDobles':
                                                            token = self.sacarToken()

                                                            if token is None:
                                                                self.agregarError('identificador','EOF')
                                                                return
                                                            elif token.tipo == 'identificador':
                                                                token = self.sacarToken()

                                                                if token is None:
                                                                    self.agregarError('comillasDobles','EOF')
                                                                    return
                                                                elif token.tipo == 'comillasDobles':
                                                                    token = self.sacarToken()

                                                                    if token is None:
                                                                        self.agregarError('dosPuntos','EOF')
                                                                        return
                                                                    elif token.tipo == 'dosPuntos':
                                                                        token = self.sacarToken()

                                                                        if token is None:
                                                                            self.agregarError('comillasDobles','EOF')
                                                                            return
                                                                        elif token.tipo == 'comillasDobles':
                                                                            token = self.sacarToken()
                                                                            name1=token.lexema

                                                                            if token is None:
                                                                                self.agregarError('identificador','EOF')
                                                                                return
                                                                            elif token.tipo == 'identificador':
                                                                                token = self.sacarToken()
                                                                                name2=token.lexema

                                                                                if token is None:
                                                                                    self.agregarError('identificador','EOF')
                                                                                    return
                                                                                elif token.tipo == 'identificador':
                                                                                    token = self.sacarToken()
                                                                                    if token is None:
                                                                                        self.agregarError('comillasDobles','EOF')
                                                                                        return
                                                                                    elif token.tipo == 'comillasDobles':
                                                                                        token = self.sacarToken()

                                                                                        if token is None:
                                                                                            self.agregarError('coma','EOF')
                                                                                            return
                                                                                        elif token.tipo == 'coma':
                                                                                            token = self.sacarToken()
                                                                                            if token is None:
                                                                                                self.agregarError('comillasDobles','EOF')
                                                                                                return
                                                                                            elif token.tipo == 'comillasDobles':
                                                                                                token = self.sacarToken()

                                                                                                if token is None:
                                                                                                    self.agregarError('identificador','EOF')
                                                                                                    return
                                                                                                elif token.tipo == 'identificador':
                                                                                                    token = self.sacarToken()

                                                                                                    if token is None:
                                                                                                        self.agregarError('comillasDobles','EOF')
                                                                                                        return
                                                                                                    elif token.tipo == 'comillasDobles':
                                                                                                        token = self.sacarToken()

                                                                                                        if token is None:
                                                                                                            self.agregarError('dosPuntos','EOF')
                                                                                                            return
                                                                                                        elif token.tipo == 'dosPuntos':
                                                                                                            token = self.sacarToken()

                                                                                                            if token is None:
                                                                                                                self.agregarError('comillasDobles','EOF')
                                                                                                                return
                                                                                                            elif token.tipo == 'comillasDobles':
                                                                                                                token = self.sacarToken()
                                                                                                                autor1=token.lexema

                                                                                                                if token is None:
                                                                                                                    self.agregarError('identificador','EOF')
                                                                                                                    return
                                                                                                                elif token.tipo == 'identificador':
                                                                                                                    token = self.sacarToken()
                                                                                                                    autor2=token.lexema

                                                                                                                    if token is None:
                                                                                                                        self.agregarError('identificador','EOF')
                                                                                                                        return
                                                                                                                    elif token.tipo == 'identificador':
                                                                                                                        token = self.sacarToken()
                                                                                                                        if token is None:
                                                                                                                            self.agregarError('comillasDobles','EOF')
                                                                                                                            return
                                                                                                                        elif token.tipo == 'comillasDobles':
                                                                                                                            token = self.sacarToken()

                                                                                                                            if token is None:
                                                                                                                                self.agregarError('llaveDerecha','EOF')
                                                                                                                                return
                                                                                                                            elif token.tipo == 'llaveDerecha':
                                                                                                                                token = self.sacarToken()

                                                                                                                                if token is None:
                                                                                                                                    self.agregarError('comillasDobles','EOF')
                                                                                                                                    return
                                                                                                                                elif token.tipo == 'comillasDobles':
                                                                                                                                    token = self.sacarToken()

                                                                                                                                    if token is None:
                                                                                                                                        self.agregarError('parentesisDerecho','EOF')
                                                                                                                                        return    
                                                                                                                                    elif token.tipo == 'parentesisDerecho':
                                                                                                                                        token = self.sacarToken()


                                                                                                                                        if token is None:
                                                                                                                                            self.agregarError('puntoYComa','EOF')
                                                                                                                                            return
                                                                                                                                        elif token.tipo == 'puntoYComa':

                                                                                                                                            
                                                                                                                                            print('si llego al final de insertar Unico ')
                                                                                                                                            bases.InsertarUnico(nombre_creacion,name1,name2,autor1,autor2)

                                                                                                                                        else:
                                                                                                                                            self.agregarError('puntoYComa',token.tipo)
                                                                                                                                            print('Error falta punto y coma')
                                                                                                                                    else:
                                                                                                                                        self.agregarError('parentesisDerecho',token.tipo)
                                                                                                                                        print('Error falta parentesisDerecho en JSON')
                                                                                                                                else:
                                                                                                                                    self.agregarError('comillasDobles',token.tipo)
                                                                                                                                    print('Error falta comillasDobles en JSON')        




                                                                                                                            else:
                                                                                                                                self.agregarError('llaveDerecha',token.tipo)
                                                                                                                                print('Error falta llaveDerecha en JSON')  

                                                                                                                        else:
                                                                                                                            self.agregarError('comillasDobles',token.tipo)
                                                                                                                            print('Error falta comillasDobles en JSON')    
                                                                                                                    else:
                                                                                                                        self.agregarError('identificador',token.tipo)
                                                                                                                        print('Error falta identificador en JSON')
                                                                                                                else:
                                                                                                                    self.agregarError('identificador',token.tipo)
                                                                                                                    print('Error falta identificador en JSON')
                                                                                                            else:
                                                                                                                self.agregarError('comillasDobles',token.tipo)
                                                                                                                print('Error falta comillasDobles en JSON')   
                                                                                                        else:
                                                                                                            self.agregarError('dosPuntos',token.tipo)
                                                                                                            print('Error falta dospuntos en JSON')
                                                                                                    else:
                                                                                                        self.agregarError('comillasDobles',token.tipo)
                                                                                                        print('Error falta comillasDobles en JSON')
                                                                                                else:
                                                                                                    self.agregarError('identificador',token.tipo)
                                                                                                    print('Error falta identificador en JSON')
                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                 
                                                                                            else:
                                                                                                self.agregarError('comillasDobles',token.tipo)
                                                                                                print('Error falta comillasDobles en JSON')                                     

                                                                                        else:
                                                                                            self.agregarError('coma',token.tipo)
                                                                                            print('Error falta coma en JSON')    

                                                                                    else:
                                                                                        self.agregarError('comillasDobles',token.tipo)
                                                                                        print('Error falta comillasDobles en JSON')    

                                                                                else:
                                                                                    self.agregarError('identificador',token.tipo)
                                                                                    print('Error falta identificador en JSON')

                                                                            else:
                                                                                self.agregarError('identificador',token.tipo)
                                                                                print('Error falta identificador en JSON')
                                                                
                                                                        else:
                                                                            self.agregarError('comillasDobles',token.tipo)
                                                                            print('Error falta comillasDobles en JSON')
                                                                        
                                                                    
                                                                    else:
                                                                        self.agregarError('dosPuntos',token.tipo)
                                                                        print('Error falta dosPuntos en JSON')
                                                                    
                                                                
                                                                else:
                                                                    self.agregarError('comillasDobles',token.tipo)
                                                                    print('Error falta comillasDobles en JSON')

                                                            else:
                                                                self.agregarError('identificador',token.tipo)
                                                                print('Error falta identificador en JSON')
                                                        else:
                                                            self.agregarError('comillasDobles',token.tipo)
                                                            print('Error falta comillasDobles en JSON')

                                                    else:
                                                        self.agregarError('llaveIzquierda',token.tipo)
                                                        print('Error falta llave Izquierda en JSON')
                                                    
                                                else:
                                                    self.agregarError('comillasDobles',token.tipo)
                                                    print('Error falta comillasDobles en el JSON')

                                            else:
                                                self.agregarError('coma',token.tipo)
                                                print('Error falta coma')

                                        else:
                                            self.agregarError('comillasDobles',token.tipo)
                                            print('Error falta comillasDobles')
                                        
                                    else:
                                        self.agregarError('identificador',token.tipo)
                                        print('Error falta identificador')    

                                else:
                                    self.agregarError('comillasDobles',token.tipo)
                                    print('Error falta comillasDobles')
                            else:
                                self.agregarError('parentesisIzquierdo',token.tipo)
                                print('Error falta parentesis Izquierdo')
                        else:
                            self.agregarError('reservada_InsertarUnico',token.tipo)
                            print('Error falta reservada InsertarUnico')
                    else:
                        self.agregarError('reservada_nueva',token.tipo)
                        print('Error falta reservada_nueva')
                else:
                    self.agregarError('signoIgual',token.tipo)
                    print('Error falta signo igual')
            else:
                self.agregarError('identificador',token.tipo)
                print('Error falta identificador')
        else:
            self.agregarError('reservada_InsertarUnico','EOF')
            print('Error')
    def ACTUALIZARUNICO(self):
        print('entro a actualizar unico')
        token = self.sacarToken()
        if token.tipo == 'reservada_ActualizarUnico':

            token = self.sacarToken()
            
            
            if token is None:
                self.agregarError('identificador','EOF')
                return
            elif token.tipo ==  'identificador':
                token = self.sacarToken()
                

                if token is None:
                    self.agregarError('signoIgual','EOF')
                    return
                elif token.tipo == 'signoIgual':
                    token = self.sacarToken()

                    if token is None:
                        self.agregarError('reservada_nueva','EOF')
                        return
                    elif token.tipo == 'reservada_nueva':
                        token = self.sacarToken()

                        if token is None:
                            self.agregarError('reservada_ActualizarUnico','EOF')
                            return
                        elif token.tipo == 'reservada_ActualizarUnico':
                            token = self.sacarToken()

                            if token is None:
                                self.agregarError('parentesisIzquierdo','EOF')
                            elif token.tipo == 'parentesisIzquierdo':
                                token = self.sacarToken()

                                if token is None:
                                    self.agregarError('comillasDobles','EOF')
                                    return    
                                elif token.tipo == 'comillasDobles':
                                    token = self.sacarToken()
                                    nombre_creacion = token.lexema

                                    if token is None:
                                        self.agregarError('identificador','EOF')
                                        return
                                    elif token.tipo == 'identificador':
                                        token = self.sacarToken()
                                        

                                        
                                        if token is None:
                                            self.agregarError('comillasDobles','EOF')
                                            return
                                        elif token.tipo == 'comillasDobles':
                                            token = self.sacarToken()

                                            if token is None:
                                                self.agregarError('coma','EOF')
                                                return
                                            elif token.tipo == 'coma':
                                                token = self.sacarToken()

                                                if token is None:
                                                    self.agregarError('comillasDobles','EOF')
                                                    return
                                                elif token.tipo == 'comillasDobles':
                                                    token = self.sacarToken()

                                                    if token is None:
                                                        self.agregarError('llaveIzquierda','EOF')
                                                        return
                                                    elif token.tipo == 'llaveIzquierda':
                                                        token = self.sacarToken()

                                                        if token is None:
                                                            self.agregarError('comillasDobles','EOF')
                                                            return
                                                        elif token.tipo == 'comillasDobles':
                                                            token = self.sacarToken()
                                                            name1= token.lexema

                                                            if token is None:
                                                                self.agregarError('identificador','EOF')
                                                                return
                                                            elif token.tipo == 'identificador':
                                                                token = self.sacarToken()

                                                                if token is None:
                                                                    self.agregarError('comillasDobles','EOF')
                                                                    return
                                                                elif token.tipo == 'comillasDobles':
                                                                    token = self.sacarToken()

                                                                    if token is None:
                                                                        self.agregarError('dosPuntos','EOF')
                                                                        return
                                                                    elif token.tipo == 'dosPuntos':
                                                                        token = self.sacarToken()

                                                                        if token is None:
                                                                            self.agregarError('comillasDobles','EOF')
                                                                            return
                                                                        elif token.tipo == 'comillasDobles':
                                                                            token = self.sacarToken()
                                                                            name2 = token.lexema
                                                                            

                                                                            if token is None:
                                                                                self.agregarError('identificador','EOF')
                                                                                return
                                                                            elif token.tipo == 'identificador':
                                                                                token = self.sacarToken()
                                                                                name3 = token.lexema
                                                                                

                                                                                if token is None:
                                                                                    self.agregarError('identificador','EOF')
                                                                                    return
                                                                                elif token.tipo == 'identificador':
                                                                                    token = self.sacarToken()

                                                                                    if token is None:
                                                                                        self.agregarError('comillasDobles','EOF')
                                                                                        return
                                                                                    elif token.tipo == 'comillasDobles':
                                                                                        token = self.sacarToken()

                                                                                        if token is None:
                                                                                            self.agregarError('llaveDerecha','EOF')
                                                                                            return
                                                                                        elif token.tipo == 'llaveDerecha':
                                                                                            token = self.sacarToken()

                                                                                            if token is None:
                                                                                                self.agregarError('coma','EOF')
                                                                                                return
                                                                                            elif token.tipo == 'coma':
                                                                                                token = self.sacarToken()

                                                                                                if token is None:
                                                                                                    self.agregarError('llaveIzquierda','EOF')
                                                                                                    return
                                                                                                elif token.tipo == 'llaveIzquierda':
                                                                                                    token = self.sacarToken()

                                                                                                    if token is None:
                                                                                                        self.agregarError('dollar','EOF')
                                                                                                        return
                                                                                                    elif token.tipo == 'dollar':
                                                                                                        token = self.sacarToken()

                                                                                                        if token is None:
                                                                                                            self.agregarError('identificador','EOF')
                                                                                                            return
                                                                                                        elif token.tipo == 'identificador':
                                                                                                
                                                                                                            token = self.sacarToken()
                                                                                                            if token is None:
                                                                                                                self.agregarError('dosPuntos','EOF')
                                                                                                                return
                                                                                                            elif token.tipo == 'dosPuntos':
                                                                                                                token = self.sacarToken()
                                                                                                                if token is None:
                                                                                                                    self.agregarError('llaveIzquierda','EOF')
                                                                                                                    return
                                                                                                                elif token.tipo == 'llaveIzquierda':

                                                                                                                    token = self.sacarToken()
                                                                                                                    

                                                                                                                    if token is None:
                                                                                                                        self.agregarError('comillasDobles','EOF')
                                                                                                                        return
                                                                                                                    elif token.tipo == 'comillasDobles':
                                                                                                                        token = self.sacarToken()
                                                                                                                        name4 = token.lexema

                                                                                                                        if token is None:
                                                                                                                            self.agregarError('identificador','EOF')
                                                                                                                            return
                                                                                                                        elif token.tipo == 'identificador':
                                                                                                                            token = self.sacarToken()
                                                                                                                        

                                                                                                                            if token is None:
                                                                                                                                self.agregarError('comillasDobles','EOF')
                                                                                                                                return
                                                                                                                            elif token.tipo == 'comillasDobles':
                                                                                                                                token = self.sacarToken()

                                                                                                                                if token is None:
                                                                                                                                    self.agregarError('dosPuntos','EOF')
                                                                                                                                    return
                                                                                                                                elif token.tipo == 'dosPuntos':
                                                                                                                                    token = self.sacarToken()

                                                                                                                                    if token is None:
                                                                                                                                        self.agregarError('comillasDobles','EOF')
                                                                                                                                        return
                                                                                                                                    elif token.tipo == 'comillasDobles':
                                                                                                                                        token = self.sacarToken()
                                                                                                                                        name5 = token.lexema
                                                                                                                                        

                                                                                                                                        if token is None:
                                                                                                                                            self.agregarError('identificador','EOF')
                                                                                                                                            return
                                                                                                                                        elif token.tipo == 'identificador':
                                                                                                                                            token = self.sacarToken()
                                                                                                                                            name6 = token.lexema
                                                                                                                                            

                                                                                                                                            if token is None:
                                                                                                                                                self.agregarError('identificador','EOF')
                                                                                                                                                return
                                                                                                                                            elif token.tipo == 'identificador':
                                                                                                                                                
                                                                                                                                                token = self.sacarToken()

                                                                                                                                                if token is None:
                                                                                                                                                    self.agregarError('comillasDobles','EOF')
                                                                                                                                                    return
                                                                                                                                                elif token.tipo == 'comillasDobles':
                                                                                                                                                    
                                                                                                                                                    token = self.sacarToken()

                                                                                                                                                    if token is None:
                                                                                                                                                        self.agregarError('llaveDerecha','EOF')
                                                                                                                                                        return
                                                                                                                                                    elif token.tipo == 'llaveDerecha':
                                                                                                                                                        
                                                                                                                                        
                                                                                                                                                        token = self.sacarToken()
                                                                                                                                                        if token is None:
                                                                                                                                                            self.agregarError('llaveDerecha','EOF')
                                                                                                                                                            return
                                                                                                                                                        elif token.tipo == 'llaveDerecha':
                                                                                                                                                           
                                                                                                                                            
                                                                                                                                                            token = self.sacarToken()

                                                                                                                                                            if token is None:
                                                                                                                                                                self.agregarError('comillasDobles','EOF')
                                                                                                                                                                return
                                                                                                                                                            elif token.tipo == 'comillasDobles':
                                                                                                                                                                
                                                                                                                                                                token = self.sacarToken()

                                                                                                                                                                if token is None:
                                                                                                                                                                    self.agregarError('parentesisDerecho','EOF')
                                                                                                                                                                    return
                                                                                                                                                                elif token.tipo == 'parentesisDerecho':
                                                                                                                                                                    token = self.sacarToken()

                                                                                                                                                                    if token is None:
                                                                                                                                                                        self.agregarError('puntoYComa','EOF')
                                                                                                                                                                        return
                                                                                                                                                                    elif token.tipo == 'puntoYComa':
                                                                                                                                                                        
                                                                                                                                                                        print('si llego al final de actualizar Unico')
                                                                                                                                                                        bases.ActualizarUnico(nombre_creacion,name1,name2,name3,name4,name5,name6)


                                                                                                                                                                    else:
                                                                                                                                                                        self.agregarError('puntoYComa',token.tipo)
                                                                                                                                                                        print('Error falta puntoYComa en JSON')


                                                                                                                                                                

                                                                                                                                                                else:
                                                                                                                                                                    self.agregarError('parentesisDerecho',token.tipo)
                                                                                                                                                                    print('Error falta parentesisDerecho en JSON')


                                                                                                                                                                

                                                                                                                                                            else:
                                                                                                                                                                self.agregarError('comillasDobles',token.tipo)
                                                                                                                                                                print('Error falta comillasDobles en JSON')


                                                                                                                                                        else:
                                                                                                                                                            self.agregarError('llaveDerecha',token.tipo)
                                                                                                                                                            print('Error falta llaveDerecha en JSON')


                                                                                                                                                    else:
                                                                                                                                                        self.agregarError('llaveDerecha',token.tipo)
                                                                                                                                                        print('Error falta llaveDerecha en JSON')



                                                                                                                                                else:
                                                                                                                                                    self.agregarError('comillasDobles',token.tipo)
                                                                                                                                                    print('Error falta comillasDobles en JSON')

                                                                                                                                            else:
                                                                                                                                                self.agregarError('identificador',token.tipo)
                                                                                                                                                print('Error falta identificador en JSON')

                                                                                                                                        else:
                                                                                                                                            self.agregarError('identificador',token.tipo)
                                                                                                                                            print('Error falta identificador en JSON')

                                                                                                                                    else:
                                                                                                                                        self.agregarError('comillasDobles',token.tipo)
                                                                                                                                        print('Error falta comillasDobles en JSON')
                                                                                                                                else:
                                                                                                                                    self.agregarError('dosPuntos',token.tipo)
                                                                                                                                    print('Error falta dosPuntos en JSON')

                                                                                                                            else:
                                                                                                                                self.agregarError('comillasDobles',token.tipo)
                                                                                                                                print('Error falta comillasDobles en JSON')
                                                                                                                        else:
                                                                                                                            self.agregarError('identificador',token.tipo)
                                                                                                                            print('Error falta identificador en JSON')

                                                                                                                    else:
                                                                                                                        self.agregarError('comillasDobles',token.tipo)
                                                                                                                        print('Error falta comillasDobles en JSON')                                    

                                                                                                                else:
                                                                                                                    self.agregarError('llaveIzquierda',token.tipo)
                                                                                                                    print('Error falta llaveIzquierda en JSON')
                                                                                                            else:
                                                                                                                self.agregarError('dospuntos',token.tipo)
                                                                                                                print('Error falta dospuntos en JSON')        

                                                                                                        else:
                                                                                                            self.agregarError('identificador',token.tipo)
                                                                                                            print('Error falta identificador en JSON')    


                                                                                                    else:
                                                                                                        self.agregarError('dollar',token.tipo)
                                                                                                        print('Error falta dollar en JSON')    

                                                                                                else:
                                                                                                    self.agregarError('llaveIzquierda',token.tipo)
                                                                                                    print('Error falta llaveIzquierda en JSON')




                                                                                            else:
                                                                                                self.agregarError('coma',token.tipo)
                                                                                                print('Error falta coma en JSON')


                                                                                        else:
                                                                                            self.agregarError('llaveDerecha',token.tipo)
                                                                                            print('Error falta llaveDerecha en JSON')    


                                                  
                                                                                    else:
                                                                                        self.agregarError('comillasDobles',token.tipo)
                                                                                        print('Error falta comillasDobles en JSON')    

                                                                                else:
                                                                                    self.agregarError('identificador',token.tipo)
                                                                                    print('Error falta identificador en JSON')

                                                                            else:
                                                                                self.agregarError('identificador',token.tipo)
                                                                                print('Error falta identificador en JSON')
                                                                
                                                                        else:
                                                                            self.agregarError('comillasDobles',token.tipo)
                                                                            print('Error falta comillasDobles en JSON')
                                                                        
                                                                    
                                                                    else:
                                                                        self.agregarError('dosPuntos',token.tipo)
                                                                        print('Error falta dosPuntos en JSON')
                                                                    
                                                                
                                                                else:
                                                                    self.agregarError('comillasDobles',token.tipo)
                                                                    print('Error falta comillasDobles en JSON')

                                                            else:
                                                                self.agregarError('identificador',token.tipo)
                                                                print('Error falta identificador en JSON')
                                                        else:
                                                            self.agregarError('comillasDobles',token.tipo)
                                                            print('Error falta comillasDobles en JSON')

                                                    else:
                                                        self.agregarError('llaveIzquierda',token.tipo)
                                                        print('Error falta llave Izquierda en JSON')
                                                    
                                                else:
                                                    self.agregarError('comillasDobles',token.tipo)
                                                    print('Error falta comillasDobles en el JSON')

                                            else:
                                                self.agregarError('coma',token.tipo)
                                                print('Error falta coma')

                                        else:
                                            self.agregarError('comillasDobles',token.tipo)
                                            print('Error falta comillasDobles')
                                        
                                    else:
                                        self.agregarError('identificador',token.tipo)
                                        print('Error falta identificador')    

                                else:
                                    self.agregarError('comillasDobles',token.tipo)
                                    print('Error falta comillasDobles')
                            else:
                                self.agregarError('parentesisIzquierdo',token.tipo)
                                print('Error falta parentesis Izquierdo')
                        else:
                            self.agregarError('reservada_ActualizarUnico',token.tipo)
                            print('Error falta reservada_ActualizarUnico')
                    else:
                        self.agregarError('reservada_nueva',token.tipo)
                        print('Error falta reservada_nueva')
                else:
                    self.agregarError('signoIgual',token.tipo)
                    print('Error falta signo igual')
            else:
                self.agregarError('identificador',token.tipo)
                print('Error falta identificador')
        else:
            self.agregarError('reservada_ActualizarUnico','EOF')
            print('Error')   
    def BUSCARTODO(self):
        print('entro a buscar todo')
        token = self.sacarToken()
        if token.tipo == 'reservada_BuscarTodo':

            token = self.sacarToken()
            
            
            if token is None:
                self.agregarError('identificador','EOF')
                return
            elif token.tipo ==  'identificador':
                token = self.sacarToken()
                

                if token is None:
                    self.agregarError('signoIgual','EOF')
                    return
                elif token.tipo == 'signoIgual':
                    token = self.sacarToken()

                    if token is None:
                        self.agregarError('reservada_nueva','EOF')
                        return
                    elif token.tipo == 'reservada_nueva':
                        token = self.sacarToken()

                        if token is None:
                            self.agregarError('reservada_BuscarTodo','EOF')
                            return
                        elif token.tipo == 'reservada_BuscarTodo':
                            token = self.sacarToken()

                            if token is None:
                                self.agregarError('parentesisIzquierdo','EOF')
                            elif token.tipo == 'parentesisIzquierdo':
                                token = self.sacarToken()

                                if token is None:
                                    self.agregarError('comillasDobles','EOF')
                                    return    
                                elif token.tipo == 'comillasDobles':
                                    token = self.sacarToken()
                                    nombre_creacion = token.lexema

                                    if token is None:
                                        self.agregarError('identificador','EOF')
                                        return
                                    elif token.tipo == 'identificador':
                                        token = self.sacarToken()
                                        

                                        
                                        if token is None:
                                            self.agregarError('comillasDobles','EOF')
                                            return
                                        elif token.tipo == 'comillasDobles':
                                            token = self.sacarToken()

                                            if token is None:
                                                self.agregarError('parentesisDerecho','EOF')
                                                return    
                                            elif token.tipo == 'parentesisDerecho':
                                                token = self.sacarToken()


                                                if token is None:
                                                    self.agregarError('puntoYComa','EOF')
                                                    return
                                                elif token.tipo == 'puntoYComa':

                                                    
                                                    print('si llego al final de BUSCAR TODO ')
                                                    bases.BuscarTodo(nombre_creacion)

                                                else:
                                                    self.agregarError('puntoYComa',token.tipo)
                                                    print('Error falta punto y coma')
                                                
                                            else:
                                                self.agregarError('parentesisDerecho',token.tipo)
                                                print('Error falta parentesisDerecho')

                                        else:
                                            self.agregarError('comillasDobles',token.tipo)
                                            print('Error falta comillasDobles')
                                        
                                    else:
                                        self.agregarError('identificador',token.tipo)
                                        print('Error falta identificador')    

                                else:
                                    self.agregarError('comillasDobles',token.tipo)
                                    print('Error falta comillasDobles')
                            else:
                                self.agregarError('parentesisIzquierdo',token.tipo)
                                print('Error falta parentesis Izquierdo')
                        else:
                            self.agregarError('reservada_BuscarTodo',token.tipo)
                            print('Error falta reservada_BuscarTodo')
                    else:
                        self.agregarError('reservada_nueva',token.tipo)
                        print('Error falta reservada_nueva')
                else:
                    self.agregarError('signoIgual',token.tipo)
                    print('Error falta signo igual')
            else:
                self.agregarError('identificador',token.tipo)
                print('Error falta identificador')
        else:
            self.agregarError('reservada_BuscarTodo','EOF')
            print('Error')
        
    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        '''x = PrettyTable()
        x.field_names = ["Descripcion"]
        for error_ in self.errores:
            x.add_row([error_])
        print(x)   '''        