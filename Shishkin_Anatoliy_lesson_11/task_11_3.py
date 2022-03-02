class NotIntError(Exception):
    pass


class Storage:

    def __init__(self, data: list):
        self.data = data

    @staticmethod
    def check(value: str):
        try:
            value = int(value)
        except ValueError:
            raise NotIntError

    def add(self, value: str):
        try:
            Storage.check(value)
            self.data.append(int(value))
        except NotIntError:
            print('Можно вводить только числа')


"""
Инструкция по работе.
Войти в терминал PyCharm.
Запустить скрипт task_11_3.py.
Вводить числа (целочисленный тип) по одному. Если ввести строку, появится информационное сообщение.
Ввести слово stop (без кавычек).
Скрипт выведет список чисел.
"""

stop = 'stop'
result = Storage([])
while True:
    user_input = input()
    if user_input == stop:
        break
    else:
        result.add(user_input)
print(result.data)

