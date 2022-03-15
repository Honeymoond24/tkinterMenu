from pageMain import *  # Импортируем необходимые файлы зависимостей.
from food import *
from dailyMenu import *
# from pageAbout import *
from tkinter import font as tkfont
from menu import *
from pageCard import *
from pageStats import *


class Application(tk.Tk):  # Класс.
    def __init__(self, *args, **kwargs):  # Конструктор приложения.
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=12,
                                      slant="italic",
                                      weight="bold"
                                      )
        self.multipliers = [1, 1.25, 1.5]  # 1280x720, 1600x900, 1920x1080
        self.multiplier = self.multipliers[0]
        print(f"multiplier {self.multiplier}")
        self.colors = {"gray": []}
        self.iconbitmap('assets/logo.ico')
        self.title('Ресторан Шакал')
        # self.geometry(str(16 * 80 * self.multiplier) + "x" +  # 1280x720
        #               str(9 * 80 * self.multiplier) + "+50+50")
        self.geometry("1280x576+50+50")
        container = tk.Frame(self, bg='#FEF2E4')  # Страницы
        # container.place(x=0, y=0)
        container.pack(side="top", fill="both", expand=False)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        self.frames["PageMain"] = PageMain(parent=container, controller=self)
        self.frames["Food"] = Food(parent=container, controller=self)
        self.frames["DailyMenu"] = DailyMenu(parent=container, controller=self)
        # self.frames["PageAbout"] = PageAbout(parent=container, controller=self)
        self.frames["PageCard"] = PageCard(parent=container, controller=self, link='link')
        self.frames["PageStats"] = PageStats(parent=container, controller=self)

        self.frames["PageMain"].grid(row=0, column=0, sticky="nsew")
        self.frames["Food"].grid(row=0, column=0, sticky="nsew")
        self.frames["DailyMenu"].grid(row=0, column=0, sticky="nsew")
        # self.frames["PageAbout"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageCard"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageStats"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageMain")
        self.menu = AppMenu(self, container)
        self.menu.add_menu()
        # self.menu.call_page_about()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
