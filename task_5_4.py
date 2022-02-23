def get_numbers(src: list):
    """
    Функция возвращает генератор из элементов списка src, соответствующих условию задачи
    """
    for i in range(1, len(src)):
        if src[i - 1] < src[i]:
           yield src[i]

def get_numbers_list(src: list) -> list:
    """
    Функция возвращает список элементов, состоящий из элементов списка src, соответствующих условию задачи
    """
    user_list = []
    for i in range(1, len(src)):
        if src[i - 1] < src[i]:
            user_list.append(src[i])
    return user_list

def get_numbers_comp(src: list) -> list:
    """
    Функция возвращает список элементов, состоящий из элементов списка src, соответствующих условию задачи.
    Применен List comprehensions
    """
    return [src[i] for i in range(1, len(src)) if src[i - 1] < src[i]]


from sys import getsizeof
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

start = perf_counter()
print(*get_numbers(src))
print(f'объем памяти - {getsizeof(get_numbers(src))} байт, время - {perf_counter() - start} сек')

"""
Результат 
12 44 4 10 78 123
объем памяти - 104 байт, время - 0.00011605300096562132 сек
"""

start = perf_counter()
print(*get_numbers_list(src))
print(f'объем памяти - {getsizeof(get_numbers_list(src))} байт, время - {perf_counter() - start} сек')

"""
12 44 4 10 78 123
объем памяти - 120 байт, время - 7.509299757657573e-05 сек
"""

start = perf_counter()
print(*get_numbers_comp(src))
print(f'объем памяти - {getsizeof(get_numbers_comp(src))} байт, время - {perf_counter() - start} сек')

"""
12 44 4 10 78 123
объем памяти - 120 байт, время - 4.4941996748093516e-05 сек
"""