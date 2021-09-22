class DoubleNode:
    def __init__(self, codigo, pais, creditos, prerequisitos, obligatorio):
        self.Codigo = codigo
        self.Pais = pais
        self.Creditos = creditos
        self.Prerequisitos = prerequisitos
        self.Obligatorio = obligatorio
        self.Sig = None
        self.Ant = None

    def getCodigo(self):
        return self.Codigo

    def setCodigo(self, codigo):
        self.Codigo = codigo

    def getPais(self):
        return self.Pais

    def setPais(self, pais):
        self.Pais = pais

    def getCreditos(self):
        date = self.Creditos
        return date

    def setCreditos(self, creditos):
        self.Creditos = creditos

    def getPrerequisitos(self):
        return self.Prerequisitos

    def setPrerequisitos(self, prerequisitos):
        self.Prerequisitos = prerequisitos

    def getObligatorio(self):
        return self.Obligatorio

    def setObligatorio(self, obligatorio):
        self.Obligatorio = obligatorio

    def getSig(self):
        return self.Sig

    def setSig(self, sig):
        self.Sig = sig

    def getAnt(self):
        return self.Ant

    def setAnt(self, ant):
        self.Ant = ant