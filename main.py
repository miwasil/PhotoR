from tkinter import X, BOTH, HORIZONTAL, ttk
import customtkinter
from customtkinter import filedialog
from basicFuncs import BasicFuncs
import tkinter as tk
from tkinter import ttk
from basicFuncs import BasicFuncs
from PIL import Image, ImageTk

class Main(tk.Tk):
    def __init__(self):
        # setup
        super().__init__()
        self.title("Photo Editor v1.0")
        self.geometry('1000x600')
        self.minsize(1000, 600)

        # widgets
        self.menu = Menu(self)
        self.photoside = PhotoSide(self)


class Menu(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.save_button = None
        self.open_button = None

        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.create_buttons()
        self.create_layout()

    def create_buttons(self):
        #creating elements
        self.open_button = ttk.Button(self, text='Open', command=add_image)
        self.save_button = ttk.Button(self, text='Save', command=save_image)

    def create_layout(self):
        #creating
        self.columnconfigure((0,1,2), weight =1, uniform='a')
        self.rowconfigure((0, 1, 2,3,4,5,6), weight=1, uniform='a')

        #label = ttk.Label(self, background='#856ff8').pack(expand=True, fill='both')
        #placing elements
        self.open_button.grid(row = 0, column= 0, sticky='nswe')
        self.save_button.grid(row =0, column =1, sticky='nswe')

class PhotoSide(tk.Canvas):
    def __init__(self, master):
        super().__init__(master)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side='left', expand=True, fill='both', padx=20, pady=20)


def add_image():
    global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.ANTIALIAS)
    root.photoside.canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    root.photoside.canvas.image = image
    root.photoside.canvas.create_image(0, 0, image=image, anchor='nw')

def save_image():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    if not file_path:
        return
    image = Image.open(file_path)
    root.photoside.canvas.postscript(file=file_path + '.eps')
    image.save(file_path)

root = Main()
root.mainloop()