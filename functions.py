from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np

class Functions:

    filtered_image = None
    original_image = None
    def __init__(self, name):
        self.original_image = Image.open(name)
        self.filtered_image = None

    def rotate(self):
        self.filtered_image = self.original_image.rotate(90, resample=Image.BICUBIC)


    #def crop(self):
    def flip_horizontal(self):
        self.filtered_image = self.original_image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    def flip_vertical(self):
        self.filtered_image = self.original_image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

#### colors functions
    def contrast(self, factor):
        self.filtered_image = ImageEnhance.Contrast(self.original_image).enhance(factor)

    def color(self,factor):
        self.filtered_image = ImageEnhance.Color(self.original_image).enhance(factor)

    def brightness(self,factor):
        self.filtered_image = ImageEnhance.Brightness(self.original_image).enhance(factor)

    def sharpness(self,factor):
        self.filtered_image = ImageEnhance.Sharpness(self.original_image).enhance(factor)

#### filtering functions

    def boxblur(self, radius):
        self.filtered_image = self.original_image.filter(ImageFilter.BoxBlur(radius = radius))

    def emboss(self):
        self.filtered_image = self.original_image.filter(ImageFilter.EMBOSS)


    def pallete(self):
        self.filtered_image = self.original_image.convert('P', palette= Image.Palette.ADAPTIVE, colors = 16)

##       self.filtered_image.show()

