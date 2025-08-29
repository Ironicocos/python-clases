from Personaje import Personaje
from Objeto import Objeto
from TipoObjeto import TipoObjeto
arma = TipoObjeto(0, "arma")
pistola = Objeto(23, "Pistola", 300, arma)
Personaje1 = Personaje(1, "Pepe", 500, 400, [pistola])
print(arma)
print(pistola)
print(Personaje1)
Personaje1.listarObjetos()