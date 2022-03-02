from pageMain import *  # Импортируем необходимые файлы зависимостей.
from food import *
from dailyMenu import *
from pageAbout import *
from menu import *
from pageCard import *


class Application(tk.Tk):  # Класс.
    def __init__(self, *args, **kwargs):  # Конструктор приложения.
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=12,
                                      slant="italic",
                                      weight="bold"
                                      )
        # self.geometry("1024x920")
        container = tk.Frame(self, bg='#FEF2E4')  # Страницы
        container.pack(side="top", fill="both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        self.frames["PageMain"] = PageMain(parent=container, controller=self)
        self.frames["PageOne"] = Food(parent=container, controller=self)
        self.frames["PageTwo"] = DailyMenu(parent=container, controller=self)
        self.frames["PageAbout"] = PageAbout(parent=container, controller=self)
        self.frames["PageCard"] = PageCard(parent=container, controller=self, link='link')

        self.frames["PageMain"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageAbout"].grid(row=0, column=0, sticky="nsew")
        self.frames["PageCard"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageMain")
        self.menu = AppMenu(self, container)
        self.menu.add_menu()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
