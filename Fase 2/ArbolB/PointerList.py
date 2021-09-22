from ArbolB.NodePointer import NodePointer


class PointerList:
    def __init__(self):
        self.First = None
        self.End = None
        self.cuenta = 0

    def Insert_Pointer(self, puntero):
        nuevo = NodePointer(puntero)
        if self.cuenta < 5:
            if self.First is None:
                self.First = nuevo
                self.End = self.First
            else:
                self.End.setSigP(nuevo)
                nuevo.setAntP(self.End)
                self.End = nuevo
            self.cuenta += 1

    def Insert_PointerP(self, pagina, posicion):
        aux = self.First
        while posicion != 0:
            posicion -= 1
            aux = aux.getSigP()
        aux.setPointer(pagina)

    def dev_Data(self, posicion):
        aux = self.First
        while posicion != 0:
            posicion -= 1
            aux = aux.getSigP()
        return aux

    def getPrimero(self):
        return self.First

    def setPrimero(self, Primero):
        self.First = Primero

    def getCuenta(self):
        return self.cuenta

    def setCuenta(self, Cuenta):
        self.cuenta = Cuenta
