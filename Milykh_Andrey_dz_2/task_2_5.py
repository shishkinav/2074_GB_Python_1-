# Задание 5
"""
Создать вручную список, содержащий цены на товары (10–20 товаров), например:

[57.8, 46.51, 97, ...]


a) Привести каждый элемент списка к виду <r> руб <kk> коп и собрать их в одну строку через запятую. Пример:

57 руб 80 коп, 46 руб 51 коп ...

Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
(должно быть 07 коп или 00 коп).

b) Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
сортировки остался тот же).

c) Создать новый список, содержащий те же цены, но отсортированные по убыванию.

d) Вернуть цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""
from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    list_str = []
    for i in range(len(list_in)):
        item_str = str(list_in[i])
        point = item_str.index('.')
        rubles = item_str[:point]
        if len(rubles) == 1:
            rubles = f'0{rubles}'
        kopeks = item_str[point+1:]
        if len(kopeks) == 1:
            kopeks = f'{kopeks}0'
        item_str = f'{rubles} руб {kopeks} коп'
        list_str.append(item_str)

    return ", ".join(list_str)  # "здесь итоговая строка"


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    list_in.sort()  # метод сортирует список и возвращает None!!!
    return list_in  # ["отсортированный результирующий список"]


# зафиксируйте здесь информацию по исходному списку my_list
print(f'my_list id:  {id(my_list)}, my_list  = {my_list}')
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(f'result_2 id: {id(result_2)}, result_2 = {result_2}')


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    list_out = list(list_in)
    # list_out = ["список элементов в списке по убыванию"]
    list_out.sort(reverse=True)
    # print(f'list_out id: {id(list_out)}, list_in  = {list_out}')
    return list_out


result_3 = sort_price_adv(my_list)
# print(result_3)
print(f'result_3 id: {id(result_3)}, result_3 = {result_3}')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_out = list(list_in)
    list_out.sort(reverse=True)
    count = len(list_out) - 5
    while count > 0:
        list_out.pop(-1)
        count -= 1
    list_out.sort()
    return list_out  # list_out = ["список из пяти самых больших элементов"]


result_4 = check_five_max_elements(my_list)
print(result_4)
