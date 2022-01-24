"""
Урок 3. Функции. Словари
"""


def func(a: int, b: int) -> int:
    """Пример простейшей функции"""
    c = a + b
    return c


c = 3
d = 5
value = func(c, d)
print(value, c, d)

value = func(5, 5)
print(value)

callback = func  # алиас(callback) для объекта func
print(type(callback), callback(3, 5))


text_example_1 = 'Опыт выполнения домашних заданий предыдущих уроков наверняка подсказывает вам, ' \
                 'что нужен какой-то способ для повторного использования уже написанного кода.'
text_example_2 = 'Один из способов был изобретен очень давно — обособление фрагментов кода в функции. ' \
                 'Мы уже говорили о них.'

from utils.string_transform import clear_punctuation, lower_and_split


for own_text in (text_example_1, text_example_2):
    new_text = clear_punctuation(own_text)
    print(lower_and_split(new_text))


# Возвращаем callback - упрощенный пример
nums = ['1578.4', '892.4', '354.1', '871.5']
value = 0
for num in nums:
    value += float(num)
print('Сумма вещественных чисел:', value)

# решение усложнённое
print(sum(map(float, nums)))

print('\n\n')

# docstring - используем help() для получения имеющейся документации
# help(str.upper)
# help(clear_punctuation)
# print(clear_punctuation.__doc__)
# help(list)

# Области видимости переменных
# def say_hello_wrapper():
#     name = 'Юля'
#
#     def say_hello():
#         print(name)
#
#     say_hello()
#
#
# name = 'Иван'
# say_hello_wrapper()


# запрещённый проброс переменной из локальной области в глобальную
# def say_hello():
#     global name
#     name = 'Тимур'
#     print(name)
#
# name = 'Мика'
# print(name)
# say_hello()
# print(name)

# пример использования nonlocal
# def counter():
#     num = 0
#
#     def incrementer():  # x += 1, y -= 1
#         nonlocal num
#         num += 1
#         return num
#     return incrementer
#
#
# v = counter()
# print(type(v), v)
# print(v())
# print(v())
# print(v())


print()
# Словари Python (Ассоциативные массивы)
pers_1 = ['pikachu', 87.9, 103]
pers_2 = ['smurfik', 10.0, 66]

# def get_info(data: list):
#     print(f'Никнейм - {data[0]}, health - {data[1]}, level - {data[2]}')
#
# get_info(pers_1)
# get_info(pers_2)
print()

# upgrade pers
# pers_1_adv = dict(nickname='pikachu')
pers_1_adv = {
    "nickname": 'pikachu',
    "health": 87.9,
    "level": 103
}
pers_2_adv = {
    "nickname": 'smurfik',
    "health": 10.0,
    "level": 66
}

def get_info(dataset: dict) -> str:
    print(f'Никнейм - {dataset["nickname"]}, health - {dataset["health"]}, level - {dataset["level"]}')

get_info(pers_1_adv)
get_info(pers_2_adv)
print()


print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

print('\n\n')

# Словари: .get() и .setdefault()
# print(pers_1_adv.get('sex'))
# print(pers_1_adv.get('sex', 'средний'))
# print(pers_1_adv)

print(pers_1_adv)
print(pers_1_adv.setdefault('sex', 'man'))
print(pers_1_adv)
print(pers_1_adv.setdefault('nickname', 'Эдуард'))
print(pers_1_adv)
print()

# Словари: .update() и .popitem()
print(pers_1_adv.update({'sex': 'woman', 'menu': 'action'}))
print(pers_2_adv.update({'sex': 'woman'}))
print(pers_1_adv)
print(pers_2_adv)
print(pers_1_adv.popitem())
print(pers_1_adv.pop('level'))
print(pers_1_adv)
print()

# Перебираем словарь циклом for in ( методы obj.key(), obj.item(), obj.value() )
dataset = {
    'mail.ru': '94.100.180.201',
    'geekbrains.ru': '178.248.232.209',
    'amazon.com': '205.251.242.103'
}

for key in dataset:
    print(key)

print()

for key in dataset.keys():
    print(key)

print()

for key, value in dataset.items():
    print(f'{key} = {value}')

print()

for key in dataset.values():
    print(key)

print()


# Позиционные аргументы *args
from utils.tools import own_sum, own_sum_upgrade

print(f'own_sum([1, 5, 6]) = {own_sum([1, 5, 6])}')
# print(own_sum(1, 5, 6))  # ОШИБКА
print(f'own_sum_upgrade([1, 5, 6]) = {own_sum_upgrade(1, 5, 6)}')


# разбираем распаковку
a = 5
b = 10
# как одной строкой поменять значения местами?
a, b = b, a
print(a, b)


own_list = [1, 5, 6, 7, 10]
print(*own_list)
print(1, 5, 6, 7, 10)
print(f'own_sum_upgrade(*[1, 5, 89]) = {own_sum_upgrade(*[1, 5, 6, 7, 10])}')
print(f'own_sum_upgrade(*own_list) = {own_sum_upgrade(*own_list)}')
print()


# Модуль random
import random
from random import randrange, randint, choice

# TODO подготовить моржовый оператор!

print(dir(random))
"""
'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 
'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 
'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate'
"""
numbers = [value * 11 for value in range(1, 11)]
# numbers = list()
# for n in range(1, 11):
#     numbers.append(n * 11)

print(numbers)

idx = randrange(len(numbers))  # как пользоваться randrange
print(f"idx = {idx}")
print(f"numbers[idx] = {numbers[idx]}")

print()

new_idx = randint(0, len(numbers) - 1)  # как пользоваться randint
print(f"new_idx = {new_idx}")
print(f"numbers[idx] = {numbers[idx]}")
print()

print(f'Случайное значение из списка {numbers} получили {choice(numbers)}')
print()
# choices, sample и shuffle - разбираем самостоятельно в методичке есть ссылки

# Необязательные аргументы, именованные аргументы - **kwargs

def my_game(count_game: int, luck: float = 0.00, **kwargs) -> None:
    """Играем на стандартном кубике"""
    if luck > 100:
        luck = 100.00
    # end_number = 6
    end_number = kwargs.get('count_edge', 6)
    # print(type(kwargs), kwargs)
    start_number = 1 + int(((end_number - 1) * luck) / 100)
    for step in range(count_game):
        print(f'При броске на кубике выпало: {randint(start_number, end_number)}')


my_game(2)
print()
my_game(2, 80.00)
print()

my_game(2, count_edge=12)
print()


# где может понадобиться распаковка словаря
dataset_1 = {'name': 'Анатолий', 'age': 106, 'sex': 'm'}
dataset_2 = {'health': 'small', 'luck': 0.5}
user_dataset = dict(
    **dataset_1, **dataset_2
)
print(user_dataset)
print()

# filter(), map(), zip() и lambda-функции
new_numbers = [value * 11 for value in range(20)]
print(f'new_numbers = {new_numbers}')
print()

def o_my_god(element) -> bool:
    """Наша функция для фильтрации"""
    return element % 10 == 5


own_filter_result = filter(o_my_god, new_numbers)
print(type(own_filter_result))
print(*own_filter_result)
print(*own_filter_result)

own_filter_result = filter(lambda obj: obj % 10 == 5, new_numbers)
print('lambda filter result =', *own_filter_result)
print()


user_names = ['Иван', 'Петр', 'Ольга', 'Сергей']
user_logins = ['ivan', 'petr', 'olga', 'sergey']
user_roles = ['user', 'staff', 'admin']
zip_result = zip(user_names, user_logins)  # , user_roles
print('zip_result =', list(zip_result))
print()


print('end lesson 3')
