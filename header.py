import tkinter as tk


class Header(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        # label = tk.Label(self, text="MainPage", font=controller.title_font)
        button1 = tk.Button(self.parent, text="Блюда", command=lambda: controller.show_frame("PageMain"),
                            background="#D55448",  # фоновый цвет кнопки
                            foreground="#F9F9FF",  # цвет текста
                            padx="20",  # отступ от границ до содержимого по горизонтали
                            pady="8",  # отступ от границ до содержимого по вертикали
                            font="16"  # высота шрифта
                            )
        print()
        button2 = tk.Button(self.parent, text="Продукты", command=lambda: controller.show_frame("PageOne"),
                            background="#D55448",  # фоновый цвет кнопки
                            foreground="#F9F9FF",  # цвет текста
                            padx="20",  # отступ от границ до содержимого по горизонтали
                            pady="8",  # отступ от границ до содержимого по вертикали
                            font="16"  # высота шрифта
                            )
        button3 = tk.Button(self.parent, text="Меню дня", command=lambda: controller.show_frame("PageTwo"),
                            background="#D55448",  # фоновый цвет кнопки
                            foreground="#F9F9FF",  # цвет текста
                            padx="20",  # отступ от границ до содержимого по горизонтали
                            pady="8",  # отступ от границ до содержимого по вертикали
                            font="16"  # высота шрифта
                            )

        # layout all of the main containers
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_columnconfigure(1, weight=1)
        self.parent.grid_columnconfigure(2, weight=1)

        self.grid(row=0, sticky="EW")

        # label.grid(row=0, column=0,  sticky="nsew")
        button1.grid(row=0, column=0, sticky="nsew")
        button2.grid(row=0, column=1, sticky="nsew")
        button3.grid(row=0, column=2, sticky="nsew")
