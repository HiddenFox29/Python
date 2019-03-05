# coding:utf8 
name = 'Alisa' # переменная с именем программы
version = 0.1  
autor = 'Bornidle'

def alisaName():
    name = 'Alisa'
    print('Привет меня зовут', name)

    userName = input('Как тебя зовут????') # ввод данных пользователя
    print('очень приятно', userName)
    print('спорим ты не знал что в твоем имени', len(userName), 'букв')

alisaName()

userOld = int(input('Сколько тебе лет???'))
print('В следующем году тебе будет', userOld+1, 'Могу посчитать в днях, в часах, минутах всю твою жизнь. Смотри!!!')

def ageInDays(userOld):  # объявляем функцию с одним аргументом old

   
    result = int(userOld) * 365  # gроизводим расчет и сохраняем в переменную
    print("вы прожили примерно", result, 'дней')  # выводим результат
    return result  # отдаем результат работы функции, в переменную


days = ageInDays(userOld)


def dayInTime(days):

    result = int(days) * 24
    print('в часах пожил', result, 'часов')
    return result


time = dayInTime(days)


def dayInMinut(time):

    result = int(time) * 60
    print('А в минутах будет', result, 'минут')
    return result


minut = dayInMinut(time)


def dayInSecond(minut):

    result = int(minut) * 60
    print('В секундах так вообще:', result, 'секунд')
    return result


second = dayInSecond(minut)


#  получилось создать функцию !!!
def kriptMany():
	a = input('Могу узнать данные по паре крипто валют. Введи краткое название валюты типа BTC или ETH>>>')
	b = input('Введи вторую крипто валюту>>>')
	import requests
	data = requests.get('https://bittrex.com/api/v1.1/public/getmarketsummary?market=' + a + '-' + b) # запрос на данные с сайта bitrix на крипто валюты по запросу пользователя
	print(data.json())

kriptMany()

# возраст через ветвление
print('Ты говорил что тебе', (userOld), 'лет,', 'Скажу тебе что я об этом думаю:')

if userOld < 18:
    print('ты слишком мал')
elif userOld >= 19 and userOld <= 50:
    print(' Ты в самом расвете сил Амиго,', 'в следующем году тебе будет всего-', userOld+1, 'Не теряй времени зря учи PYTHON')
else:
    print('Нет! Чувак ты слишком стар')

def userGame():
    ports = [80, 94, 77, 55]
    answer = input('хочешь сыграть? да/нет >>>').lower()

    if answer == 'да':
        print('давай сыграем')
        print('"какой порт сейчас открыт"')

        for port, value_list in enumerate(ports, 1):
            print('порт', port, '-', value_list)
        index = int(input('Введи число от 1 до 4, где 80-1, 91-2, 255-3, 300-4 >>>'))

        import random

        winIndex = random.randint(1, 4)
        

        if index == winIndex:
            print('Поздравляю ты угадал!!! Открытый порт был', winIndex)
        elif index != winIndex:
            print('Непрвильно, попробуй еще раз! Открытый порт был', winIndex)
            userGame()
        elif index <= 0 or index > 4:
            print('Ты не очень внимателен, сосредоточься!!!!')
            userGame()
    elif answer == 'нет':
        print('Пока')
    else:
        print('Будь внимательнее')
        userGame()

userGame()
 # IMPORTENT ОЧЕНЬ ВАЖНО СОБЛЮДАТЬ ПРАВИЛЬНОЕ КОЛИЧЕСТВО ОТСТУПОВ И СЛЕДИТЬ ЗА ТЕМ ЧТОБЫ ТЕЛА ФУНКИИЙ НЕ ПЕРЕМЕШИВАЛИСЬ И СОБЛЮДАЛИ
 # КОЛИЧЕСТВО ОТСТУПОВ ОТ КРАЯ !!!!!!!! ЭТО ОЧЕНЬ ВАЖНО

# игра
# угадай порт игра Игра должна быть функцией
# есть массив с портами [80, 91, 255, 300]
# спросить хочет ли человек сыграть в игру
#если пользователь отвечает да
#начинаем игру и просим угадать открытыц порт
#выводить список имеющихся портов
# введите число от 1 до 4 чтобы угодать какой порт открыт
# и если человек вводит число мы показываем какое значение внутри массива хранится под введенным индексом
# и если этот индекс не 80 порт говорим что пользователь проиграл и запускаем игру заново с помощью recurs()

def recursUserGame():
    game = input('Хочешь сыграть в игру? >>>')
    ports = [80, 91, 255, 300]
    if game == 'да':
        print('Начинаем! Угадай какой порт открыт сейчас', ports, 'Введи число от 1 до 4 >>>')
    else:
        print('Ты проиграл')

    recursUserGame()





# функции для преобразования типов
str()
int()
float()
bool()
# задача написать функцию спрашивающию колличество лет (если пользователь введет меньше 18 (ты еще молод))