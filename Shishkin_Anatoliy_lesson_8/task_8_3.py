from functools import wraps


def val_checker(aux_function):
    '''
    Декоратор, принимающий в качестве аргумента функцию, проверяющую принадлежность входных аргументов calc_cube к целочисленному типу.
    '''
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            aux_function(*args)
            result = func(*args)

            return result

        return wrapper

    return _val_checker


def aux_val_checker(*args):
    '''
    Функция, проверяющая принадлежность входных аргументов calc_cube к целочисленному типу.
    '''
    msg = '\n'
    for value in args:
        if not str(type(value)) == str(type(0)) or value < 0:
            msg = msg + ' Incorrect value: ' + str(value) + '\n'
    if not len(msg) == len('\n'):
        raise ValueError(msg)


@val_checker(aux_val_checker)
def calc_cube(*numbers):
    '''
    Функция, возводящая входные аргументы в 3-ю степень.
    '''
    return [x ** 3 for x in numbers]


if __name__ == '__main__':
    print(f'Название функции: {calc_cube.__name__}')
    a = calc_cube(1, 'gg', -7.98)
    print(*a)


