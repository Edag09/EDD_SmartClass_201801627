import json
from io import open
import re
from NodeThreeAVL_Student import NSThreeAVL
from ThreeAVLStudent import ThreeAVL


class Symbol:
    def __init__(self):
        self.token = ""
        self.lex = ""

    def insert(self, Id, Cont):
        self.token = Id
        self.lex = Cont


sym = Symbol()


class Analyzer:
    def __init__(self):
        self.cad = " "
        self.condition = False
        self.symbol = []
        # alumnos
        self.state = 0
        self.student_entry = None
        self.entry = ''
        self.student = False
        self.homework = False
        self.value = ""
        self.id = False
        self.cad = False
        self.number = False

    def Files_Pens_Upload(self, data):
        file = open(data, 'r', encoding='UTF-8')
        linea = file.read()
        JsonF = self.analyzer(linea)
        newFile = open('CursPensum.json', 'w', encoding='UTF-8')
        newFile.write(JsonF)
        newFile.close()

        with open('CursPensum.json', 'r', encoding='UTF-8') as information:
            data = json.load(information)
        for name in data:
            print(name.get('Nombre') + ' -> ' + str(name.get("Codigo")) + ' -> ' + str(name.get("Creditos")))

    def analyzer(self, data):
        for character in data:
            if character == "[":
                self.condition = True
                self.cad += character
            elif character == "]":
                self.condition = False
                self.cad += character
            elif self.condition:
                self.cad += character
        return self.cad

    def File_Entry(self):
        file = open("Estudiantes.txt", 'r', encoding='UTF-8')
        line = file.read()
        file.close()
        self.entry = line.split("\n")
        for data in self.entry:
            if re.match(r'[^\t]*¿element type=\"user\"?', data):
                # print(data)
                self.student = True
                self.homework = False
            elif re.match(r'[^\t]*¿element type=\"task\"?', data):
                if self.student is True:
                    self.student = False
                    self.homework = True
            elif self.student is True:
                self.Student_(data)
            elif self.homework:
                pass

    def Student_(self, data):
        char = list(data)
        for character in char:
            if self.id:
                self.Identification(character)
            elif self.cad:
                self.Cad(character)
            elif self.number:
                self.Number(character)
            elif character.isalpha():
                self.id = True
                self.value = character
            elif character.isdigit():
                self.id = True
                self.value = character
            elif ord(character) == 34:
                self.cad = True
            elif ord(character) == 32:
                pass

    def Identification(self, character):
        if character.isalpha():
            self.value += character
            return
        elif ord(character) == 32:
            self.symbol.append(sym.insert("ID", self.value))
            self.value = ""
            self.id = False
        elif ord(character) == 61:
            self.symbol.append(sym.insert("ID", self.value))
            self.value = ""
            self.id = False
        elif ord(character) == 63:
            self.symbol.append(sym.insert("ID", self.value))
            self.value = ""
            self.id = False
        print(sym.token)
        print(sym.lex)

    def Cad(self, character):
        if ord(character) == 34:
            self.symbol.append(sym.insert("Cadena", self.value))
            self.value = ""
            self.cad = False
            return
        self.value += character

    def Number(self, character):
        if character.isdigit():
            self.value += character
            return
        self.symbol.append(sym.insert("Numero", self.value))
        self.value = ""
        self.number = False

    def sep_student(self, character):
        print(character)
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
                self.student_entry.Carnet = character.lex
                self.state = 2
        elif self.state == 2:
            if character.lex == "item":
                self.state = 0
            if character.lex == "element":
                # Aqui va el incertar alumnos al arbol
                self.student_entry = None
                self.student = False
                self.state = 0
        elif self.state == 3:
            if character.token == "Cadena":
                self.student_entry.DPI = character.lex
                self.state = 2
        elif self.state == 4:
            if character.token == "Cadena":
                self.student_entry.Name = character.lex
                self.state = 2
        elif self.state == 5:
            if character.token == "Cadena":
                self.student_entry.Carrera = character.lex
                self.state = 2
        elif self.state == 6:
            if character.token == "Cadena":
                self.student_entry.Password = character.lex
                self.state = 2
        elif self.state == 7:
            if character.token == "Cadena":
                self.student_entry.Creditos = character.lex
                self.state = 2
        elif self.state == 8:
            if character.token == "Numero":
                self.student_entry.Edad = character.lex
                self.state = 2
        elif self.state == 9:
            if character.token == "Cadena":
                self.student_entry.Correo = character.lex
                self.state = 2

    def insert(self):
        for data in self.symbol:
            if self.student is False:
                self.sep_student(data)
            elif data.lex == "item":
                self.state = 0
                self.state = True
