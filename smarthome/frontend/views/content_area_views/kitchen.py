from tkinter import ttk
from utils.ui_utils import add_product

class KitchenView(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.product_info_labels = {}
        self.create_widgets()

    def create_widgets(self):
        products = [
            ("lavadora", "./smarthome/frontend/assets/images/washmachine_off.png", "Lavadora 100 kw/h"),
            ("nevera", "./smarthome/frontend/assets/images/fridge_off.png", "Nevera 150 kw/h")
        ]
        
        for key, image_path, initial_info in products:
            product_frame = ttk.Frame(self, padding=10)
            product_frame.pack(pady=10, fill='x', expand=True)
            self.product_info_labels = add_product(product_frame, key, image_path, initial_info, self.product_info_labels)

    def update_product_info(self, key, new_info):
        # Method to update the product information
        if key in self.product_info_labels:
            self.product_info_labels[key].configure(text=new_info)
