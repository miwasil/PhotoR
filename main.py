from tkinter import X, BOTH, HORIZONTAL, ttk
import customtkinter
from customtkinter import filedialog
from basicFuncs import BasicFuncs
import tkinter as tk
from tkinter import ttk
from basicFuncs import BasicFuncs


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
        self.open_button = ttk.Button(self, text='Open')
        #self.open_button = BasicFuncs(self)
        self.save_button = ttk.Button(self, text='Save')


    def create_layout(self):
        #creating
        self.columnconfigure((0,1,2), weight =1, uniform='a')
        self.rowconfigure((0, 1, 2,3,4,5,6), weight=1, uniform='a')

        #label = ttk.Label(self, background='#856ff8').pack(expand=True, fill='both')
        #placing elements
        self.open_button.grid(row = 0, column= 0, sticky='nswe')
        self.save_button.grid(row =0, column =1, sticky='nswe')


# class PhotoSide(ttk.Frame):
#     def __init__(self, master):
#         super().__init__(master)
#
#         self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
#
#         frame = ttk.Frame(self)
#         label = ttk.Label(frame, background='#856ff8')
#         label.pack(expand=True, fill='both')
#         frame.pack(side='left', expand=True, fill='both', padx=20, pady=20)

class PhotoSide(tk.Canvas):
    def __init__(self, master):
        super().__init__(master)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        canvas = tk.Canvas(self)
        label = ttk.Label(canvas, background='#856ff8')
        label.pack(expand=True, fill='both')
        canvas.pack(side='left', expand=True, fill='both', padx=20, pady=20)




