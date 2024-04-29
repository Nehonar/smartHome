import tkinter as tk
from tkinter import ttk
from frontend import color_palette as cp 

class HomeAreasView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, bg=cp.BACKGROUND, *args, **kwargs)
        
        ttk.Button(self, text="Cocina", style='TButton').pack(pady=2, fill='x')
        ttk.Button(self, text="Sala", style='TButton').pack(pady=2, fill='x')
        ttk.Button(self, text="Dormitorio", style='TButton').pack(pady=2, fill='x')
