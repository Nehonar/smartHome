import tkinter as tk
from frontend.sidebar import Sidebar
from frontend.styles import setup_styles
from frontend.views.content_area_views.content_area import ContentArea
from frontend.views.content_area_views.home import HomeView

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        setup_styles()
        
        self.title("SmartHome")
        self.geometry("1200x900")
        
        
        self.content_area = ContentArea(self)
        self.content_area.pack(side="right", fill="both", expand=True)
        
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        self.content_area.show_view(HomeView)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()