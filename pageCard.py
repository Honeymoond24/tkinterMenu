from tkinter import *
from PIL import ImageTk, Image
from header import *
from datetime import datetime


class PageCard(tk.Frame):  # Класс.
    def __init__(self, parent, controller, database, link):  # Конструктор описания карточки.
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.controller = controller
        self.database = database
        self.link = link
        # print(self.link)

        top_frame = Frame(self)
        Header(top_frame, self.controller)
        self.center = Frame(self)  # #FEF2E4 гриб

        self.data = self.database.select("SELECT * FROM dish")
        self.dish_image = ImageTk.PhotoImage(Image.open(self.data[self.link - 1][3]), height=256, width=256)
        self.dish_image_label = Label(self.center,
                                      text="123",
                                      image=self.dish_image
                                      )
        self.order = Button(self.center, text="Заказать", command=lambda: self.send_order(
                            f'INSERT INTO `order` (dish_id) VALUES ({self.link})'),
                            background="#00a1df",  # фоновый цвет кнопки
                            activebackground="#00a1df",
                            foreground="#FEF2E4",  # цвет текста
                            padx="5",  # отступ от границ до содержимого по горизонтали
                            pady="4",  # отступ от границ до содержимого по вертикали
                            font="5"  # высота шрифта
                            )
        self.order.grid(row=4, column=0, sticky="N")
        self.dish_image_label.grid(row=1, column=0, sticky="N")

        self.title = Label(self.center, text=self.data[self.link - 1][1], font=20)
        self.description = Label(self.center,
                                 text=self.data[self.link - 1][2],
                                 font=20)
        self.title.grid(row=1, column=1, sticky="N")
        self.description.grid(row=2, column=1, sticky="N")
        # layout all of the main containers
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        top_frame.grid(row=0, sticky="EW")
        self.center.grid(row=1, sticky="N")

        # create the self.center widgets
        self.center.grid_rowconfigure(0, weight=1)
        self.center.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)

        # ctr_left = Frame(self.center, bg='blue')
        # ctr_right = Frame(self.center, bg='green')
        print(f"{__name__} loaded")

    def send_order(self, select):
        self.select = select

        self.data = self.database.insert(self.select)
