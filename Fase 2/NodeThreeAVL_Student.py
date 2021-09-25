from LCD_Year import *


class NSThreeAVL:
    def __init__(self, Carnet, DPI, Name, Carrera, Correo, Password, Credits, Age):
        self.Carnet = Carnet
        self.DPI = DPI
        self.Name = Name
        self.Carrera = Carrera
        self.Correo = Correo
        self.Password = Password
        self.Creditos = Credits
        self.Edad = Age
        self.anios = ListCircularDobleYear()
        self.father = None
        self.der = None
        self.izq = None
        self.alt = 0
