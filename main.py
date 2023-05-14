import tkinter as tk
from tkinter import colorchooser, Scale, HORIZONTAL, ttk, filedialog, Label, Entry
from basicFuncs import draw, clear_drawing, clear_all, open_image
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
import io


app = tk.Tk()
app.geometry('1400x700')
#app.minsize(1000, 800)
app.title('Photo Editor v1.0')

app.tk.call("source", "azure.tcl")
app.tk.call("set_theme", "dark")



app.update()
app.minsize(app.winfo_width(), app.winfo_height())
x_cordinate = int((app.winfo_screenwidth() / 2) - (app.winfo_width() / 2))
y_cordinate = int((app.winfo_screenheight() / 2) - (app.winfo_height() / 2))
app.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

file_path = ""
pen_color = "black"
pen_size = 5

default_enhancements = {
    "Brightness": 1.0,
    "Contrast": 1.0,
    "Sharpness": 1.0,
    "Color": 1.0
}

def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title='Select color')[1]


def change_size(size):
    global pen_size
    pen_size = size

def scale(image, frame_width, frame_height):
    #global image
    frame_width = frame_width*0.8
    frame_height = frame_height*0.8
    image_width, image_height = image.size
    scaled_image = image

    if (image_width > frame_width) or (image_height > frame_height):
        factor = 1/max(image_height/frame_height, image_width/frame_width)
        new_image_size = (int(image.size[0]*factor), int(image.size[1]*factor))
        scaled_image = image.resize(new_image_size)
    return scaled_image
def displayimage(image):
    frame_width = photoside.winfo_width()
    frame_height = photoside.winfo_height()
    center_x = frame_width // 2
    center_y = frame_height // 2
    image = scale(image, frame_width, frame_height)
    dispimage = ImageTk.PhotoImage(image)
    Label(photoside, image=dispimage).place(x=center_x, y=center_y, anchor='center')
    photoside.image = dispimage


def rotate():
    global image

    image = image.rotate(90, resample=Image.BICUBIC, expand=True)
    #new_image = Image.new("RGBA", image.size,'yellow')

    displayimage(image)

def flip_horizontal():
    global image
    image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    displayimage(image)

def flip_vertical():
    global image
    image = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    displayimage(image)



def changeImg():
    global image, initial_photo, original_image
    imgname = filedialog.askopenfilename()
    if imgname:
        image = Image.open(imgname)
        #scale()
        original_image = image
        displayimage(image)
        initial_photo = image
        frame_width = edit_photo_frame.winfo_width()
        frame_height = edit_photo_frame.winfo_height()
        center_x = frame_width // 2
        center_y = frame_height // 2
        initial_photo = scale(image, frame_width, frame_height)
        initial_photo_TK = ImageTk.PhotoImage(initial_photo)
        Label(edit_photo_frame, image=initial_photo_TK).place(x=center_x, y=center_y, anchor='center')
        edit_photo_frame.image = initial_photo_TK

def save():
    global image
    savefile = filedialog.asksaveasfile(defaultextension=".jpg")
    image.save(savefile)


def choose_filter(filter):
    global outputImage, image
    match filter:
        case 'Emboss':
            outputImage = image.filter(ImageFilter.EMBOSS)
        case 'Blur':
            outputImage = image.filter(ImageFilter.BLUR)
        case 'Contour':
            outputImage = image.filter(ImageFilter.CONTOUR)
        case 'Smooth':
            outputImage = image.filter(ImageFilter.SMOOTH_MORE)
        case 'Detail':
            outputImage = image.filter(ImageFilter.DETAIL)
        case 'Edge enhance':
            outputImage = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        case 'No filter':
            outputImage = image

    displayimage(outputImage)

def set_filter(filter):
    global image
    match filter:
        case 'Emboss':
            image = image.filter(ImageFilter.EMBOSS)
        case 'Blur':
            image = image.filter(ImageFilter.BLUR)
        case 'Contour':
            image = image.filter(ImageFilter.CONTOUR)
        case 'Smooth':
            image = image.filter(ImageFilter.SMOOTH_MORE)
        case 'Detail':
            image = image.filter(ImageFilter.DETAIL)
        case 'Edge enhance':
            image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        case 'No filter':
            pass

    displayimage(image)


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

def open_image(canvas, photo):
    global image
    photo = ImageTk.PhotoImage(photo)
    canvas.image = photo
    canvas.create_image((0,0), image=photo, anchor='nw')
    #ps_data = canvas.postscript(colormode='color')
    #image = Image.open(io.BytesIO(ps_data.encode('utf-8')))


def create_canvas():
    global canvas, image
    canvas = tk.Canvas(photoside, bg='white')
    frame_width = photoside.winfo_width()
    frame_height = photoside.winfo_height()
    canvas.place(relx=0.5, rely=0.5, anchor='center')
    canvas.bind("<B1-Motion>", lambda event: draw(canvas, event, pen_size, pen_color))
    pensizeSlider.config(state='normal')
    color_button.config(state='normal')
    image = scale(image, frame_width, frame_height)
    canvas.config(width=image.width, height=image.height)
    open_image(canvas, image)

