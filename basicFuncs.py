from PIL import Image
from customtkinter import filedialog

class BasicFuncs():
    def add_image():
        global file_path
        file_path = filedialog.askdirectory()
        image = Image.open(file_path)
