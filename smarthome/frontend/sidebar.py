import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from frontend.views.sidebar_views.home_areas_view import HomeAreasView
from utils import logger_color as log

class Sidebar(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs, style="Sidebar.TFrame")
        self.content_area = parent.content_area
        
        image_path = './smarthome/frontend/assets/images/smarthome_logo.jpeg'
        logo_image = Image.open(image_path)
        logo_photo = ImageTk.PhotoImage(logo_image)
        
        logo_label = ttk.Label(self, image=logo_photo)
        logo_label.image = logo_photo
        logo_label.pack(pady=10, fill='x')
        
        self.home_areas_view = HomeAreasView(self)
        self.home_areas_button = ttk.Button(self, text='Zonas de casa', style='TButton', command=self.home_areas_view_sidebar)
        self.home_areas_button.pack(pady=10, fill='x')
        
        # Menu expand
        self.home_areas_expanded = False
        
    def home_areas_view_sidebar(self):
        if self.home_areas_expanded:
            self.home_areas_view.pack_forget()
        else:
            self.home_areas_view.pack(pady=10, fill='x')
        self.home_areas_expanded = not self.home_areas_expanded
