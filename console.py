import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk
from sprigatito import Sprigatito

class console:
    def __init__(self):
        self.size = "1000x700"
        self.base = tk.Tk()
        self.base.geometry(self.size)
        self.base.title("ProjectSprigatito - v0.1 Console")
        
        self.frame1 = tk.Frame(self.base,relief=tk.RAISED,bd=1,padx=10,pady=10)
        self.exitbutton = tk.Button(self.frame1,width=10,height=5,text="終了",command=lambda:self.base.destroy())
        self.exitbutton.pack()
        self.frame1.pack(side=tk.LEFT,fill=tk.BOTH)

        self.frame2 = tk.Frame(self.base,relief=tk.RAISED,bd=1,padx=10,pady=10)
        self.canvas = tk.Canvas(self.frame2,bg="#000",width=850,height=500)
        
        self.Sprigatitoimage = ImageTk.PhotoImage(file="Sprigatito.png")
        self.Sprigatito = Sprigatito()
        
        self.Sprigatito.setModelPosX(425) #初期値：425（中央）
        self.Sprigatito.setModelPosY(250) #初期値：250（中央）

        self.canvas.create_image(
            self.Sprigatito.getModelPosX(),
            self.Sprigatito.getModelPosY(),
            image=self.Sprigatitoimage
        )        
        self.outputbox = tk.Text(self.frame2,width=10,height=7)
        self.outputbox.configure(state="disabled")
        self.inputbox = tk.Text(self.frame2,width=10,height=3)

        self.canvas.pack()
        self.outputbox.pack(fill=tk.BOTH)
        self.inputbox.pack(fill=tk.BOTH)
        self.frame2.pack(side=tk.BOTTOM,fill=tk.BOTH)