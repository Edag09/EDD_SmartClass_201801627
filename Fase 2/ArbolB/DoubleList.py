from ArbolB.NodeDouble import DoubleNode


class DoubleList:
    def __init__(self):
        self.cuenta = 0
        self.First = None
        self.End = None

    def InsertNodeData(self, codigo, pais, creditos, prerequisitos, obligatorios):
        nuevo = DoubleNode(codigo, pais, creditos, prerequisitos, obligatorios)
        if self.cuenta < 4:
            if self.First is None:
                self.First = nuevo
                self.End = self.First
            else:
                self.End.setSig(nuevo)
                nuevo.setAnt(self.End)
                self.End = nuevo
            self.cuenta += 1
        else:
            print('Nodo superado')

    def InsertData(self, codigo, posicion):
        aux = self.First
        while posicion is not 0:
            posicion -= 1
            aux = aux.getSig()
        aux.setCodigo(codigo)

    def Dev_Data(self, posicion):
        aux = self.First
        while posicion is not 0:
            posicion -= 1
            aux = aux.getSig()
        return aux

    def show_Data(self):
        aux = self.First
        while aux is not None:
            print('Dato: ' + aux.getCodigo())
            aux = aux.getSig()
