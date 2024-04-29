import tkinter as tk
from frontend.sidebar import Sidebar
from frontend.content_area import ContentArea
from frontend.styles import setup_styles

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        setup_styles()
        
        self.title("SmartHome")
        self.geometry("1200x900")
        
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")
        
        self.content_area = ContentArea(self)
        self.content_area.pack(side="right", fill="both", expand=True)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
