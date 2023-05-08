from PIL import Image, ImageOps, ImageTk, ImageFilter



def open_image(canvas, image):
    image = image.resize((700, 600))
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")


def draw(canvas, event, pen_size, pen_color):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')


def clear_drawing(canvas):
    canvas.delete('all')
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")


def clear_all(canvas):
    canvas.delete('all')
