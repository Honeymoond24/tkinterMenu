from header import *


class PageCard(tk.Frame):
    def __init__(self, parent, controller, link):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.link = link
        # print(self.link)

        top_frame = Frame(self)  # Верхний блок
        Header(top_frame, self.controller)  # Обработка верхнего блока
        self.center = Frame(self)

        self.ph_img = tk.PhotoImage(file='assets/111.png').subsample(15, 15)  # Добавляем фото в переменную
        self.image = Button(self.center, image=self.ph_img, relief='flat')  # Добавляем переменную с фото
        self.image.grid(row=1, column=0, sticky="N")  # Прилипание к северу - вверх

        self.title = Label(self.center, text="Корейский суп Чов Зва", font=20)
        self.description = Label(self.center,
                                 text="Данное блюдо очень распространено в Северной Корее. \nЕго рецепт очень сложен.",
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
