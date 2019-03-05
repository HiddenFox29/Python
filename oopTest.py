class Person:
	name =''
	surname =''
	quality = 0

	def __init__(self, n, s, q):
		self.name = n
		self.surname = s
		self.quality = q

	def showPerson(self):
		print(self.name, self.surname, self.quality, 'количество трудового стажа в годах')
		
	def __del__(self):
		delit = int(input('Введите номер сотрудникаn\nNiklai введите - 1:\nOlga введите - 2:\nMita введите - 3:\n'))
		if delit == 1:
			print('досведания мистер', nikola.name, nikola.surname)
		if delit == 2:
			print('досведания мистер', olga.name, olga.surname)
		if delit == 3:
			print('досведания мистер', mita.name, mita.surname)
		else:
			print('Введите число от 1 до 3')


nikola = Person('nikolai', 'Ivanov', 2)
nikola.showPerson()
olga = Person('olga', 'Petrova', 7)
olga.showPerson()
mita = Person('mita', 'Nita', 3)
mita.showPerson()
nikola.__del__()
