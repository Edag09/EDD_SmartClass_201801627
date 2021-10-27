import json
from io import open
import re
from NodeThreeAVL_Student import NSThreeAVL
from ThreeAVLStudent import ThreeAVL
from LCD_Homeworks import ListCircularDoubleHomeworks
from NodeHomework import Nodehomework
from SparseMatrix import HeadBoard
from ArbolB.Tree_B import TreeB
from SparseMatrix import Data
from LCD_Meses import ListCircularDoubleMeses

headDay = HeadBoard()
headHora = HeadBoard()
avl = ThreeAVL()
homework = ListCircularDoubleHomeworks()
pensum = TreeB()
data = Data()
mes = ListCircularDoubleMeses()


class Analyzer:
    def __init__(self):
        self.cad = " "
        self.condition = False
        self.symbol = []
        self.symbolTask = []
        self.listTask = []
        self.day = []
        self.hora = []
        self.date = ""
        self.state = 0
        self.student_entry = None
        self.homework_entry = None
        self.entry = ''
        self.student = False
        self.homework = False
        self.value = ""
        self.id = False
        self.cad = False
        self.number = False

    # ------------------------------ Analyzer Json ----------------------------

    def Files_Pens_Upload(self, dataJ):
        with open(dataJ, encoding='UTF-8') as file:
            data = json.load(file)

            for pen in data['Cursos']:
                """print('Codigo: ', pen['Codigo'])
                print('Nombre: ', pen['Nombre'])
                print('Creditos: ', pen['Creditos'])
                print('Prerequisitos: ', pen['Prerequisitos'])
                print('Obligatorio: ', pen['Obligatorio'])
                print('\n')"""
                # Informacion agregada al B
                pensum.InsertDataB(pen['Codigo'], pen['Nombre'], pen['Creditos'], pen['Prerequisitos'], pen['Obligatorio'])

    def File_Student_Curse(self, curseS):
        with open(curseS, encoding='UTF-8') as file:
            data = json.load(file)

            for student in data['Estudiantes']:
                # print("Carnet: ", student['Carnet'])
                for years in student['Años']:
                    # print('Año', years['Año'])
                    avl.insert_year(student['Carnet'], years['Año'], avl.root)
                    for semester in years['Semestres']:
                        avl.findS(student['Carnet'], years['Año'], int(semester['Semestre']), avl.root)
                        for curse in semester['Cursos']:
                            # print('Codigo: ', curse['Codigo'])
                            # print('Nombre: ', curse['Nombre'])
                            # print('Creditos: ', curse['Creditos'])
                            # print('Prerequisitos: ', curse['Prerequisitos'])
                            # print('Obligatorio: ', curse['Obligatorio'])
                            avl.insertCurse(student['Carnet'], years['Año'], int(semester['Semestre']), curse['Codigo'], curse['Nombre'], curse['Creditos'], curse['Prerequisitos'], curse['Obligatorio'], avl.root)

    # ------------------------------ Analyzer txt ----------------------------

    def File_Entry(self, student):
        file = open(student, 'r', encoding='UTF-8')
        line = file.read()
        file.close()
        self.entry = line.split("\n")
        for data in self.entry:
            if re.match(r'[^\t]*¿element type=\"user\"?', data):
                self.student = True
                self.homework = False
            elif re.match(r'[^\t]*¿element type=\"task\"?', data):
                if self.student is True:
                    self.student = False
                    self.homework = True
            elif self.student is True:
                self.Student_(data)
            elif self.homework is True:
                self.Homeworks(data)

    # ------------------------------------------------------------------------------ Student

    def Student_(self, data):
        # print(data)
        char = list(data)
        # print(char)
        for character in char:
            if self.id:
                # print(character)
                self.Identification(character)
            elif self.cad:
                # print(character)
                self.Cad(character)
            elif self.number:
                # print(character)
                self.Number(character)
            elif character.isalpha():
                self.id = True
                self.value = character
                # print(self.value)
            elif character.isdigit():
                self.number = True
                self.value = character
                # print(character)
            elif ord(character) == 34:
                self.cad = True
            elif ord(character) == 32:
                pass

    def Identification(self, character):
        if character.isalpha():
            self.value += character
            return
        elif ord(character) == 32:
            # print(self.value)
            self.symbol.append(Symbol("ID", self.value))
            self.value = ""
            self.id = False
        elif ord(character) == 61:  # =
            # print(self.value)
            self.symbol.append(Symbol("ID", self.value))
            self.value = ""
            self.id = False
        elif ord(character) == 63:  # ?
            # print(self.value)
            self.symbol.append(Symbol("ID", self.value))
            self.value = ""
            self.id = False

    def Cad(self, character):
        if ord(character) == 34:
            self.symbol.append(Symbol("Cadena", self.value))
            self.value = ""
            self.cad = False
            return
        self.value += character

    def Number(self, character):
        if character.isdigit():
            self.value += character
            return
        self.symbol.append(Symbol("Numero", self.value))
        self.value = ""
        self.number = False

    def sep_student(self, character):
        if self.state == 0:
            if character.lex == "Carnet":
                self.student_entry = NSThreeAVL(0, 0, 0, 0, 0, 0, 0, 0)
                self.state = 1
            elif character.lex == "DPI":
                self.state = 3
            elif character.lex == "Nombre":
                self.state = 4
            elif character.lex == "Carrera":
                self.state = 5
            elif character.lex == "Password":
                self.state = 6
            elif character.lex == "Creditos":
                self.state = 7
            elif character.lex == "Edad":
                self.state = 8
            elif character.lex == "Correo":
                self.state = 9
        elif self.state == 1:
            if character.token == "Cadena":
                # print(character.lex)
                self.student_entry.Carnet = character.lex
                self.state = 2
        elif self.state == 2:
            if character.lex == "item":
                self.state = 0
            if character.lex == "element":
                avl.insertThree(self.student_entry)
                self.student_entry = None
                self.student = False
                self.state = 0
        elif self.state == 3:
            if character.token == "Cadena":
                # print(character.lex)
                self.student_entry.DPI = character.lex
                self.state = 2
        elif self.state == 4:
            if character.token == "Cadena":
                # print(character.lex)
                self.student_entry.Name = character.lex
                self.state = 2
        elif self.state == 5:
            if character.token == "Cadena":
                # print(character.lex)
                self.student_entry.Carrera = character.lex
                self.state = 2
        elif self.state == 6:
            if character.token == "Cadena":
                # print(character.lex)
                self.student_entry.Password = character.lex
                self.state = 2
        elif self.state == 7:
            if character.token == "Numero":
                # print(character.lex)
                self.student_entry.Creditos = character.lex
                self.state = 2
        elif self.state == 8:
            if character.token == "Numero":
                # print(character.lex)
                self.student_entry.Edad = character.lex
                self.state = 2
        elif self.state == 9:
            if character.token == "Cadena":
                self.student_entry.Correo = character.lex
                self.state = 2

    def insert(self):
        for a in self.symbol:
            if self.student:
                self.sep_student(a)
            elif a.lex == "item":
                self.state = 0
                self.student = True

    # ---------------------------------------------------------------------------- Homeworks

    def Homeworks(self, data):
        # print(data)
        char = list(data)
        for character in char:
            if self.id:
                self.IdentificationH(character)
            elif self.cad:
                self.CadH(character)
            elif character.isalpha():
                self.id = True
                self.value = character
            elif ord(character) == 34:
                self.cad = True
            elif ord(character) == 32:
                pass

    def IdentificationH(self, data):
        if data.isalpha():
            self.value += data
            return
        elif ord(data) == 32:
            self.symbolTask.append(Symbol("ID", self.value))
            self.value = ""
            self.id = False
        elif ord(data) == 61:
            self.symbolTask.append(Symbol("ID", self.value))
            self.value = ""
            self.id = False
        elif ord(data) == 63:
            self.symbolTask.append(Symbol("ID", self.value))
            self.value = ""
            self.id = False

    def CadH(self, data):
        if ord(data) == 34:
            self.symbolTask.append(Symbol("Cadena", self.value))
            self.value = ""
            self.cad = False
            return
        self.value += data

    def sep_homeworks(self, data):
        if self.state == 0:
            if data.lex == "Carnet":
                self.state = 1
                self.homework_entry = Nodehomework(0, 0, 0, 0, 0, 0, 0, 0)
            elif data.lex == "Nombre":
                self.state = 3
            elif data.lex == "Descripcion":
                self.state = 4
            elif data.lex == "Materia":
                self.state = 5
            elif data.lex == "Fecha":
                self.state = 6
            elif data.lex == "Hora":
                self.state = 7
            elif data.lex == "Estado":
                self.state = 8
        elif self.state == 1:
            if data.token == "Cadena":
                self.homework_entry.Carne = data.lex
                # print(self.homework_entry.Carne)
                self.state = 2
        elif self.state == 2:
            if data.lex == "item":
                self.state = 0
            elif data.lex == "element":
                # self.listTask.append(self.homework_entry)
                avl.insert_List_Homework(self.homework_entry, avl.root, self.homework_entry.Carne, self.homework_entry.Name, self.homework_entry.Description, self.homework_entry.Materia, self.homework_entry.Date, self.homework_entry.Hora, self.homework_entry.Status, 'insertar')
                avl.insert_List_Homework(self.homework_entry, avl.root, self.homework_entry.Carne, self.homework_entry.Name, self.homework_entry.Description, self.homework_entry.Materia, self.homework_entry.Date, self.homework_entry.Hora, self.homework_entry.Status, 'tarea')
                self.homework_entry = None
                self.homework = False
                self.state = 0
        elif self.state == 3:
            if data.token == "Cadena":
                self.homework_entry.Name = data.lex
                # print(self.homework_entry.Name)
                self.state = 2
        elif self.state == 4:
            if data.token == "Cadena":
                self.homework_entry.Description = data.lex
                # print(self.homework_entry.Description)
                self.state = 2
        elif self.state == 5:
            if data.token == "Cadena":
                self.homework_entry.Materia = data.lex
                # print(self.homework_entry.Materia)
                self.state = 2
        elif self.state == 6:
            if data.token == "Cadena":
                self.homework_entry.Date = data.lex
                self.date = data.lex.split('/')
                # headDay.Insert_Headboard(self.date[0])
                # self.day.append(self.date[0])
                # print(self.date)
                avl.insert_year(self.homework_entry.Carne, self.date[2], avl.root)
                avl.findM(self.homework_entry.Carne, self.date[2], int(self.date[1]), avl.root)
                # print(self.homework_entry.Date)
                self.state = 2
        elif self.state == 7:
            if data.token == "Cadena":
                self.homework_entry.Hora = data.lex
                # hora = data.lex.split(':')
                # headHora.Insert_Headboard(self.date[0])
                # self.hora.append(self.date[0])
                # print(self.homework_entry.Hora)
                avl.findMatrix(self.homework_entry.Carne, self.date[2], self.date[1], self.date[0], self.homework_entry.Hora, avl.root)
                self.homework_entry.dispersa = self.date
                self.state = 2
        elif self.state == 8:
            if data.token == "Cadena":
                self.homework_entry.Status = data.lex
                # print(self.homework_entry.Status)
                self.state = 2

    def insert_H(self):
        for t in self.symbolTask:
            if self.homework:
                self.sep_homeworks(t)
            elif t.lex == "item":
                self.state = 0
                self.homework = True
        print("entra")
        self.ver()

    """def llenado(self):
        cont = 1
        for task in self.listTask:
            homework.AddHomeworks(cont, task.Carne, task.Name, task.Description, task.Materia, task.Date, task.Hora,
                                  task.Status)
            cont += 1"""

    def ver(self):
        homework.showList()


class Symbol:
    def __init__(self, ID, cont):
        self.token = ID
        self.lex = cont
