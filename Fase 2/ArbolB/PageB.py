from ArbolB.DoubleList import DoubleList
from ArbolB.PointerList import PointerList


class PageB:
    def __init__(self):
        self.cuenta = 0
        self.maxClaves = 0
        self.punteros = PointerList()
        self.datos = DoubleList()

        for i in range(1, 6):
            if i != 4:
                self.datos.InsertNodeData("", None, None, None, None)
            self.punteros.Insert_Pointer(None)
        self.maxClaves = 5

    def paginaLlena(self):
        return self.cuenta == self.maxClaves - 1

    def paginacasillenax3(self):
        return self.cuenta == self.maxClaves/2

    def getCuenta(self):
        return self.cuenta

    def setCuenta(self, cuenta):
        self.cuenta = cuenta

    def getMaxClaves(self):
        return self.maxClaves

    def setMaxClaves(self, maxClaves):
        self.maxClaves = maxClaves

    def getCodigo(self, posicion):
        return self.datos.Dev_Data(posicion).getCodigo()

    def setCodigo(self, posicion, codigo):
        self.datos.InsertData(codigo, posicion)

    def getPais(self, posicion):
        return  self.datos.Dev_Data(posicion).getPais()

    def setPais(self, posicion, pais):
        return self.datos.Dev_Data(posicion).setPais(pais)

    def getCreditos(self, posicion):
        return self.datos.Dev_Data(posicion).getCreditos()

    def setCreditos(self, posicion, creditos):
        self.datos.Dev_Data(posicion).setCreditos(creditos)

    def getPrerequisitos(self, posicion):
        return self.datos.Dev_Data(posicion).getPrerequisitos()

    def setPrerequisitos(self, posicion, prerrequisito):
        self.datos.Dev_Data(posicion).setPrerequisitos(prerrequisito)

    def getObligatorio(self, posicion):
        return self.datos.Dev_Data(posicion).getObligatorio()

    def setObligatorio(self, posicion, pre):
        self.datos.Dev_Data(posicion).setObligatorio(pre)

    def getApuntador(self, posicion):
        return self.punteros.dev_Data(posicion).getPointer()

    def setApuntador(self, posicion, puntero):
        self.punteros.Insert_PointerP(puntero, posicion)
