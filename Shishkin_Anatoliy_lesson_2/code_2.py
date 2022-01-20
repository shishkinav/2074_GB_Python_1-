# что такое типы и как их проверять
a = 1
print(type(a))

if not isinstance(a, str):  # int, float, dict ...
    print('Не является объектом строкового типа')

print(type(a) == bool)

# Как смотреть методы объекта
im_list = list()
print(dir(im_list))

# Методы списка
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
im_list.append(100)
print(f'{im_list} - {len(im_list)}')

im_list.extend([10, 15])
print(f'{im_list} - {len(im_list)}')

im_list.append([10, 15])
print(f'{im_list} - {len(im_list)}')

im_list.extend([10, 15])
print(f'{im_list} - {len(im_list)}')
search_value = 10
print(f'Количество искомого {search_value} - {im_list.count(search_value)}')


year = ['январь', 'февраль', 'март', 'апрель', 'май']
print(year)

element_1 = year.pop()
print(element_1)
print(year)

element_2 = year.pop(2)
print(element_2)
print(year)

year.insert(2, 'март')
print(year)

year.append('март')
print(year)

while year.count('март'):
    year.remove('март')
    print('Удаляю март')

print('Список год =', year)

print('\n\nРеверс списка in_place')
print(id(year), year)
year.reverse()
print(id(year), year)

print('\n\nРеверс списка not in_place')
print(id(year), year)
year_reversed = list(reversed(year))
print(id(year_reversed), year_reversed)

print(id(year), year)
new_year = year[::-1]
print(id(new_year), new_year)

# Реверсы и срезы списков
# параметры среза obj[start=0, stop=len(obj), step=1]
print('Hello world!'[6:-1])

# Сортировка списков
print('\n\nСортировка списка in_place')
print(id(year), year)
year.sort()
print(id(year), year)

print('\n\nСортировка списка not in_place')
print(id(year), year)
year_sorted = sorted(year)
print(id(year_sorted), year_sorted)


# Кортежи
import sys


some_list = ['hello', True, 'word', 1, 2.2]
print(type(some_list), sys.getsizeof(some_list), some_list)
some_tuple = ('hello', True, 'word', 1, 2.2)
print(type(some_tuple), sys.getsizeof(some_tuple), some_tuple)

# Методы списка - 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
print(dir(some_tuple))  # Методы кортежа - 'count', 'index'


# Нюансы присваивания и копирования объектов
a = [['hello'], 10]
b = a
print(id(a), id(b))
b[1] = 15
print(a, b)
print(id(a), id(b))

from copy import copy, deepcopy

print('\n\n')
a = [['Привет'], 10]
b = copy(a)
print(id(a), id(b))
b[1] = 15
print(a, b)
b[0][0] = 'world'
print(id(a), id(b))
print(a, b)

print('\n\n')
a = [['Привет'], 10]
b = deepcopy(a)
print(id(a), id(b))
b[1] = 15
print(a, b)
b[0][0] = 'world'
print(id(a), id(b))
print(a, b)

print('\n')
# Работа со строками
hello = list('Hello world!')
print(hello)

print(f'я - {ord("я")}')
print(chr(1103))
print(f'а - {ord("а")}')
print(chr(1072))
print(f'б - {ord("б")}')
print(chr(1073))

print(f'{chr(ord("я") - 32)} - {ord(chr(ord("я") - 32))}')

# Форматирование строк
name = "Тарас"
minute = 5
print('Проснись, %s! Вебинар скоро закончится. Осталось %d минут.' % (name, minute))
print('Проснись, {:^20}! Вебинар скоро закончится. Осталось {} минут.'.format(name, minute))
print(f'Проснись, {name}! Вебинар скоро закончится. Осталось {minute:.2f} минут.')

# на самостоятельный разбор через dir и Интернет
# str.spite()
# str.join()
# str.upper() и str.lower()
# str.title() и str.capitalize()

# реверс строки
message = 'екшамод к ьрепет илангоп'
print(message[::-1])

print('end lesson 2')
