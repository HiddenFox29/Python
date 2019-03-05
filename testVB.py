# # 	# импортируем модуль
import os # os предназначен для работы с деректориями и операционной системой
import ast
from tkinter import *
# глобальные переменные "global"
emailLogin = ''
path = 'C:\\Program Files\\virtual bank\\'
workData = ''
month_pay = ''
month_payLegal = ''
auditValue = ''
# def run():
# 	print()
# run()
#========================================================================================
# Функция проверки данных введеных при подачи заявки на кредит

def auditClient(path, emailLogin, month_pay, audit_Value):# в качестве аргументов передаем название глобальных переменных переменых
# с помощью цикла with открываем фаил на чтение и передаем его в промежут перемен в дальнейшем фаил авто закроется
	with open(path + emailLogin + '\\' 'userCredit.txt', 'r') as file:
		data = file.read() # записываем с фаила и передаем в data
		data2 = ast.literal_eval(data) # содержимое переменной data конвертирум в коллекцию
	if data2['salary'] < auditValue: # с коллекции по ключу берем значение и с равниваем его со значением ветвления
		print('Извените вам отказано в кредитование!\n')
		clientDashboard()
	if data2['experience'] <= 5:
		print('Извените вам отказано в кредитование!\n')
		clientDashboard()
	else:
		print('Вам одобрен запрашиваемый кредит!\nМы вышлим вам на почту документы для подписания.\nСпасибо что вы с нами.\n')
		clientDashboard()
	

# auditClient('C:\\Program Files\\virtual bank\\', emailLogin)

#==============================================================================================

def getCredit(path, emailLogin):
	print('')
	placeOfWork = input('Введите место работы:')
	salary = int(input('Введите вашу месячную зарплату:'))
	experience = int(input('Введите количество лет трудового стажа:'))
	workList = {'placeOfWork': placeOfWork, 'salary': salary, 'experience': experience}
	os.chdir(path + '\\' + emailLogin)
	if not (os.path.exists(path + '\\' + emailLogin)):
		with open('userCredit.txt', 'w') as file:
			file.write(str(workList))
	else:
		with open('userCredit.txt', 'w') as file:
			file.write(str(workList))
		print('Спасибо! Ваша заявка принята. Мы сообщим вам о нашем решении.\n')
		global auditValue
		auditValue = auditClient('C:\\Program Files\\virtual bank\\', emailLogin, month_pay, auditValue)
	return workList

# workData = getCredit('C:\\Program Files\\virtual bank\\', emailLogin)

#===============================================================================================

# расчет процентов по кредиту.

def creditCalculate():
	print('')
	print('Вы выбрали кредитование физических лиц\n\nУсловия кредитования для физических лиц:\nставка: 10% годовых\nсумма кредита:от 30000 до 3000000 рублей \nСрок кредитования:от 1 до 5 лет\n')
	summ = int(input('Введите сумму кредитования:'))
	time = int(input('Укажите колличество лет для пользования кредитом:'))
	yearTime = time * 12
	percents = float(0.1 * time)
	monthPay = float(summ * percents + summ)/yearTime
	global auditValue
	auditValue = float(summ * (percents * 1.3))

	if summ < 30000 or summ > 3000000:
		print('Вы ввели параметры  не удолетворяющие условием кредитования')
		creditCalculate()
	if time < 1 or time > 5:
		print('Вы ввели параметры  не удолетворяющие условием кредитования')
		creditCalculate()
	else:
		print('Ежемесячный платеж составит:', '%.2f' % monthPay)

		if input('Желаете отправить заявку?:').lower() == 'да':
			global workData
			global emailLogin
			workData = getCredit('C:\\Program Files\\virtual bank\\', emailLogin)
		else:
			clientDashboard()
	return auditValue


