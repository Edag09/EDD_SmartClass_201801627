import NodeThreeAVL_Student
import os


class ThreeAVL:
    def __init__(self):
        self.root = None

    def insertThree(self, node_Student):
        self.root = self.secondInsert(node_Student, self.root)

    def compare(self, value, value1):
        if value > value1:
            return value
        else:
            return value1

    def long(self, node):
        if node is not None:
            return node.alt
        return -1

    def secondInsert(self, student, root):
        if root is None:
            return student
        else:
            if student.Carnet < root.Carnet:
                root.izq = self.secondInsert(student, root.izq)
                if self.long(root.der) - self.long(root.izq) == -2:
                    if student.Carnet < root.izq.Carnet:
                        root = self.RI(root)
                    else:
                        root = self.RDI(root)
            elif student.Carnet > root.Carnet:
                root.der = self.secondInsert(student, root.der)
                if self.long(root.der) - self.long(root.izq) == 2:
                    if student.Carnet > root.der.Carnet:
                        root = self.RD(root)
                    else:
                        root = self.RDD(root)
            else:
                root.label = student
        root.alt = self.compare(self.long(root.izq), self.long(root.der)) + 1
        return root

    def RD(self, student):
        temp = student.der
        student.der = temp.izq
        temp.izq = student
        student.alt = self.compare(self.long(student.izq), self.long(student.der)) + 1
        temp.alt = self.compare(self.long(temp.izq), self.long(temp.der)) + 1
        return temp

    def RI(self, student):
        temp = student.izq
        student.izq = temp.der
        temp.der = student
        student.alt = self.compare(self.long(student.izq), self.long(student.der)) + 1
        temp.alt = self.compare(self.long(temp.izq), self.long(temp.der)) + 1
        return temp

    def RDI(self, student):
        student.izq = self.RD(student.izq)
        return self.RI(student)

    def RDD(self, student):
        student.der = self.RI(student.der)
        return self.RD(student)

    def Graph_AVL(self, leaf_students):
        graph = "digraph Three {\nrankdir=TB;\nnode [shape = record, color=black , style=filled, fillcolor=gray93];\n"
        body = self.Graph_ThreeAVL(leaf_students)
        graph += body
        graph += "\n}"

        try:
            file = open("ArbolEstudiantes.dot", 'w', encoding='UTF-8')
            file.write(graph)
            file.close()

            os.system("dot -Tpng ArbolEstudiantes.dot -o ArbolEstudiantes.png")
            os.startfile("ArbolEstudiantes.png")
            print("Si jalo :D")
        except:
            print("No se genero :)")

    def Graph_ThreeAVL(self, leaf_students):
        data = ""
        if (leaf_students.izq is None) and (leaf_students.der is None):
            data += "Node" + str(leaf_students.Carnet) + "[label=\"" + "Carne: " + str(leaf_students.Carnet) + "\"];\n"
        else:
            data += "Node" + str(leaf_students.Carnet) + "[label =\"<C0>|" + str(leaf_students.Carnet) + "|<C1>\"];\n"

        if leaf_students.izq is not None:
            data += self.Graph_ThreeAVL(leaf_students.izq) + "Node" + str(leaf_students.Carnet) + ":C0->Node" + str(
                leaf_students.izq.Carnet) + "\n"
        if leaf_students.der is not None:
            data += self.Graph_ThreeAVL(leaf_students.der) + "Node" + str(leaf_students.Carnet) + ":C1->Node" + str(
                leaf_students.der.Carnet) + "\n"
        return data

    # ingresa el anio si el estudiante si tiene tarea
    def insert_year(self, carnet, year, node):
        if node is None:
            print("Tree is empty year")
        elif node.Carnet == carnet:
            node.anios.AddListYear(year)
            print("Los datos son: ", node.Carnet)
        elif carnet < node.Carnet:
            return self.insert_year(carnet, year, node.izq)
        elif carnet > node.Carnet:
            return self.insert_year(carnet, year, node.der)

    # busca el mes y e interiormente inserta los meses si existe el patojo
    def findM(self, carnet, year, mes, node):
        if node is None:
            print('Tree is empty mes')
        elif node.Carnet == carnet:
            node.anios.insertM(year, mes, node.anios.first)
        elif carnet < node.Carnet:
            return self.findM(carnet, year, mes, node.izq)
        elif carnet > node.Carnet:
            return self.findM(carnet, year, mes, node.der)

    # busca el semestre y e interiormente inserta los semestres si existe el patojo
    def findS(self, carnet, year, semester, node):
        if node is None:
            print("Tree is empty semester")
        elif node.Carnet == carnet:
            node.anios.insertSemester(year, semester, node.anios.first)
        elif carnet < node.Carnet:
            return self.findS(carnet, year, semester, node.izq)
        elif carnet > node.Carnet:
            return self.findS(carnet, year, semester, node.der)

    # Mostrar el json de los estudiantes
    def ShowStudentJSON(self, node, carnet):
        if node is not None:
            return 'Tree AVL is empty'
        elif node.Carnet == carnet:
            Student = {
                'Carnet ': node.Carnet,
                'DPI ': node.DPI,
                'Nombre ': node.Name,
                'Carrera ': node.Carrera,
                'Correo ': node.Correo,
                'Password ': node.Password,
                'Creditos ': node.Creditos,
                'Edad ': node.Edad
                }
            return Student
        elif carnet < node.Carnet:
            return self.ShowStudentJSON(node.izq, carnet)
        elif carnet > node.Carnet:
            return self.ShowStudentJSON(node.der, carnet)

    # Update (PUT) Student
    def Update_Student(self, carnet, dpi, nombre, carrera, correo, password, creditos, edad, node):
        if node is None:
            return 'Tree is Empty'
        elif node.Carnet == carnet:
            node.Carnet = carnet
            node.DPI = dpi
            node.Name = nombre
            node.Carrera = carrera
            node.Correo = correo
            node.Password = password
            node.Creditos = creditos
            node.Edad = edad
        elif carnet < node.Carnet:
            return self.Update_Student(carnet, dpi, nombre, carrera, correo, password, creditos, edad, node.izq)
        elif carnet > node.Carnet:
            return self.Update_Student(carnet, dpi, nombre, carrera, correo, password, creditos, edad, node.der)

    # Busacar en la matriz el nodo de la tarea
    def findMatrix(self, carnet, year, mes, day, hora, node):
        if node is None:
            return 'Tree is empty'
        elif node.Carnet == carnet:
            return node.anios.find_Mes(year, mes, day, hora, node.anios.first)
        elif carnet < node.Carnet:
            return self.findMatrix(carnet, year, mes, day, hora, node.izq)
        elif carnet > node.Carnet:
            return self.findMatrix(carnet, year, mes, day, hora, node.der)

    # ingreso del nodo de la tarea
    def insert_List_Homework(self, task, node, lex):
        if node is None:
            return 'Tree is Empty'
