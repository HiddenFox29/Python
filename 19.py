from tkinter import *
from random import randint
from random import shuffle, choice
from datetime import datetime, date, time


root = Tk()
root.geometry('500x300')


def psw(): #создание генератора случайных паролей
    numbers = '1234567890' #создание строки символов для пароля
    string = 'qwertyuiopasdfghjklzxcvbnm'
    symbols = '!@#$%^&*'
    stringUpper = string.upper()

    allSymbols = numbers+string+stringUpper+symbols
    ls=list(allSymbols) #объединение в массив с разделителями

    shuffle(ls) #перемешивание симвлов внутри
    psw = ''.join(choice(ls) for x in range(20)) #выбор 20 случайных символов

    with open('psw.txt','a')as g: #открытие файла на запись. Если файла нет - создаёт
        now = datetime.now() # дата текущего времени записи файла 
        g.write(psw + ' ' + now.strftime('%c') + '\n') # записываем в фаил список с указанием времени в форматирование даты
    hello.config(text = psw)

hello = Label(root, text = 'Click Button For Generate PASS') #создание объекта в классе Lable привязка к окну рут с текстом...
hello.config(font=('Arial',25,'underline')) #изменение конфигурации шрифта
hello.pack() #отображение текста

#BUTTONS
button = Button(root,text='Создание пароля',command=psw) #создание кнопки к объкту root с текстом с запуском функции hi
button.config(width=20, #задание параметров ширина
            height=5, #высота
            bg='purple', #цвет кнопки
            fg='white') #цвет шрифта
button.pack() #вывод кнопки

def createWindow():
    createWindow = Tk() # создание окна класса Тк в нутри функции что позволяет создать окно по нажатию кнопки
    createWindow.geometry('600x400') # устоновка размеров окна через функцию
    text = Text(createWindow) # создание текстового врагмента с помощью класса Text модуля tkinter
    with open('psw.txt', 'r')as psw: # открытие файла для чтения (можно не указывать 'r' т.к идет по умолчанию)
        pswR =[] # создание массива 
        for line in psw: # построчная запись с помощью спец переменной line
            pswR.append(line) # добовление в конец списка
            pswR.reverse()

        for i in pswR: # перебераем пароли из списка pswR
            text.insert(END, i + '\n') # выводим в окне построчно содержимое файла 
    text.pack() # размещаем текст
    createWindow.mainloop() #функция, рисующая окно. Всегда пишется последней



createWindow = Button(root, text="Показать пароли", command=createWindow)   # кнопка вызовав окна со списком паролей 
createWindow.config(width=20,
            height=5,
            bg='black',
            fg='white'
            ) # настройки внешнего вида окна
createWindow.pack() # размещение кнопки в основном окне






root.mainloop()#функция, рисующая окно. Всегда пишется последней


# Поэксперементировать с библиотекой!
# Сделать возможность отображения паролей в новом окне
# По нажатии на кнопку ПОКАЗАТЬ ПАРОЛИ должы отобразиться пароли из файла