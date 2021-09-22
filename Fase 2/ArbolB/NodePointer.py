class NodePointer:
    def __init__(self, pointer):
        self.Pointer = pointer
        self.SigP = None
    
    def getPointer(self):
        return self.Pointer

    def setPointer(self, Pointer):
        self.Pointer = Pointer

    def getSigP(self):
        return self.SigP
    
    def setSigP(self, SigP):
        self.SigP = SigP

    def getAntP(self):
        return self.AntP
    
    def setAntP(self, AntP):
        self.AntP = AntP
