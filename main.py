import tkinter as tk
from tkinter import colorchooser, Scale, HORIZONTAL, ttk, filedialog, Label, Entry
from basicFuncs import draw, clear_drawing, clear_all, open_image
from PIL import Image, ImageTk, ImageEnhance, ImageFilter

app = tk.Tk()
app.geometry('1000x600')
app.minsize(1000, 800)
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


def displayimage(image):
    dispimage = ImageTk.PhotoImage(image)
    Label(photoside, image=dispimage).grid(row=0, column=0, padx=5, pady=5)
    photoside.image = dispimage

def rotate():
    global image
    image = image.rotate(90)
    displayimage(image)

def flip_horizontal():
    global image
    image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    displayimage(image)

def blurr():
    global image
    image = image.filter(ImageFilter.BLUR)
    displayimage(image)


def changeImg():
    global image, initial_photo, original_image

    imgname = filedialog.askopenfilename()
    if imgname:
        image = Image.open(imgname)
        image = image.resize((700, 600))
        original_image = image
        displayimage(image)
        initial_photo = image
        initial_photo = image.resize((200, 100))
        initial_photo_TK = ImageTk.PhotoImage(initial_photo)
        Label(edit_photo_frame, image=initial_photo_TK).grid(row=0, column=0)
        edit_photo_frame.image = initial_photo_TK

def save():
    global image
    savefile = filedialog.asksaveasfile(defaultextension=".jpg")
    outputImage.save(savefile)


def brightness(factor):
    factor = float(factor)
    global outputImage
    enhancer = ImageEnhance.Brightness(image)
    outputImage = enhancer.enhance(factor)
    displayimage(outputImage)



def contrast(factor):
    factor = float(factor)
    global outputImage
    enhancer = ImageEnhance.Contrast(image)
    outputImage = enhancer.enhance(factor)
    displayimage(image)
    displayimage(outputImage)


def sharpen(factor):
    factor = float(factor)
    global outputImage
    enhancer = ImageEnhance.Sharpness(image)
    outputImage = enhancer.enhance(factor)
    displayimage(outputImage)


def color(factor):
    factor = float(factor)
    global outputImage
    enhancer = ImageEnhance.Color(image)
    outputImage = enhancer.enhance(factor)
    displayimage(outputImage)


def create_canvas():
    global canvas
    canvas = tk.Canvas(photoside, bg='white')
    canvas.grid(row=0, column=0)
    canvas.bind("<B1-Motion>", lambda event: draw(canvas, event, pen_size, pen_color))
    pensizeSlider.config(state='normal')
    color_button.config(state='normal')
    open_image(canvas, image)

def temp_text(e):
    resize_entry.delete(0, "end")

def resize(entry):
    global image
    size = entry.get()
    if 'x' in size:
        width, height = map(int, size.split('x'))
        image = image.resize((width, height))
        displayimage(image)
    else:
        pass
    displayimage(image)

def go_back():
    global image, original_image
    image = original_image
    displayimage(image)




menu = tk.Frame(app, bg='#856ff8')  # zawsze stworzyc i potem
menu.place(x=0, y=0, relwidth=0.3, relheight=1)  # pack, place lub grid zeby to gdzies wlozyc

photoside = tk.Frame(app, bg='yellow')
photoside.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

edit_photo_frame = tk.Frame(menu)
edit_photo_frame.pack(side=tk.BOTTOM)

menubar = tk.Menu(menu)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=changeImg)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Draw", command=create_canvas)
menubar.add_cascade(label="File", menu=filemenu)

#open_button = tk.Button(menu, text='Open to draw', command=create_canvas)
#open_button2 = tk.Button(menu, text='Open2', command=changeImg)
resize_entry = Entry(menu, width=30)
resize_entry.insert(0, "Provide with format 0000x0000")
resize_button = tk.Button(menu, text='Resize', command=lambda: resize(resize_entry))
blurr_button = tk.Button(menu, text='Blurr', command=blurr)
color_button = tk.Button(menu, text='Change color of draw', command=change_color)
rotate_button = tk.Button(menu, text='Rotate', command=rotate)
flip_horizontal_button = tk.Button(menu, text='Flip Horizontal', command=flip_horizontal)
apply1_button = tk.Button(menu, text='Apply')
apply2_button = tk.Button(menu, text='Apply')
apply3_button = tk.Button(menu, text='Apply')
apply4_button = tk.Button(menu, text='Apply')

pensizeSlider = Scale(menu, label="Change size of pen", from_=1, to=10, orient=HORIZONTAL,
                      command=lambda val: change_size(pensizeSlider.get()))
brightnessSlider = Scale(menu, label="Brightness", from_=0, to=2, resolution=0.1, orient=HORIZONTAL, command=brightness)
contrastSlider = Scale(menu, label="Contrast", from_=0, to=2, resolution=0.1, orient=HORIZONTAL, command=contrast)
sharpnessSlider = Scale(menu, label="Sharpness", from_=0, to=2, resolution=0.1, orient=HORIZONTAL, command=sharpen)
colorSlider = Scale(menu, label="Color", from_=0, to=2, resolution=0.1, orient=HORIZONTAL, command=color)

clear_dr_button = tk.Button(menu, text='Clear drawing', bg='pink', command=lambda: clear_drawing(canvas))
clear_all_button = tk.Button(menu, text='Go back to original', bg='pink', command=go_back, width=20)
#save_button = tk.Button(menu, text='Save', command=save)



filter_label = tk.Label(menu, text="Select filter")
filter_combobox = ttk.Combobox(menu, values=["Emboss", "Blur"])


pensizeSlider.set(5)
brightnessSlider.set(1)
contrastSlider.set(1)
sharpnessSlider.set(1)
colorSlider.set(1)




#open_button.pack(pady=5)
#open_button2.pack(pady=5)
resize_entry.pack(pady=5)
resize_button.pack(pady=5)
blurr_button.pack(pady=5)
color_button.pack(pady=5)
rotate_button.pack(pady=5)
flip_horizontal_button.pack(pady=5)
pensizeSlider.pack(pady=5)
filter_label.pack()
filter_combobox.pack()
brightnessSlider.pack(pady=2)
contrastSlider.pack(pady=2)
sharpnessSlider.pack(pady=2)
apply3_button.pack()
colorSlider.pack(pady=2)
apply4_button.pack()
clear_dr_button.pack(pady=5)
clear_all_button.pack(pady=5)
#save_button.pack(pady=5)



image = Image.open("dc.png")
image = image.resize((700, 600))
imageTK = ImageTk.PhotoImage(image)
initial_photo = image.resize((200,100))
initial_photo_TK = ImageTk.PhotoImage(initial_photo)
Label(photoside, image=imageTK).grid(row=0, column=0)
Label(edit_photo_frame, image=initial_photo_TK).grid(row=0, column=0)
original_image = image

filter_combobox.bind("<<ComboboxSelected>>")

resize_entry.bind("<FocusIn>", temp_text)

app.config(menu=menubar)
app.mainloop()
