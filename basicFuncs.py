from PIL import ImageTk

def max_colors(image):
    img = image
    img_out = img
    img = img.convert("RGBA")
    img_out = img_out.convert("RGBA")
    width, height = img.size
    numb_of_pixs = 8 # zmień na 21 :>                                        good luck :)
    pixs_taken = numb_of_pixs // 2 - 1
    for y in range(pixs_taken + 1, height - pixs_taken - 1):
        for x in range(pixs_taken + 1, width - pixs_taken - 1):
            list_R = []
            list_G = []
            list_B = []

            for i in range(x - pixs_taken, x + pixs_taken):
                for j in range(y - pixs_taken, y + pixs_taken):
                    pixel_colour = img.getpixel((i, j))
                    # print(i + j)
                    # print(pixel_colour)
                    list_R.append(pixel_colour[0])
                    list_G.append(pixel_colour[1])
                    list_B.append(pixel_colour[2])
                # print("-----------------")
                # print(list_R)
                # print(max(list_G))
            img_out.putpixel((x, y), (max(list_R), max(list_G), max(list_B), 255))
            # img.getpixel((i, j))
    #length = 255-4
    #pool = string.ascii_letters
    #random_string = ''.join(random.choice(pool) for i in range(length))
    #bubu = random_string+".png"
    #img_out.save(bubu)
    image = img_out
    return img_out

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
