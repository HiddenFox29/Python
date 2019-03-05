import os # "библиотека операционная система"

print('Версия ядра', os.name)
print('Имя пользователя', os.getlogin())

print('текущая деректория', os.getcwd())

print('files on dick', os.listdir("C:"))

# библиотека path
print('Absolutle way', os.path.abspath("1.py")) # абсолютный путь до файла
print('Absolutle way', os.path.getatime("1.py")) # абсолютный путь до файла
data = os.path.getatime("2.py")
print(data / 60 / 60)
import socket
hostname = socket.gethostname()

print(hostname)


# python.org в поисковой строке можно находить документация к модулям
