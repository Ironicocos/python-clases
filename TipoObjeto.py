class TipoObjeto:
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre

    def setID(self, newID):
        self.__id = newID

    def getID(self):
        return self.__id
    
    def setNombre(self, newName):
        self.__nombre = newName

    def getNombre(self):
        return self.__nombre
    
    def __str__(self):
        return f"Nombre: {self.__nombre}"