# month_pay, auditValue = creditCalculate()
#===========================================================================================================================================
def creditCalculateLegal():
	print('')
	print('Вы выбрали кредитование юридических лиц\n\nУсловия кредитования для юридических лиц:\nставка: 20% годовых\nсумма кредита:от 3000000 до 50000000 рублей \nСрок кредитования:от 5 до 25 лет\n')
	summ = int(input('Введите сумму кредитования:'))
	time = int(input('Укажите колличество лет для пользования кредитом:'))
	yearTime = time * 12
	percents = float(0.2 * time)
	monthPay = float(summ * percents + summ)/yearTime
	global auditValue
	auditValue = float(summ * (percents * 1.3))
	print(auditValue)
	if summ < 3000000 or summ > 50000000:
		print('Вы ввели параметры  не удолетворяющие условием кредитования')
		creditCalculateLegal()
	if time < 5 or time > 25:
		print('Вы ввели параметры  не удолетворяющие условием кредитования')
		creditCalculateLegal()
	else:
		print('Ежемесячный платеж составит:', '%.2f' % monthPay)
		print('')
		if input('Желаете отправить заявку?:').lower() == 'да':
			global workData
			workData = getCredit('C:\\Program Files\\virtual bank\\', emailLogin)
		else:
			clientDashboard()
	return auditValue


# month_payLegal, audit_Value = creditCalculateLegal()
#================================================================================================================
# Показываем информацию для клиента после того как он залогинился.
# Депозит платежи, остаток по кредиту и пеннииdef clientDashboard():
def clientDashboard():
	print('Добро пожаловать в личный кабинет.')
	ask = int(input('Выберите нужный вам пункт\n\nКредитование физических лиц. Введите 1\nКредитование юредических лиц. Введите 2\nДепозит. Введите 3\nПлатежи. Введите 4\nОстаток по кредиту и пеннии. Введите 5\n'))

	if ask == 1:
		month_pay, auditValue = creditCalculate()
	elif ask == 2:
		month_payLegal, auditValue = creditCalculateLegal()
	elif ask > 5:
		print('Вы ввели не существующий пункт')
		clientDashboard()
	else:
		print('Данные разделы находятся на разработке\nПриносим свои извинения.')
		clientDashboard()
#=================================================================================================================
# #создаем клиента с логином и надежным паролем + уникальным идетификаторм
# #уникальный ID будет EMAIL.
# # храним инфу в файлах. На каждого пользоваетля, заводим отдельную папку
# # Для информации о платежах делаем отдельный файл, для инфомрации о юзере
# # отдельный

def login(path):
	print('Пройдите авторизацию пользователя')
	global emailLogin
	emailLogin = input('Введите ел.почту:')
	if (os.path.exists(path + '\\' + emailLogin)):
		print('')
	else:
		print('Вы ввели не существующий адрес')
		login(path)
	password = input('Введите пароль:')
	if password in open(path + '\\' + emailLogin + '\\' 'userData.txt').read():
		print('')
		clientDashboard()
	else:
		print('Вы ввели неверный пароль')
		login(path)
	return emailLogin

# emailLogin = login('C:\\Program Files\\virtual bank\\')
#==============================================================================================================
# # в этой функции храним информацию о банке
# #     название, каптиализацю, дату создания. Информация должна храниться 
# #     в хеше и выодиться на экран в красивом отформатированном виде
def bankInfo():
	infoBank = {'nameBank': '"Your moneY".', 'capitalis': 10000000000000, 'creativeDate': '25 декабря 2018г.'}
	print('\nЗдравствуйте. Рады преветствовать вас в вертуальном пространстве Банка', infoBank['nameBank'])
	print('')
	print('Капитал Банка "Your moneY" на 2018г. равен', infoBank['capitalis'], 'рублей.')
	print('Дата создания:', infoBank['creativeDate'])
	print('')
	if input('ВНИМАНИЕ!!!\nКОНТЕНТ ДОСТУПЕН ТОЛЬКО АТОРИЗОВАНЫМ ПОЛЬЗОВАТЕЛЯМ.\n\nЖелаете проити регистрацию? да/нет:').lower() == 'нет':
		print('')
		global emailLogin
		emailLogin = login('C:\\Program Files\\virtual bank\\')

bankInfo()

#=========================================================================================================

