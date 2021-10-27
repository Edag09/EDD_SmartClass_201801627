from ArbolB.PageB import PageB
import os


class TreeB:
    def __init__(self):
        self.root = PageB()
        self.Codigo = 0
        self.Nombre = ''
        self.prerrequisitos = ''
        self.creditos = ''
        self.obligatorio = False

        self.aux = False
        self.aux2 = PageB()
        self.up = False
        self.status = False
        self.compare = False

        self.graph = ''
        self.graph2 = PageB()
        self.nombre = ''
        self.node = 0

    def InsertDataB(self, codigo, nombre, creditos, prerequisitos, obligatorio):
        self.Insert_Intern(self.root, codigo, nombre, creditos, prerequisitos, obligatorio)

    def Insert_Intern(self, root, codigo, nombre, creditos, prerequisitos, obligatorio):
        self.push(root, codigo, nombre, creditos, prerequisitos, obligatorio)
        if self.up:
            self.root = PageB()
            self.root.setCuenta(1)
            self.root.setCodigo(0, self.Codigo)
            self.root.setPais(0, self.Nombre)
            self.root.setCreditos(0, self.creditos)
            self.root.setPrerequisitos(0, self.prerrequisitos)
            self.root.setObligatorio(0, self.obligatorio)

            self.root.setApuntador(0, root)
            self.root.setApuntador(1, self.aux2)

    def push(self, root, codigo, nombre, creditos, prerequisitos, obligatorio):
        posicion = 0
        self.status = False
        if ((root is None) or (root.getCuenta() == 0)) and self.compare is False:
            self.up = True
            self.Codigo = codigo
            self.Nombre = nombre
            self.creditos = creditos
            self.prerrequisitos = prerequisitos
            self.obligatorio = obligatorio
            self.aux2 = None
        else:
            posicion = self.FindB(codigo, root)
            if self.compare is False:
                if self.status:
                    self.up = False
                else:
                    self.push(root.getApuntador(posicion), codigo, nombre, creditos, prerequisitos, obligatorio)
                    if self.up:
                        if root.getCuenta() < 4:
                            self.up = False
                            self.pushLeaf(root, posicion, self.Codigo, self.Nombre, self.creditos, self.prerrequisitos,
                                          self.obligatorio)
                        else:
                            self.up = True
                            self.sepPageB(root, posicion, self.Codigo, self.Nombre, self.creditos, self.prerrequisitos,
                                          self.obligatorio)
            else:
                print("Repetido " + codigo)
                self.compare = False

    def compareTo(self, codigo, root):
        codlen = len(codigo)
        rootlen = len(root)
        limite = min(codlen, rootlen)

        v1 = list(codigo)
        v2 = list(root)

        i = 0
        while i < limite:
            if ord(v1[i]) != ord(v2[i]):
                return ord(v1[i]) - ord(v2[i])
            i += 1
        return codlen - rootlen

    def FindB(self, codigo, root):
        cont = 0
        if self.compareTo(codigo, root.getCodigo(0)) < 0:
            self.status = False
            cont = 0
        else:
            while cont is not root.getCuenta():
                if codigo == root.getCodigo(cont):
                    self.compare = True
                cont += 1
            cont = root.getCuenta()

            while (self.compareTo(codigo, root.getCodigo(cont - 1)) < 0) and cont > 1:
                cont -= 1
                if codigo == root.getCodigo(cont - 1):
                    self.status = True
                else:
                    self.status = False
        return cont

    def pushLeaf(self, root, posicion, codigo, nombre, creditos, prerrequisitos, obligatorio):
        aux = root.getCuenta()
        while aux is not posicion:
            if aux != 0:
                root.setCodigo(aux, root.getCodigo(aux - 1))
                root.setPais(aux, root.getPais(aux - 1))
                root.setCreditos(aux, root.getCreditos(aux - 1))
                root.setPrerequisitos(aux, root.getPrerequisitos(aux - 1))
                root.setObligatorio(aux, root.getObligatorio(aux - 1))
                root.setApuntador(aux + 1, root.getApuntador(aux))
            aux -= 1

        root.setCodigo(posicion, codigo)
        root.setPais(posicion, nombre)
        root.setCreditos(posicion, creditos)
        root.setPrerequisitos(posicion, prerrequisitos)
        root.setObligatorio(posicion, obligatorio)

        root.setApuntador(posicion + 1, self.aux2)
        root.setCuenta(root.getCuenta() + 1)

    def sepPageB(self, root, posicion, codigo, nombre, creditos, prerrequisitos, obligatorio):
        p2 = 0
        medium = 0

        if posicion <= 2:
            medium = 2
        else:
            medium = 3

        derecha = PageB()
        p2 = medium + 1

        while p2 != 5:
            if (p2 - medium) != 0:
                derecha.setCodigo((p2 - medium) - 1, root.getCodigo(p2 - 1))
                derecha.setPais((p2 - medium) - 1, root.getPais(p2 - 1))
                derecha.setCreditos((p2 - medium) - 1, root.getCreditos(p2 - 1))
                derecha.setPrerequisitos((p2 - medium) - 1, root.getPrerequisitos(p2 - 1))
                derecha.setObligatorio((p2 - medium) - 1, root.getObligatorio(p2 - 1))
                derecha.setApuntador(p2 - medium, root.getApuntador(p2))
            p2 += 1

        derecha.setCuenta(4 - medium)
        root.setCuenta(medium)

        if posicion <= 2:
            self.aux = True
            self.pushLeaf(root, posicion, codigo, nombre, creditos, prerrequisitos, obligatorio)
        else:
            self.aux = True
            self.pushLeaf(derecha, (posicion - medium), codigo, nombre, creditos, prerrequisitos, obligatorio)

        self.Codigo = root.getCodigo(root.getCuenta() - 1)
        self.Nombre = root.getPais(root.getCuenta() - 1)
        self.creditos = root.getCreditos(root.getCuenta() - 1)
        self.prerrequisitos = root.getPrerequisitos(root.getCuenta() - 1)
        self.obligatorio = root.getObligatorio(root.getCuenta() - 1)

        derecha.setApuntador(0, root.getApuntador(root.getCuenta()))

        root.setCuenta(root.getCuenta() - 1)
        self.aux2 = derecha

        if self.aux:
            root.setCodigo(3, '')
            root.setPais(3, '')
            root.setCreditos(3, '')
            root.setPrerequisitos(3, '')
            root.setObligatorio(3, '')
            root.setApuntador(4, None)

            root.setCodigo(2, '')
            root.setPais(2, '')
            root.setCodigo(2, '')
            root.setPrerequisitos(2, '')
            root.setObligatorio(2, '')
            root.setApuntador(3, None)

    def show(self):
        self.showPre(self.root)

    def showPre(self, root):
        if root is not None:
            for i in range(root.getCuenta()):
                if root.getCodigo(i) is not None:
                    if root.getCodigo(i) != "":
                        print(
                            "Codigo: " + str(root.getCodigo(i)) + "\nCurso: " + root.getPais(i) + "\nCreditos: " + str(root.getCreditos(i)) + "\nPrerequisitos: " + root.getPrerequisitos(i) + "\nObligatorio " + str(root.getObligatorio(i)) + '\n')

            self.showPre(root.getApuntador(0))
            self.showPre(root.getApuntador(1))
            self.showPre(root.getApuntador(2))
            self.showPre(root.getApuntador(3))
            self.showPre(root.getApuntador(4))

    def graphG(self, type):
        self.graph = 'digraph TreeB {\n'
        self.graph += 'rankdir=TB;\nNode[color=\"blue\",style=\"rounded,filled\",fillcolor=lightgray, shape=record];\n'

        self.graphG2(self.root)
        self.graphG3(self.root)

        self.graph = '\n}\n'

        file = open('TreeB.dot', 'w', encoding='UTF-8')
        file.write(self.graph)
        file.close()

        os.system('dot -Tpng TreeB.dot -o TreeB' + type + '.png')
        os.startfile('TreeB' + type + '.png')

    def graphG2(self, root):
        cont = 0
        if root is not None:
            self.node = 0
            for i in range(root.getCuenta()):
                if root.getCodigo(i) != '':
                    self.node += 1
                    if i != 0:
                        self.graph += '|'
                    if self.node == 1:
                        self.graph += '\nNode' + root.getCodigo(i) + '[label=\"<f0>|'
                    if i == 0:
                        self.graph += '<f' + str(cont) + '>' + str(root.getCodigo(i)) + '\n' + root.getPais(
                            i) + '|<f' + str(i + 2) + '>'
                        cont = 3
                    else:
                        self.graph += '<f' + str(cont) + '>' + str(root.getCodigo(i)) + '\n' + root.getPais(
                            i) + '|<f' + str(cont + 1) + '>'
                        cont += 2

                    if i == (root.getCuenta() - 1):
                        cont = 0
                        self.graph += '\",group=0];\n'

            self.graphG2(root.getApuntador(0))
            self.graphG2(root.getApuntador(1))
            self.graphG2(root.getApuntador(2))
            self.graphG2(root.getApuntador(3))
            self.graphG2(root.getApuntador(4))

    def graphG3(self, root):
        if root is not None:
            if root.getCodigo(0) is not None:
                if root.getCodigo(0) != '':
                    if (root.getApuntador(0) is not None) and (root.getApuntador(0).getCodigo(0) is not None):
                        self.graph += '\nNode' + str(root.getCodigo(0)) + ':fo->Node' + str(
                            root.getApuntador(0).getCodigo(0))
                        print(self.graph)
                        if (root.getApuntador(1) is not None) and (root.getApuntador(1).getCodigo(0) is not None):
                            self.graph += '\nNode' + str(root.getCodigo(0)) + ':f2->Node' + str(
                                root.getApuntador(1).getCodigo(0))
                        if (root.getApuntador(2) is not None) and (root.getApuntador(2).getCodigo(0) is not None):
                            self.graph += '\nNode' + str(root.getCodigo(0)) + ':f4->Node' + str(
                                root.getApuntador(2).getCodigo(0))
                        if (root.getApuntador(3) is not None) and (root.getApuntador(3).getCodigo(0) is not None):
                            self.graph += '\nNode' + str(root.getCodigo(0)) + ':f6->Node' + str(
                                root.getApuntador(3).getCodigo(0))
                        if (root.getApuntador(4) is not None) and (root.getApuntador(4).getCodigo(0) is not None):
                            self.graph += '\nNode' + str(root.getCodigo(0)) + ':f8->Node' + str(
                                root.getApuntador(4).getCodigo(0))

            self.graphG3(root.getApuntador(0))
            self.graphG3(root.getApuntador(1))
            self.graphG3(root.getApuntador(2))
            self.graphG3(root.getApuntador(3))
            self.graphG3(root.getApuntador(4))
