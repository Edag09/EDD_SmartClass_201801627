import json
from io import open


class Analyzer:
    def __init__(self):
        self.cad = " "
        self.condition = False

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



