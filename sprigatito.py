class Sprigatito:
    def __init__(self):
        self.modelname = "Sprigatito"
        self.modelposx = 0
        self.modelposy = 0
    
    def getModelName(self):
        return self.modelname
    
    def getModelPosX(self):
        return self.modelposx

    def getModelPosY(self):
        return self.modelposy
    
    def setModelPosX(self,x):
        self.modelposx = x

    def setModelPosY(self,y):
        self.modelposy = y