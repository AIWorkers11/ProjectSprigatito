class Sprigatito:
    def __init__(self):
        self.modelname = "Sprigatito"
        self.modelposx = 0
        self.modelposy = 0
        self.sendmes = ""

    def send(self,text):
        if text == "すき":
            self.sendmes = "はにゃ！"
        elif text == "きらい":
            self.sendmes = "はんにゃ……"
        else:
            self.sendmes = "はにゃ？"

    def getModelName(self):
        return self.modelname
    
    def getModelPosX(self):
        return self.modelposx

    def getModelPosY(self):
        return self.modelposy
    
    def getSendMessage(self):
        return self.sendmes

    def setModelPosX(self,x):
        self.modelposx = x

    def setModelPosY(self,y):
        self.modelposy = y