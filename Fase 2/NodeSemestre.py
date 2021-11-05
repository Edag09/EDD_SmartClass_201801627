from ArbolB.Tree_B import TreeB
from ArbolB.ListCurseDouble import ListCurse


class NodeSemester:
    def __init__(self, Semester):
        self.Semester = Semester
        self.ant = None
        self.sig = None
        self.curse = TreeB()
        self.cur = ListCurse()

