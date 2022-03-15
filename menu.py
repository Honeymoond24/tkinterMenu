from tkinter import *
from tkinter import ttk
from tkinter import font as tkfont
from PIL import ImageTk, Image
import webbrowser


class AppMenu(Tk):  # Класс.
    def __init__(self, parent, controller):  # Конструктор.
        self.parent = parent
        self.controller = controller
        self.m = Menu(self.parent)
        # Вкладки меню
        self.menu = Menu(self.m, tearoff=0)  # Меню
        self.view = Menu(self.m, tearoff=0)  # Тема
        # self.screensize = Menu(self.m, tearoff=0)  # Размер экрана
        self.about = Menu(self.m, tearoff=0)  # Справка
        print(f"{__name__} loaded")

    def add_menu(self):
        self.parent.config(menu=self.m)
        # Меню главное меню
        self.m.add_cascade(label="Меню", menu=self.menu)
        self.menu.add_command(label="Открыть базу данных", command=self.parent.destroy)
        self.menu.add_command(label="Сохранить базу данных", command=self.parent.destroy)
        self.menu.add_separator()
        self.menu.add_command(label="Выйти", command=self.parent.destroy)
        # Меню тема
        self.m.add_cascade(label="Вид", menu=self.view)
        self.view.add_command(label="Белый", command=self.color_white)
        self.view.add_command(label="Серый", command=self.color_gray)
        # Меню размер экрана
        # self.m.add_cascade(label="Размер экрана", menu=self.screensize)
        # self.screensize.add_command(label="640x480", command=self.square)
        # self.screensize.add_command(label="800x600", command=self.rectangle)
        # Меню справка
        self.m.add_cascade(label="Справка", menu=self.about)
        self.about.add_command(label="Поставить оценку",
                               command=lambda: webbrowser.open("https://github.com/Honeymoond24/tkinterMenu"))
        self.about.add_command(label="О программе", command=self.call_page_about)

    def call_page_about(self):  # Окно "О программе"
        page_about = Toplevel(self.controller, height=512, width=512, pady=10, padx=10)  # Окно "О программе"
        page_about.title('Ресторан Шакал: сведения')
        page_about.iconbitmap('assets/logo.ico')
        logo = ImageTk.PhotoImage(Image.open("assets/logo.png"), height=256, width=256)
        logo_label = Label(page_about,
                           text="123",
                           image=logo
                           )
        logo_label.grid(row=0, column=0, columnspan=2, sticky="ew")
        separator = ttk.Separator(page_about, orient='horizontal')
        separator.grid(row=1, column=0, columnspan=2, sticky="ew")
        info = Label(page_about,
                     text="Данная программа была разработана в рамках лабораторной работы 2.\n"
                          "Работу выполнили студенты группы АПО-19:\n"
                          "Жантурин Д.Р.\n"
                          "Семейников А.Н.\n"
                          "Долгушин Н.Л.\n"
                          "Одарич К.Н.",
                     justify='left',
                     font=tkfont.Font(family='Helvetica', size=12, slant="italic"))
        info.grid(row=2, column=0, columnspan=2)
        btn_review = Button(page_about, text="Поставить оценку",
                            command=lambda: webbrowser.open("https://github.com/Honeymoond24/tkinterMenu"),
                            background="#00a1df",  # фоновый цвет кнопки
                            foreground="#F9F9FF",  # цвет текста
                            padx="20",  # отступ от границ до содержимого по горизонтали
                            pady="8",  # отступ от границ до содержимого по вертикали
                            font="16",  # высота шрифта
                            )
        btn_review.grid(row=3, column=0)
        btn_close = Button(page_about, text="ОК", command=page_about.destroy,
                           background="#00a1df",  # фоновый цвет кнопки
                           foreground="#F9F9FF",  # цвет текста
                           padx="20",  # отступ от границ до содержимого по горизонтали
                           pady="8",  # отступ от границ до содержимого по вертикали
                           font="16",  # высота шрифта
                           )
        btn_close.grid(row=3, column=1)

        # page_about.grid_rowconfigure(0, weight=1)
        # page_about.grid_rowconfigure(1, weight=10)
        # page_about.grid_rowconfigure(2, weight=10)
        # page_about.grid_rowconfigure(3, weight=1)
        # page_about.grid_columnconfigure(0, weight=1)
        # page_about.grid_columnconfigure(1, weight=10)
        # page_about.grid_columnconfigure(2, weight=1)
        page_about.transient(self.controller)
        page_about.grab_set()
        page_about.focus_set()
        page_about.wait_window()

    def color_white(self):
        self.controller.config(bg="white")
        self.controller.pack()

    def color_gray(self):
        self.controller.config(bg="black")
        self.controller.pack()

    # def square(self):
    #     self.controller.config(width=960)
    #     self.controller.config(height=720)
    #     self.controller.pack()
    #
    # def rectangle(self):
    #     self.controller.config(width=1280)
    #     self.controller.config(height=720)
    #     self.controller.pack()
