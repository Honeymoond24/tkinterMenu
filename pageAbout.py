import tkinter as tk


class PageAbout(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self,
                         text="Эта программа была разработана в рамках лабораторной работы 2. "
                              "Работу выполнили: 1 2 3 4",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("PageMain"))
        button.pack()
