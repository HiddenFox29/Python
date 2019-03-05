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



# ports = [80, 94, 77, 55]

# for port, value_list in enumerate(ports, 1):
# 	print('порт ', port, '-', value_list)
# # i, value_list in enumerate(l, 1): # Аттрибут 1 - начало сортировки
#  #   print(i, value_list)




# задача в Игре угадай порт вывести все
# порты которые есть в массиве, построчно
# и пронумеровать
 
# вывод должен выглядеть так
# >>> у тебя есть 4 порта
# >>> порт 1 - 80
# >>> порт 2 - 94
# >>> порт 3 - 77
# >>> порт 4 - 55
 
# Введи число от 1 до 4 что бы угадать какой порт
# открыт