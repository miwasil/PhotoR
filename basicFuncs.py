from tkinter import CENTER, ROUND, ttk #zamienic na CTKinter??

from PIL import Image, ImageDraw, ImageTk
from customtkinter import filedialog, CTkFrame, CTkCanvas
import tkinter

class BasicFuncs(ttk.Button):
    def __init__(self):
        super().__init__(master, text='Open')
    def open_file(self):
        filepath=""
