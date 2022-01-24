# Задание 2
"""
На вход будет выдаваться список, пример:

['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
'была', '+5', 'градусов']

a) Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до
и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:

['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']


b) Сформировать из обработанного списка строку:

в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел
со знаком?

Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
Главное: дополнить числа до двух разрядов нулём!
"""


def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    # пишите реализацию своей программы здесь
    list_out = []
    signs = ["-", "+"]
    for i in range(len(list_in)):
        i_str = list_in[i]
        if i_str.isnumeric():
            list_out.append('\"')
            number_str = i_str
            if len(number_str) == 1:
                number_str = f'0{number_str}'
            list_out.append(number_str)
            list_out.append('\"')
        elif i_str[:1] in signs and i_str[1:].isnumeric():
            list_out.append('\"')
            number_str = i_str[1:]
            if len(number_str) == 1:
                number_str = f'{i_str[:1]}0{number_str}'
            else:
                number_str = f'{i_str[:1]}{number_str}'
            list_out.append(number_str)
            list_out.append('\"')
        else:
            list_out.append(list_in[i])
    print(list_out)
    # the formation of the processed list has been debugged

    str_out = ' '.join(list_out)
    list_out = list(str_out)

    i = 0
    count = 0
    while i < len(list_out):
        if list_out[i] == '\"':
            count = 2
        if list_out[i] == " ":
            if count > 0:
                count -= 1
                del list_out[i]
                i += 1
        i += 1

    str_out = ''.join(list_out)
    return str_out  # здесь полученная после всех преобразования строковая переменная


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list)
result = convert_list_in_str(my_list)
print(result)
