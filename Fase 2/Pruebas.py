from Analizadores import Analyzer
from LCD_Semestre import ListCircularDoubleSemester
from LCD_Year import ListCircularDobleYear
from LCD_Meses import ListCircularDoubleMeses
from LCD_Homeworks import ListCircularDoubleHomeworks
from Analizadores import Analyzer
from ThreeAVLStudent import ThreeAVL

semester = ListCircularDoubleSemester()
year = ListCircularDobleYear()
mes = ListCircularDoubleMeses()
tar = ListCircularDoubleHomeworks()
analisis = Analyzer()


def pri():
    analisis.File_Entry()
    #analisis.insert()


pri()
