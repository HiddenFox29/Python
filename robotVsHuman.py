from random import randint # импортируем из модуля random метод randint
from time import sleep # Метод sleep () приостанавливает выполнение на указанное количество секунд.
						# Аргумент может быть числом с плавающей запятой, чтобы указать более точное время .

class Unit(): #создаем класс содержащий основные значения игры
# поле глобальных переменных класса Unit
	name = ''
	health = 1000
	wins = 0
	# конструктор классов
	def __init__(self, n):
		self.name = n
	# метод info выводит значения глоб.переменных
	def info(self):
		print('Имя: ' + self.name)
		print('Здоровье: ' + str(self.health))
		print('Побед: ' + str(self.wins))
		print('!!!!!!!!!!')
	# метод atack с помомощью модулей randint,sleep генерирует случайные числа для формулы  1000(self.health)-val и задерживает время вывода на 2 и 1 сек
	def atack(self, enemy):
		val = randint(0, 1000) # random dugit from 0 to 1000
		print(self.name + ' атакует ' + enemy.name)
		sleep(2)
		print(' ')
		print(self.name + ' отнимает' + ' у ' + enemy.name + ' ' + str(val) + ' жизней')
		sleep(1)
		enemy.takeAway(self, val) # отдает с генериваное число в def takeAway
		print('.........')
	# метод takeAway осуществляет вычетание из health, логическое условия устроенно так: 
	# если жизни одного из игороков меньше нуля сообщать о победе и прибовлять к имени переменной win 1
	def takeAway(self, attacker, val):

		self.health-= val 
		print('У ' + self.name +' осталось ' + str(self.health) + ' жизней')
		sleep(2)
		if self.health <= 0:
			print('--------------')
			print('Еден.изм ' + attacker.name + ' победил! ' + self.name + ' умер')
			print('--------------')
			attacker.wins+=1
			attacker.info() 

			attacker.health = 1000
			self.health = 1000
			sleep(3)
			print(' ')

# класс Robot евляется дочернем классом и наследует все значения класса(Unit)
class Robot(Unit):
	# глоб.перемн класса Robot
	production = ''
	# конструктор классов
	def __init__(self, name, prod):
		Unit.__init__(self, name)
		self.production = prod
	# метод класса Robot выводит информацию о Robot
	def info(self):
		print('Имя: ' + self.name)
		print('Здоровье: ' + str(self.health))
		print('Побед: ' + str(self.wins))
		print('Производство: ' + self.production)
		print('!!!!!!!!!!')
# тоже самое что и с классом Robot
class Human(Unit):
	country = ''
	def __init__(self, name, c):
		Unit.__init__(self, name)
		self.country = c
	
	def info(self):
		print('Имя: ' + self.name)
		print('Здоровье: ' + str(self.health))
		print('Побед: ' + str(self.wins))
		print('Страна: ' + self.country)
		print('!!!!!!!!!!')
# Game класс который с помощью своих методов позволяет юзеру указать именна робота и человека
class Game():
	def gameInfo(self):
		print('Добро пожаловать в игру!')
		sleep(2)
		
	def start(self):
		self.gameInfo()
		robotName = input('Введите имя робота: ')
		robot = Robot(robotName, 'Sony')
		print('сохранение...')
		sleep(2)
		print('создано!')
		robot.info()

		humanName = input('Введите имя человека: ')
		human = Human(humanName, 'Россия')
		print('сохранение...')
		sleep(2)
		print('создоно!')
		human.info()
		self.arena(human, robot)
# метод включающий в себя цикл по условию которого робот и человек по очереди отнимают 
# у друг друга с генерированые числа из переменной health и ведет счет значений переменной win
# пока win одного из методов робота или человека не будет ровно 3 цикл будет продолжаться
# как только условие будет выполнено выведется 'the end'цикл будет остановлен и программа будет закрыта
	def arena(self, robot, human):
		while True:
			robot.atack(human)
			human.atack(robot)
			if robot.wins >= 3 or human.wins >= 3:
				print('The End')
				break

def game():
	robotName = input('Введите имя робота: ')
	robot = Robot(robotName, 'Sony')
	print('сохранение...')
	sleep(2)
	print('создано!')
	robot.info()

	humanName = input('Введите имя человека: ')
	human = Human(humanName, 'Россия')
	print('сохранение...')
	sleep(2)
	print('создано!')
	human.info()

	while True:
		robot.atack(human)
		human.atack(robot)
		if robot.wins >= 3 or human.wins >= 3:
			print('The End')
			break

#game()
game = Game()
game.start()







#class Human

#human = Unit('Putin')
#robot = Unit('T1000')