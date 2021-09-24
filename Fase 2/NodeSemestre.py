from ArbolB.Tree_B import TreeB


class NodeSemester:
    def __init__(self, Semester):
        self.Semester = Semester
        self.ant = None
        self.sig = None
        self.curse = TreeB()
