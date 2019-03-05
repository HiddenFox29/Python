version=0.1
autor='Виктор Кувшинов'
#слово='значение' - задание переменной
name=input('Введите ваше имя>>>>')
#задаем в переменную name - имя пользователя
income=int(input('Введи свой уровень дохода>>>'))

def menu():
  print('Привет', name, ', выбери нужный пункт')
  print('Информация о банке - 1')
  print('Взять кредит - 2')
  print('Взять кредит - 3')
  choice=int(input('Введите нужный вариант>>>'))
  if choice == 1:
    info(name)
  elif choice == 2:
    percent(income)
  elif choice == 3:
    bank(percent)

def info(name):
  #def функция для создания функций. Формат def наименование(агрумент):
  print('Здравствуйте',name,'Вас приветствует банк VIRTUAL MONEY')
  print('Капитализация банка 10000000$')
  print()
  print('Банк семьи Кувшиновых')
  print('Версия банка',version)
  print('Автор программы',autor)
  menu()

def percent(income):
  result=(income/100)*30
  print('Размер минимального платежа по Вашему кредиту составит', result)
  menu()
  return result


def bank(percent):
  global income
  size = int(input('Введите размер кредита>>>>'))
  result=(income/100)*30
  print('Размер минимального платежа по Вашему кредиту составит', result)
  percent = 10
  result1 = size/percent
  print('Ваш срок погашения кредита будет равен', result1, 'месяцев')
  
  menu()

menu()