from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import numpy as np

def open_image(name):
    return Image.open(name)

def rotate(image):
    return image.rotate(90, resample=Image.BICUBIC)

def flip_horizontal(image):
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

def flip_vertical(image):
    return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

#### colors functions
def contrast(image, factor):
    return ImageEnhance.Contrast(image).enhance(factor)

def color(image, factor):
    return ImageEnhance.Color(image).enhance(factor)

def brightness(image, factor):
    return ImageEnhance.Brightness(image).enhance(factor)

def sharpness(image, factor):
    return ImageEnhance.Sharpness(image).enhance(factor)

#### filtering functions
def boxblur(image, radius):
    return image.filter(ImageFilter.BoxBlur(radius=radius))

def emboss(image):
    return image.filter(ImageFilter.EMBOSS)

def pallete(image):
    return image.convert('P', palette=Image.Palette.ADAPTIVE, colors=16)