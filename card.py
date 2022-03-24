from pageCard import *


class Card(tk.Frame):  # Класс.
    def __init__(self, parent, controller, lable_text, link):  # Конструктор карточки.
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.lable_text = lable_text
        self.link = link
        self.cardframe = tk.Frame(self, padx="10", pady="8", background='#00bff6', highlightbackground="#805A3B",
                                  highlightthickness=1, bd=0)
        self.ph_img = tk.PhotoImage(file='assets/111.png').subsample(25, 25)

        button0 = tk.Button(self.cardframe,
                            image=self.ph_img,
                            relief='flat',
                            width=100,
                            height=100,
                            )
        button0.grid(column=0, row=0, rowspan=2)

        label = tk.Label(self.cardframe, background='#00bff6', foreground="#FEF2E4", text=self.lable_text,
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
