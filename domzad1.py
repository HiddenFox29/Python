def randGame(): # создаем функцию 
    import random # импортируем модуль random
    ports = [80, 944, 255, 67] # в переменную ports заносим список
 
 
    print('у тебя есть 4 порта', ports, 'угадай какой из них открытый') # выводим сообщение о правилах игры
    index = int(input('Введи число от 1 до 4 >')) # получаем значение пользователя в целых числах
   
    if index < 1 or index > 4: # ветвление если переменная index меньше 0 или больше 4 выводить сообщениее о не праввильном вводе
        print('Ты введ не то что я тебя просил')  # вывод сообщения
        mainGame() # рекурсии функции
    else:  # также  
        winindex = random.randint(0, 3) # переменная созданная случайным образом из чисел в деапозоне от 0 до 3
        index = index - 1 # так как исчесление списков в python на чинается с нуля(0) отнимаем 1 от введенного значения для соответствия 
                          # со значением порта
       
        if index == winindex: # если index равен генерируему значению переменной winindex
            print('Ты выбрал порт', ports[index]) # выводим сообщение введенное пользователем и которое совпадает с индексом порта
            print('открытый порт был', ports[winindex]) # выводим сообщение с генерируемое знаением в переменной winindex 
            print('Ты выиграл!!!') 
            mainGame() # рекурсия функции
        else: # также если значение переменных index и winindex не совпало выводить следующие сообщение
            print('Ты не угадал. Повезет в другой раз')# сообщение о проигреше пользователя
            print('открытый порт был', ports[winindex])# указание на с генерированный порт 
            mainGame() # рекурсия функции
 
def mainGame(): # создаем функции
    yesOrNo = input('Хочешь сыграть в игру "Угадай открытый порт"? Введи да или нет >') # предлагаем пользователю сыграть в игру и предлагаем на выбор "да" или "нет"
   
    if yesOrNo.lower() == 'да': # если пользователь вводит да (lower() переводит введенные данные в нижний регистр) 
                                # вызывыаем функциию которая начинает игру 
        randGame() # рекурсия функции (перенаправление в игру пользователя)
    elif yesOrNo.lower() == 'нет': # если пользователь вводит не (lower() переводит введенные данные в нижний регистр) 
                                    # заканчиваем игру 
        print('Ты скучный') # сообщение пользователю
        mainGame()#  не нужная рекурсия
    else: # также если пользователь ввел не соответствующие требованиям значение выводим сообщение и рекурсируем функцию снова
        print('Ты ввел не то что я тебя просил')
        mainGame()
 
mainGame() # вызов функции