import tkinter as tk
import customtkinter as ctk

class Subconsole:

    def __init__(self):
        self.subconsole_trigger = False

    def init(self):
        self.size = "600x500"
        self.base = ctk.CTkToplevel()
        self.base.geometry(self.size)
        self.base.title("ProjectSprigatito - v0.1 Sub-Console")
        self.base.protocol("WM_DELETE_WINDOW",self.destroy_window)
        self.canvas = ctk.CTkCanvas()


    def destroy_window(self):
        self.subconsole_trigger = False
        print("subconsole closed")
        self.base.destroy()