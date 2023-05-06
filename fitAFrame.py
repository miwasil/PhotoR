from tkinter import  Scale, HORIZONTAL, RIGHT
from PIL import Image, ImageMath
from customtkinter import CTkLabel, CTkButton, CTkToplevel


class AdjustFrame(CTkToplevel):

    def __init__(self, master=None):
        CTkToplevel.__init__(self, master=master)

        self.brightness_value = 0
        self.previous_brightness_value = 0

        self.original_image = self.master.processed_image
        self.processing_image = self.master.processed_image

        self.brightness_label = CTkLabel(self, text="Brightness")
        self.brightness_scale = Scale(self, from_=0, to_=2, length=250, resolution=0.1,
                                      orient=HORIZONTAL)
        self.r_label = CTkLabel(self, text="R")
        self.r_scale = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL)
        self.g_label = CTkLabel(self, text="G")
        self.g_scale = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL)
        self.b_label = CTkLabel(self, text="B")
        self.b_scale = Scale(self, from_=-100, to_=100, length=250, resolution=1,
                             orient=HORIZONTAL)
        self.apply_button = CTkButton(self, text="Apply")
        self.preview_button = CTkButton(self, text="Preview")
        self.cancel_button = CTkButton(self, text="Cancel")

        self.brightness_scale.set(1)

        self.apply_button.bind("<ButtonRelease>", self.apply_button_released)
        self.preview_button.bind("<ButtonRelease>", self.show_button_release)
        self.cancel_button.bind("<ButtonRelease>", self.cancel_button_released)

        self.brightness_label.pack()
        self.brightness_scale.pack()
        self.r_label.pack()
        self.r_scale.pack()
        self.g_label.pack()
        self.g_scale.pack()
        self.b_label.pack()
        self.b_scale.pack()
        self.cancel_button.pack(side=RIGHT)
        self.preview_button.pack(side=RIGHT)
        self.apply_button.pack()

    def apply_button_released(self, event):
        self.master.processed_image = self.processing_image
        self.close()

    def show_button_release(self, event):
        self.processing_image = self.original_image.copy()
        brightness_scale_value = self.brightness_scale.get()
        self.processing_image = self.processing_image.point(lambda x: x * brightness_scale_value)
        b, g, r = self.processing_image.split()

        self.processing_image = Image.merge(
            "RGB",
            (
                ImageMath.eval("a + b", a=b, b=Image.new("L", b.size, self.b_scale.get())),
                ImageMath.eval("a + b", a=g, b=Image.new("L", g.size, self.g_scale.get())),
                ImageMath.eval("a + b", a=r, b=Image.new("L", r.size, self.r_scale.get())),
            ),
        )

        self.show_image(self.processing_image)

    def cancel_button_released(self, event):
        self.close()

    def show_image(self, img=None):
        self.master.image_viewer.show_image(img=img)

    def close(self):
        self.show_image()
        self.destroy()