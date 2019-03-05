from tkinter import * # модуль для работы с графическим интерфейсом

import datetime # модуль для работы с датами

from datetime import datetime, timedelta # импорт из модуля объекта для работы с датами и вычесления дат

import locale # модуль для перевода дат с английского на русский 
locale.setlocale(locale.LC_ALL, "") # функция для перевода всех встроеных выводов

def deadLine(): # создаем функция расчета дедлайна
	now = datetime.now() # устонавливаев действуещее время сохроняем в переменную 
	deadLine = datetime(2019, 1, 30, 23, 59) # устонавливаев дату дедлайна
	a = ('Уведомляем вас что, ' + deadLine.strftime('%d %b (%a) %Y') + ' года заканчивается время выполнения проекта!' + '\n')
	b = ('Сегодня ' + now.strftime('%d %b (%a) %Y') + ' года' +'\n') # актуальную дату для сравнения в формате день,месяц(сокр),год,день недели сокращенно
	if now > deadLine:
		c = ('Срок сдачи проекта прошел ' + str(now.day - deadLine.day) +' дней назад') # использовать + иначе появляются фигурные скобки{}
	elif now.day == deadLine.day and now.month == deadLine.month and now.year == deadLine.year:
		c = ('Срок сдачи проекта сегодня ' + now.strftime('%d %b (%a) %Y') + ' года.' + '\n') # при конструкции if нужно использовать одну и туже еременную как 'c' иначе ошибка
	else:
		period = deadLine - now
		c = ('Осталось {} дней до сдачи проекта.'.format(period.days) + '\n')
	text.insert(1.0, c) # вызов текста в окно при нажатии кнопки, первым вывводит нижний insert
	text.insert(1.0, b)
	text.insert(1.0, a)

	

# deadLine()
def deleteText():
	text.delete(1.0, END)

root = Tk()
root.geometry('500x300')

text = Text(width=70, height=10, bg='green', fg='white', wrap=WORD) # настройки текста wrap перенос слов на новую строку
text.pack() # размещение окна с текстом

lable = Label(root, text='Дедлайн') # заголовок в окне
lable.config(font=('ALGERIAN', 25)) # настройки заголовка
lable.pack() # размещение заголовка
# кнопка
button = Button(root, text='Определить время дедлайна', command=deadLine) # настрока кнопки
button.config(width=30,
			height=5,
			bg='black',
			fg='white')
button.pack() # размещение кнопки в окне

b_delete = Button(root, text='Удалить текст', command=deleteText)
b_delete.config(width=10,
			height=5,
			bg='black',
			fg='white')
b_delete.pack()

root.mainloop() # вызов окна