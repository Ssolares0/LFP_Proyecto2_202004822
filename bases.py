

def CrearBD(name):
    print(f'use(\'{name}\');')

def EliminarBD(name):
    print(f'db.dropDatabase();')

def CrearColeccion(name):
    print(f'db.createCollection(\'{name}\');')    