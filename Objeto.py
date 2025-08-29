class Objeto:
    def __init__(self, id, nombre, daño, tipoObjeto):
        self.__id = id
        self.__nombre = nombre
        self.__daño = daño
        self.__tipoObjeto = tipoObjeto
    
    def setID(self, newID):
        self.__id = newID

    def getID(self):
        return self.__id
    
    def setNombre(self, newName):
        self.__nombre = newName

    def getNombre(self):
        return self.__nombre
    
    def setDaño(self, newDaño):
        self.__daño = newDaño

    def getDaño(self):
        return self.__daño
    
    def atacarConArma(self):
        print(f"El arma genera {self.__daño} puntos de daño")

    def __str__(self):
        return f"Nombre: {self.__nombre}\nDaño: {self.__daño}\ntipoObjeto: {self.__tipoObjeto}"