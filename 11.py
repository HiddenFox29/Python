import ast
# создаем коллекцию ключ значение
user = {'name': 3000, 'balance': 200000, 'zuy': [13, 15, 30, 19], 'company': {'name': 'VISA', 'CEO':'Shon Parker', 'cap': 10000}}
# открываем фаил
file = open('nameFile.txt', 'w')
# записываем в фаил как строки
file.write(str(user))
# закрываем фаил
file.close()
# открываем фаил для чтения и передаем имени file2
file2 = open('nameFile.txt', 'r')
# передаем в имя data прочтенное с file2
data = file2.read()
# с помощью модуля ast и метода literal_eval из переменной data в переменную data 2 передаем коллекцию
data2 = ast.literal_eval(data)
print(type(data2))
file.close()

print(data2['balance'])
if data2['balance'] <= 30000:
	print('иди на хуй ты мало зарабатываешь!!!!')
else:
	print('ok')
# b = 3
# user = {'name': 3000, 'balance': 2000, 'zuy': [13, 15, 30, 19], 'company': {'name': 'VISA', 'CEO':'Shon Parker', 'cap': 10000}}
# print(user['name'])
# print(user['balance'])
# print(user['zuy'[0]])
# print(user['company'])
# print(user['CEO'])

#  >>>import ast
# >>>x = ast.literal_eval("{'foo' : 'bar', 'hello' : 'world'}")
# >>>type(x)
# <type'dict'>

# # dict.clear()
# # dict.copy()
# # dict.items()
# # dict.keys()
# # dict.values()

# # задания 
# # почитать про функции строк , массивов, хешей(словарей), 
# # научится программными средствами создовать хеши 
# # recrus рекрусивные функции изучить
