import tkinter as tk
from PIL import ImageTk,Image,ImageOps
import time
import customtkinter as ctk

import sprigatito
import user

class console:
    def __init__(self):
        self.size = "850x900"
        self.base = ctk.CTk()
        self.base.geometry(self.size)
        self.base.title("ProjectSprigatito - v0.1 Console")
        self.base.resizable(width=False,height=False)
        ctk.set_default_color_theme("green")
        
        self.frame1 = ctk.CTkFrame(
            master=self.base,
        )
        self.exitbutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="終了",command=lambda:self.base.destroy(),fg_color="red",hover_color="maroon")
        self.exitbutton.pack(padx=10,pady=20)
        self.movebutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="上に移動\n（デモ）",command=lambda:self.moveup())
        self.movebutton.pack(padx=10,pady=20)
        self.movedbutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="下に移動\n（デモ）",command=lambda:self.movedown())
        self.movedbutton.pack(padx=10,pady=20)
        self.reversebutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="反転\n（デモ）",command=lambda:self.reverse())
        self.reversebutton.pack(padx=10,pady=20)
        self.pushbutton = ctk.CTkButton(master=self.frame1,width=120,height=40,text="送信",command=lambda:self.push())
        self.pushbutton.pack(padx=10,pady=20,side=tk.BOTTOM)
        
        self.frame1.pack(side=tk.LEFT,padx=10,pady=10,fill=tk.Y)

        self.frame2 = ctk.CTkFrame(
            master=self.base,
        )
        self.frame2.pack(side=tk.RIGHT,padx=10,pady=10,fill=tk.BOTH)
        
        self.canvas = ctk.CTkCanvas(self.frame2,bg="#000",width=750,height=500)
        
        self.Sprigatitoimage = Image.open("./img/Sprigatito.png")
        self.Sprigatitoimg = ImageTk.PhotoImage(self.Sprigatitoimage)
        self.Sprigatito = sprigatito.Sprigatito()
        
        self.Sprigatito.setModelPosX(425) #初期値：425（中央）
        self.Sprigatito.setModelPosY(250) #初期値：250（中央）
        self.User = user.user()
        self.imgid = self.canvas.create_image(
            self.Sprigatito.getModelPosX(),
            self.Sprigatito.getModelPosY(),
            image=self.Sprigatitoimg
        )
        self.outlabel = ctk.CTkLabel(self.frame2,text="出力")
        self.outputbox = ctk.CTkTextbox(self.frame2,width=600,height=200)
        self.outputbox.configure(state="disabled")
        self.inlabel = ctk.CTkLabel(self.frame2,text="入力")
        self.inputbox = ctk.CTkTextbox(self.frame2,width=600,height=50)

        self.canvas.pack(padx=10,pady=10)
        self.outlabel.pack(padx=5,pady=3)
        self.outputbox.pack(padx=5,pady=3)
        self.inlabel.pack(padx=5,pady=3)
        self.inputbox.pack(padx=5,pady=3)

    def moveup(self):
        for i in range(10):
            self.canvas.move(self.imgid,0,-5)
            self.canvas.update()
            time.sleep(0.03)
        self.Sprigatito.setModelPosY(self.Sprigatito.getModelPosY()-50)
    
    def movedown(self):
        for i in range(10):
            self.canvas.move(self.imgid,0,5)
            self.canvas.update()
            time.sleep(0.03)
        self.Sprigatito.setModelPosY(self.Sprigatito.getModelPosY()+50)

    def reverse(self):
            self.canvas.delete(self.imgid)
            self.Sprigatitoimage = ImageOps.mirror(self.Sprigatitoimage)
            self.Sprigatitoimg = ImageTk.PhotoImage(self.Sprigatitoimage)
            self.imgid = self.canvas.create_image(
                self.Sprigatito.getModelPosX(),
                self.Sprigatito.getModelPosY(),
                image=self.Sprigatitoimg
            )    

    def push(self):
        text = self.inputbox.get("1.0","end")
        if not text.isspace():
            text = text.replace("\n","")
            self.inputbox.delete("1.0","end")
            self.insertoutput(self.User.getUserName()+":"+text)
            self.Sprigatito.send(text)
            self.insertoutput(self.Sprigatito.getModelName()+":"+self.Sprigatito.getSendMessage())

    def insertoutput(self,text):
            self.outputbox.configure(state="normal")
            self.outputbox.insert("end",text+"\n")
            self.outputbox.configure(state="disabled")