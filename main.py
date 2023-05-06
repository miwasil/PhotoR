from tkinter import X, BOTH, HORIZONTAL, ttk
import customtkinter
from customtkinter import filedialog
from basicFuncs import BasicFuncs

class Main(customtkinter.CTk):
    def __init__(self):
        customtkinter.CTk.__init__(self)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.title("Photo Editor")

#   dark-blue ??
        self.filename = ""
        self.original_image = None
        self.processed_image = None
        self.is_image_selected = False
        self.is_draw_state = False
        self.is_crop_state = False

        self.filter_frame = None
        self.adjust_frame = None
        #self.editbar = EditBar(master=self)
        separator1 = ttk.Separator(master=self, orient=HORIZONTAL)
        self.image_viewer = BasicFuncs(master=self)

        self.editbar.pack(pady=10)
        separator1.pack(fill=X, padx=20, pady=5)
        self.image_viewer.pack(fill=BOTH, padx=20, pady=10, expand=1)


        #file_path = ""


      #  self.basics = BasicFuncs(master=root) # or self??


        # frame = customtkinter.CTkFrame(master=root)
        # frame.pack(pady=20, padx=60, fill=" both", expand=True)
        #
        # label = customtkinter.CTkLabel(master=frame, text="test")
        # label.pack(pady=12, padx=10)


