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
