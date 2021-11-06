from LCD_Apuntes import HashListApuntes
import os


class nodeHash:
    def __init__(self, carnet):
        self.Carnet = carnet
        self.ListApuntes = HashListApuntes()


class TableHash:
    def __init__(self, long):
        self.Hash = None
        self.Long = long
        self.min = 0
        self.add = 0
        self.Start()
        self.primos = [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                       107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                       211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
                       317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433,
                       439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]

    def Start(self):
        self.add = 0
        self.min = (self.Long / 2) + 0.5
        table = [None] * self.Long
        self.Hash = table

    def insertData(self, info, title, content):
        pos = self.FunctionHash(info)
        try:
            bo = 0
            bo2 = 0
            while info != self.Hash[pos].Carnet:
                if self.Hash[pos] is not None:
                    if bo < 4:
                        bo += 1
                        pos = self.CollisionHash(info, pos)
                        bo2 += 1
                    elif (pos < (self.Long - 1)) and (bo >= 4):
                        pos += 1
                    elif pos == (self.Long - 1):
                        pos = 0
            self.Hash[pos].ListApuntes.addApunte(title, content)
        except:
            print("No existe el dato")

    def FunctionHash(self, info):
        return info % self.Long

    def CollisionHash(self, info, index):
        return (info + (index * index)) % self.Long

    def findID(self, carnet):
        for car in self.Hash:
            if car is None:
                pass
            elif car.Carnet == carnet:
                return True
        return False

    def addHash(self, info):
        if (info is not None) and (self.findID(info) is False):
            pos = self.FunctionHash(info.Carnet)
            cont = 0
            cont1 = 0
            if pos < self.Long:
                while self.Hash[pos] is not None:
                    if cont < 4:
                        cont += 1
                        pos = self.CollisionHash(info.Carnet, pos)
                        cont1 += 1
                    elif (pos < (self.Long - 1)) and (cont >= 4):
                        pos += 1
                    elif pos == (self.Long - 1):
                        pos = 0
            else:
                pos = 0

            self.Hash[pos] = info
            self.add += 1
            self.Rehash()

    def Div(self, data):
        for a in range(0, len(self.primos)):
            if int(data) == int(self.primos[a]):
                return self.primos[a + 1]

    def Rehash(self):
        if self.add >= self.min:
            var = self.Hash
            tam = self.Long
            calculo = self.Div(self.Long)
            self.Long = calculo
            self.Start()
            for i in range(0, tam):
                if var[i] != -1:
                    self.addHash(var[i])

    def showHash(self):
        for hashing in range(0, len(self.Hash)):
            if self.Hash[hashing] is not None:
                print(str(hashing) + " -----> " + str(self.Hash[hashing].Carnet))
            else:
                print(str(hashing) + " -----> " + "Vacio")


if __name__ == "__main__":
    has = TableHash(7)
    has.addHash(nodeHash(201801627))
    has.addHash(nodeHash(201801603))
    has.addHash(nodeHash(201801628))
    has.addHash(nodeHash(201908402))
    has.insertData(201801627, "Apunte 1", "Hola que haces jeje")
    has.insertData(201801603, "Apunte 2", "Hola que haces jeje")
    has.insertData(201801628, "Apunte 3", "Hola que haces jeje")
    has.insertData(201908402, "Apunte 4", "Hola que haces jeje")
    has.showHash()

