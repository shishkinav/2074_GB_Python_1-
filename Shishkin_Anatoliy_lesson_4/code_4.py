"""
Урок 4. Работа с модулями и пакетами
"""
# Батарейки для Python: pypi.org
# https://pypi.org/project/num2words/
# from num2words import num2words

# print(num2words(42))
# print(num2words(42, to='ordinal'))
# print(num2words(42, to='ordinal_num'))
# print(num2words(42, to='year'))
# print(num2words(12.42, to='currency'))
# print()
# print(num2words(42, lang='ru'))
# print(num2words(42, to='ordinal', lang='ru'))
# print(num2words(42, to='ordinal_num', lang='ru'))
# print(num2words(42, to='year', lang='ru'))
# print(num2words(12.42, to='currency', lang='ru'))
#
#
# import hello_module
#
# hello_module.say_hello('Борис')

# Пакеты
import requests

# Ctrl + Alt + O — PyCharm автоматически поправит импорты в скрипте и уберёт лишнее

response = requests.api.get('http://www.cbr.ru/scripts/XML_daily.asp')
print(type(response), response)
print(response.status_code)
# print(response.content[:1000])  # бинарные данные
print(response.text[:1000])  # текстовая информация


# создаём свой CLI - my_cli.py
# Рекомендуем в будущем изучить модуль argparse — он позволяет писать серьёзные инструменты для командной строки.
# argparse - https://docs.python.org/3.8/library/argparse.html#module-argparse


# Модуль time: профилируем время выполнения участков кода
# time_profiler.py


# Модуль datetime: работа с датой и временем
# datetime_difference.py





print('end lesson 4')
