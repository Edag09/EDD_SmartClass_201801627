import os


class ThreeAVL:
    def __init__(self):
        self.root = None

    def insertThree(self, node_Student):
        self.root = self.secondInsert(node_Student, self.root)
        print('Estudiante Ingresado')

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
            return 'Year is Empty in ALV'
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
            return 'Tree is empty mes'
        elif node.Carnet == carnet:
            node.anios.insertM(year, mes, node.anios.first)
        elif carnet < node.Carnet:
            return self.findM(carnet, year, mes, node.izq)
        elif carnet > node.Carnet:
            return self.findM(carnet, year, mes, node.der)

    # busca el semestre y e interiormente inserta los semestres si existe el patojo
    def findS(self, carnet, year, semester, node):
        if node is None:
            return "Tree is empty semester"
        elif node.Carnet == carnet:
            node.anios.insertSemester(year, semester, node.anios.first)
        elif carnet < node.Carnet:
            return self.findS(carnet, year, semester, node.izq)
        elif carnet > node.Carnet:
            return self.findS(carnet, year, semester, node.der)

    # Mostrar el json de los estudiantes
    def ShowStudentJSON(self, node, carnet, passo):
        if node is None:
            return 'Tree AVL is empty'
        elif node.Carnet == carnet and node.Password == passo:
            Student = {
                'Carnet': node.Carnet,
                'Nombre': node.Name,
                'Status': 'Yes'
            }
            return Student
        elif carnet.lower() == 'admin' and passo.lower() == 'admin':
            Admin = {
                'Status': 'admin'
            }
            return Admin
        elif node.Carnet != carnet or node.Password != passo:
            Err = {
                'Status': 'No'
            }
            return Err
        elif carnet < node.Carnet:
            return self.ShowStudentJSON(node.izq, carnet, passo)
        elif carnet > node.Carnet:
            return self.ShowStudentJSON(node.der, carnet, passo)

    # Update (PUT) Student
    def Update_Student(self, student, node):
        if node is None:
            return 'Tree is Empty'
        elif node.Carnet == student['Carnet']:
            node.Carnet = student['Carnet']
            node.DPI = student['DPI']
            node.Name = student['Nombre']
            node.Carrera = student['Carrera']
            node.Correo = student['Correo']
            node.Password = student['Password']
            node.Creditos = student['Creditos']
            node.Edad = student['Edad']
        elif student['Carnet'] < node.Carnet:
            return self.Update_Student(student, node.izq)
        elif student['Carnet'] > node.Carnet:
            return self.Update_Student(student, node.der)

    # Busacar en la matriz el nodo de la tarea
    def findMatrix(self, carnet, year, mes, day, hora, node):
        if node is None:
            return 'Tree is empty'
        elif node.Carnet == carnet:
            hor = hora.split(':')
            return node.anios.find_Mes(year, mes, day, hor[0], node.anios.first)
        elif carnet < node.Carnet:
            return self.findMatrix(carnet, year, mes, day, hora, node.izq)
        elif carnet > node.Carnet:
            return self.findMatrix(carnet, year, mes, day, hora, node.der)

    # --------------------------------------- // Insertar Tareas // ----------------------------------------------------
    # insertar la tarea desde el avl
    def insert_List_Homework(self, task, node, carnet, nombre, descripcion, materia, fecha, hora, estado, lex):
        if node is None:
            return 'Empty AVL Homework'
        elif node.Carnet == task.Carne:
            node.anios.insert_HomeworkY(task, node.anios.first, lex, carnet, nombre, descripcion, materia, fecha, hora,
                                        estado)
        elif task.Carne < node.Carnet:
            return self.insert_List_Homework(task, node.izq, carnet, nombre, descripcion, materia, fecha, hora, estado,
                                             lex)
        elif task.Carne > node.Carnet:
            return self.insert_List_Homework(task, node.der, carnet, nombre, descripcion, materia, fecha, hora, estado,
                                             lex)

    # insertar la tarea a manita desde el avl
    def insert_a_manita_homework(self, task, node, lex, enlaces):
        if node is None:
            return 'No hay tarea'
        elif node.Carnet == task['Carnet']:
            node.anios.insert_a_manita_HomeworkY(task, node.anios.first, lex, enlaces)
        elif task['Carnet'] < node.Carnet:
            return self.insert_a_manita_homework(task, node.izq, lex, enlaces)
        elif task['Carnet'] > node.Carnet:
            return self.insert_a_manita_homework(task, node.der, lex, enlaces)

    # ------------------------------------------- // Fin de la insercion // --------------------------------------------

    # ------------------  Obtenicon, eliminacion y actualizacion de la tarea desde el avl para cada estudiante ---------
    def get_Homework_AVL(self, carnet, year, mes, day, hora, Id, node, peticion):  # Obtener y eliminar
        if node is None:
            return 'Empty Homework student'
        elif node.Carnet == carnet:
            return node.anios.get_Homework_year(year, mes, day, hora, Id, peticion)
        elif carnet < node.Carnet:
            return self.get_Homework_AVL(carnet, year, mes, day, hora, Id, node.izq, peticion)
        elif carnet > node.Carnet:
            return self.get_Homework_AVL(carnet, year, mes, day, hora, Id, node.der, peticion)

    def update_homework_AVL(self, carnet, year, mes, day, hora, Id, node, peticion, taskJ):
        if node is None:
            return 'No se encontro ninguna tarea'
        elif node.Carnet == carnet:
            return node.anios.update_Homework_year(year, mes, day, hora, Id, peticion, taskJ)
        elif carnet < node.Carnet:
            return self.update_homework_AVL(carnet, year, mes, day, hora, Id, node.izq, peticion, taskJ)
        elif carnet > node.Carnet:
            return self.update_homework_AVL(carnet, year, mes, day, hora, Id, node.der, peticion, taskJ)

    # ------------------------------ Fin -------------------------------------------------------------------------------

    # Ingresar los cursos al arbol b
    def insertCurse(self, carnet, year, semester, codigo, nombre, creditos, prerequisitos, obligatorio, node):
        if node is None:
            return 'Informacion vacia'
        elif node.Carnet == carnet:
            node.anios.Insert_Curse(year, semester, codigo, nombre, creditos, prerequisitos, obligatorio,
                                    node.anios.first)
        elif carnet < node.Carnet:
            return self.insertCurse(carnet, year, semester, codigo, nombre, creditos, prerequisitos, obligatorio,
                                    node.izq)
        elif carnet > node.Carnet:
            return self.insertCurse(carnet, year, semester, codigo, nombre, creditos, prerequisitos, obligatorio,
                                    node.der)

    # La banda unida :D
    def Together(self, nodeAVL, task, enlaces):
        if nodeAVL is None:
            return 'insert invalido'
        elif nodeAVL.Carnet == task['Carnet']:
            # inserta el anio
            self.insert_year(task['Carnet'], enlaces[2], nodeAVL)
            # inserta el mes
            self.findM(task['Carnet'], enlaces[2], enlaces[1], nodeAVL)
            # inserta las cabeceras
            self.findMatrix(task['Carnet'], enlaces[2], enlaces[1], enlaces[0], task['Hora'], nodeAVL)
            # inserta la tarea
            self.insert_a_manita_homework(task, nodeAVL, 'insertar', enlaces)
            self.insert_a_manita_homework(task, nodeAVL, 'tarea', enlaces)
        elif task['Carnet'] < nodeAVL.Carnet:
            return self.Together(nodeAVL.izq, task, enlaces)
        elif task['Carnet'] > nodeAVL.Carnet:
            return self.Together(nodeAVL.der, task, enlaces)

    # Graficar las tareas
    def Go_Graph_HomeworksAVL(self, carnet, year, mes, day, hora, node):
        if node is None:
            'No hay tareas aun ingresadas'
        elif node.Carnet == carnet:
            node.anios.Go_Graph_HomeworksY(year, mes, day, hora, node.anios.first)
        elif carnet < node.Carnet:
            return self.Go_Graph_HomeworksAVL(carnet, year, mes, day, hora, node.izq)
        elif carnet > node.Carnet:
            return self.Go_Graph_HomeworksAVL(carnet, year, mes, day, hora, node.der)
