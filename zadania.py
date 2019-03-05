"""
Написать функцию arithmetic, 
принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. 
Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). 
В остальных случаях вернуть строку "Неизвестная операция".
"""
# def arithmetic(x, y, z):
# 	if z == '-':
# 		return x - y
# 	elif z == '*':
# 		return x * y
# 	elif z == '/':
# 		return x / y
# 	elif z == '+':
# 		return x +y
# 	else:
# 		print('Неизвестная операция')
# print(arithmetic(10,2,'*'))



def is_year_leap():
	year = int(input('enter year'))
	if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
		print('false')
	else:
		print('True')
is_year_leap()
