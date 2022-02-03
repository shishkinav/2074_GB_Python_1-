def num_translate(num_dict: dict, num: str) -> str:
    """Переводит числительное с английского на русский"""

    # str_out = num_dict[num] # В случае если искомого слова нет в словаре возвращает ошибку
    str_out = num_dict.get(num)
    return str_out


# Словарь размещаем в теле программы, чтобы к нему могли обращаться другие функции
user_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'zero': 'нуль',
    }

print(f'Перевод слова "two": {num_translate(user_dict, "two")}')
print(f'Перевод слова "eight": {num_translate(user_dict, "eight")}')
print(f'Перевод слова "eleven": {num_translate(user_dict, "eleven")}')