import tkinter as tk
import customtkinter as ctk

class Subconsole:
    def __init__(self):
        self.size = "600x500"
        self.base = ctk.CTk()
        self.base.geometry(self.size)
        self.base.title("ProjectSprigatito - v0.1 Sub-Console")

        self.canvas = ctk.CTkCanvas()

    def func(self):
        pass