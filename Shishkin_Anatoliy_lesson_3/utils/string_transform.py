import typing
from string import punctuation


def clear_punctuation(text: str) -> str:
    """Очищает полученный string от пунктационных знаков не учитывая пробелы"""
    return ''.join([simbol for simbol in text if simbol not in punctuation])


def lower_and_split(text: str) -> typing.List:
    """
    Переводим все символы в lowercase и разбираем на список

    :param text: строковая переменная
    :return: List[str] список строковых элементов
    """
    return text.lower().split(' ')
