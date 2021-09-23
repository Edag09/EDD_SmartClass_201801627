from SparseMatrix import *
from LCD_Homeworks import ListCircularDoubleHomeworks


class NodeMatrix:
    def __init__(self):
        self.rowM = HeadBoard()
        self.columnM = HeadBoard()
        self.data = Data()


class NodeHeadboard:
    def __init__(self, num):
        self.number = num
        self.sig = None
        self.ant = None
        self.up = None
        self.down = None


class NodeData:
    def __init__(self, data, row, column):
        self.data = data
        self.rowData = row
        self.columnData = column
        self.ListHomework = ListCircularDoubleHomeworks()
        self.sigData = None
        self.antData = None
        self.upData = None
        self.downData = None
