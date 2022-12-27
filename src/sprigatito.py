class Sprigatito:
    def __init__(self):
        self.modelname = "Sprigatito"
        self.modelposx = 0
        self.modelposy = 0
        self.sendmes = ""

    def send(self,text):

        word = {
            "好き"      : 5,
            "すき"      : 5,
            "大好き"    : 10,
            "嫌い"      : 1,
            "きらい"    : 1,
            "大嫌い"    : 0,
            "大キライ"  : 0
        }

        if word.get(text) == 5:
            self.sendmes = "はにゃ！"
        elif word.get(text) == 10:
            self.sendmes = "はにゃ～♡"
        elif word.get(text) == 1: 
            self.sendmes = "はんにゃ……"
        elif word.get(text) == 0:
            self.sendmes = "……"
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