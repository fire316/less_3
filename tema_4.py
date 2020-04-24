# tema 4

# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

import random  # берём библиотеку перемешивания для выполнения задания
names = ['tima', 'vova', 'jo', 'dima', 'jeni']

def func(imia, N):
  kol_vo = 20 # количество имён 
  spisok_imen = kol_vo * imia
  out = random.sample(spisok_imen, N) # перемешиваем по длине входа 100
  print(out)
  
func(names, 100) # подаём на вход по условиям задания 
#==========
# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F
#--
# 1 способ

def func(**list_names): # делаем функцию под словари для работы с ключами
  print(list_names)
  
  c = list_names.items() # подаём в "с" ключи и значения для работы со значениями

  list_names_sort = sorted(c, key = lambda i: i[1], reverse = True) # берём элементы словаря, лямбдой делаем сортировку по значениям, по убыванию

  for i in list_names_sort[0:1]: # проходим по значениям срезом берём максимальное
    print(i[0], '=', i[1]) # смотрим ключ и соответствующее значение, по выборке
    
func(Kolia = 1, vasia = 2, petia = 3)
#--
# 2 способ, не через функцию

list_names =  ['Kolia', 'vasia', 'petia', 'Kolia', 'Kolia', 'petia']
slovar = {} # подготавливаем пустой словарь для формирования списка с ключами и значениями

for i in list_names: # проходимся по элементам словаря
  slovar[i] = list_names.count(i) # считает имена и записывает их количество в значение этого элемента в словаре

print(slovar) 

list_names_sort = sorted(slovar.items(), key = lambda i: i[1], reverse = True) # берём элементы словаря, лямбдой делаем сортировку по значениям, по убыванию

for i in list_names_sort[0:1]: # проходим по значениям и срезом берём максимальное
 print(i[0], '=', i[1]) # смотрим ключ и соответствующее значение, по выборке
#=====
# 3. Напишите функцию вывода самой редкой буквы, с которой начинаются имена в списке на выходе функции F
#=====
def func(**list_names):  # делаем функцию под словари для работы с ключами
 print(list_names)
 
 spisok_bukv = [] # подготавливаем  пустой список , для добавления туда первых букв
 for i in list_names: # проходим по списку
  spisok_bukv.append(i[0]) # добавляем в новый список первые буквы от каждого слова
 print(spisok_bukv) # проверяем
 
 slovar = {} # подготавливаем  пустой словарь чтоб помимо слов были и значения их
 for i in spisok_bukv:
  slovar[i] = spisok_bukv.count(i) # считаем количество букв в словаре
 print(slovar)
 
 list_names_sort = sorted(slovar.items(), key = lambda i: i[1]) # берём элементы словаря, лямбдой делаем сортировку по значениям 

 for i in list_names_sort[0:1]: # проходим по значениям срезом выбираем редкую букву
   print(i[0], '=', i[1]) # смотрим ключ и соответствующее значение, по выборке

func(kolia = 1, kotia = 2, vasia = 2, petia = 3) # произвольный вход в функцию
#===== 
# 4. В файле с логами найти дату самого позднего лога (по метке времени)

import re # берём модуль регулярных выражений, который поможет нам делать поиск даты

c = open('log', 'r')  # закидываем файл log в папку проекта, т.е. log и 123.py должны лежать в одном каталоге
c = c.read()  # считать информацию файла в текстовую переменную

date_line = re.findall('\d{4}-\d{2}-\d{2}.\d{2}:\d{2}:\d{2}', c) # библиотекой find all найти всё - ищем дату в файле, конфигурируем поиск, указываем где искать "с"

for item in date_line: # посмотрим в столбик все даты найденные в тексте
  print(item)         

names_sort = sorted(date_line, reverse = True) # сортируем даты по убыванию
print(names_sort[:1]) # берём дату последнего лога