# logic operator

# конструкция if
test = 'String'

if test:
 	print('hello, world')

human = 100
robots = 1000

if robots > human: #если роботов больше чем людей
 	print('all right')# если роботов действительно больше(если переменная robots больше чем переменная human) выводить на экран это  сообщ

# конструкция else
if 2+2 > 5:
	print('вы нарушили правила математики')
else:
	print('естественно меньше')

# new constraction if
ports = [80, 91, 255, 300]

def gameRules(portsVal):
	
    if input(r'Хотите ли Вы сыграть игру <<Угадай порт>> ?>>>').lower() == 'да':
    	if ports[int(input('Выберите любое число от 0 до 3 >>>'))] == 80:
    		print('Поздравляю!!! Вы выиграли')
    	else:
    	    print('К сожалению Вы проиграли. Попробуйте еще раз')
    	    gameRules(ports)
    
    else:
    	print('Удачного дня!')

gameRules(ports)

