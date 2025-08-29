class Personaje:
    def __init__(self, id, nombre, vida, fuerza, objetos=None):
        self.__id = id
        self.__nombre = nombre
        self.__vida = vida
        self.__fuerza = fuerza
        self.__objetos = objetos if objetos is not None else []

    def setID(self, newID):
        self.__id = newID

    def getID(self):
        return self.__id
    
    def setNombre(self, newName):
        self.__nombre = newName

    def getNombre(self):
        return self.__nombre
    
    def setFuerza(self, newFuerza):
        self.__fuerza = newFuerza

    def getFuerza(self):
        return self.__fuerza
    
    def setVida(self, newVida):
        self.__vida = newVida

    def getVida(self):
        return self.__vida
    
    def atacar(self):
        print(f"El personaje ataca con {self.__fuerza}")

    def agregarObjeto(self, object):
        self.__objetos.append(object)

    def eliminarObjetos(self, object):
        for i in self.__objetos:
            if i == object:
                self.__objetos.remove(object)
    
    def listarObjetos(self):
        if not self.__objetos:
            print("No tiene objetos")
        for objeto in self.__objetos:
            print(objeto)

    def __str__(self):
        return f"Nombre: {self.__nombre}\nVida: {self.__vida}\nDaño: {self.__fuerza}\nObjetos: {self.__objetos}"