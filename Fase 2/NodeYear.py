from LCD_Meses import ListCircularDoubleMeses
from LCD_Semestre import ListCircularDoubleSemester


class NodeYear:
    def __init__(self, year):
        self.Year = year
        self.sig = None
        self.ant = None
        self.mes = ListCircularDoubleMeses()
        self.semester = ListCircularDoubleSemester()
