import os

def checkSystemInfo():# обявление функции
	print('Версия ядра', os.name)
	print('Имя пользователя', os.getlogin())
	print('текущая деректория', os.getcwd())
	print('files on dick', os.listdir("C:"))

	# библиотека path входит в состав os
	print('Обсалютный путь', os.path.abspath("2.py"))

checkSystemInfo() # вызов функции


# аргументы функций

def hello(name):
	print('вы ввели', name)

hello('alex')

def summ(val1, val2, val3):
	result = val1 + val2 + val3
	print(result)
	return result # возращение и сохранение в переменной \return функция


val = summ(13, 3456, 34567)

# функции для преобразования типов данных
str()
int()
float()
bool()