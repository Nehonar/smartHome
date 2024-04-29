import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class HomeView(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        image_path = './smarthome/frontend/assets/images/welcome_image.jpeg'
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        
        self.welcome_image_label = ttk.Label(self)
        self.welcome_image_label.image = photo
        self.welcome_image_label['image'] = photo
        self.welcome_image_label.pack(expand=True)
        
        ttk.Label(self, text="Bienvenido a\n  SmartHome", style="Welcome.TLabel").pack(expand=True)
        
        
