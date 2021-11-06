from NodeApuntes import NodeApuntesHash


class HashListApuntes:
    def __init__(self):
        self.first = None
        self.end = None

    def addApunte(self, nombre, apunte):
        nuevoApunte = NodeApuntesHash(nombre, apunte)
        if self.first is None:
            self.first = nuevoApunte
            self.end = self.first
            self.first.Sig = None
            self.end.Ant = None
        else:
            self.end.Sig = nuevoApunte
            nuevoApunte.Ant = self.end
            nuevoApunte.Sig = None
            self.end = nuevoApunte

    def showList(self):
        aux = self.first
        while aux is not None:
            print("Nombre del Apunte: " + aux.Titulo + "\nContenido: " + aux.Contenido + "\n")
            aux = aux.Sig

    def GraphList(self, data):
        aux = self.first
        cont = 0
        body = ""
        while aux is not None:
            body += 'Node' + str(data) + 'A' + str(cont) + '[label="' + aux.Titulo + '\\n' + aux.Contenido + '" shape="box"] \n'
            if aux == self.first:
                body += 'struct1:f' + str(data) + '->Node' + str(data) + 'A' + str(cont) + '\n'
                cont += 1
                aux = aux.Sig
            else:
                body += 'Node' + str(data) + 'A' + str(cont-1) + '->Node' + str(data) + 'A' + str(cont) + '\n'
                cont += 1
                aux = aux.Sig
        return body
