import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk


def open_image(canvas, file_path):
    # global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.ANTIALIAS)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")


def draw(canvas, event, pen_size, pen_color):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')  # rysujemy wiele owali


def clear_drawing(canvas):
    canvas.delete('all')
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")


def clear_all(canvas):
    canvas.delete('all')
