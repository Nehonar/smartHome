from tkinter import ttk
from frontend import color_palette as cp 

def setup_styles():
    style = ttk.Style()
    style.theme_use('clam')
    
    style.configure("TButton", 
                    font=("Consolas", 12), 
                    background=cp.BACKGROUND, 
                    foreground=cp.FOREGROUND)
    
    style.map("TButton", 
              background=[("active", cp.ACTIVE)],
              foreground=[("active", cp.DEACTIVATE)])
    
    style.configure("TLabel", 
                    font=("Consolas", 12), 
                    background=cp.BACKGROUND, 
                    foreground=cp.FOREGROUND)
    
    style.configure('Welcome.TLabel', font=("Consolas", 20))
    
    style.configure('Sidebar.TFrame', background=cp.BACKGROUND)
