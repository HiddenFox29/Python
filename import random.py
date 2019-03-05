import random
from random import shuffle, choice
from tkinter import*
from tkinter import messagebox
from datetime import datetime, date, time

def psw(): #создание генератора случайных паролей
    numbers = '123456789' #создание строки символов для пароля
    string = 'qwertyuiopasdfghjklzxcvbnm'
    symbols = '!@#$%^&*'
    stringUpper = string.upper()
    allSymbols = numbers+string+stringUpper+symbols
    ls=list(allSymbols) #объединение в массив с разделителями
    shuffle(ls) #перемешивание симвлов внутри
    psw = ''.join(choice(ls) for x in range(20)) #выбор 20 случайных символов
    g = open('psw.txt','a') #открытие файла а запись. Если файла нет - создаёт
    now = datetime.now() 
    g.write(psw+' '+now.strftime('%d %B %Y %X %A')+'\n')
    g.close()
    hello.config(text = psw)

root = Tk() #создание окна в классе Tk
root.geometry('500x250') #задние размера окна через функцию

#LABELS
hello = Label(root, text = 'This is my programm') #создание объекта в классе Lable привязка к окну рут с текстом...
hello.config(font=('Arial',25,'underline')) #изменение конфигурации шрифта
hello.pack() #отображение текста. 

#def hi():
#    print('Hello')

def windowPasswords():
    newPasswords = Tk() #создание окна в классе Tk
    newPasswords.geometry('500x250') #задание размера окна через функцию
    t = Text(newPasswords) #создание текстового фрагмента
    psw = open('psw.txt')
    
    pswR=[]
    for line in psw:      #чтение из файла построчно
        pswR.append(line)
    
    pswR.reverse()
    
    for i in pswR: #вывод информации из файла в окно
       t.insert(END, i + '\n')
    psw.close()

    t.pack()
    newPasswords.mainloop()

#BUTTONS
chek = Button(root,text='Создание пароля',command=psw) #создание кнопки к объкту root с текстом с запуском функции hi
chek.config(width=20, #задание параметров ширина
            height=5, #высота
            bg='purple', #цвет кнопки
            fg='white') #цвет шрифта
chek.pack() #вывод кнопки

def pincode():
    def pinCheks():
        pinCheck = pinMess.get()
        if pinCheck=='1234':
            windowPasswords()
        else:
            messagebox.showinfo("Pin", 'неверный пин, повторите попытку')
            
    pin = Tk() #создание окна в классе Tk
    pin.geometry('200x100') #задание размера окна через функцию
    pinLable = Label(pin, text = 'Введите пин-код')
    pinLable.pack()
    pinMess = Entry(pin)
    pinMess.pack()
    pinCh = Button(pin,text='Проверить',command=pinCheks)
    pinCh.pack()
    pin.mainloop()
   
    
passGen = Button(root,text='Вывод пароля',command=pincode) #создание кнопки к объкту root с текстом с запуском функции hi
passGen.config(width=20, #задание параметров ширина
            height=2, #высота
            bg='yellow', #цвет кнопки
            fg='black') #цвет шрифта
passGen.pack() #вывод кнопки


root.mainloop() #функция, рисующая окно. Всегда пишется последней