import tkinter as tk
from frontend.views.content_area_views.home import HomeView

class ContentArea(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.current_view = None
        self.show_view(HomeView)
        
    def show_view(self, view_class):
        if self.current_view is not None:
            self.current_view.destroy()
        
        self.current_view = view_class(self)
        self.current_view.pack(fill='both', expand=True)
