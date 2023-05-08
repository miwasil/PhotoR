import tkinter as tk
from tkinter import colorchooser, Scale, HORIZONTAL, ttk
from basicFuncs import open_image, draw, clear_drawing, clear_all

app = tk.Tk()
app.geometry('1000x600')
app.minsize(1000, 600)
app.title('Photo Editor v1.0')
app.config(bg='white')

file_path = ""
pen_color = "black"
pen_size = 5


def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title='Select color')[1]


def change_size(size):
    global pen_size
    pen_size = size


menu = tk.Frame(app, bg='#856ff8')  # zawsze stworzyc i potem
menu.place(x=0, y=0, relwidth=0.3, relheight=1)  # pack, place lub grid zeby to gdzies wlozyc

open_button = tk.Button(menu, text='Open', command=lambda: open_image(canvas, file_path))
save_button = tk.Button(menu, text='Save')
color_button = tk.Button(menu, text='Change color of draw', command=change_color)
pensizeSlider = Scale(menu, from_=1, to=10, orient=HORIZONTAL, command=lambda val: change_size(pensizeSlider.get()))

clear_dr_button = tk.Button(menu, text='Clear drawing', bg='pink', command=lambda: clear_drawing(canvas))
clear_all_button = tk.Button(menu, text='Destroy image', bg='pink', command=lambda: clear_all(canvas))

filter_label = tk.Label(menu, text="Select filter")

pensizeSlider.set(5)

open_button.pack(pady=5)
save_button.pack(pady=5)
color_button.pack(pady=5)
pensizeSlider.pack(pady=5)
filter_label.pack(pady=5)
clear_dr_button.pack(pady=5)
clear_all_button.pack(pady=5)

canvas = tk.Canvas(app)
canvas.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

canvas.bind("<B1-Motion>",
            lambda event: draw(canvas, event, pen_size, pen_color))  # when u click and drag call draw function

app.mainloop()  # zazwyczaj sie uzywa root albo master
