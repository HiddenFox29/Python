# данная программа рассчитает сколько дне прожил человек

def ageInDays():  # объявляем функцию с одним аргументом old
	age = input('скажи свой возраст>')  # берем у пользователя возраст    
	result = int(age) * 365  # gроизводим расчет и сохраняем в переменную
	print("вы прожили примерно", result, 'дней')  # выводим результат
	return result  # отдаем результат работы функции, в переменную


days = ageInDays()


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


