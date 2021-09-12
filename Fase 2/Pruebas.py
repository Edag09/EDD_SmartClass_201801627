from LCD_Semestre import ListCircularDoubleSemester
from LCD_Year import ListCircularDobleYear
from LCD_Meses import ListCircularDoubleMeses
from LCD_Homeworks import ListCircularDoubleHomeworks

semester = ListCircularDoubleSemester()
year = ListCircularDobleYear()
mes = ListCircularDoubleMeses()
tar = ListCircularDoubleHomeworks()


def pri():
    year.AddListYear(2018)
    year.AddListYear(2019)
    year.AddListYear(2020)
    print('\n')
    mes.AddListMeses(1)
    mes.AddListMeses(5)
    mes.AddListMeses(6)
    mes.AddListMeses(11)
    print('\n')
    year.showListYear()
    print('\n')
    mes.showListMeses()


pri()
