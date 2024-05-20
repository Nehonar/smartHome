# ui_utils.py
from PIL import Image, ImageTk
from tkinter import ttk

def add_product(frame, key, image_path, info, product_info_labels):
    image = Image.open(image_path)
    
    resized_image = resize_image(image)
    
    photo = ImageTk.PhotoImage(resized_image)
    
    image_label = ttk.Label(frame, image=photo)
    image_label.image = photo
    image_label.pack(side="left")

    info_label = ttk.Label(frame, text=info)
    info_label.pack(side="left", padx=10)
    
    product_info_labels[key] = info_label
    
    return product_info_labels

def resize_image(image):
    new_size = (image.width * 2, image.height * 2)
    resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    return resized_image