def temp_text(e):
    resize_entry.delete(0, "end")

def resize(entry):
    global image
    size = entry.get()
    if image is not None:
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
    brightnessSlider.set(default_enhancements['Brightness'])
    contrastSlider.set(default_enhancements['Contrast'])
    sharpnessSlider.set(default_enhancements['Sharpness'])
    colorSlider.set(default_enhancements['Color'])
    pensizeSlider.set(5)
    displayimage(image)

def set_default(name):
    global image
    if name == 'Brightness':
        brightnessSlider.set(default_enhancements[name])
    elif name == 'Contrast':
        contrastSlider.set(default_enhancements[name])
    elif name == 'Sharpness':
        sharpnessSlider.set(default_enhancements[name])
    elif name == 'Color':
        colorSlider.set(default_enhancements[name])
    displayimage(image)

def set_apply(slider, name):
    global image
    default_value = default_enhancements[name]
    factor = float(slider.get()) if slider.get() else default_value
    enhancer = getattr(ImageEnhance, name)(image)
    image = enhancer.enhance(factor)
    displayimage(image)

def change_theme():
    if app.tk.call("ttk::style", "theme", "use") == "azure-dark":
        app.tk.call("set_theme", "light")
    else:
        app.tk.call("set_theme", "dark")




menu = ttk.Frame(app, style='Card.TFrame', padding=(5, 6, 7, 8))  # zawsze stworzyc i potem , bg='#856ff8'
menu.place(x=0, y=0, relwidth=0.3, relheight=1)  # pack, place lub grid zeby to gdzies wlozyc

photoside = ttk.Frame(app)
photoside.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

edit_photo_frame = tk.Frame(menu, width=400, height=300)
edit_photo_frame.place(relx=0.5, rely=1, anchor='s')
#edit_photo_frame.config(bg='red')

menubar = tk.Menu(menu)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=changeImg)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Draw", command=create_canvas)
menubar.add_cascade(label="File", menu=filemenu)

resize_entry = ttk.Entry(menu, width=30)
resize_entry.insert(0, "Provide with format 0000x0000")
resize_button = ttk.Button(menu, text='Resize', command=lambda: resize(resize_entry))
color_button = ttk.Button(menu, text='Color of pen', command=change_color)
rotate_button = ttk.Button(menu, text='Rotate', command=rotate)
flip_horizontal_button = ttk.Button(menu, text='Flip Horizontal', command=flip_horizontal)
flip_vertical_button = ttk.Button(menu, text='Flip Vertical', command=flip_vertical)
changetheme_button = ttk.Checkbutton(menu, text='Dark/Light mode', style='Switch.TCheckbutton', command=change_theme)

pensizeSlider = ttk.Scale(menu,  from_=1, to=10, style='Tick.TScale',orient=HORIZONTAL,
                      command=lambda val: change_size(pensizeSlider.get())) #label="Change size of pen",
brightnessSlider = ttk.Scale(menu, from_=0.1, to=2, orient=HORIZONTAL, command=brightness)
contrastSlider = ttk.Scale(menu, from_=0.1, to=2, orient=HORIZONTAL, command=contrast)
sharpnessSlider = ttk.Scale(menu, from_=0.1, to=2, orient=HORIZONTAL, command=sharpen)
colorSlider = ttk.Scale(menu, from_=0.1, to=2,  orient=HORIZONTAL, command=color)

apply1_button = ttk.Button(menu, text='Apply', command=lambda: set_apply(brightnessSlider, 'Brightness'))
apply2_button = ttk.Button(menu, text='Apply', command=lambda: set_apply(contrastSlider, 'Contrast'))
apply3_button = ttk.Button(menu, text='Apply', command=lambda: set_apply(sharpnessSlider, 'Sharpness'))
apply4_button = ttk.Button(menu, text='Apply', command=lambda: set_apply(colorSlider, 'Color'))
default1_button = ttk.Button(menu, text='Default', command=lambda: set_default('Brightness'))
default2_button = ttk.Button(menu, text='Default', command=lambda: set_default('Contrast'))
default3_button = ttk.Button(menu, text='Default', command=lambda: set_default('Sharpness'))
default4_button = ttk.Button(menu, text='Default', command=lambda: set_default('Color'))
apply_filter = ttk.Button(menu, text='Apply', command=lambda: set_filter(filter_combobox.get()))
clear_dr_button = ttk.Button(menu, text='Clear drawing', style='Accent.TButton', command=lambda: clear_drawing(canvas))
clear_all_button = ttk.Button(menu, text='Go back to original', style='Accent.TButton', command=go_back, width=20)

values = ("No filter", "Emboss", "Blur", "Contour", "Smooth", "Detail", "Edge enhance")
filter_combobox = ttk.Combobox(menu, values=values)
filter_combobox['state'] = 'readonly'
filter_combobox.set('Select filter')
filter_combobox.bind("<<ComboboxSelected>>", lambda event: choose_filter(filter_combobox.get()))

