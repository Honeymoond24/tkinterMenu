from tkinter import *
from menu import AppMenu
from tkinter import font as tkfont
from pageMain import *
from pageOne import *
from pageTwo import *


class Application(Tk):
    def __init__(self):
        self.root = Tk()
        self.root.title("Ресторан \"Шакал\"")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        # Параметры по умолчанию
        self.fra = Frame(self.root, width=960, height=720, bg="White")
        self.fra.pack()
        self.menu = AppMenu(self.root, self.fra)
        self.menu.add_menu()
        self.frames = {}

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def start(self):
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.root.mainloop()
