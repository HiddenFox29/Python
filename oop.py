class User:   #создаем класс с именем User обязательно с большой буквы

# описываем класс с помощью переменных строки цифры словарь
	name = ''
	city = ''
	work = ''
	money = 0
	posts = []
	userCount = 0

	# self ссылка на сам объект например darkhan
	# Конструктор класса
	def __init__(self, n, с, w, m): #Так как объект создается в момент вызова класса по имени, то в этот момент вызывается метод __init__(), если он определен в классе.
		self.name = n # передаем именам аргументами
		self.city = с
		self.work = w
		self.money = m
		self.posts = []

	def info(self): # выводим на экран переменные переданные спомощью ссылки self
		print('')
		print(self.name)
		print(self.city)
		print(self.work)
		print(self.money)

	def editUserInfo(self, n, с, w, m):
		self.name = n
		self.city = с
		self.work = w
		self.money = m

	def addPost(self):# создаем экземпляр для ввода пользователя текста и дабавляем в конец списка с помощью append
		text = input('Введи текст>>>')
		date = '13.44.66'
		post = Post(text, date, self)
		self.posts.append(post)
		self.showPosts()

	def showPosts(self):
		print('Все посты юзера', self.name)
		print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
		for post in self.posts:
			print(post.text)

class Post: # создаем класс с именами переменнных описыываем класс
	text = ''
	created_at = ''
	user_name = ''

	def __init__(self, t, date, user): # c помощью конструктора классов создаем сыллки self 
		print('Вы добавляете пост для', user.name)
		self.text = t
		self.created_at = date
		self.user_name = user.name

darkhan = User('Darkhan', 'Almaati', 'RozGosStrah', 1000000)
darkhan.addPost()
darkhan.addPost()
darkhan.addPost()
darkhan.addPost()

print('Darkhana Posti')
darkhan.showPosts()
darkhan.info()


slava = User('Slava', 'Doneck', 'Oper', 1000000)
slava.addPost()
slava.addPost()
slava.addPost()
slava.addPost()
print('Slavini Posti')
slava.showPosts()
slava.info()

# slava.editUserInfo('Slava', 'Doneck', 'Oper', 2000000)
# slava.info()

# print(type(darkhan))



