from functools import wraps


def type_logger(func):
    '''
    Декоратор формирует лог-файл user_log.txt в той же папке, где сохранен данный модуль,
    а также выводит на печать название функции, которую декорирует. Если вводится несколько аргументов
    через запятую, названия функции и тип аргумента печатаются построчно, а в лог-файле сохраняются через запятую.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):

        for i in range(len(args)):
            if i == len(args) - 1:
                msg = 'Type of arg ' + str(args[i]) + ' = ' + str(type(args[i])) + '\n'
            else:
                msg = 'Type of arg ' + str(args[i]) + ' = ' + str(type(args[i])) + ', '
            with open('user_log.txt', 'a', encoding='utf-8') as f:
                f.write(msg)
            print(f'{calc_cube.__name__}, {args[i]}: {type(args[i])}')
        result = func(*args)
        return result

    return wrapper


@type_logger
def calc_cube(*numbers):
    '''
    Функция, проверяющая принадлежность входных аргументов calc_cube к целочисленному типу.
    '''
    return [x ** 3 for x in numbers]


if __name__ == '__main__':
    a = calc_cube(6, 7, 8, 5.55, -9)
    print(*a)
    b = calc_cube(0)
    print(*b)
