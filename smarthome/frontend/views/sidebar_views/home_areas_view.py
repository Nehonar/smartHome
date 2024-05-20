import tkinter as tk
from tkinter import ttk
from frontend import color_palette as cp 
from frontend.views.content_area_views.kitchen import KitchenView

class HomeAreasView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, bg=cp.BACKGROUND, *args, **kwargs)
        self.content_area = parent.content_area
        
        ttk.Button(self, text="Cocina", style='TButton', command=self.show_kitechen).pack(pady=2, fill='x')
        ttk.Button(self, text="Lavadero", style='TButton').pack(pady=2, fill='x')
        ttk.Button(self, text="Sala", style='TButton').pack(pady=2, fill='x')
        ttk.Button(self, text="Dormitorio", style='TButton').pack(pady=2, fill='x')
        ttk.Button(self, text="Lavabo", style='TButton').pack(pady=2, fill='x')

    def show_kitechen(self):
        self.content_area.show_view(KitchenView)