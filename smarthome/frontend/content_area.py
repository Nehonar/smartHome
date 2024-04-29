import tkinter as tk
from frontend.views.content_area_views.home import HomeView

class ContentArea(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.current_view = HomeView(self)
        self.current_view.pack(fill="both", expand=True)