def createClient():
	userName = input('Введите Ваше имя:')
	surName = input('Введите Вашу фамилию:')
	emailClient = input('Введите Ваш адрес электронной почты:')
	telClient = int(input('Введите номер вашего телефона:+7'))
	passportNo = int(input('Введите номер вашего паспорта:'))
	dateBirth = int(input('Введите дату рождения:'))
	datePassport = int(input('Введите дату выдачи паспорта:'))
	authorityPassport = input('Введите орган выдавший паспорт:')
	placeBirth = input('Введите место вашего рождения:')
	passwordClient = input(
		'Придумайте пароль.\n Он должен быть написан латинскими буквами, содержать цифры, буквы в верхнем регистре:')
	# в переменную user с помощью массива сохраняем введеные данные пользователя
	user = [userName, surName, emailClient, telClient, passportNo, dateBirth, datePassport, authorityPassport,
			placeBirth, passwordClient]
	# for userInfo, value_list in enumerate(user, 1):
	# 	print(userInfo, '-', value_list)
	print('Вы успешно прошли регистрация!')
	global emailLogin
	return user, emailClient, passwordClient # сохраняем результаты ввода в переменные
	# передаем значения переменных в функцию
userData, emailClient, passwordClient = createClient()


# # print(userData, emailClient)
#==========================================================================================================================
# # создает фаил с именем электронной почты в указоном месте с помощью указоного пути
# # вписываем в фаил данные пользователя сохраненные в массиве под именем userData 
# # и закрываем фаил.

def createFile(path, userData):

	#изменяет текущий рабочий каталог на заданный путь.
	os.chdir(path)

	# открывает фаил с указоным именем на запись
	file = open('userData.txt', 'w')

	# перебираем массив userData и записваем каждый элемент массива с новой строки
	for userValue in userData:

	# записываем фаил через временную переменную userVolue в которой сохраняем данные массива userData
	# конвертируем весь массив в строки и записваем каждый элемент массива с новой строки
	# с помощью 'n'(вожно что при конвертации экранирование не может находится в одних скобках
	# обязательно должен быть вынесен за скобках)
		file.write(str(userValue) + '\n')

	# закрываем фаил
	file.close()
#================================================================================================================
# создаем функцию для создания папки и в ней файла из функцию createFile
# ВАЖНО используем аргументы в которые передадим значения переменных при вызове функции
# emailClient=folder_name, path=путь C:\\Program Files\\virtual bank\ и 
# userData=данны массива из ввода пользователя ГЛАВНОЕ ЧЕТКО СОБЛЮДАТЬ ПОСЛЕДОВАТЕЛЬНОСТЬ АРГУМЕНТОВ И ПЕРЕМЕННЫХ

def createFolder(folder_name, path, userData):

# если нет папки по указоному пути(path) c таким именем(folder_name)
# создать папупку. Если папка существует с таким именем(folder_name)
# вывести сообщение об этом.
	if not(os.path.exists(path + '\\' + folder_name)):
		os.chdir(path)
# создаем папку 
		os.mkdir(folder_name)
# создаем путь для создания папки и сохраняем его в переменную userPath
		userPath = path + '\\' + folder_name
		createFile(userPath, userData)
		emailLogin = login('C:\\Program Files\\virtual bank\\')
		return True
	else:
		("Адрес эл.почты " + folder_name + "уже существует")
		return False

createFolder(emailClient, 'C:\\Program Files\\virtual bank\\', userData)


#================================================================================================================
def Run():
	bankInfo()
# # кредитный асортимент
def creditAsort():
	# создаем массив с перечнем услуг
	indexCredit = ['Для физических лиц', 'Для юредических лиц']

# просим пользователя выбрать услугу
	indexCredit = int(input(
		'Выберите категорию кридитования. \nДля физических лиц:Введите  - 1\nДля юридических лиц:Введите - 2\n'))
# отнимаем 1 от ввода пользователя для идентичности выбраного индекса в массиве, так как исчесление начинается с 0
	indexCredit = indexCredit - 1
# создаем условия с помощью  if для выбора нужной услуги и действий при некорректном вводе
	if indexCredit == 0:
		print('Вы выбрали кредит для физических лиц.')
		creditCalculate()
	elif indexCredit == 1:
		print('Вы выбрали кредит для юредических лиц.')
		creditCalculateLegal()
	else:
		print('Вы выбрали не существующий пункт.')
# предусматриваем не корректный ввод пользователя и вызываем рекурсию функции(на данный момент она не работает корректно)
# при отрицательном ответе заканчиваем деолог с пользователем 
		if input('Желаете выбрать категорию кредитования?').lower() == 'да':
			creditAsort()
		else:
			print('Спасибо что посетили нашу страницу.\nДосвидания.')
			bankInfo()

creditAsort()

#===================================================================================================================
