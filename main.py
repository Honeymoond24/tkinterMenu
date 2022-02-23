# Виджеты:
#
# imports-----------------------
from tkinter import *

# создаем главное окно программы
root = Tk()
root.title("Заголовок окна программы")


def colorR():
    fra.config(bg="Red")


def colorG():
    fra.config(bg="Green")


def colorB():
    fra.config(bg="Blue")


def square():
    fra.config(width=640)
    fra.config(height=480)


def rectangle():
    fra.config(width=800)
    fra.config(height=600)


# Параметры по умолчанию
fra = Frame(root, width=400, height=200, bg="Black")
fra.pack()

# создаем объект меню на главном окне
m = Menu(root)
root.config(menu=m)

# второе меню
menu = Menu(m)
m.add_cascade(label="Меню", menu=menu)
menu.add_command(label="Выйти", command=exit)
menu.add_command(label="800x600", command=rectangle)

# первое меню
cm = Menu(m)
m.add_cascade(label="Цвет", menu=cm)
cm.add_command(label="Красный", command=colorR)
cm.add_command(label="Зеленый", command=colorG)
cm.add_command(label="Синий", command=colorB)

# второе меню
sm = Menu(m)
m.add_cascade(label="Размер", menu=sm)
sm.add_command(label="640x480", command=square)
sm.add_command(label="800x600", command=rectangle)

root.mainloop()
