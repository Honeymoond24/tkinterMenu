from database import Database
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
        self.geometry("1920x1080+0+0")
        self.container = tk.Frame(self, bg='#FEF2E4')  # Страницы
        self.container.pack(side="top", fill="both", expand=False)
        self.db = Database()
        self.frames = {}

        self.frames["PageMain"] = PageMain(parent=self.container, controller=self, database=self.db)
        self.frames["Food"] = Food(parent=self.container, controller=self, database=self.db)
        self.frames["DailyMenu"] = DailyMenu(parent=self.container, controller=self, database=self.db)
        # self.frames["PageCard"] = PageCard(parent=self.container, controller=self, link='link')
        self.frames["PageStats"] = PageStats(parent=self.container, controller=self, database=self.db)

        self.frames["PageMain"].grid(row=0, column=0, sticky="nsew")
        self.frames["Food"].grid(row=0, column=0, sticky="nsew")
        self.frames["DailyMenu"].grid(row=0, column=0, sticky="nsew")
        # self.frames["PageCard"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageStats"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageMain")
        self.menu = AppMenu(self, self.container)
        self.menu.add_menu()
        self.database = Database()
        # for row in self.database.select("select * from dish"):
        #     print(row)

    def show_frame(self, page_name):
        self.frame = self.frames[page_name]
        self.frame.tkraise()

    def show_frame_food(self, page_name, id):
        if "PageCard" in self.frames:
            self.frames["PageCard"].destroy()
        self.frames["PageCard"] = PageCard(parent=self.container, controller=self, database=self.db, link=id)
        self.frames["PageCard"].grid(row=0, column=0, sticky="nsew")
        self.frame = self.frames["PageCard"]
        self.frame.tkraise()
