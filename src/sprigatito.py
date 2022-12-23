class Sprigatito:
    def __init__(self):
        self.modelname = "Sprigatito"
        self.modelposx = 0
        self.modelposy = 0
        self.sendmes = ""

    def send(self,text):
        positive_word = ["好き","スキ","好きだよ"]
        negative_word = ["嫌い","キライ","嫌い"]
        hyper_negative_word = ["大嫌い"]

        if text in positive_word:
            self.sendmes = "はにゃ！"
        elif text in negative_word:
            self.sendmes = "はんにゃ……"
        elif text in hyper_negative_word: 
            self.sendmes = "は……"
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