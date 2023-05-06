from tkinter import CENTER, ROUND #zamienic na CTKinter??

from PIL import Image, ImageDraw, ImageTk
from customtkinter import filedialog, CTkFrame, CTkCanvas

class BasicFuncs(CTkFrame):

    def __init__(self, master=None):
        CTkFrame.__init(self, master=master, bg="gray", width=700, height=500)
        self.showing=None
        self.x=0
        self.y=0
        self.crop_start_x=0
        self.crop_start_y=0
        self.crop_end_x=0
        self.crop_enb_y=0
        self.draw_ids=list()
        self.rectangle_id=0
        self.ratio=0
        self.canvas=CTkCanvas(self, bg="gray", width=700, height=500)
        #self.canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.canvas.place(relx=0.5, rely=0.5, x=0.5, y=0.5)


    def add_image(self, img=None):
        self.clear_canvas()
        if img is None:
            image = self.master.processed_image.copy()
        else:
            image = img

        #
        global file_path
        file_path = filedialog.askdirectory()
        image = Image.open(file_path)
        #

        image =image.convert('RGB')

        width, height = image.size
        ratio = height / width

        new_width = width
        new_height = height

        if height > self.winfo_height() or width > self.winfo_width():
            if ratio < 1:
                new_width = self.winfo_width()
                new_height = int(new_width * ratio)
            else:
                new_height = self.winfo_height()
                new_width = int(new_height * (width / height))

        self.shown_image = image.resize((new_width, new_height))
        self.shown_image = ImageTk.PhotoImage(Image.fromarray(self.shown_image))

        self.ratio = height / new_height

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(new_width / 2, new_height / 2, anchor=CENTER, image=self.shown_image)
    def activate_draw(self):
        self.canvas.bind("<ButtonPress>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.master.is_draw_state = True

    def activate_crop(self):
        self.canvas.bind("<ButtonPress>", self.start_crop)
        self.canvas.bind("<B1-Motion>", self.crop)
        self.canvas.bind("<ButtonRelease>", self.end_crop)

        self.master.is_crop_state = True

    def deactivate_draw(self):
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")

        self.master.is_draw_state = False

    def deactivate_crop(self):
        self.canvas.unbind("<ButtonPress>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease>")

        self.master.is_crop_state = False

    def start_draw(self, event):
        self.x = event.x
        self.y = event.y

    def draw(self, event):
        # self.draw_ids.append(self.canvas.create_line(self.x, self.y, event.x, event.y, width=2,
        #                                              fill="red", capstyle=ROUND, smooth=True))
        #
        # cv2.line(self.master.processed_image, (int(self.x * self.ratio), int(self.y * self.ratio)),
        #          (int(event.x * self.ratio), int(event.y * self.ratio)),
        #          (0, 0, 255), thickness=int(self.ratio * 2),
        #          lineType=8)
        #
        # self.x = event.x
        # self.y = event.y
        draw = ImageDraw.Draw(self.master.image)
        draw.line((self.x, self.y, event.x, event.y), fill="red", width=2)
        self.draw_ids[-1] = self.canvas.create_line(self.x, self.y, event.x, event.y, width=2,
                                                    fill="red", capstyle=ROUND, smooth=True)
        self.x = event.x
        self.y = event.y
    def start_crop(self, event):
        self.crop_start_x = event.x
        self.crop_start_y = event.y

    def crop(self, event):
        if self.rectangle_id:
            self.canvas.delete(self.rectangle_id)

        self.crop_end_x = event.x
        self.crop_end_y = event.y

        self.rectangle_id = self.canvas.create_rectangle(self.crop_start_x, self.crop_start_y,
                                                         self.crop_end_x, self.crop_end_y, width=1)

    def end_crop(self, event):
        if self.crop_start_x <= self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x > self.crop_end_x and self.crop_start_y <= self.crop_end_y:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_start_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_end_y * self.ratio)
        elif self.crop_start_x <= self.crop_end_x and self.crop_start_y > self.crop_end_y:
            start_x = int(self.crop_start_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_end_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)
        else:
            start_x = int(self.crop_end_x * self.ratio)
            start_y = int(self.crop_end_y * self.ratio)
            end_x = int(self.crop_start_x * self.ratio)
            end_y = int(self.crop_start_y * self.ratio)

        x = slice(start_x, end_x, 1)
        y = slice(start_y, end_y, 1)

        self.master.processed_image = self.master.processed_image[y, x]

        self.show_image()

    def clear_canvas(self):
        self.canvas.delete("all")

    def clear_draw(self):
        self.canvas.delete(self.draw_ids)
