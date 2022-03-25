from tkinter import *
from pageCard import *
from PIL import ImageTk, Image


class Card(tk.Frame):  # Класс.
    def __init__(self, parent, controller, database, label_text, link):  # Конструктор карточки.
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.database = database
        self.label_text = label_text
        self.link = link
        self.cardframe = tk.Frame(self, padx="30", pady="8", background='#00bff6', highlightbackground="#805A3B",
                                  highlightthickness=1, bd=0, width=2000)
        self.data = self.database.select("SELECT * FROM dish")
        print(self.link)
        # id = self.link - 1
        self.dish_image = ImageTk.PhotoImage(Image.open(self.data[self.link - 1][3]).resize((150, 150)))
        # print(self.data[id][3], self.link)
        self.dish_image_label = Label(self.cardframe, text="123", image=self.dish_image)
        self.dish_image_label.grid(column=0, row=0, rowspan=2)

        label = tk.Label(self.cardframe, background='#00bff6', foreground="#FEF2E4", text=self.label_text,
                         font=controller.title_font)
        label.grid(column=1, row=0)
        # self.controller.frames[self.link] = PageCard(parent=self, controller=controller, link=self.link)
        button1 = tk.Button(self.cardframe, text="Посмотреть", command=lambda: controller.show_frame_food('PageCard',link),
                            background="#00a1df",  # фоновый цвет кнопки
                            activebackground="#00a1df",
                            foreground="#FEF2E4",  # цвет текста
                            padx="5",  # отступ от границ до содержимого по горизонтали
                            pady="4",  # отступ от границ до содержимого по вертикали
                            font="5"  # высота шрифта
                            )
        button1.grid(column=1, row=1)

        self.cardframe.grid(row=1, column=1)
        print(f"{__name__} loaded")
