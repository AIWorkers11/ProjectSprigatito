import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk

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
        self.canvas.create_image(
            425,
            250,
            image=self.Sprigatitoimage
        )        
        self.inputbox = tk.Text(self.frame2,width=10,height=5)
        self.outputbox = tk.Text(self.frame2,width=10,height=5)

        self.canvas.pack()
        self.inputbox.pack(fill=tk.BOTH)
        self.outputbox.pack(fill=tk.BOTH)
        self.frame2.pack(side=tk.BOTTOM,fill=tk.BOTH)






