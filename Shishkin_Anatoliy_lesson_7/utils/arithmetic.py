from .my_exceptions import FuncAttributeFailError


def division(a, b):
    """Функция деления"""
    try:
        return a / b
    except ZeroDivisionError as err:
        message = f'Получили ошибку деления на ноль: {err}'
        raise ZeroDivisionError(message)


def division_with_my_exc(a, b):
    """Функция деления с собственными исключениями"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise FuncAttributeFailError(
            f'Оба атрибута должны быть целочисленными. a={a}, b={b}')
    try:
        return a / b
    except ZeroDivisionError as err:
        message = f'Получили ошибку деления на ноль: {err}'
        raise ZeroDivisionError(message)