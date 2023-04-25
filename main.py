import customtkinter
import tkinter
from customtkinter import filedialog
from basicFuncs import BasicFuncs

class Main(customtkinter.CTk):
    def __init__(self):

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

#   dark-blue ??

        root = customtkinter.CTk()
        root.geometry("1000x500")

        file_path = ""


      #  self.basics = BasicFuncs(master=root) # or self??


        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="test")
        label.pack(pady=12, padx=10)