size_text = ttk.Label(menu, text='Size of pen')
br_text = ttk.Label(menu, text='Brightness')
ct_text = ttk.Label(menu, text='Contrast')
sh_text = ttk.Label(menu, text='Sharpness')
cl_text = ttk.Label(menu, text='Color')


pensizeSlider.set(5)
brightnessSlider.set(1)
contrastSlider.set(1)
sharpnessSlider.set(1)
colorSlider.set(1)


# resize_entry.grid(row=0, column=0, padx=5, pady=10, sticky='nsew')
# resize_button.grid(row=0, column=1, padx=5, pady=10, sticky='nsew')
# color_button.grid(row=1, column=0, padx=5, pady=10, sticky='ns')
# size_text.grid(row=1, column=1, padx=5, pady=50)
# pensizeSlider.grid(row=1, column=2, padx=5, pady=10)
# rotate_button.grid(row=2, column=0, padx=5, pady=10)
# flip_horizontal_button.grid(row=2, column=1, padx=5, pady=10)
# flip_vertical_button.grid(row=2, column=2, padx=5, pady=10)
# filter_combobox.grid(row=3, column=0, padx=5, pady=10)
# apply_filter.grid(row=3, column=1, padx=5, pady=10)
# br_text.grid(row=4, column=0, padx=5, pady=10)
# brightnessSlider.grid(row=4, column=1, padx=5, pady=10)
# apply1_button.grid(row=4, column=2, padx=5, pady=10)
# default1_button.grid(row=4, column=3, padx=5, pady=10)
# ct_text.grid(row=5, column=0, padx=5, pady=10)
# contrastSlider.grid(row=5, column=1, padx=5, pady=10)
# apply2_button.grid(row=5, column=2, padx=5, pady=10)
# default2_button.grid(row=5, column=3, padx=5, pady=10)
# sh_text.grid(row=6, column=0, padx=5, pady=10)
# sharpnessSlider.grid(row=6, column=1, padx=5, pady=10)
# apply3_button.grid(row=6, column=2, padx=5, pady=10)
# default3_button.grid(row=6, column=3, padx=5, pady=10)
# cl_text.grid(row=7, column=0, padx=5, pady=10)
# colorSlider.grid(row=7, column=1, padx=5, pady=10)
# apply4_button.grid(row=7, column=2, padx=5, pady=10)
# default4_button.grid(row=7, column=3, padx=5, pady=10)
# changetheme_button.grid(row=8, column=0, padx=5, pady=10)
# clear_dr_button.grid(row=8, column=1, padx=5, pady=10)
# clear_all_button.grid(row=8, column=2, padx=5, pady=10)
#
# edit_photo_frame.grid(row=9, column=0, sticky="S")


resize_entry.place(x=30, y=10, width=245)
resize_button.place(x=288, y=10)
size_text.place(x=30, y=58)
pensizeSlider.place(x=125, y=60, width=140)
color_button.place(x=284, y=52)
rotate_button.place(x=50, y=95)
flip_horizontal_button.place(x=153, y=95)
flip_vertical_button.place(x=270, y=95)
filter_combobox.place(x=70, y=140)
apply_filter.place(x=240, y=140)
br_text.place(x=30, y=190)
brightnessSlider.place(x=120, y=192)
apply1_button.place(x=240, y=185, width=65)
default1_button.place(x=315, y=185, width=65)
ct_text.place(x=30, y=235)
contrastSlider.place(x=120, y=237)
apply2_button.place(x=240, y=230, width=65)
default2_button.place(x=315, y=230, width=65)
sh_text.place(x=30, y=280)
sharpnessSlider.place(x=120, y=282)
apply3_button.place(x=240, y=275, width=65)
default3_button.place(x=315, y=275, width=65)
cl_text.place(x=30, y=325)
colorSlider.place(x=120, y=328)
apply4_button.place(x=240, y=320, width=65)
default4_button.place(x=315, y=320, width=65)
changetheme_button.place(x=125, y=360)
clear_dr_button.place(x=30, y=400, width=167)
clear_all_button.place(x=212, y=400, width=167)
# edit_photo_frame.place(x=420, y=500, relwidth=0.7, relheight=0.9)


image = None
#image = image.resize((700, 600))
#imageTK = ImageTk.PhotoImage(image)
#initial_photo = image.resize((200,100))
#initial_photo_TK = ImageTk.PhotoImage(initial_photo)
#Label(photoside, image=imageTK).grid(row=0, column=0)
#Label(edit_photo_frame, image=initial_photo_TK).grid(row=0, column=0)
original_image = image

filter_combobox.bind("<<ComboboxSelected>>")

resize_entry.bind("<FocusIn>", temp_text)
# app.state('zoomed')
app.resizable(False,False)
app.config(menu=menubar)


app.mainloop()