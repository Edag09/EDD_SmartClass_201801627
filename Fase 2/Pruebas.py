from Analizadores import Analyzer
from LCD_Semestre import ListCircularDoubleSemester
from LCD_Year import ListCircularDobleYear
from LCD_Meses import ListCircularDoubleMeses
from LCD_Homeworks import ListCircularDoubleHomeworks
from Analizadores import Analyzer
from ThreeAVLStudent import ThreeAVL
import Analizadores
from SparseMatrix import HeadBoard
from SparseMatrix import Data
from SparseMatrix import NodeData

semester = ListCircularDoubleSemester()
year = ListCircularDobleYear()
mes = ListCircularDoubleMeses()
home = ListCircularDoubleHomeworks()
analisis = Analyzer()
cabecera = HeadBoard()
cabecera2 = HeadBoard()
data = Data()
node = NodeData(0, 1, 8)


def pri():
    """mes.AddListMeses(1)
    mes.AddListMeses(3)
    mes.showListMeses()"""

    # analisis.Files_Pens_Upload("CursosPensum.json")

    analisis.File_Entry()
    analisis.insert()
    analisis.insert_H()
    analisis.llenado()
    analisis.File_Student_Curse()
    Analizadores.homework.showList()
    Analizadores.homework.Delete_homework(2)
    Analizadores.homework.showList()
    """cabecera.Insert_Headboard(14)
    cabecera.Insert_Headboard(1)
    cabecera.Insert_Headboard(14)
    cabecera.show()
    print("\n")
    cabecera2.Insert_Headboard(8)
    cabecera2.Insert_Headboard(16)
    cabecera2.Insert_Headboard(10)
    cabecera2.show()"""
    # Analizadores.headDay.show()
    data.insert_nodeData(1, 8, Analizadores.headDay, Analizadores.headHora, node)
    data.show(Analizadores.headDay, Analizadores.headHora, 1, 8)


pri()
