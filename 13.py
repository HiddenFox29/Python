def recursUserGame(): # создаем переменную  
    ports = [80, 91, 255, 300]  # создаем список(массив) с портами
    answer = input('хочев сыграть в игру? (ответ "да" или "нет" >>>)') # с помощью ввода получаем ответ от пользователя

	 

    if answer == "да":
        print('начинаем игру')
        print('какой порт сейчас открыт', ports[0:5])
        index = int(input('Введи число от 1 до 4, где 80-1, 91-2, 255-3, 300-4 >>>'))

        import random

        winIndex = random.randint(1, 4)
        

        if index == winIndex:
            print('Поздравляю ты угадал!!! Открытый порт был', winIndex)
        elif index != winIndex:
            print('Непрвильно, попробуй еще раз! Открытый порт был', winIndex)
            recursUserGame()
        elif index <= 0 or index > 4:
        	print('Ты не очень внимателен, сосредоточься!!!!')
        	recursUserGame()

    elif answer == "нет":
        print('Как хочешь, скучно так жить')
    else:
        print('Ты не очень внимателен, сосредоточься!!!!')
        recursUserGame()

recursUserGame()
 # IMPORTENT ОЧЕНЬ ВАЖНО СОБЛЮДАТЬ ПРАВИЛЬНОЕ КОЛИЧЕСТВО ОТСТУПОВ И СЛЕДИТЬ ЗА ТЕМ ЧТОБЫ ТЕЛА ФУНКИИЙ НЕ ПЕРЕМЕШИВАЛИСЬ И СОБЛЮДАЛИ
 # КОЛИЧЕСТВО ОТСТУПОВ ОТ КРАЯ !!!!!!!! ЭТО ОЧЕНЬ ВАЖНО