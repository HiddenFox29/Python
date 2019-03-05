# massive(colection)
ports = [80, 255, 90, 255]
print(ports)

host = ['google', '123.345.45.55', 'R1:B5:F6:D3:V10', ports]
host.append(port) # добовляет элемент в конец массива

# функции массивов
# list.append() добовляет элемент в конец массива
# list.insert(i, x) заменяет элемент массива по индексу
# list.remove(x) удаляет элемент из массива
# list.count(x) сколько элементов есть с таким значением
# list.reverse() разворот массива
# list.copy() копирует массив
# list.clear() очищает массив

data = 'Lorem Epsum Epsum Lore'
print(data[0:4]) # срезы с первого (0) по (4) не включая (4)
print(data[0:10:2]) # третий аргумент указывает шаг
