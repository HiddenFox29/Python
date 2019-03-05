from tkinter import *
from random import randint


root = Tk()
root.geometry('300x300')


def gener():
	gen = randint(1, 10000000)
	hello.config(text=gen)

	
def getUserData():
	text = entry.get()
	userText.config(text=text)

# lables
hello = Label(root,text='INT GENERATOR')
hello.config(font=('Tahoma', 25, 'underline'))
hello.pack() # отрисовывает текст на экране

userText = Label(root,text='USER TEXT')
userText.config(font=('Tahoma', 25, 'underline'))
userText.pack() # отрисовывает текст на экране

# buttons
button = Button(root, text='ДИКАЯ КНОПКА')
button.config(width=20, height=10, bg='orange', fg='black', command=gener)
button.pack()

getUserInput = Button(root, text='забрать данные ввода')
getUserInput.config(width=20, height=10, bg='orange', fg='black', command=getUserData)
getUserInput.pack()

# ENTRY ВВОД ТЕКСТА
entry = Entry(root)
entry.pack()

# запускает окно(отрисовывает)
root.mainloop()
# from tkinter import *
# root = Tk()
# text = Text(root, height=3, width=60)
# text.pack(side='left')
# scrollbar = Scrollbar(root)
# scrollbar.pack(side='left')
# # первая привязка
# scrollbar['command'] = text.yview
# # вторая привязка
# text['yscrollcommand'] = scrollbar.set
# root.mainloop()