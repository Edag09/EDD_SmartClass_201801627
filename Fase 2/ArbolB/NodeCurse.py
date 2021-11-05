class DoubleNodeCurse:
    def __init__(self, codigo, nombre, creditos, prerequisitos, obligatior):
        self.Codigo = codigo
        self.Nombre = nombre
        self.Creditos = creditos
        self.Prerequisitos = prerequisitos
        self.Obligatorio = obligatior
        self.Sig = None
        self.Ant = None