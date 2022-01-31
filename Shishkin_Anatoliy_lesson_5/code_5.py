"""
Урок 5. Генераторы и comprehensions. Множества
"""
import sys


# Что такое генератор?
# миллион элементов в списке, которые занимают память
# nums = []
# for num in range(1, 10 ** 6 + 1, 2):
#     nums.append(num ** 2)
# print(type(nums), sys.getsizeof(nums))  # <class 'list'> 4167352

# миллион объектов не выдаются разом, поэтому памяти занимает минимум
# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))
# print(type(nums_gen), sys.getsizeof(nums_gen))  # <class 'generator'> 112

# профилируем чтобы понять не в ущерб ли используем генератор
from time import perf_counter

# start = perf_counter()
# nums_sum = sum(nums)
# print(nums_sum, perf_counter() - start)
#
# start = perf_counter()
# nums_gen_sum = sum(nums_gen)
# print(nums_gen_sum, perf_counter() - start)

# второй пример профилирования - в чём разница?
# start = perf_counter()
# nums = []
# for num in range(1, 10 ** 6 + 1):
#     nums.append(num ** 2)
# nums_sum = sum(nums)
# print(nums_sum, perf_counter() - start)
#
# start = perf_counter()
# nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1))
# nums_gen_sum = sum(nums_gen)
# print(nums_gen_sum, perf_counter() - start)


# генераторы не поддерживают слайсы
nums = []
for num in range(1, 10 ** 6 + 1, 2):
    nums.append(num ** 2)
nums_gen = (num ** 2 for num in range(1, 10 ** 6 + 1, 2))

print(nums[:5])
print(next(nums_gen), next(nums_gen), next(nums_gen), next(nums_gen), next(nums_gen), sep=', ')

# но мы можем получить следующие несколько значений - генератор "помнит своё состояние"
from itertools import islice

print(*islice(nums_gen, 5), sep=', ')


# генераторы ОДНОРАЗОВЫЕ
nums_gen_sum = sum(nums_gen)
print(nums_gen_sum)

nums_gen_sum = sum(nums_gen)
print(nums_gen_sum)             # 0


"""
Задание: создать генератор, который будет возвращать по очереди 
символы между указанным начальным и конечным значением
"""
import typing


def letter_generator(start: str, end: str) -> typing.Generator:
    """
    Возвращаем символы из дипазона
    :param start: начальный символ кодировки, с которого начинать возврат
    :param end: конечный символ кодировки, которым необходимо закончить
    :return: Generator
    """
    for code in range(ord(start), ord(end) + 1):
        yield chr(code)
        print('end func generator')


eng_uppercase_letters = letter_generator('A', 'Z')
print(*eng_uppercase_letters, sep='')
print('\n\n')


# List Comprehensions - не является генератором
nums_cube = [num ** 3 for num in range(5 + 1)]
print(type(nums_cube), *nums_cube)

# Nested List Comprehensions
matrix_1 = [
    [1, 1, 1, 1],
    [2, 2, 2, 2]
]
matrix_2 = [
    [3, 3, 3, 3],
    [4, 4, 4, 4]
]
matrix_sum = [
    [matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))]
    for i in range(len(matrix_1))
]
print(matrix_sum)

weather_data = [
   [-17.5, -18.9, -21.0, -16.1],
   [-9.3, -11.7, -14.3, -15.8],
]
flat_weather_data = [el for row in weather_data for el in row if el > -15]
print(flat_weather_data)


# Dict Comprehensions
eng_ru_nums = {'one': 'один', 'first': 'один', 'two': 'два'}
ru_eng_nums = {val: key for key, val in eng_ru_nums.items()}
print(ru_eng_nums)


# Множества в Python (Хэш-таблицы)
basket = ['apple', 'dell', 'samsung', 'apple', 'huawei', 'asus', 'samsung']
# unique_brands = [el for el in basket if basket.count(el) == 1]
# print(unique_brands)

# Задача: получить список элементов, которые встречаются только один раз
# и вывести полученные элементы в том же порядке в котором они были добавлены
unique_brands = set()
tmp = set()
for el in basket:
    if el not in tmp:
        unique_brands.add(el)
    else:
        unique_brands.discard(el)
    tmp.add(el)
print(unique_brands)

# сохранение последовательности элементов
unique_brands_ord = [el for el in basket if el in unique_brands]
print(unique_brands_ord)

print('\n\n')
# ещё методы множества
chat_1 = {'user_1', 'user_5', 'user_7', 'user_8', 'user_11'}
chat_2 = {'user_1', 'user_2', 'user_2', 'user_7', 'user_9', 'user_10'}
# пересечения по множествам
chats_common = chat_1.intersection(chat_2)
print(chats_common)  # {'user_7', 'user_1'}
print(chat_1 & chat_2)
# только пользователи конкретного чата
chat_1_only = chat_1 - chat_2
chat_2_only = chat_2 - chat_1
print(chat_1_only)  # {'user_11', 'user_8', 'user_5'}
print(chat_1.difference(chat_2))
print(chat_2_only)  # {'user_9', 'user_2', 'user_10'}
print(chat_2.difference(chat_1))
# объединение пользователей двух множеств
both_chats = chat_1.union(chat_2)
print(both_chats)  # {'user_1', 'user_5', 'user_7', 'user_11', 'user_8', 'user_9', 'user_10', 'user_2'}
print(chat_1 | chat_2)

# Снова множества — frozenset
chat_1 = frozenset(('user_1', 'user_5', 'user_7', 'user_8', 'user_11'))
chat_2 = frozenset(('user_1', 'user_2', 'user_2', 'user_7', 'user_9'))

chats_common = chat_1.intersection(chat_2)
print(chats_common)


# Set Comprehensions
import random


random_nums = {random.randint(1, 100) for _ in range(200)}
print(type(random_nums), len(random_nums), random_nums)


print('end lesson 5')
